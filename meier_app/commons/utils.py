def clean_html(raw_html):
    from bs4 import BeautifulSoup
    cleantext = BeautifulSoup(raw_html, "lxml").text
    return cleantext