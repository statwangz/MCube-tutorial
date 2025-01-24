============
Installation
============

Install ``MCube`` from GitHub
=============================

The R package ``MCube`` is publicly available at https://github.com/YangLabHKUST/MCube/.
You can install the development version of ``MCube`` from `GitHub <https://github.com/>`_:

.. code-block:: r

  # install.packages("devtools")
  devtools::install_github("YangLabHKUST/MCube")

Suggested packages
==================

To conduct parallel computing,
the R packages ``doParallel`` (https://CRAN.R-project.org/package=doParallel),
``foreach`` (https://CRAN.R-project.org/package=foreach),
and ``iterators`` (https://cran.r-project.org/package=iterators) are required:

.. code-block:: r

  install.packages(c("doParallel", "foreach", "iterators"))