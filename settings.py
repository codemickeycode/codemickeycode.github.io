from __future__ import unicode_literals

AUTHOR = 'Micaela Reyes'
SITENAME = 'codemickeycode'
TAGLINE = 'Code. Passion. Freedom. Making a Difference :)'
USER_LOGO_URL = 'http://www.gravatar.com/avatar/a39a05d336c2733ca8a9553f9a2284ab.png?size=140x140'
SITEURL = 'http://codemickeycode.github.io'
DEFAULT_DATE_FORMAT = '%A, %B %d, %Y'
SUMMARY_MAX_LENGTH = (50)

GITHUB_URL = 'https://github.com/codemickeycode/codemickeycode.github.com'
#DISQUS_SITENAME = ''
#GOOGLE_ANALYTICS = ''

FEED_DOMAIN = SITEURL
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
FEED_ALL_ATOM = 'feeds/all.atom.xml'

SOCIAL = (('@codemickeycode', 'https://twitter.com/codemickeycode'),
          ('opensource', 'https://github.com/codemickeycode'),
          ('email', 'mailto:codemickeycode@gmail.com'),)
TWITTER_USERNAME = 'codemickeycode'

THEME = '.pelican_themes/pelican-svbhack'
TIMEZONE = 'Asia/Manila'
DEFAULT_PAGINATION = 4

MARKUP = (('md', 'rst'))
MD_EXTENSIONS = (['codehilite', 'extra'])	
