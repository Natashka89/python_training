# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username = "admin", password = "secret")
    app.contact.creation(Contact("first", "middle", "last", "nick", "company", "adress", "485", "238", "432", "123"))
    app.session.logout()

def test_add_empty_contact(app):
    app.session.login(username = "admin", password = "secret")
    app.contact.creation(Contact("", "", "", "", "", "", "", "", "", ""))
    app.session.logout()


