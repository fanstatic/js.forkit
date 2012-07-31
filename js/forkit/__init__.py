# -*- coding: utf-8 -*-

from fanstatic import Group
from fanstatic import Library
from fanstatic import Resource

library = Library('forkit.js', 'resources')

forkit_css = Resource(library,
                      'css/forkit.css',
                      minified='css/forkit.min.css')

forkit_js = Resource(library,
                     'js/forkit.js',
                     minified='js/forkit.min.js')

forkit = Group([forkit_css, forkit_js, ])
