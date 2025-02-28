=====
Usage
=====

Pipeline overview
=================

.. figure:: figures/pipeline.png
   :width: 720px
   :align: center
   :alt: Pipeline

Required data
=============

* Spatial transcriptomic (ST) data: gene expression + spatial coordinates;

* Annotated single-cell RNA-sequencing (scRNA-seq) data: gene expression + cell type labels.

Cell type deconvolution
=======================

To identify cell-type-specific spatially variable genes (SVGs) while considering the cell type mixtures in the ST data,
we first need to determine the cell type proportions by using deconvolution methods.
Through our numerical experiments, we found that the estimated cell type proportions play an important role in the cell-type-specific SVG identification, 
and thus keeping the deconvolution and SVG models consistent in terms of the definition of cell type proportion
is essential to controlling the false positive rates and yielding reliable and interpretable results.

Within the MMM model, cell type proportion represents the ratio of the transcript count from a certain cell type to all transcripts at the spot.
Here, we highlight its difference with another definition based on the number of cells rather than transcripts.
Therefore, the two most suitable deconvolution methods for ``MCube`` are ``RCTD`` :cite:p:`cable2022robust` (https://github.com/dmcable/spacexr)
and ``STitch3D`` :cite:p:`wang2023construction` (https://github.com/YangLabHKUST/STitch3D).
Specifically, ``STitch3D`` is a deep learning-based method that can infer 3D spatial distributions of fine-grained cell types in tissues.
We also provide a modified version of ``STitch3D`` (https://github.com/YangLabHKUST/MCube/tree/main/deconvolution)
with new features for sparsifying the estimated cell type proportions and writing the full deconvolution results to disk.

Cell-type-specific SVG identification
=====================================

With the deconvolution results, we can identify cell-type-specific SVGs by applying ``MCube``.
Please see more examples in :doc:`/analysis/index`.

.. bibliography::
    :filter: {"usage"} & docnames

