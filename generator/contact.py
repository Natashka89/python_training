# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:],"n:f:",["number of contacts]", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif 0 == "-f":
        f = a

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


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent = 2)
    out.write(jsonpickle.encode(testdata))