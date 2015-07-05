# -*- coding: utf-8 -*-
__author__ = 'Администратор'
import re
from model.contact import Contact


def test_contact_properties(app, db):
    list_contacts = app.contact.get_contact_list()
    def clean(contact):
        return Contact(id = contact.id, first = contact.first.strip(), middle = contact.middle.strip(), last = contact.last.strip(),
                       all_phones_from_home_page = merge_phones_like_on_home_page(contact),
                       all_emails_from_home_page = merge_emails_like_on_home_page(contact))
    db_list = map(clean, db.get_contact_list())
    assert sorted(list_contacts, key = Contact.id_or_max) == sorted(db_list, key = Contact.id_or_max)


def clear(s):
    return re.sub("[() -]","", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.mobile, contact.work]))))

def merge_emails_like_on_home_page(contact):
        return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                   [contact.email1, contact.email2, contact.email3])))