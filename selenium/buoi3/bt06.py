from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import re

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

all_links = []
d = pd.DataFrame({"name":[], "birth":[], "death":[], "nationality":[]})

for i in range(ord("A"), ord("Z")+1):
    letter = chr(i)
    try:
        url = f"https://en.wikipedia.org/wiki/List_of_painters_by_name_beginning_with_%22{letter}%22"
        driver.get(url)
        time.sleep(2)

        ul = driver.find_element(By.XPATH, "(//div[@class='mw-parser-output']/ul)[1]")
        li_tags = ul.find_elements(By.TAG_NAME, "li")

        for li in li_tags:
            a = li.find_element(By.TAG_NAME, "a")
            all_links.append(a.get_attribute("href"))
    except:
        pass

driver.quit()

driver = webdriver.Chrome(options=options)

for link in all_links:
    try:
        driver.get(link)
        time.sleep(2)

        try:
            name = driver.find_element(By.TAG_NAME, "h1").text
        except:
            name = ""

        try:
            birth = driver.find_element(By.XPATH, "//th[text()='Born']/following-sibling::td").text
            birth = re.findall(r"[0-9]{1,2}\s+[A-Za-z]+\s+[0-9]{4}", birth)[0]
        except:
            birth = ""

        try:
            death = driver.find_element(By.XPATH, "//th[text()='Died']/following-sibling::td").text
            death = re.findall(r"[0-9]{1,2}\s+[A-Za-z]+\s+[0-9]{4}", death)[0]
        except:
            death = ""

        try:
            nationality = driver.find_element(By.XPATH, "//th[text()='Nationality']/following-sibling::td").text
        except:
            nationality = ""

        painter = {"name": name, "birth": birth, "death": death, "nationality": nationality}
        d = pd.concat([d, pd.DataFrame([painter])], ignore_index=True)
    except:
        pass

driver.quit()

file_name = "Painters.xlsx"
d.to_excel(file_name, index=False)
print("Data exported to:", file_name)