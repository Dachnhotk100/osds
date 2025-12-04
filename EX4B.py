from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from getpass import getpass
import time

# ======= Nhập thông tin đăng nhập =======
email_input = input("Nhập email/SDT Facebook: ")
password_input = getpass("Nhập mật khẩu Facebook: ")

# ======= Cấu hình WebDriver =======
gecko_path = r"C:/Users/MIN/repositori/selenium/buoi4/geckodriver.exe"
service = Service(gecko_path)
options = webdriver.FirefoxOptions()
options.binary_location ="C:/Users/MIN/repositori/Mozilla Firefox/firefox.exe"
options.headless = False

driver = webdriver.Firefox(service=service, options=options)

# ======= Login Facebook =======
driver.get("https://www.facebook.com/login")

email_box = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.ID, "email"))
)
email_box.send_keys(email_input)

password_box = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.ID, "pass"))
)
password_box.send_keys(password_input)

login_button = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.NAME, "login"))
)
login_button.click()

time.sleep(500)

# ======= MỞ Ô SOẠN BÀI ĐĂNG =======
post_box = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Bạn đang nghĩ gì?']"))
)
post_box.click()

# ======= NHẬP NỘI DUNG BÀI ĐĂNG =======
content = "Hello, đây là bài đăng được tự động tạo bằng Selenium "

text_area = WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.XPATH, "//div[@role='textbox']"))
)
text_area.send_keys(content)

# ======= NÚT ĐĂNG =======
post_button = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//div[@aria-label='Đăng' or @aria-label='Post']")
    )
)
post_button.click()

time.sleep(10)
driver.quit()
