# -*- coding: utf-8 -*-
__author__ = 'Администратор'
from sys import maxsize

class Contact:

    def __init__(self, first= None, middle= None, last= None, nick= None, company= None, adress= None, home= None, mobile= None, work= None, fax= None, id=None):
        self.first = first
        self.middle = middle
        self.last = last
        self.nick = nick
        self.company = company
        self.adress = adress
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.first, self.last)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.first == other.first and self.last == other.last
               #(self.first is None or other.first is None or self.first == other.first) and (self.last is None or other.last is None or self.last == other.last)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
