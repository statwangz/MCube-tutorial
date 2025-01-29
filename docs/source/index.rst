=================================
Welcome to MCube's documentation!
=================================

.. image:: figures/sticker.png
   :height: 128px
   :align: right
   :alt: Sticker
   :target: https://github.com/YangLabHKUST/MCube

The R package ``MCube`` (`GitHub <https://github.com/YangLabHKUST/MCube>`_) implements the methods in the **MMM** paper.
**MMM**, standing for the **Mixture of Mixed Models**,
is a unified framework for statistical identification of cell-type-specific spatially variable genes in spatial transcriptomic (ST) studies.
.. Beginning with the raw count data, **MMM** uses a log-mixture structure to account for cell type composition
.. while simultaneously correcting for the spot and platform effects between ST and scRNA-seq data.
.. The mixed-effects model decomposes the cell-type-specific gene expression in ST data into three components:
.. the average gene expression of the same cell type obtained from scRNA-seq data, spatial variations, and non-spatial variations,
.. enabling a statistically rigorous way to examine the significance of the spatial variations.
.. The statistical significance of spatial variations is then examined using a powerful non-parametric test capable of detecting diverse spatial patterns.

In this tutorial website, we provide guidelines for using ``MCube`` along with real data analysis examples.
The souce code for building the website can be found at https://github.com/statwangz/MCube-tutorial.

Contents
========

.. toctree::
   :maxdepth: 2

   installation.rst
   usage.rst
   analysis/index.rst

Reference
=========

If you find the ``MCube`` package or any of the source code in this repository useful for your work, please cite:
   | A unified framework for identification of cell-type-specific spatially variable genes in spatial transcriptomic studies.
   | Zhiwei Wang, Yeqin Zeng, Ziyue Tan, Yuheng Chen, Xinrui Huang, Hongyu Zhao, Zhixiang Lin, and Can Yang.
   | 2025.

Development
===========

The R package ``MCube`` is developed by `Zhiwei Wang <https://sites.google.com/view/statwangz>`_.

Contact
=======

Please feel free to contact `Zhiwei Wang <zhiwei.wang@connect.ust.hk>`_  or `Prof. Can Yang <macyang@ust.hk>`_ if any inquiries.