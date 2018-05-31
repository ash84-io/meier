def clean_html(raw_html):
    from bs4 import BeautifulSoup
    if raw_html:
        clean_text = BeautifulSoup(raw_html, "lxml").text
        return clean_text
    else:
        return None