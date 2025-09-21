from scraper import get_html, get_tutorial_links, get_navbar_items, get_headings, get_image_links
from utils import save_to_csv, print_summary

URL = "https://www.w3schools.com"

def main():
    soup = get_html(URL)

    tutorials = get_tutorial_links(soup)
    navbar = get_navbar_items(soup)
    headings = get_headings(soup)
    images = get_image_links(soup)

    # Save data into CSV
    save_to_csv("tutorial_links.csv", tutorials, "Tutorial Links")
    save_to_csv("navbar_items.csv", navbar, "Navbar Items")
    save_to_csv("headings.csv", headings, "Headings")
    save_to_csv("images.csv", images, "Image Links")

    # Print summary
    print_summary(tutorials, navbar, headings, images)

if __name__ == "__main__":
    main()
