# -*- coding: utf-8 -*-

from plone.app.layout.viewlets.common import LogoViewlet as ViewletBase
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class LogoViewlet(ViewletBase):
    index = ViewPageTemplateFile('templates/logo.pt')

    def update(self):
        super(LogoViewlet, self).update()

        portal = self.portal_state.portal()
        bprops = portal.restrictedTraverse("base_properties", None)
        if bprops is not None:
            logoName = bprops.logoName
        else:
            logoName = "logo.png"

        logoTitle = self.portal_state.portal_title()
        logo = portal.restrictedTraverse(logoName, None)
        if logo:
            self.logo_tag = logo.tag(
                title=logoTitle, alt=logoTitle, scale=0.5, css_class="logo")
        else:
            self.logo_tag = ""
        self.navigation_root_title = self.portal_state.navigation_root_title()
