# -*- coding: utf-8 -*-
__author__ = 'Администратор'
from fixture.class_manager import Manager
from selenium.webdriver.common.alert import Alert
from model.contact import Contact
import re

class ContactHelper(Manager):

    def create(self, contact):
        wd = self.app.wd
        self.return_to_home_page()
        self.init_contact_creation_form()
        # fill contact form
        self.fill_contact_form(contact)
        self.submit_contact_creation()
        self.contact_cache = None

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.return_to_home_page()
        self.select_contact_by_index(index)
        #submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        Alert(wd).accept()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

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

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.return_to_home_page()
        self.select_contact_by_index(index)
        self.edit_contact_creation_form()
        # fill modification form
        self.fill_contact_form(new_contact_data)
        self.submit_contact_edition()
        self.contact_cache = None

    def modify_first_contact(self, new_contact_data):
        self.modify_first_contact(0)

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
        self.return_to_home_page()
        self.select_first_contact()
        self.edit_contact_creation_form()
        wd.find_element_by_xpath("//input[contains(@value,'Delete')]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_first_contact(self):
        self.select_contact_by_index(0)

    def count(self):
        wd = self.app.wd
        self.return_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))
#wd.find_elements_by_xpath("//a[contains(@href,'edit.php?id')]"))

    def return_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/")):
            wd.find_element_by_link_text("home").click()

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.return_to_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                firstname = cells[2].text
                lastname = cells[1].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text
                all_emails = cells[4].text
                self.contact_cache.append(Contact(first = firstname, last = lastname, id = id,all_phones_from_home_page = all_phones, all_emails_from_home_page = all_emails))
        return list(self.contact_cache)

    def open_contact_edit_by_index(self, index):
        wd = self.app.wd
        self.return_to_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.return_to_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        fax = wd.find_element_by_name("fax").get_attribute("value")
        email1 = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(first = firstname, last = lastname, id = id,
                       home = home, work = work,
                       mobile = mobile, fax = fax,
                       email1 = email1, email2 = email2, email3 = email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home = re.search("H: (.*)",text).group(1)
        work = re.search("W: (.*)",text).group(1)
        mobile = re.search("M: (.*)",text).group(1)
        fax = re.search("F: (.*)",text).group(1)
        return Contact(home = home, work = work,
                mobile = mobile, fax = fax)