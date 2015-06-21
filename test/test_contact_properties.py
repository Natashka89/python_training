# -*- coding: utf-8 -*-
__author__ = 'Администратор'
import re
from random import randrange

def test_contact_properties(app):
    list_contacts = app.contact.get_contact_list()
    index = randrange(len(list_contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.first == contact_from_edit_page.first
    assert contact_from_home_page.last == contact_from_edit_page.last
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


def clear(s):
    return re.sub("[() -]","", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.mobile, contact.work, contact.fax]))))

def merge_emails_like_on_home_page(contact):
        return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                   [contact.email1, contact.email2, contact.email3])))