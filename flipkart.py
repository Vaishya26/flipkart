import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import chromedriver_binary
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox')
class Flipkart:
    x= 0

    def flipkart(self,page_url):
        z = []
        
        driver = webdriver.Chrome(executable_path = '/usr/lib/chromium-browser/chromedriver', options=chrome_options)
        driver.get(page_url)
        rows = driver.find_elements_by_css_selector("div.hCUpcT > div:nth-child(2) > div.bhgxx2")
        for i in rows:
            for j in range(1,5):
                d ={}
                try:
                    image_url = i.find_element_by_css_selector("div._3O0U0u div:nth-child("+str(j)+") div._1SSAGr a._3dqZjq div div div._3JlYXy div._3ZJShS img._3togXc").get_attribute("src")
                except NoSuchElementException:
                    image_url = ""
                try:
                    url = i.find_element_by_css_selector("div._3O0U0u div:nth-child("+str(j)+") div._1SSAGr a._3dqZjq").get_attribute("href")
                except NoSuchElementException:
                    url = ""
                try:
                    title = i.find_element_by_css_selector("div._3O0U0u div:nth-child("+str(j)+") div._1SSAGr  div._2LFGJH a._2mylT6").text
                except NoSuchElementException:
                    title = ""
                try:
                    price = i.find_element_by_css_selector("div._3O0U0u div:nth-child("+str(j)+") div._1SSAGr  div._2LFGJH a._2W-UZw ._1uv9Cb ._1vC4OE").text
                except NoSuchElementException:
                    price = ""

                mrp_ = i.find_elements_by_css_selector("div._3O0U0u div:nth-child("+str(j)+") div._1SSAGr  div._2LFGJH a._2W-UZw ._1uv9Cb ._3auQ3N")
                if(len(mrp_)!=0):
                    mrp = mrp_[0].text
                else:
                    mrp = ""
                try:
                    savings = i.find_element_by_css_selector("div._3O0U0u div:nth-child("+str(j)+") div._1SSAGr  div._2LFGJH a._2W-UZw ._1uv9Cb .VGWI6T").text
                except NoSuchElementException:
                    savings = ""
                Flipkart.x+=1
                d["url"] = url
                d["title"] = title
                d["price"] = price
                d["image"] = image_url
                d["mrp"] = mrp
                d["savings"] = savings
                d["code"] = "fk_"+str(Flipkart.x)
                Flipkart.z.append(d)
        with open("products_flipkart_nike_shoes.json",'a') as f:
            json.dump(Flipkart.z,f,indent=4)
instance = Flipkart()
driver_ = webdriver.Chrome(executable_path='/usr/lib/chromium-browser/chromedriver', options=chrome_options)
driver_.get('https://www.flipkart.com/search?q=nike%20shoes&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off')
num_ = driver_.find_element_by_css_selector("div.hCUpcT > div:nth-child(2) > div:nth-child(12) div div._2zg3yZ span").text.split()[3]
for i in range(1,int(num_)+1):
    page_url = "https://www.flipkart.com/search?q=nike+shoes&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)
    instance.flipkart(page_url)
