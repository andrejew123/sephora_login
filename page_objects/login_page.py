import page_objects.base as base
from lookups.locator import Locator


class LoginPage(base.BasePage):
    """
    Buttons and methods used on Search Page
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = "https://www.sephora.pl/secure/user/login.jsp"

        self.email_field = Locator(
            driver=self.driver,
            selector="[type='email']",
        )
        self.password_field = Locator(
            driver=self.driver,
            selector="[type='password']",
        )
        self.login_button = Locator(
            driver=self.driver,
            selector="#handleLogin.btn_red",
        )
        self.account_name = Locator(
            driver=self.driver,
            selector=".nameRegistration",
        )
        self.empty_password_error = Locator(
            driver=self.driver,
            selector="//div[@class = 'erreur']",
            by="xpath",
            many=True,
        )
        self.user_email = "aiigwezwohzbkxdkvd@awdrt.net"

        self.user_password = "12345a"

        self.user_name = "Aaaaa"

    def get_car_by_model(self, car_model):
        return Locator(
            driver=self.driver,
            selector="//tr//td[contains(text(),'{}')]/following-sibling::td/a".format(car_model),
            by="xpath",
            many=True,
        )
