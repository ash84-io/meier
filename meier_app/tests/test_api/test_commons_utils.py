from meier_app.commons.utils import clean_html


def test_clean_html():
    test1 = clean_html(raw_html="<h1>test</h1>")
    assert test1 == "test"
    test2 = clean_html(raw_html=None)
    assert test2 is None
    test3 = clean_html(raw_html="<h1><div>test</div></h1>")
    assert test3 == "test"
