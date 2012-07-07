Components
==========

Typography
----------

.. index::
   single: Headings

Headings
^^^^^^^^

Heading is bold, larger font-size style has been applied.
And heading takes a lot of margin in order to stand out.

.. raw:: html

   <h1>This is an H1 Heading</h1>
   <p>The above is an <code>h1</code> element</p>

.. raw:: html

   <h2>This is an H2 Heading</h2>
   <p>The above is an <code>h2</code> element. It can be used throughout the page as a sub-section of <code>h1</code>. Multiple <code>h2</code> elements can be used, however they must not be used as sub-headings of themselves.</p>

.. raw:: html

   <h3>This is an H3 Heading</h3>
   <p>The above is an <code>h3</code> element. It should be used as the first subheading below <code>h2</code>.</p>

.. raw:: html

   <h4>This is an H4 Heading</h4>

.. raw:: html

   <h5>This is an H5 Heading</h5>

.. raw:: html

   <h6>This is an H6 Heading</h6>


.. index::
   single: Paragraph

Paragraph
^^^^^^^^^

Here are some paragraphs.

Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.


.. index::
   single: Anchor

Anchor
^^^^^^

.. raw:: html

   <p>The <code>a</code> element is used to denote hyperlink text, for example:</p>

Click here to go to `Google`_ or Click here to return to the :ref:`admonitions`.

.. _Google: http://www.google.com


.. index::
   single: Strong
   single: Emphasis

Strong, Emphasis
^^^^^^^^^^^^^^^^

Strong: **Lorem ipsum** dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante venenatis.

Emphasis: *Lorem ipsum* dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante venenatis.


.. index::
   single: Table

Table
-----

+------------------------+------------+----------+----------+
| Header row, column 1   | Header 2   | Header 3 | Header 4 |
| (header rows optional) |            |          |          |
+========================+============+==========+==========+
| body row 1, column 1   | column 2   | column 3 | column 4 |
+------------------------+------------+----------+----------+
| body row 2             | ...        | ...      |          |
+------------------------+------------+----------+----------+
| body row 3             | ...        | ...      |          |
+------------------------+------------+----------+----------+


.. index::
   single: List

List
----

Unordered list
^^^^^^^^^^^^^^

.. raw:: html

   <p>The <code>ul</code> element denotes an unordered list.</p>

- Unordered list
- Unordered list
- Unordered list

Ordered list
^^^^^^^^^^^^

.. raw:: html

   <p>The <code>ol</code> element denotes an ordered list.</p>

1. Ordered list
2. Ordered list
3. Ordered list

Definition Lists
^^^^^^^^^^^^^^^^

.. raw:: html

   <p>Definition lists, denoted by the <code>dl</code> element contain a list of terms and definitions. Terms are displayed with the <code>dt</code>, and definitions are displayed with the <code>dd</code> element.</p>

term 1
    Definition 1.
term 2
    Definition 2, paragraph 1.
    Definition 2, paragraph 2.
term 3 : classifier
    Definition 3.
term 4 : classifier one : classifier two
    Definition 4.


.. index::
   single: Images

Images
------

There are two image directives: "image" and "figure".

image
^^^^^

An "image" is a simple picture.

The URI for the image source file is specified in the directive argument.
As with hyperlink targets, the image URI may begin on the same line as the
explicit markup start and target name, or it may begin in an indented
text block immediately following, with no intervening blank lines.
If there are multiple lines in the link block, they are stripped of leading
and trailing whitespace and joined together.

figure
^^^^^^

A "figure" consists of image data (including image options), an optional
caption (a single paragraph), and an optional legend (arbitrary body elements).
For page-based output media, figures might float to a different position if this
helps the page layout.

.. index::
   single: Pre
   single: Code

Pre, Code
---------

.. code-block:: python

   import sys

   def fact(x):
       if x == 0:
           return 1
       else:
           return x * fact(x-1)


.. index::
   single: Admonitions

.. _admonitions:

Admonitions
-----------

Admonitions are specially marked "topics" that can appear anywhere an ordinary
body element can. They contain arbitrary body elements.

attention
^^^^^^^^^

.. attention::
   This is sample of "Attention" admonition directive.

caution
^^^^^^^

.. caution::
   This is sample of "Caution" admonition directive.

danger
^^^^^^

.. danger::
   This is sample of "Danger" admonition directive.

error
^^^^^

.. error::
   This is sample of "Error" admonition directive.

hint
^^^^

.. error::
   This is sample of "Hint" admonition directive.

important
^^^^^^^^^

.. important::
   This is sample of "Important" admonition directive.

note
^^^^

.. note::
   This is sample of "Note" admonition directive.

tip
^^^

.. tip::
   This is sample of "Tip" admonition directive.

warning
^^^^^^^

.. warning::
   This is sample of "Warning" admonition directive.

