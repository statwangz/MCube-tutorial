# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'MCube'
copyright = '2025, Zhiwei Wang'
author = 'Zhiwei Wang'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.bibtex', # Manage bibliography
    'nbsphinx', # Jupyter Notebook tools for Sphinx
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

# html_theme = 'sphinx_rtd_theme'
html_theme = 'press'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# References
bibtex_bibfiles = ['refs.bib']
bibtex_bibliography_header = ".. rubric:: References"

def remove_jquery_and_underscore(app):
    # We need to remove the jquery and underscore file that are
    # added by default because we already add it in the <head> tag.
    remove = lambda x: not any(js in x for js in ['jquery', 'underscore'])
    if hasattr(app.builder, 'script_files'):
        app.builder.script_files = [x for x in app.builder.script_files
                                    if remove(x)]

def setup(app):
    app.connect('builder-inited', remove_jquery_and_underscore)