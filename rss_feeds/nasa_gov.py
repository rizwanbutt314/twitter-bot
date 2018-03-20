import requests
from bs4 import BeautifulSoup


# Not needed now
def already_posted(post_link=''):
    pass


# Packing up each RSS feed in specific format
def process_items(items):
    print("Processing feeds...")
    processed_items = list()
    for item in items:
        processed_items.append({
            'post_title': item.find('title').get_text().encode('utf-8').strip(),
            'post_link': item.find('link').get_text().strip(),
            'post_pubDate': item.find('pubDate').get_text().encode('utf-8').strip(),
            'post_description': item.find('description').get_text().encode('utf-8').strip()[:120] + '...'
        })

    return processed_items


# Extracting RSS feeds
def main(NASA_GOV_URL):
    print("Extracting Feeds from: {0}".format(NASA_GOV_URL))
    # Getting RSS feeds
    response = requests.get(NASA_GOV_URL)

    # Parsing XML content
    soup = BeautifulSoup(response.content, 'xml')
    all_items = soup.find_all('item')
    processed_items = process_items(all_items)
    print("Feeds Extracted !")
    return processed_items
