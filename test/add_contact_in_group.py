# -*- coding: utf-8 -*-
__author__ = 'Администратор'
from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import random

def test_add_contact_in_group(app, db):
    db = ORMFixture(host="127.0.0.1", name = "addressbook", user="root", password="")
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(last="test"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.contact.add_contact_to_group(contact.id, group)
    app.contact.show_contacts_in_group(group)
    list_contacts = app.contact.get_contact_list()
    def clean(contact):
        return Contact(id = contact.id, first = contact.first.strip(), last = contact.last.strip())
    db_list = map(clean, db.get_contacts_in_group(group))
    assert sorted(list_contacts, key = Contact.id_or_max) == sorted(db_list, key = Contact.id_or_max)



