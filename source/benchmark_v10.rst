.. toctree::
   :maxdepth: 2


.. include:: raw_htmls.txt

**Visual Trackers**
*******************

This benchmark includes the results from 50 test sequences and 29 trackers. The results are reported in the CVPR 2013 paper `[Paper] <http://faculty.ucmerced.edu/mhyang/papers/cvpr13_benchmark.pdf>`_ `[Supplement] <http://faculty.ucmerced.edu/mhyang/papers/cvpr13_benchmark_sup.pdf>`_.::

  @inproceedings{ WuLimYang13,
    Title = {Online Object Tracking: A Benchmark},
    Author = {Yi Wu and Jongwoo Lim and Ming-Hsuan Yang},
    Booktitle = {IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
    Year = {2013}
    }

How to get the tracker benchmark codebase.
++++++++++++++++++++++++++++++++++++++++++
The tracker codes used in this benchmark can be download: `tracker_benchmark_v1.0.zip <./v1.0/tracker_benchmark_v1.0.zip>`_ (229MB).
|br|
If you suffer from slow download speed, try `this link to the file on Google Drive <https://docs.google.com/file/d/0B9tbggDUSMNSYmFIUS1HaWl2Y2s/edit?usp=sharing>`_.
|br|
The benchmark results using the above code is available also : tracker_benchmark_v1.0_results.zip (222MB, [`Google Drive <https://docs.google.com/file/d/0B9tbggDUSMNSejNzeHlPUFRjV0k/edit?usp=sharing>`_]).
|br|
The results zip-file needs to be unzipped **in** the ‘tracker_behcnmark_v1.0′ directory.
|br|
Join `visual-tracking Google groups <https://groups.google.com/d/forum/visual-tracking>`_ for further updates and discussions.


How to get the test data.
+++++++++++++++++++++++++
Simply, you can download the test sequence from the `zip <./zip>`_ link in the test sequences table below. For evaluating your tracker, you can find the ground-truth markings as well as MATLAB functions for evaluation in the the benchmark codebase.


How to compare your result with the benchmark results.
++++++++++++++++++++++++++++++++++++++++++++++++++++++
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

**Test results**
****************
The success plots for all sequences and attributes are listed below.
|br|
For an overlap threshold (x-axis of the plot), the success ratio is the ratio of the frames whose tracked box has more overlap with the ground-truth box than the threshold. 
|br|
The values in the brakets in the figures are the AUC (area under curve), each of which is the average of all success rates at different thresholds when the thresholds are evenly distributed.

.. include :: /benchmark_v10_figures.rst