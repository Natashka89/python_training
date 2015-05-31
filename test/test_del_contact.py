# -*- coding: utf-8 -*-
__author__ = 'Администратор'

def test_delete_first_contact(app):
    app.contact.delete_first_contact()

def test_delete_button_contact(app):
    app.contact.delete_button_contact()
