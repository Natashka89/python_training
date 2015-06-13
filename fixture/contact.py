# -*- coding: utf-8 -*-
__author__ = 'Администратор'
from fixture.class_manager import Manager
from selenium.webdriver.common.alert import Alert

class ContactHelper(Manager):

    def creation(self, contact):
        wd = self.app.wd
        self.return_to_home_page()
        self.init_contact_creation_form()
        # fill contact form
        self.fill_contact_form(contact)
        self.submit_contact_creation()

    def delete_first_contact(self):
        wd = self.app.wd
        self.return_to_home_page()
        self.select_first_contact()
        #submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        Alert(wd).accept()

    def submit_contact_creation(self):
        wd = self.app.wd
        # submit_contact_creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def submit_contact_edition(self):
        wd = self.app.wd
        # submit update
        wd.find_element_by_xpath("//input[contains(@value,'Update')]").click()

    def init_contact_creation_form(self):
        wd = self.app.wd
        # init_contact_creation_form
        wd.find_element_by_link_text("add new").click()

    def edit_contact_creation_form(self):
        wd = self.app.wd
        # init_contact_creation_form
        wd.find_element_by_xpath("//a[contains(@href,'edit.php?id')]").click()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.return_to_home_page()
        self.select_first_contact()
        self.edit_contact_creation_form()
        # fill modification form
        self.fill_contact_form(new_contact_data)
        self.submit_contact_edition()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.first)
        self.change_field_value("middlename", contact.middle)
        self.change_field_value("lastname", contact.last)
        self.change_field_value("nickname", contact.nick)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.adress)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_button_contact(self):
        wd = self.app.wd
        self.select_first_contact()
        self.edit_contact_creation_form()
        wd.find_element_by_xpath("//input[contains(@value,'Delete')]").click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_xpath("//a[contains(@href,'edit.php?id')]"))

    def return_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/")):
            wd.find_element_by_link_text("home").click()
