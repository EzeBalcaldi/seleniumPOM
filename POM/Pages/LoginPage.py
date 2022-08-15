from POM.Locators.Locators import Locators
class LoginPage():
    def __init__(self, driver):
        self.driver = driver
        self.username_input_id = Locators.username_input_id
        self.password_input_id = Locators.password_input_id
        self.login_button_id = Locators.login_button_id




    def enterUsername(self, username):
        self.driver.find_element_by_id(self.username_input_id).clear()
        self.driver.find_element_by_id(self.username_input_id).send_keys(username)

    def enterPassword(self, password):
        self.driver.find_element_by_id(self.password_input_id).clear()
        self.driver.find_element_by_id(self.password_input_id).send_keys(password)

    def clickButton(self):
        self.driver.find_element_by_id(self.login_button_id).click()
