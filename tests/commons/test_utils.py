from meier.commons.utils import clean_html


def test_clean_html():
    assert clean_html("str") == "str"
    assert clean_html("<b>boy</b>") == "boy"
