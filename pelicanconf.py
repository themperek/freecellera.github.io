#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Contributing Developers'
SITENAME = u'Freecellera'
SITEURL = ''

PATH = 'content'
TIMEZONE = 'GMT'

DEFAULT_LANG = u'en'

THEME = "notmyidea"

# Social widget
SOCIAL = [('github', 'http://github.com/freecellera')]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['images']

INDEX_SAVE_AS = 'blog_index.html'
MENUITEMS = [('Home', 'index.html'), ('Blog', 'blog_index.html')]
