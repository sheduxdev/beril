import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import scan_vibe


def test_missing_rls_is_high(tmp_path):
    (tmp_path / "db").mkdir()
    (tmp_path / "db" / "001.sql").write_text("create table profiles (id uuid primary key, email text);\n")
    report = scan_vibe.scan(str(tmp_path))
    finding = next(f for f in report.findings if f.check == "vibe.rls-missing")
    assert finding.severity == "high"
    assert "enable row level security" in finding.fix


def test_rls_present_is_clean(tmp_path):
    (tmp_path / "db").mkdir()
    (tmp_path / "db" / "001.sql").write_text(
        "create table profiles (id uuid primary key);\n"
        "alter table profiles enable row level security;\n"
        "create policy own on profiles for select using (auth.uid() = id);\n"
    )
    report = scan_vibe.scan(str(tmp_path))
    assert "vibe.rls-missing" not in {f.check for f in report.findings}


def test_service_role_in_client(tmp_path):
    (tmp_path / "components").mkdir()
    (tmp_path / "components" / "table.tsx").write_text("const key = process.env.SUPABASE_SERVICE_ROLE_KEY;\n")
    report = scan_vibe.scan(str(tmp_path))
    assert "vibe.service-role-client" in {f.check for f in report.findings}


def test_public_secret_name(tmp_path):
    (tmp_path / "app").mkdir()
    (tmp_path / "app" / "page.tsx").write_text("const k = process.env.NEXT_PUBLIC_STRIPE_SECRET;\n")
    report = scan_vibe.scan(str(tmp_path))
    assert "vibe.public-secret" in {f.check for f in report.findings}


def test_dangerous_html_without_sanitize(tmp_path):
    (tmp_path / "app").mkdir()
    (tmp_path / "app" / "x.tsx").write_text("<div dangerouslySetInnerHTML={{__html: body}} />\n")
    report = scan_vibe.scan(str(tmp_path))
    assert "vibe.dangerous-html" in {f.check for f in report.findings}


def test_firebase_open_rule(tmp_path):
    (tmp_path / "firestore.rules").write_text("match /users/{id} { allow read: if true; }\n")
    report = scan_vibe.scan(str(tmp_path))
    assert "vibe.firebase-open" in {f.check for f in report.findings}
