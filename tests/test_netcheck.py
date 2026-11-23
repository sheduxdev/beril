import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import netcheck


def test_sshd_root(tmp_path):
    (tmp_path / "sshd_config").write_text("PermitRootLogin yes\nPasswordAuthentication yes\n")
    report = netcheck.scan(str(tmp_path))
    assert any("root login" in f.title.lower() for f in report.findings)


def test_nftables_default_accept(tmp_path):
    (tmp_path / "nftables.conf").write_text("chain input {\n  policy accept;\n}\n")
    report = netcheck.scan(str(tmp_path))
    assert any("defaults to accept" in f.title for f in report.findings)


def test_empty_dir(tmp_path):
    report = netcheck.scan(str(tmp_path))
    assert report.errors
