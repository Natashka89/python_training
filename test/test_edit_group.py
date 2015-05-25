# -*- coding: utf-8 -*-
__author__ = 'Администратор'

from model.group import Group

def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group("qaw", "uyt", "nyr"))
    app.session.logout()