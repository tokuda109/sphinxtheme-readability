Sphinx Readability Theme
========================

.. attention:: Experimental!
   This theme is an experimental and rapidly developing.

Sphinx Readability Theme provides a comfortably reading environment for your documentation.

This theme is inspired by `Readability <https://www.readability.com/>`_.

Installation
------------

To use this style in your Sphinx documentation, follow
this guide.

Installing this sphinx theme is simply::

    $ pip install sphinxtheme.readability

or::

    $ sudo easy_install sphinxtheme.readability

Add this to your conf.py::

    import sphinxtheme

    html_theme = 'readability'
    html_theme_path = sphinxtheme.get_html_theme_path()

Author
------

- Tsuyoshi Tokuda (@tokuda109)
