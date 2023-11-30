#
# testreport test docs documentation build configuration file, created by
# sphinx-quickstart on Tue Mar 28 11:37:14 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
from ast import literal_eval
import os
from pprint import pprint
import sys

from sphinxcontrib.test_reports.directives.test_case import TestCase
from sphinx_needs.needs import Need

sys.path.insert(0, os.path.abspath("../../sphinxcontrib"))

# -- General configuration ------------------------------------------------

# If your documentation testreport a minimal Sphinx version, state it here.
#
# testreport_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = ["sphinx_needs", "sphinxcontrib.test_reports"]

def add_ntd_links_from_properties(need):
    """Called for each `testcase` need after it is created, to update the links with the testcase parent properties.
    
    This encapsulates the product-specific logic for how we are using the pytest properties: notably
    `tests_requirement_ref` for the requirement numbers, and a filter for the product requirements file we are interested in.
    Tests can trace to more than one product.
    """
    if isinstance(need, dict) and need["type"] == "testcase":
        #print("INGESTION", need["id"], need['properties'])
        try:
            # Sphinx reprs a dict containing a string into a string, so we need to eval twice to extract.
            props = literal_eval(need["properties"])
            new_links = literal_eval(props["tests_requirement_ref"])
            links_filtered = [k for k in new_links if k.startswith('NTD')]
            print(need["id"], " links +=", links_filtered, " not ", [k for k in new_links if k not in links_filtered])
            links = need.get("links", [])
            links += [k for k in links_filtered if k not in links]
            need["links"] = links
        except KeyError:
            pass

tr_ingestion_hook = add_ntd_links_from_properties
tr_case_id_length = 8
needs_build_json = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "test-report test docs"
copyright = "2023 TidalSense Ltd"
author = "gordon.deane@tidalsense.com"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = "1.0"
# The full version, including alpha/beta/rc tags.
release = "1.0"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "alabaster"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ["_static"]

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "testreporttestdocsdoc"

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        "testreporttestdocs.tex",
        "testreport test docs Documentation",
        "team useblocks",
        "manual",
    ),
]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (
        master_doc,
        "testreporttestdocs",
        "testreport test docs Documentation",
        [author],
        1,
    )
]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "testreporttestdocs",
        "testreport test docs Documentation",
        author,
        "testreporttestdocs",
        "One line description of project.",
        "Miscellaneous",
    ),
]
