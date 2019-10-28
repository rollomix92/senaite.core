# -*- coding: utf-8 -*-

from plone.app.layout.viewlets.common import PathBarViewlet as BaseViewlet
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class PathBarViewlet(BaseViewlet):
    index = ViewPageTemplateFile("templates/path_bar.pt")
