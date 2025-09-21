import requests
from bs4 import BeautifulSoup

def get_html(url):
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

def get_tutorial_links(soup):
    anchors = soup.find_all('a')
    tutorial_links = []
    for a in anchors:
        href = a.get('href')
        if href and "tutorial" in href:
            full_link = "https://www.w3schools.com" + href
            tutorial_links.append(full_link)
    return tutorial_links

def get_navbar_items(soup):
    navbar = soup.find('nav')
    return [item for item in navbar.stripped_strings] if navbar else []

def get_headings(soup):
    return [h.get_text().strip() for h in soup.find_all(['h1', 'h2', 'h3'])]

def get_image_links(soup):
    return [img['src'] for img in soup.find_all('img') if img.get('src')]
