import os
import smtplib
from email.message import EmailMessage

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

user = "nn1701505@gmail.com"
password = os.getenv("GMAIL_APP_PASSWORD")

if not password:
    raise ValueError("Set GMAIL_APP_PASSWORD environment variable before running this script.")

website = "https://www.thehindu.com/latest-news/"
local_driver_path = r"C:\Users\Naveen\OneDrive\Desktop\Python Automation\chromedriver-win64\chromedriver-win64\chromedriver.exe"

options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

if os.name == "nt" and os.path.exists(local_driver_path):
    service = Service(executable_path=local_driver_path)
    driver = webdriver.Chrome(service=service, options=options)
else:
    driver = webdriver.Chrome(options=options)

driver.get(website)
containers = driver.find_elements(by="xpath", value='//div[@class="right-content"]')

news_items = {}

for container in containers:
    title = container.find_element(by="xpath", value="./h3").text
    link = container.find_element(by="xpath", value="./h3/a").get_attribute("href")
    news_items[title] = link

driver.quit()

for title, link in news_items.items():
    print(f"{title} : \n     {link}\n")

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.starttls()
    smtp.login(user=user, password=password)

    msg = EmailMessage()
    msg["Subject"] = "Latest News"
    msg["From"] = user
    msg["To"] = "nnaveenprakash2003@gmail.com"

    body = "Check out the latest news!\n\n" + "\n".join(
        [f"{title}: {link}" for title, link in news_items.items()]
    )
    msg.set_content(body, charset="utf-8")
    smtp.send_message(msg)
