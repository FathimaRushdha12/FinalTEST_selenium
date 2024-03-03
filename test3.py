from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_case_3():
    driver = webdriver.Chrome()
    driver.get("https://fathimarushdha12.github.io/Test_Food_Delivery_Site.github.io/")

    # Click on "About" bar
    about_bar = driver.find_element(By.XPATH, "//*[@id='top']/header/div/nav/ul/li[2]/a")
    about_bar.click()

    # Verify navigation to the About page by checking for an element on the About page
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='top']/header/div/nav/ul/li[2]/a")))
        print("Navigation to the About page failed.")
    except:
        print("Successfully navigated to the About page.")

    driver.quit()


if __name__ == "__main__":
    test_case_3()
