import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class SeleniumTest(unittest.TestCase):

    def setUp(self):
        # Set up the Chrome WebDriver using WebDriverManager to automatically handle driver installation
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_google_search(self):
        driver = self.driver
        driver.get("https://www.google.com")

        # Find the search box using its name attribute
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("Hello, World!")
        search_box.submit()

        # Wait for the page to load and check if the title contains "Hello, World!"
        self.assertIn("Hello, World!", driver.title)

    def tearDown(self):
        # Close the browser after the test
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
