# -*- coding: utf-8 -*-

from cgi import escape

from plone.app.layout.viewlets.common import GlobalSectionsViewlet
from Products.CMFPlone.utils import safe_unicode
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.component import getMultiAdapter


class SectionsDropdownViewlet(GlobalSectionsViewlet):
    index = ViewPageTemplateFile("templates/sections_dropdown.pt")

    def update(self):
        super(SectionsDropdownViewlet, self).update()
        portal_state = getMultiAdapter((self.context, self.request),
                                       name=u"plone_portal_state")
        self.navigation_root_url = portal_state.navigation_root_url()
        self.portal_title = escape(
            safe_unicode(portal_state.navigation_root_title()))
