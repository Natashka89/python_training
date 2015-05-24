# -*- coding: utf-8 -*-
__author__ = 'Администратор'

from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session_contact import SessionContactHelper
from fixture.contact import ContactHelper

class Application_contact:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session_contact = SessionContactHelper(self)
        self.contact = ContactHelper(self)

    def return_to_home_page(self):
        wd = self.wd
        wd.find_element_by_link_text("home page").click()

    def move_to_url(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()