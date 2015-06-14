# -*- coding: utf-8 -*-
__author__ = 'Администратор'

from model.contact import Contact
from random import randrange

#def test_modify_group_first_name_empty(app):
 #   if app.contact.count == 0:
  #      app.contact.create(Contact(name=""))
   # old_contacts = app.contact.get_contact_list()
    #app.contact.modify_first_contact(Contact(first = "New contact first name"))
    #new_contacts = app.contact.get_contact_list()
    #assert len(old_contacts) == len(new_contacts)

def test_modify_group_first_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first="Last contact first name"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(first = "New contact first name")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index]=contact
    assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)

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
