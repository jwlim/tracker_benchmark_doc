from config import *
from model.sphinx_benchmark import *
from writing_table import *
import shutil

def make():
	items = SphinxBenchmark.getBenchmarkList()
	makeBenchmarkFiles(items)
	results_OPE, results_SRE, results_TRE = SphinxBenchmarkResult.getResultList()
	makeResultFiles(results_OPE, results_SRE, results_TRE)
	# figures = SphinxBenchmarkFigure.getFigureList()
	# makeFigureFiles(figures)
	v10Figures = SphinxBenchmarkFigureV10.getFigureList()
	makeV10Files(v10Figures)
	copyPdfZipfiles()

def makeBenchmarkFiles(items):
	print "for {0} benchmarks".format(len(items))
	makeBenchSubsFile(items)
	makeBenchRstFile(items)

def makeBenchSubsFile(items):
	referFile = open(PATH_TRACK + SUB_REFERENCE_FILE,'w')
	nameFile = open(PATH_TRACK + SUB_NAME_FILE, 'w')
	codeFile = open(PATH_TRACK + SUB_CODE_FILE, 'w')
	for item in items:
		referFile.write(item.refer_sub + "\n")
		nameFile.write(item.name_sub)
		codeFile.write(item.code_sub)
	referFile.close()
	nameFile.close()
	codeFile.close()
	print "\t" + PATH_TRACK + SUB_REFERENCE_FILE + " created."
	print "\t" + PATH_TRACK + SUB_NAME_FILE + " created."
	print "\t" + PATH_TRACK + SUB_CODE_FILE + " created."

def makeBenchRstFile(items):
	dataFile = open(PATH_SRC + BENCHMARK_TRACKERS_FILE, 'w')
	includePrefix = ".. include :: "
	path = "/benchmark/trackers/"
	dataFile.write(includePrefix + path + SUB_REFERENCE_FILE + "\n")
	dataFile.write(includePrefix + path + SUB_CODE_FILE + "\n")
	dataFile.write(includePrefix + path + SUB_NAME_FILE + "\n\n")

	room1 = len(SphinxBenchmark.NAME_SUB.format(0))
	room2 = len(SphinxBenchmark.CODE_SUB.format(0))
	roomList = [room1, room2, 70]	

	table = WritingTable(roomList, dataFile)
	table.writeBenchHeader()
	for i in range(len(items)):
		table.writeBenchmark(i)

	print "\t" + PATH_SRC + BENCHMARK_TRACKERS_FILE + " created."

def makeResultFiles(results_OPE, results_SRE, results_TRE):
	print "for {0} results".format(len(results_OPE))
	makeResultSubsFile(results_OPE, results_SRE, results_TRE)
	makeResultRstFile(results_OPE, results_SRE, results_TRE)

def makeResultSubsFile(results_OPE, results_SRE, results_TRE):
	resultOPEFile = open(PATH_BENCH + SUB_RESULT_OPE_FILE, 'w')
	resultSREFile = open(PATH_BENCH + SUB_RESULT_SRE_FILE, 'w')
	resultTREFile = open(PATH_BENCH + SUB_RESULT_TRE_FILE, 'w')
	trackerFile = open(PATH_BENCH + SUB_TRACKER_FILE, 'w')
	attrList = SphinxAttribute.getAttributeList()
	attrList.sort()
	for i in range(len(results_OPE)):
		result_OPE = results_OPE[i]
		result_SRE = results_SRE[i]
		result_TRE = results_TRE[i]
		trackerFile.write(result_OPE.name_sub)
		trackerFile.write(result_SRE.name_sub)
		trackerFile.write(result_TRE.name_sub)
		resultOPEFile.write(result_OPE.result_sub['ALL']+ "\n")
		resultSREFile.write(result_SRE.result_sub['ALL']+ "\n")
		resultTREFile.write(result_TRE.result_sub['ALL']+ "\n")
		for attr in attrList:
			resultOPEFile.write(result_OPE.result_sub.get(attr.name) + "\n")
			resultSREFile.write(result_SRE.result_sub.get(attr.name) + "\n")
			resultTREFile.write(result_TRE.result_sub.get(attr.name) + "\n")
	resultOPEFile.close()
	resultSREFile.close()
	resultTREFile.close()
	print "\t" + PATH_BENCH + SUB_RESULT_OPE_FILE + " created."
	print "\t" + PATH_BENCH + SUB_RESULT_SRE_FILE + " created."
	print "\t" + PATH_BENCH + SUB_RESULT_TRE_FILE + " created."
	print "\t" + PATH_BENCH + SUB_TRACKER_FILE + " created."

def makeResultRstFile(results_OPE, results_SRE, results_TRE):
	dataFile = open(PATH_SRC + BENCHMARK_RESULTS_FILE, 'w')
	includePrefix = ".. include :: "
	path = "/benchmark/"
	dataFile.write(includePrefix + path + SUB_RESULT_OPE_FILE + "\n")
	dataFile.write(includePrefix + path + SUB_RESULT_SRE_FILE + "\n")
	dataFile.write(includePrefix + path + SUB_RESULT_TRE_FILE + "\n")
	dataFile.write(includePrefix + path + SUB_TRACKER_FILE + "\n\n")

	attrList = SphinxAttribute.getAttributeList()
	attrNum = len(attrList) + 1
	room1 = len(SphinxBenchmarkResult.NAME_SUB.format('OPE',0))
	rooms = len(SphinxBenchmarkResult.RESULT_SUB.format('OPE', 0))
	roomList = [room1] + [rooms] * (attrNum)
	table = WritingTable(roomList, dataFile)
	table.writeResultHeader('OPE', attrList)
	for i in range(len(results_OPE)):
		table.writeResult(i, attrNum, 'OPE')
	table.write('\n')
	table.writeResultHeader('SRE', attrList)
	for i in range(len(results_SRE)):
		table.writeResult(i, attrNum, 'SRE')
	table.write('\n')
	table.writeResultHeader('TRE', attrList)
	for i in range(len(results_TRE)):
		table.writeResult(i, attrNum, 'TRE')

	print "\t" + PATH_SRC + BENCHMARK_RESULTS_FILE + " created."

