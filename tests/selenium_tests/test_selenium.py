import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

class SeleniumTest(unittest.TestCase):

    def setUp(self):
        # Set up Chrome options to run headless
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run headless
        chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
        chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

        # Set up the Chrome WebDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

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
