# -*- coding: utf-8 -*-
__author__ = 'Администратор'

from model.contact import Contact

def test_edit_contact(app):
    app.session.login(username = "admin", password = "secret")
    app.contact.edit(Contact("first_up", "middle_up", "last_up", "nick_up", "company_up", "adress_up", "123", "321", "231", "213"))
    app.session.logout()
