# -*- coding: utf-8 -*-
__author__ = 'Администратор'

from model.contact import Contact
import random

#def test_modify_group_first_name_empty(app):
 #   if app.contact.count == 0:
  #      app.contact.create(Contact(name=""))
   # old_contacts = app.contact.get_contact_list()
    #app.contact.modify_first_contact(Contact(first = "New contact first name"))
    #new_contacts = app.contact.get_contact_list()
    #assert len(old_contacts) == len(new_contacts)

def test_modify_contact_first_last_name(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first="Last contact first name"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.select_contact_by_id(contact.id)
    contact_new = Contact(first = "New contact first name", last = "New contact last name")
    contact_new.id = contact.id
    app.contact.modify_contact_by_id(contact_new.id, contact_new)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts.remove(contact)
    old_contacts.append(contact_new)
    assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

#def test_modify_group_middle_name_empty(app):
 #   if app.contact.count == 0:
  #      app.contact.create(Contact(middle=""))
   # old_contacts = app.contact.get_contact_list()
    #app.contact.modify_first_contact(Contact(middle = "New contact middle name"))
    #new_contacts = app.contact.get_contact_list()
    #assert len(old_contacts) == len(new_contacts)

#def test_modify_group_middle_name_(app):
 #   if app.contact.count == 0:
  #      app.contact.create(Contact(middle="Last contact middle name"))
   # old_contacts = app.contact.get_contact_list()
    #app.contact.modify_first_contact(Contact(middle = "New contact middle name"))
    #new_contacts = app.contact.get_contact_list()
    #assert len(old_contacts) == len(new_contacts)

#def test_modify_group_last_name_empty(app):
 #   if app.contact.count == 0:
  #      app.contact.create(Contact(last=""))
   # old_contacts = app.contact.get_contact_list()
    #app.contact.modify_first_contact(Contact(last = "New contact last name"))
    #new_contacts = app.contact.get_contact_list()
    #assert len(old_contacts) == len(new_contacts)

#def test_modify_group_last_name(app):
 #   if app.contact.count == 0:
  #      app.contact.create(Contact(last="Last contact last name"))
   # old_contacts = app.contact.get_contact_list()
    #app.contact.modify_first_contact(Contact(last = "New contact last name"))
    #new_contacts = app.contact.get_contact_list()
    #assert len(old_contacts) == len(new_contacts)
