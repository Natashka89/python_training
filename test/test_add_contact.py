# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact("first", "middle", "last", "nick", "company", "adress", "485", "238", "432", "123")
    app.contact.creation(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)

#def test_add_empty_contact(app):
 #   old_contacts = app.contact.get_contact_list()
  #  app.contact.creation(Contact("", "", "", "", "", "", "", "", "", ""))
   # new_contacts = app.contact.get_contact_list()
    #assert len(old_contacts) + 1 == len(new_contacts)

