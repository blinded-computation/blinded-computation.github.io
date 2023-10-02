# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Blinded Memory'
copyright = '2022&ndash;2023 Secure Systems Group'
author = 'H ElAtali, L J Gunn, H Liljestrand, N Asokan'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.mathjax',
    'fslit.sphinx4fstar',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
#        'searchbox.html',
    ]
}

import os
import sys
sys.path.insert(0, os.path.abspath('/home/lachlan/fstar-mode.el/etc'))

github_repo = 'ssg-research/BliMe'
github_button = True
