import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

def site_scrapper(website_url):
    print("starting the chrome brouser")

    chrome_driver_path = "./chromedriver.exe"

    option = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=option)

    try:
        driver.get(website_url)
        print("page is loaded...")
        html_doc = driver.page_source
        

        return html_doc
    finally:
        driver.quit()


def clean_html_content(html_data):
    soup = BeautifulSoup(html_data, "html.parser")
    content = soup.body
    if content :
        return str(content)
    return ""

def clean_content(content):
    soup = BeautifulSoup(content, "html.parser")

    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()
    
    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )

    return cleaned_content

def split_cleaned_content(content, max_char_hold=6000):
    return [
        content[i: i + max_char_hold] for i in range(0, len(content), max_char_hold)
    ]
