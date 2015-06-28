# -*- coding: utf-8 -*-
from model.group import Group
import random
import string
import os.path
import json


constant = [
    Group(name="name1", header = "header1", footer= "footer1"),
    Group(name="name2", header = "header2", footer= "footer2")
]

def random_string(prefix, maxlen):
    symbols = string.ascii_letters+string.digits+string.punctuation+" "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Group(name = "", header = "", footer = "")]+[
    Group(name = random_string("name",10) ,header = random_string("header",20),footer = random_string("footer",20))
    for i in range(5)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/group.json")

with open(file, "w") as f:
    f.write(json.dumps(testdata, default = lambda x: x.__dict__, indent = 2))