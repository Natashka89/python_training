# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application_contact import Application_contact


@pytest.fixture
def app_contact(request):
    fixture = Application_contact()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app_contact):
    app_contact.session_contact.login(username = "admin", password = "secret")
    app_contact.contact.creation(Contact("first", "middle", "last", "nick", "company", "adress", "485", "238", "432", "123"))
    app_contact.session_contact.logout()

def test_add_empty_contact(app_contact):
    app_contact.session_contact.login(username = "admin", password = "secret")
    app_contact.contact.creation(Contact("", "", "", "", "", "", "", "", "", ""))
    app_contact.session_contact.logout()


