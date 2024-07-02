# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Mark Zimmerman's Portfolio"
copyright = '2024, Mark Zimmerman'
author = 'Mark Zimmerman'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
html_theme_options = {
    "nosidebar": "false",
    "description": "A demonstration of exploits in Data Science and Machine Learning Engineering.",
    "logo":"logo.png",
    # "github_button":True,
    # 'github_user': 'mzimm003',
    # 'github_repo': '',
    "extra_nav_links":{
        "LinkedIn":"https://www.linkedin.com/in/mark-zimmerman-122b1a60/",
        "GitHub":"https://www.github.com/mzimm003",
        "Resume":"_static/Mark_Zimmerman_Resume_5.2024_MLE.pdf"},
    "fixed_sidebar":True,
    "sidebar_width":"15%",
    "page_width":"90%"
}