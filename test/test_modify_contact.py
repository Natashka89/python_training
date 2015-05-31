# -*- coding: utf-8 -*-
__author__ = 'Администратор'

from model.contact import Contact

def test_modify_group_first_name(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(first = "New contact first name"))
    app.session.logout()

def test_modify_group_middle_name(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(middle = "New contact middle name"))
    app.session.logout()

def test_modify_group_last_name(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(last = "New contact last name"))
    app.session.logout()