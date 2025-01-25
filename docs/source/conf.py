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
    # 'sphinx_gallery.gen_gallery', # plotly
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'press'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# References
bibtex_bibfiles = ['refs.bib']
bibtex_bibliography_header = ".. rubric:: References"

# plotly renderer
import plotly.io as pio
pio.renderers.default = 'sphinx_gallery'
