# -*- coding: utf-8 -*-
#
# This file is part of SENAITE.CORE.
#
# SENAITE.CORE is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, version 2.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Copyright 2018-2019 by it's authors.
# Some rights reserved, see README and LICENSE.
from Products.CMFCore.permissions import AccessContentsInformation, View, \
    ListFolderContents, ModifyPortalContent

from bika.lims import api
from bika.lims.api import security


def ObjectInitializedEventHandler(client, event):
    """Actions to be done when a client is created
    """
    # Create a new client-specific role. We use the ID of the client as the
    # role name because client id won't never change (while client's name could)
    role = api.get_id(client)
    portal = api.get_portal()
    portal._addRole(role)

    # We manually apply the basic permissions for this client. Contacts from
    # this client will have the role Client too, but role Client does not have
    # these "basic" permissions set to prevent them to access to all Clients.
    permissions = [
        AccessContentsInformation,
        ListFolderContents,
        ModifyPortalContent,
        View
    ]
    for perm in permissions:
        security.grant_permission_for(client, perm, role)
