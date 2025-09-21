import csv

def save_to_csv(filename, data, header):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([header])
        for item in data:
            writer.writerow([item])

def print_summary(tutorial_links, navbar_items, headings, images):
    print("==== Summary Report ====")
    print("Total tutorial links:", len(tutorial_links))
    print("Total navbar items:", len(navbar_items))
    print("Total headings:", len(headings))
    print("Total images:", len(images))
