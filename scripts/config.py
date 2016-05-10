import os
import sys

############### sphinx config #######################

BUILD_DIR = "build/"

DATASET_SEQ_FILE = "datasets_{0}.rst"			# result : sequence page
DATASET_ATTR_FILE = "datasets_attrs.rst"	# result : attribute page

BENCHMARK_TRACKERS_FILE = "benchmark_trackers.rst"
BENCHMARK_RESULTS_FILE = "benchmark_results.rst"
BENCHMARK_FIGURES_FILE = "benchmark_figures.rst"
BENCHMARK_V10_FILE = "benchmark_v10_figures.rst"

PATH_SRC = "./source/"
PATH_DATA = "./source/datasets/"
PATH_ATTR = "./source/datasets/attributes/"
PATH_BENCH = "./source/benchmark/"
PATH_TRACK = "./source/benchmark/trackers/"

RAW_HTML_FILE = "raw_htmls.txt"

# for sequence entries.
NUM_SEQ_SET = 2														# number of sequences sets.
SRC_ITEM_FILE = "src_items.txt"						# source : sequence list.
SUB_IMAGE_FILE = "sub_images.rst"					# result : image link list.
SUB_LINK_FILE = "sub_links.rst"						# result : download link list.
SUB_ATTR_FILE = "sub_attrs.rst"						# result : attributes list.

# for attribute entries
SRC_ATTRIBUTE_FILE = "src_attribute.txt"	# source : attributes list.	
SRC_DESC_FILE = "src_desc.txt"						# source : attr's description list.
ATTR_FILE = "attrs.rst"										# result : attr list.
ATTR_SEQ_LIST_FILE = "attrs_list.rst"			# reuslt : seq (has attr) list.
DESC_FILE = "desc.rst"										# result : desc list.

# for benchmark tracker entries
SRC_TRACKERS_FILE = "src_trackers.txt"		# source : tracker references list
SUB_CODE_FILE = "sub_code.rst"
SUB_NAME_FILE = "sub_name.rst"
SUB_REFERENCE_FILE = "sub_reference.rst"

# for benchmark result entries
SRC_OVERLAP_FILE = "src_overlap.txt"			# source : benchmarks's overlap percent list.
SRC_OVERLAP_OPE_FILE = "src_overlap_OPE.txt"
SRC_OVERLAP_SRE_FILE = "src_overlap_SRE.txt"
SRC_OVERLAP_TRE_FILE = "src_overlap_TRE.txt"
SRC_FAILURE_FILE = "src_failure.txt"			# source : benchmarks's number of failure list.
SUB_RESULT_OPE_FILE = "sub_result_OPE.rst"
SUB_RESULT_SRE_FILE = "sub_result_SRE.rst"
SUB_RESULT_TRE_FILE = "sub_result_TRE.rst"
SUB_TRACKER_FILE = "sub_tracker.rst"

SUB_FIGURE_NAME_FILE = "sub_figure_name.rst"
SUB_FIGURE_IMAGE_FILE = "sub_figure_image.rst"
SUB_FIGURE_PDF_FILE = "sub_figure_pdf.rst"

SUB_V10_NAME_FILE = "sub_v10_name.rst"
SUB_V10_OVERLAP_FILE = "sub_v10_overlap.rst"
SUB_V10_ERROR_FILE = "sub_v10_error.rst"

