import sprockets_status


project = 'sprockets-status'
copyright = 'AWeber Communications, Inc.'
version = sprockets_status.version
release = '.'.join(str(v) for v in sprockets_status.version_info[:2])

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.intersphinx']
master_doc = 'index'
source_suffix = '.rst'

html_sidebars = {'**': ['about.html', 'navigation.html']}
html_static_path = ['.']
intersphinx_mapping = {
    'python': ('http://docs.python.org/3/', None),
    'tornado': ('http://tornadoweb.org/en/stable/', None),
}
