Install **MCube** from GitHub
=============================

The R package ``MCube`` is publicly available at https://github.com/YangLabHKUST/MCube/ .

You can install the development version of ``MCube`` from `GitHub <https://github.com/>`_:

.. code-block:: r

  # install.packages("pak")
  pak::pak("YangLabHKUST/MCube")

Suggested package
=================

To conduct parallel computing, the R pacakge ``foreach`` (https://CRAN.R-project.org/package=foreach) is required:

.. code-block:: r

  install.packages(c("foreach", "iterators"))