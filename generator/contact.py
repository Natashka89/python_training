# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import string
import os.path
import json


constant = [
    Contact(first="first1", middle="middle1", last="last1"),
    Contact(first="first2", middle="middle2", last="last2"),
]

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

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/contact.json")

with open(file, "w") as f:
    f.write(json.dumps(testdata, default = lambda x: x.__dict__, indent = 2))
