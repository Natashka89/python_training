# -*- coding: utf-8 -*-
__author__ = 'Администратор'

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
        return "%s:%s:%s" % (self.id, self.last, self.first)

    def __eq__(self, other):
        return (self.id == other.id and self.last == other.last and self.first == other.first)