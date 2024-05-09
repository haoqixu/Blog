#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "xu0o0"
SITENAME = "~xu0o0"
SITEURL = "//blog.xu0o0.org"

PATH = "content"

TIMEZONE = "Asia/Shanghai"
DEFAULT_LANG = "zh"
LOCALE = "zh_CN.UTF-8"

DATE_FORMATS = {
    "en": (("en_US", "utf8"), "%a %Y-%b-%d"),
    "zh": (("zh_CN", "utf8"), "%Y年%m月%d日(周%a)"),
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = ()

SOCIAL = [
    ("github", "https://github.com/haoqixu"),
    ("twitter", "https://twitter.com/haoqixu_0o0"),
    ("envelope-o", "mailto:hqcat6@gmail.com"),
]

DEFAULT_PAGINATION = 10

PATH = "content"
STATIC_PATHS = ["img", "static"]

THEME = "theme"
SITELOGO = "/img/avatar.jpg"
SITETITLE = "~xu0o0"
OG_LOCALE = "zh_CN"
CC_LICENSE = {"name": "CC-BY-NC-SA", "version": "4.0", "slug": "by-nc-sa"}
MAIN_MENU = True
MENUITEMS = [
    ("archives", "/archives.html"),
    ("categories", "/categories.html"),
    ("tags", "/tags.html"),
]

STATIC_PATHS = ["static", "img", "static/CNAME"]

EXTRA_PATH_METADATA = {"static/CNAME": {"path": "CNAME"}}

MARKDOWN = {
    "extension_configs": {
        "admonition": {},
        "toc": {},
        "codehilite": {"css_class": "highlight", "linenums": False},
        "extra": {},
    }
}

ARTICLE_URL = "posts/{date:%Y}/{date:%m}/{slug}.html"
ARTICLE_SAVE_AS = "posts/{date:%Y}/{date:%m}/{slug}.html"
ARTICLE_LANG_URL = "posts/{date:%Y}/{date:%m}/{slug}-{lang}.html"
ARTICLE_LANG_SAVE_AS = "posts/{date:%Y}/{date:%m}/{slug}-{lang}.html"
YEAR_ARCHIVE_SAVE_AS = "posts/{date:%Y}/index.html"
MONTH_ARCHIVE_SAVE_AS = "posts/{date:%Y}/{date:%m}/index.html"

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
