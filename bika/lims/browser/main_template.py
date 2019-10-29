# -*- coding: utf-8 -*-

from bika.lims import api
from bika.lims import logger
from bika.lims.interfaces import IBootstrapView
from Products.CMFPlone.browser.main_template import MainTemplate as Base
from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.component import getMultiAdapter
from zope.interface import implementer


class MainTemplate(Base):
    """SENAITE Main Template
    """
    def __init__(self, context, request):
        super(MainTemplate, self).__init__(context, request)

    @property
    def macros(self):
        # Reinstanciating the templatefile is a workaround for
        # https://github.com/plone/Products.CMFPlone/issues/2666
        # Without this a inifite recusion in a template
        # (i.e. a template that calls its own view)
        # kills the instance instead of raising a RecursionError.
        return ViewPageTemplateFile(self.template_name).macros


@implementer(IBootstrapView)
class BootstrapView(BrowserView):
    """Twitter Bootstrap helper view for SENAITE LIMS
    """

    def __init__(self, context, request):
        super(BrowserView, self).__init__(context, request)

    def get_icon_for(self, brain_or_object):
        """Get the navigation portlet icon for the brain or object

        The cache key ensures that the lookup is done only once per domain name
        """
        portal_types = api.get_tool("portal_types")
        fti = portal_types.getTypeInfo(api.get_portal_type(brain_or_object))
        icon = fti.getIcon()
        if not icon:
            return ""
        # Always try to get the big icon for high-res displays
        icon_big = icon.replace(".png", "_big.png")
        # fall back to a default icon if the looked up icon does not exist
        if self.context.restrictedTraverse(icon_big, None) is None:
            icon_big = None
        portal_url = api.get_url(api.get_portal())
        title = api.get_title(brain_or_object)
        html_tag = "<img title='{}' src='{}/{}' width='16' />".format(
            title, portal_url, icon_big or icon)
        logger.info("Generated Icon Tag for {}: {}".format(
            api.get_path(brain_or_object), html_tag))
        return html_tag

    def get_viewport_values(self, view=None):
        """Determine the value of the viewport meta-tag
        """
        values = {
            "width": "device-width",
            "initial-scale": "1.0",
        }

        return ",".join("%s=%s" % (k, v) for k, v in values.items())

    def get_columns_classes(self, view=None):
        """Determine whether a column should be shown. The left column is
           called plone.leftcolumn; the right column is called
           plone.rightcolumn.
        """

        layout = getMultiAdapter(
            (self.context, self.request), name=u"plone_layout")
        state = getMultiAdapter(
            (self.context, self.request), name=u"plone_portal_state")

        sl = layout.have_portlets("plone.leftcolumn", view=view)
        sr = layout.have_portlets("plone.rightcolumn", view=view)

        isRTL = state.is_rtl()

        # pre-fill dictionary
        columns = dict(one="", content="", two="")

        if not sl and not sr:
            # we don"t have columns, thus conten takes the whole width
            columns["content"] = "col-md-12"

        elif sl and sr:
            # In case we have both columns, content takes 50% of the whole
            # width and the rest 50% is spread between the columns
            columns["one"] = "col-xs-12 col-md-2"
            columns["content"] = "col-xs-12 col-md-8"
            columns["two"] = "col-xs-12 col-md-2"

        elif (sr and not sl) and not isRTL:
            # We have right column and we are NOT in RTL language
            columns["content"] = "col-xs-12 col-md-10"
            columns["two"] = "col-xs-12 col-md-2"

        elif (sl and not sr) and isRTL:
            # We have left column and we are in RTL language
            columns["one"] = "col-xs-12 col-md-2"
            columns["content"] = "col-xs-12 col-md-10"

        elif (sl and not sr) and not isRTL:
            # We have left column and we are in NOT RTL language
            columns["one"] = "col-xs-12 col-md-2"
            columns["content"] = "col-xs-12 col-md-10"

        return columns
