# -*- coding: utf-8 -*-
__author__ = 'Администратор'

def test_delete_first_contact(app):
    app.session.login(username = "admin", password = "secret")
    app.contact.delete_first_contact()
    app.session.logout()

def test_delete_button_contact(app):
    app.session.login(username = "admin", password = "secret")
    app.contact.delete_button_contact()
    app.session.logout()