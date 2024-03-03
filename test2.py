from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def test_case_2():
    driver = webdriver.Chrome()
    driver.get("https://fathimarushdha12.github.io/Test_Food_Delivery_Site.github.io/")

    # Click on "Reservation" button
    reservation_button = driver.find_element(By.XPATH, "//*[@id='top']/header/div/div/button[2]")
    reservation_button.click()

    # Wait for message box in the footer page to appear
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "message")))
        print("Message box in the footer page appeared.")
    except TimeoutException:
        print("Message box in the footer page did not appear.")

    # Fill in details

    # Trigger pop-up for successful booking

    driver.quit()


if __name__ == "__main__":
    test_case_2()
