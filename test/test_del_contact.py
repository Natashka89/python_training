# -*- coding: utf-8 -*-
__author__ = 'Администратор'
from model.contact import Contact
from random import randrange


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(last="test"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[index:index+1] = []
    assert new_contacts == old_contacts

#def test_delete_button_contact(app):
 #   if app.contact.count == 0:
  #      app.contact.create(Contact(last="test"))
   # old_contacts = app.contact.get_contact_list()
    #app.contact.delete_button_contact()
    #new_contacts = app.contact.get_contact_list()
    #assert len(old_contacts) - 1 == len(new_contacts)