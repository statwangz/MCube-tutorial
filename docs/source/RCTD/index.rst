================================================
Integration with ``RCTD`` using one line of code
================================================

We provide the ``MCube::mcubeRCTD()`` function to integrate ``MCube`` with the cell type deconvolution results from ``RCTD`` :cite:p:`cable2022robust` (https://github.com/dmcable/spacexr) in just one line of code.
Note that the choice of the ``RCTD`` mode determines the analysis strategy of ``MCube``:

* For the ST data with low resolution like Visium, we recommend using the ``full`` mode. Then, ``MCube`` will analyze all the cell types of interest together and store the results in a single ``mcube`` object.
* For the ST data with high resolution and large sample size like Visium HD and Xenium, we recommend using the ``doublet`` mode. Then, ``MCube`` will analyze each cell type separately using the spots with a high probability of containing the target cell type according to the deconvolution results. The results will be stored in a list of ``mcube`` objects, each corresponding to a cell type.

We also provide three examples of real data analysis, including the Visium adult mouse brain dataset :cite:p:`you2024systematic`, the Visium human CRC dataset :cite:p:`oliveira2025high`, and the Xenium human CRC dataset :cite:p:`oliveira2025high`:

.. toctree::
   :maxdepth: 1
   
   mouse_brain
   CRC

.. bibliography::
    :filter: {"RCTD/index"} & docnames