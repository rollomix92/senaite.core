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

from setuptools import setup, find_packages

version = '2.0.0'

setup(
    name='senaite.core',
    version=version,
    description="SENAITE Core",
    long_description=open("README.rst").read() + "\n" +
    open("RELEASE_NOTES.rst").read() + "\n" +
    open("CHANGES.rst").read() + "\n",
    # Get more strings from
    # http://pypi.python.org/pypi?:action=list_classifiers
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Zope2",
        "Programming Language :: Python",
    ],
    keywords=['senaite', 'lims', 'opensource'],
    author='SENAITE Foundation',
    author_email='support@senaite.com',
    url='https://github.com/senaite/senaite.core',
    license='GPLv2',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['bika'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'plone.api',
        'plone.subrequest',
        'plone.jsonapi.core',
        'Products.ATExtensions',
        'Products.CMFEditions',
        'Products.DataGridField',
        # 'Products.TinyMCE',
        'Products.TextIndexNG3',
        'collective.monkeypatcher',
        'collective.js.jqueryui',
        'plone.app.z3cform',
        'openpyxl==1.5.8',
        'plone.app.iterate',
        'magnitude',
        'jarn.jsi18n',
        'collective.progressbar',
        'plone.app.dexterity',
        'plone.app.relationfield',
        'plone.app.referenceablebehavior',
        'z3c.jbot',
        'plone.resource',
        'zopyx.txng3.ext==3.4.0',
        'senaite.core.supermodel',
        'senaite.core.listing',
        'senaite.impress',
        'archetypes.referencebrowserwidget',
        'plonetheme.sunburst',
        # Python 2/3 compatibility library: https://six.readthedocs.io/
        'six',
    ],
    extras_require={
        'test': [
            'unittest2',
            'plone.app.testing',
        ]
    },
    entry_points="""
          # -*- Entry points: -*-
          [z3c.autoinclude.plugin]
          target = plone
          """,
)
