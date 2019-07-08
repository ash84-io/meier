from bs4 import BeautifulSoup


def clean_html(raw_html: str) -> str:
    if raw_html:
        return BeautifulSoup(raw_html, "lxml").text
