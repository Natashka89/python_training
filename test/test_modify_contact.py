# -*- coding: utf-8 -*-
__author__ = 'Администратор'

from model.contact import Contact

def test_modify_group_first_name_empty(app):
    if app.contact.count == 0:
        app.contact.create(Contact(name=""))
    app.contact.modify_first_contact(Contact(first = "New contact first name"))

def test_modify_group_first_name(app):
    if app.contact.count == 0:
        app.contact.create(Contact(name="Last contact first name"))
    app.contact.modify_first_contact(Contact(first = "New contact first name"))

def test_modify_group_middle_name_empty(app):
    if app.contact.count == 0:
        app.contact.create(Contact(middle=""))
    app.contact.modify_first_contact(Contact(middle = "New contact middle name"))

def test_modify_group_middle_name_(app):
    if app.contact.count == 0:
        app.contact.create(Contact(middle="Last contact middle name"))
    app.contact.modify_first_contact(Contact(middle = "New contact middle name"))

def test_modify_group_last_name_empty(app):
    if app.contact.count == 0:
        app.contact.create(Contact(last=""))
    app.contact.modify_first_contact(Contact(last = "New contact last name"))

def test_modify_group_last_name(app):
    if app.contact.count == 0:
        app.contact.create(Contact(last="Last contact last name"))
    app.contact.modify_first_contact(Contact(last = "New contact last name"))
