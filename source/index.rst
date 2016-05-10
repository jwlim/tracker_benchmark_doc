.. firstProject documentation master file, created by
   sphinx-quickstart on Thu Jul 02 11:22:31 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. toctree::
   :maxdepth: 2


.. include:: raw_htmls.txt

**Introduction**
*****************

This website contains data and code of the benchmark evaluation of online visual tracking algorithms.
|br|
Join `visual-tracking Google groups <https://groups.google.com/d/forum/visual-tracking>`_ for further updates, discussions, or QnAs.


You can find the following resources from this site

* Benchmark results
* Dataset with ground-truth annotations
* Code library

Later we have plan to add

* Online submission script that facilitates evaluating your algorithms.

**Tracker Results used in PAMI15 paper**
+++++++++++++++++++++++++++++++++++++++++

The raw results (zipped matlab .mat files) can be downloaded at the following links.

* `v1.1/pami15_SRE.zip <v1.1/pami15_SRE.zip>`_ (250,651,768 bytes) : SRE results for the baseline trackers.
* `v1.1/pami15_TRE.zip <v1.1/pami15_TRE.zip>`_ (223,347,083 bytes) : TRE results for the baseline trackers.
* `v1.1/pami15_SRER.zip <v1.1/pami15_SRER.zip>`_ (1,037,508,658 bytes) : SRER results for the baseline trackers.
* `v1.1/pami15_SRE_rev.zip <v1.1/pami15_SRE_rev.zip>`_ (56,328,515 bytes) : SRE results for more recent trackers.
* `v1.1/pami15_TRE_rev.zip <v1.1/pami15_TRE_rev.zip>`_ (38,265,788 bytes) : TRE results for more recent trackers.

**How to get the tracker benchmark codebase.**
+++++++++++++++++++++++++++++++++++++++++++++++

The tracker codes used in this benchmark can be download: `tracker_benchmark_v1.0.zip <./v1.0/tracker_benchmark_v1.0.zip>`_ (229MB).
|br|
If you suffer from slow download speed, try `this file <https://docs.google.com/file/d/0B9tbggDUSMNSYmFIUS1HaWl2Y2s/edit?usp=sharing>`_ on Google Drive.
|br|
The benchmark results using the above code is available also : `tracker_benchmark_v1.0_results.zip <./v1.0/tracker_benchmark_v1.0_results.zip>`_ (222MB, or `Google Drive version <https://docs.google.com/file/d/0B9tbggDUSMNSejNzeHlPUFRjV0k/edit?usp=sharing>`_ ).
|br|
The results zip-file needs to be unzipped **in** the ‘tracker_behcnmark_v1.0′ directory.

**How to get the test data.**
++++++++++++++++++++++++++++++

Simply, you can download the test sequence from the link in the `test sequences table <https://docs.google.com/file/d/0B9tbggDUSMNSejNzeHlPUFRjV0k/edit?usp=sharing>`_ . For evaluating your tracker, you can find the ground-truth markings as well as MATLAB functions for evaluation in the the benchmark codebase.

**How to compare your result with the benchmark results.**
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

The benchmark results are reported as success plots and precision plots. Note that the reported performance is the average over all sequences in the category. The test sequences table and attributes table shows which sequence has which attributes. For the detailed information about evaluation, refer the CVPR 2013 paper above.


Consider the performance of each tracker reported in this site as a reasonable lower-bound performance. We used one default parameter (used in the original implementation) for all sequences without any tuning. In later versions the performance of the trackers may be updated. However, we still do NOT allow hand-tuning and using different parameters for individual sequences.

The **protocol for tracker evaluation** using the benchmark data:

* Tracking starts from one initial bounding box in a start frame.
  The start frame may not be the first frame of the sequence.
* DO NOT use manually-tuned, different parameters for individual sequences.
  Any additional information, such as sequence name or attributes, may not be used in determining the parameters.
  It is allowed for a tracker to automatically adapt its parameters only using features from input images.
* The tracking result is a sequence of bounding boxes at each frame.
  Affine or similarity parameters are converted into bounding boxes for comparison.
* Use the AUC (area under curve) to show the tracker’s overall performance.
* The success plots are preferred over the precision plots, since precision only uses the bounding box locations, and ignores the size or overlap.