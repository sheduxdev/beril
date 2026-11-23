import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import ast_rules


def checks_py(text):
    return {finding.check for finding in ast_rules.scan_python("a.py", text)}


def test_shell_true_and_sql_expression():
    checks = checks_py("import subprocess\nsubprocess.run(cmd, shell=True)\ncur.execute(f'select {x}')\n")
    assert {"ast.shell-true", "ast.sql-expression"} <= checks


def test_yaml_and_eval():
    checks = checks_py("import yaml\nyaml.load(data)\neval(source)\n")
    assert {"ast.yaml-load", "ast.eval"} <= checks


def test_timeout_and_jwt():
    checks = checks_py("requests.get(url)\njwt.decode(token)\n")
    assert {"ast.requests-timeout", "ast.jwt-algorithms"} <= checks


def test_syntax_error_is_empty():
    assert ast_rules.scan_python("a.py", "def (") == []


def test_js_rules_need_esprima():
    pytest.importorskip("esprima")
    text = 'require("child_process").exec(cmd);\nres.send(req.query.q);\n'
    checks = {finding.check for finding in ast_rules.scan_js("a.js", text)}
    assert {"ast.child-process", "ast.xss-response"} <= checks


def test_js_syntax_error_is_empty():
    pytest.importorskip("esprima")
    assert ast_rules.scan_js("a.js", "function (") == []


def test_source_audit_includes_ast():
    import source_audit

    checks = {finding.check for finding in source_audit.scan_text("a.py", "eval(x)", "python")}
    assert "ast.eval" in checks
