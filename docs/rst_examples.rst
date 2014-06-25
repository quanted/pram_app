rst examples
---------------------------

There should only be one of these per page and this will also -- when
converting to pdf -- be used for the chapters.

H2 -- Page Sections
+++++++++++++++++++

H3 -- Subsection
************************

H4 -- Subsubsection
=====================

**bold** and *italics*

* A thing.
* Another thing.

or

1. Item 1.
2. Item 2.
3. Item 3.

or

- Some.
- Thing.
- Different.

COMPLEX TABLE:

+------------+------------+-----------+
| Header 1   | Header 2   | Header 3  |
+============+============+===========+
| body row 1 | column 2   | column 3  |
+------------+------------+-----------+
| body row 2 | Cells may span columns.|
+------------+------------+-----------+
| body row 3 | Cells may  | - Cells   |
+------------+ span rows. | - contain |
| body row 4 |            | - blocks. |
+------------+------------+-----------+

SIMPLE TABLE:

=====  =====  ======
   Inputs     Output
------------  ------
  A      B    A or B
=====  =====  ======
False  False  False
True   False  True
False  True   True
True   True   True
=====  =====  ======

This is a statement.

.. warning::

   Never, ever, use this code!

.. versionadded:: 0.0.1

It's okay to use this code.

Here is a Python function::

    def my_fn(foo, bar=True):
        """A really useful function.

        Returns None
        """