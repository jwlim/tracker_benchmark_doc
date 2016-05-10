.. include:: raw_htmls.txt

**Datasets**
************

The full benchmark contains 100 sequences from recent literatures.

* The sequence names are in CamelCase without any blanks or underscores (_).
* When there exist multiple targets each target is identified as dot+id_number (e.g. Jogging.1 and Jogging.2).
* Each row in the ground-truth files represents the bounding box of the target in that frame,
  (x, y, box-width, box-height).
* In most sequences the first row corresponds to the first frame and the last row to the last frame, except the following sequences:
  
  * David(300:770), Football1(1:74), Freeman3(1:460), Freeman4(1:283).

  

**TB-50 Sequences.**
++++++++++++++++++++

.. include:: /datasets_seq1.rst

**The rest of TB-100 Sequences.**
+++++++++++++++++++++++++++++++++

.. include:: /datasets_seq2.rst

**Attributes**
++++++++++++++

We have manually tagged the test sequences with 11 attributes, which represents the challenging aspects in visual tracking.

.. include:: /datasets_attrs.rst