def makeFigureFiles(figures):
	print "for {0} figures".format(len(figures))
	makeFigureSubsFile(figures)
	makeFigureRstFile(figures)

def makeFigureSubsFile(figures):
	imageFile = open(PATH_BENCH + SUB_FIGURE_IMAGE_FILE, 'w')
	pdfFile = open(PATH_BENCH + SUB_FIGURE_PDF_FILE, 'w')
	for figure in figures:
		for image_sub in figure.image_sub:
			imageFile.write(image_sub + "\n")
		for pdf_sub in figure.pdf_sub:
			pdfFile.write(pdf_sub + "\n")
	imageFile.close()
	pdfFile.close()
	print "\t" + PATH_BENCH + SUB_FIGURE_IMAGE_FILE + " created."
	print "\t" + PATH_BENCH + SUB_FIGURE_PDF_FILE + " created."

def makeFigureRstFile(figures):
	dataFile = open(PATH_SRC + BENCHMARK_FIGURES_FILE, 'w')
	includePrefix = ".. include :: "
	path = "/benchmark/"
	dataFile.write(includePrefix + path + SUB_FIGURE_IMAGE_FILE + "\n")
	dataFile.write(includePrefix + path + SUB_FIGURE_PDF_FILE + "\n\n")

	typeNum = len(SphinxBenchmarkFigure.TYPE_LIST)
	room1 = 23
	rooms = len(SphinxBenchmarkFigure.IMAGE_SUB.format(0))
	roomList = [room1] + [rooms] * typeNum
	table = WritingTable(roomList, dataFile)
	table.writeFigureHeader()
	for i in range(len(figures)):
		table.writeFigure(i)

	print "\t" + PATH_SRC + BENCHMARK_FIGURES_FILE + " created."

def makeV10Files(figures):
	print "for {0} v10 figures".format(len(figures))
	makeV10SubsFile(figures)
	makeV10RstsFile(figures)

def makeV10SubsFile(figures):
	nameFile = open(PATH_BENCH + SUB_V10_NAME_FILE, 'w')
	overlapFile = open(PATH_BENCH + SUB_V10_OVERLAP_FILE, 'w')
	errorFile = open(PATH_BENCH + SUB_V10_ERROR_FILE, 'w')
	for figure in figures:
		nameFile.write(figure.name_sub)
		for image_overlap_sub in figure.image_overlap_sub:
			overlapFile.write(image_overlap_sub)
		for image_error_sub in figure.image_error_sub:
			errorFile.write(image_error_sub)
	nameFile.close()
	overlapFile.close()
	errorFile.close()
	print "\t" + PATH_BENCH + SUB_V10_NAME_FILE + " created."
	print "\t" + PATH_BENCH + SUB_V10_OVERLAP_FILE + " created."
	print "\t" + PATH_BENCH + SUB_V10_ERROR_FILE + " created."

def makeV10RstsFile(figures):
	dataFile = open(PATH_SRC + BENCHMARK_V10_FILE, 'w')
	includePrefix = ".. include :: "
	path = "/benchmark/"
	dataFile.write(includePrefix + "/" + RAW_HTML_FILE + "\n")
	dataFile.write(includePrefix + path + SUB_V10_NAME_FILE + "\n")
	dataFile.write(includePrefix + path + SUB_V10_OVERLAP_FILE + "\n")
	dataFile.write(includePrefix + path + SUB_V10_ERROR_FILE + "\n\n")

	typeNum = len(SphinxBenchmarkFigureV10.TYPE_LIST)
	room1 = len(SphinxBenchmarkFigureV10.NAME_SUB.format(0))
	#rooms = len(SphinxBenchmarkFigureV10.IMAGE_OVERLAP_SUB.format(0))
	rooms = 20
	roomList = [room1] + [rooms] * typeNum
	table = WritingTable(roomList, dataFile)

	table.writeV10OverlapHeader()
	for i in range(len(figures)):
		table.writeV10Overlap(i)

	table.write("\n\nSimilarly a precision plot shows the ratio of successful frames whose tracker output is within the given threshold (x-axis of the plot, in pixels) from the ground-truth, measured by the center distance between bounding boxes.\n\n")

	table.writeV10ErrorHeader()
	for i in range(len(figures)):
		table.writeV10Error(i)

	print "\t" + PATH_SRC + BENCHMARK_V10_FILE + " created."

def copyPdfZipfiles():
	SRC_PREFIX = './source/'
	DES_PREFIX = BUILD_DIR
	target_dirs = ['seq', 'v1.0', 'v1.1', 'v1.2']

	for d in target_dirs:
		src = SRC_PREFIX + d
		dest = DES_PREFIX + d
		if not os.path.exists(dest):
			os.makedirs(dest)
		files = os.listdir(src)
		for f in files:
			if f.endswith('.zip'):
				fileName = os.path.join(src, f)
				destName = os.path.join(dest, f)
				shutil.copy(fileName, destName)
			elif f.endswith('.pdf'):
				fileName = os.path.join(src, f)
				destName = os.path.join(dest, f)
				shutil.copy(fileName, destName)
