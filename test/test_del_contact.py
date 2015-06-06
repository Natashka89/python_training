# -*- coding: utf-8 -*-
__author__ = 'Администратор'
from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count == 0:
        app.contact.create(Contact(name="test"))
    app.contact.delete_first_contact()

def test_delete_button_contact(app):
    app.contact.delete_button_contact()
