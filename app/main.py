import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_stealth import stealth
from flask import Flask, request, jsonify
import time
import json
import os

options = Options()
options.add_argument("--headless");
options.add_argument("--disable-gpu");
options.add_argument("--no-sandbox");
options.add_argument("--enable-javascript")

def init_webdriver():
    driver = webdriver.Chrome(options=options)
    stealth(driver, platform="Win32")
    return driver
    
print("Браузер успешно открыт")

app = Flask(__name__)

driver = init_webdriver()
@app.route('/post_endpoint', methods=['POST'])
def handle_post():
    url = request.json['url']
    print(url)
    driver.get(url)
    print(driver.page_source)
    time.sleep(5)
    product_link = driver.current_url
    product_title = driver.find_element(By.CLASS_NAME, "sm1_27").text
    product_price = driver.find_element(By.CLASS_NAME, "rm5_27").text

    response_data = {'status': 'success', 'link': f'{product_link}', 'title': f'{product_title}', 'price': f'{product_price}'}
    return jsonify(response_data)
