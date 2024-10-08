from tests.web.pages.page_base import PageBase
from tests.web.helpers.element import Element
from munch import munchify


class LoginPage(PageBase):
    def __init__(self, driver):
        PageBase.__init__(self, driver = driver)

        self.page_elements = {
            'username': Element('//input[@id="username"]', self),
            'password': Element('//input[@id="password"]', self),
            'login': Element('//button[@id="login"]', self),
            'username_logged_in': Element('//label[@id="user-name"]', self),
        }

        self.elements = munchify(self.page_elements)

class RegisterPage(PageBase):
    def __init__(self, driver):
        PageBase.__init__(self, driver = driver)

        self.page_elements = {
            'username': Element('//input[@id="username"]', self),
            'password1': Element('//input[@id="password1"]', self),
            'password2': Element('//input[@id="password2"]', self),
            'register': Element('//button[@id="register"]', self),
            #'username_logged_in': Element('//label[@id="user-name"]', self),
            'username_registered': Element('//div[@id="errormsg"]', self),
        }

        self.elements = munchify(self.page_elements)


class CalcPage(PageBase):
    def __init__(self, driver):
        PageBase.__init__(self, driver = driver)

        self.page_elements = {
            'username': Element('//input[@id="username"]', self),
            'password': Element('//input[@id="password"]', self),
            'login': Element('//button[@id="login"]', self),
            'key1': Element('//button[@id="key-1"]', self),
            'key2': Element('//button[@id="key-2"]', self),
            'key3': Element('//button[@id="key-3"]', self),
            'key4': Element('//button[@id="key-4"]', self),
            'key5': Element('//button[@id="key-5"]', self),
            'key6': Element('//button[@id="key-6"]', self),
            'key8': Element('//button[@id="key-7"]', self),
            'key9': Element('//button[@id="key-8"]', self),
            'key0': Element('//button[@id="key-9"]', self),
            'key0': Element('//button[@id="key-0"]', self),
            'keyadd': Element('//button[@id="key-add"]', self),
            'keysub': Element('//button[@id="key-subtract"]', self),
            'keydiv': Element('//button[@id="key-divide"]', self),
            'keymulti': Element('//button[@id="key-multiply"]', self),
            'keyequals': Element('//button[@id="key-equals"]', self),
            'keyclear': Element('//button[@id="key-clear"]', self),
            'summa': Element('//input[@id="calculator-screen"]', self),
            'historybutton': Element('//button[@id="toggle-button"]', self),
            'historypanel': Element('//textarea[@id="history"]', self)
        }

        self.elements = munchify(self.page_elements)
