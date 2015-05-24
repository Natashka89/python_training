# -*- coding: utf-8 -*-
__author__ = 'Администратор'

class SessionContactHelper():

    def __init__(self, app_contact):
        self.app_contact = app_contact

    def login(self, username, password):
        wd = self.app_contact.wd
        self.app_contact.move_to_url()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    def logout(self):
        wd = self.app_contact.wd
        wd.find_element_by_link_text("Logout").click()
