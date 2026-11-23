import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import scan_jar


def build_jar(path: Path, name="OtherName", extra=b"", include_ioc=False):
    with zipfile.ZipFile(path, "w") as zf:
        zf.writestr("plugin.yml", f"name: {name}\nversion: 1.0\nmain: com.example.Main\n")
        zf.writestr("com/example/Main.class", b"\xca\xfe\xba\xbe" + extra)
        if include_ioc:
            zf.writestr("plugin-config.bin", b"data")


def test_ioc_file_and_mismatch(tmp_path):
    jar = tmp_path / "FreeRank.jar"
    build_jar(jar, name="PremiumRanks", include_ioc=True)
    report = scan_jar.scan(str(jar))
    checks = {f.check for f in report.findings}
    assert "jar.ioc-file" in checks
    assert "jar.manifest-mismatch" in checks


def test_behaviour_strings(tmp_path):
    jar = tmp_path / "x.jar"
    build_jar(jar, extra=b"Runtime.getRuntime\thttps://pastebin.com/raw/abc\tProcessBuilder")
    report = scan_jar.scan(str(jar))
    checks = {f.check for f in report.findings}
    assert any(c.startswith("jar.string.") for c in checks)
    assert "jar.urls" in checks


def test_hash_always_present(tmp_path):
    jar = tmp_path / "x.jar"
    build_jar(jar)
    report = scan_jar.scan(str(jar))
    assert any(f.check == "jar.hash" for f in report.findings)


def test_directory_mode(tmp_path):
    for i in range(2):
        build_jar(tmp_path / f"p{i}.jar")
    report = scan_jar.scan(str(tmp_path))
    assert len([f for f in report.findings if f.check == "jar.hash"]) == 2


def test_invalid_jar(tmp_path):
    path = tmp_path / "bad.jar"
    path.write_bytes(b"not a zip")
    report = scan_jar.scan(str(path))
    assert any(f.check == "jar.invalid" for f in report.findings)


def test_known_good_hash(tmp_path, monkeypatch):
    jar = tmp_path / "EssentialsX.jar"
    build_jar(jar, name="EssentialsX")
    digest = scan_jar.sha256(str(jar))
    monkeypatch.setattr(
        scan_jar,
        "load_iocs",
        lambda: {
            "files": [],
            "strings": [],
            "known_sha256": {},
            "known_good_sha256": {digest: "EssentialsX test"},
            "plugins": [],
        },
    )
    findings = scan_jar.scan_one(str(jar))
    assert "jar.known-good" in {finding.check for finding in findings}
