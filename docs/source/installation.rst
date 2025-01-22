Install **MCube** from GitHub
=============================

The R package **MCube** is publicly available at https://github.com/YangLabHKUST/MCube/ .

You can install the development version of **MCube** from `GitHub <https://github.com/>`_:

.. code-block:: r

  # install.packages("pak")
  pak::pak("YangLabHKUST/MCube")

Suggested packages
==================

To conduct parallel computing, the R pacakges ``foreach`` (https://CRAN.R-project.org/package=foreach)
and ``iterators`` (https://cran.r-project.org/package=iterators) are required:

.. code-block:: r

  install.packages(c("foreach", "iterators"))