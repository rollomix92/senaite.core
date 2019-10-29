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

from bika.lims.catalog.analysis_catalog import CATALOG_ANALYSIS_LISTING


def searchResults(self, query=None, **kw):
    """Search the catalog

    Search terms can be passed as a query or as keyword arguments.
    """

    if query and query.get("getRequestUID") \
            and self.id == CATALOG_ANALYSIS_LISTING:

        # Fetch all analyses that have the request UID passed in as an
        # ancestor, cause we want Primary ARs to always display the analyses
        # from their derived ARs (if result is not empty)

        _query = query.copy()
        orig_uid = _query.get("getRequestUID")

        # If a list of _query uid, retrieve them sequentially to make the
        # masking process easier
        if isinstance(orig_uid, list):
            results = list()
            for uid in orig_uid:
                _query["getRequestUID"] = [uid]
                results += self.searchResults(query=_query, **kw)
            return results

        # Get all analyses, those from descendant ARs included
        del _query["getRequestUID"]
        _query["getAncestorsUIDs"] = orig_uid
        results = self.searchResults(query=_query, **kw)

        # Masking
        primary = filter(lambda an: an.getParentUID == orig_uid, results)
        derived = filter(lambda an: an.getParentUID != orig_uid, results)
        derived_keys = map(lambda an: an.getKeyword, derived)
        results = filter(lambda an: an.getKeyword not in derived_keys, primary)
        return results + derived

    # Normal search
    return self._catalog.searchResults(query, **kw)
