import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import infra


def test_terraform_public_acl(tmp_path):
    (tmp_path / "main.tf").write_text('resource "aws_s3_bucket" "b" {\n  acl = "public-read"\n}\n')
    report = infra.scan(str(tmp_path))
    assert "infra.tf-public-acl" in {f.check for f in report.findings}


def test_k8s_privileged_and_no_policy(tmp_path):
    (tmp_path / "pod.yaml").write_text(
        "apiVersion: v1\nkind: Pod\nspec:\n  containers:\n  - name: x\n    securityContext:\n      privileged: true\n"
    )
    report = infra.scan(str(tmp_path))
    checks = {f.check for f in report.findings}
    assert "infra.k8s-privileged" in checks
    assert "infra.k8s.no-network-policy" in checks


def test_docker_no_user(tmp_path):
    (tmp_path / "Dockerfile").write_text("FROM alpine:3.20\nRUN true\n")
    report = infra.scan(str(tmp_path))
    assert "infra.docker.no-user" in {f.check for f in report.findings}
