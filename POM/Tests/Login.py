from selenium import webdriver
from POM.Pages.LoginPage import LoginPage
from POM.Pages.HomePage import HomePage
import unittest










class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\Users\ezequ\PycharmProjects\seleniumTest\drivers\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login(cls):
        URL = "https://opensource-demo.orangehrmlive.com/"
        user = "Admin"
        password = "admin123"
        driver = cls.driver

        driver.get(URL)

        login = LoginPage(driver)
        homePage = HomePage(driver)

        login.enterUsername(user)
        login.enterPassword(password)
        login.clickButton()
        homePage.clickWelcome()
        homePage.logout()



    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test finished")












