import os
import sys
sys.path.append(os.curdir)

AUTHOR = 'Robotic Perception Lab'
SITENAME = 'Robotic Perception Lab'
SITEURL = ''
# THEME = "/home/danfergo/pelican-themes/html5-dopetrope"
THEME = "theme/"
# THEME = "/home/danfergo/pelican-themes/pelican-fh5co-marble"
# THEME = "/home/danfergo/pelican-themes/MinimalXY"

PATH = 'content'

ABOUT_LINK = 'pages/about.html'
ABOUT_TEXT = """
    The smARTLab is part of the Agent ART research group in the Department of Computer Science and its members carry out research in the areas of swarm intelligence, (bio-inspired) machine learning, planning, multi-robot systems, human-robot interaction, probabilistic robotics, and unmanned aerial vehicles.
"""


# PATH_METADATA = '(?P<path_no_ext>.*)\..*'
# ARTICLE_URL = '{path_no_ext}'

# PLUGINS = ['i18n_subsites', 'tipue_search']

TIMEZONE = 'GMT'

DEFAULT_LANG = 'en-GB'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


ACTIVITIES = (
    ('ICRA Vitac Workshop', 'icra-vitac-workshop'),
    ('Reading Group', 'icra-vitac-workshop'),
    ('RoboCup@Work', 'icra-vitac-workshop'),
    ('ICRA Vitac Workshop', 'icra-vitac-workshop'),

)

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True