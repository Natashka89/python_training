# -*- coding: utf-8 -*-
__author__ = 'Администратор'

from fixture.class_manager import Manager

class SessionContactHelper(Manager):

    def login(self, username, password):
        wd = self.app.wd
        self.app.move_to_url()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()