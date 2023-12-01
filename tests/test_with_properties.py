from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "test_app",
    [{"buildername": "html", "srcdir": "doc_test/pytest_with_properties"}],
    indirect=True,
)
def test_doc_build_html_for_pytest_with_properties(test_app):
    app = test_app
    app.build()
    html = Path(app.outdir, "index.html").read_text(encoding="utf-8")

    assert "Tests: 5" in html
    assert "Failures: 0" in html
    assert "Errors: 0" in html
    assert "Skips: 5" in html

    assert "NTD-SR-032" in html
    assert "tests_requirement_ref" in html
