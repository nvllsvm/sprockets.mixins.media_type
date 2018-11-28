import pkg_resources

needs_sphinx = '1.0'
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.viewcode',
              'sphinx.ext.intersphinx',
              'sphinxcontrib.autohttp.tornado']
master_doc = 'index'
project = 'sprockets.mixins.mediatype'
copyright = '2015-2016, AWeber Communications'
release = pkg_resources.get_distribution('sprockets.mixins.mediatype').version
version = '.'.join(release.split('.')[0:1])

html_style = 'custom.css'
html_static_path = ['static']
html_sidebars = {
    '**': ['about.html', 'navigation.html'],
}
html_theme_options = {
    'github_user': 'sprockets',
    'github_repo': 'sprockets.mixins.media_type',
    'description': 'Content-Type negotation mix-in',
    'github_banner': True,
    'travis_button': True,
    'sidebar_width': '230px',
    'codecov_button': True,
}

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'requests': ('https://requests.readthedocs.org/en/latest/', None),
    'sprockets': ('https://sprockets.readthedocs.org/en/latest/', None),
    'tornado': ('http://tornadoweb.org/en/latest/', None),
}
