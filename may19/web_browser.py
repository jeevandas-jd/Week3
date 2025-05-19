import requests

from selenium import webdriver
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup  # Make sure the package is spelled 'beautifulsoup4' when installing

# If you still get "Import 'bs4' could not be resolved from source", try:
# 1. Run: pip install beautifulsoup4
# 2. Ensure you're using the same Python interpreter in your IDE/terminal as where you installed the package.
# 3. Restart your IDE or Python environment after installing.



def get_page_source(url):
    # Using requests to get the page source
    driver= webdriver.Chrome()
    driver.get(url)
    page_source = driver.page_source
    soup=BeautifulSoup(page_source, 'html.parser')
    driver.quit()
    for tag in soup(['script', 'style', 'nav', 'footer', 'header', 'aside']):
        tag.decompose()

    # Extract meaningful text from visible tags
    content_tags = soup.find_all(['h1', 'h2', 'h3', 'p', 'ul', 'ol', 'li'])
    text_blocks = [tag.get_text(strip=True) for tag in content_tags if tag.get_text(strip=True)]

    return "\n".join(text_blocks)

"""def main():
    url="https://pypi.org/project/beautifulsoup4/"
    #url = "https://www.thehindu.com/news/national/andhra-pradesh/nia-grills-two-youth-arrested-for-possessing-explosive-material-in-vizianagaram/article69593269.ece"
    page_source = get_page_source(url)
    print(page_source)
if __name__ == "__main__":
    main()"""