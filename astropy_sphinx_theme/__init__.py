""" Dorado Sphinx Theme """
import os


def get_html_theme_path():
    """Return list of HTML theme paths."""
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    return [cur_dir]


def setup(app):
    app.add_html_theme('bootstrap-dorado', os.path.abspath(os.path.join(os.path.dirname(__file__), 'bootstrap-dorado')))
