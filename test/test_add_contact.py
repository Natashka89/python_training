# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application_contact import Application_contact

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

@pytest.fixture
def app_contact(request):
    fixture = Application_contact()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app_contact):
    app_contact.login(username = "admin", password = "secret")
    app_contact.fill_contact_creation_form(Contact("first", "middle", "last", "nick", "company", "adress", "485", "238", "432", "123"))
    app_contact.logout()

def test_add_empty_contact(app_contact):
    app_contact.login(username = "admin", password = "secret")
    app_contact.fill_contact_creation_form(Contact("", "", "", "", "", "", "", "", "", ""))
    app_contact.logout()


