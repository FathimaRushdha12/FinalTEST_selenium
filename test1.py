from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_case_1():
    driver = webdriver.Chrome()
    driver.get("https://fathimarushdha12.github.io/Test_Food_Delivery_Site.github.io/")

    # Click on "Book Table" button
    book_table_button = driver.find_element(By.XPATH, "//*[@id='home']/div/div/button")
    book_table_button.click()

    # Wait for the popup message to appear
    try:
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert_text = alert.text
        print("Alert text:", alert_text)
        alert.accept()  # Dismiss the alert
        print("Alert dismissed.")
    except:
        print("No alert found.")

    # Add a delay to allow any potential alerts to be dismissed
    time.sleep(2)  # Adjust the delay time as needed

    # Scroll to the footer page where the social links are located
    footer = driver.find_element(By.TAG_NAME, "footer")
    driver.execute_script("arguments[0].scrollIntoView(true);", footer)

    driver.quit()


if __name__ == "__main__":
    test_case_1()
