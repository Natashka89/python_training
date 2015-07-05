# -*- coding: utf-8 -*-
__author__ = 'Администратор'
from model.contact import Contact
import random
import time


def test_delete_first_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(last="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    time.sleep(20)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert new_contacts == old_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

#def test_delete_button_contact(app):
 #   if app.contact.count == 0:
  #      app.contact.create(Contact(last="test"))
   # old_contacts = app.contact.get_contact_list()
    #app.contact.delete_button_contact()
    #new_contacts = app.contact.get_contact_list()
    #assert len(old_contacts) - 1 == len(new_contacts)