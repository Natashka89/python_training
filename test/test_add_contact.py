# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters+string.digits+string.punctuation+" "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_phone(maxlen):
    symbols = string.digits+"-"*10+"("*10+")"*10+" "*10
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(first = "", last = "", middle = "", home = "", mobile = "", work = "", fax = "")]+[
    Contact(first = random_string("first",10) ,last = random_string("last",10),middle = random_string("middle",10),
            home = random_phone(5), mobile = random_phone(5), work = random_phone(5), fax = random_phone(5),
            email1 = random_string("email",10), email2 = random_string("email2",10), email3 = random_string("email3",10)
          )
    for i in range(5)
]

@pytest.mark.parametrize("contact", testdata, ids = [repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key= Contact.id_or_max) == sorted(new_contacts, key= Contact.id_or_max)


