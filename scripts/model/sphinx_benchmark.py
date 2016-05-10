from config import *
from model.sphinx_attr import *
import sys

class SphinxBenchmark:
	## attributes
	# name : tracker's name
	# code	: tracker's code
	# reference	: tracker's reference
	# link : reference link
	# name_sub
	# code_sub
	# refer_sub

	REFERENCE_SUB = "|refer{0:03d}|"
	NAME_SUB = "|names{0:03d}|"
	CODE_SUB = "|codes{0:03d}|"

	def __init__(self, line, num):
		benchmark = line.strip().split('\t')
		self.name = benchmark[0]
		self.initNameSub(self.name, num)

		self.code = benchmark[1]
		self.initCodeSub(self.code, num)

		if len(benchmark) == 4:
			self.link = benchmark[3]

		self.reference = benchmark[2]
		self.initRefSub(self.reference, num)

	def initNameSub(self, name, num):
		self.name_sub = ".. "+self.NAME_SUB.format(num)+" replace:: {0}\n".format(name)
 
	def initCodeSub(self, code, num):
		self.code_sub = ".. "+self.CODE_SUB.format(num)+" raw:: html\n\n\t" + \
			"<span id={0}>{1}</span>\n\n".format(code.lower(),code)

	def initRefSub(self, reference, num):
		if reference.count('[www]') == 0:
			self.refer_sub = ".. "+self.REFERENCE_SUB.format(num)+" raw:: html\n\n\t"+ reference
		else :
			self.refer_sub = ".. "+self.REFERENCE_SUB.format(num)+" raw:: html\n\n\t" + \
				reference.replace("[www]","<a href=\""+self.link+"\" target=_blank>[www]</a>")
		self.refer_sub += '<a href="v1.2/raw/{0}.zip"> [Raw-Results] </a>'.format(
			self.code) + '<a href="v1.2/processed/{0}.zip"> [Processed-Results] </a>\n'.format(self.code)
		
	@staticmethod
	def getBenchmarkLines():
		srcTrackersFile = open(PATH_TRACK + SRC_TRACKERS_FILE)
		trackerLines = srcTrackersFile.readlines()
		return trackerLines

	@staticmethod
	def getBenchmarkList():
		trackerLines = SphinxBenchmark.getBenchmarkLines()
		benchmarkList = []
		for i in range(len(trackerLines)):
			benchmark = SphinxBenchmark(trackerLines[i], i)
			benchmarkList.append(benchmark)
		return benchmarkList


class SphinxBenchmarkResult:
	## attributes
	# name : tracker's name
	# evalType
	# overlap : avg overlap in percent dict {Attributes : percent}
	# failure : avg number of failure dict {Attributes : number}
	# rank_overlap : 
	# rank_failure : 
	# name_sub : 
	# result_sub : 

	NAME_SUB = "|tracker{0}{1:03d}|"
	RESULT_SUB = "|result{0}{1:03d}|"

	def __init__(self, overlapline, evalType, attrList, num):
		overlap = overlapline.strip().split('\t')

		self.name = overlap[0]
		self.evalType = evalType
		overlapList = map(float,overlap[1:])

		# failureList = map(float,failure[1:])

		self.rank_overlap = dict()
		
	
		# if not len(overlapList) == len(attrList):
		# 	sys.exit(self.name + " : number of result  doesn't match with # of attrs")
		
		self.initOverlap(overlapList, attrList)
		# self.initFailure(failureList, attrList)

	def initOverlap(self, overlapList, attrList):
		count = len(overlapList)
		attrList.sort()
		self.overlap = dict()
		for i in range(count):
			self.overlap[attrList[i].name] = overlapList[i]

	def initFailure(self, failureList, attrList):
		count = len(failureList)
		avg = sum(failureList) / float(count)
		self.failure = {'ALL' : avg}
		attrList.sort()
		for i in range(count):
			self.failure[attrList[i].name] = failureList[i]

	def initSub(self, num, attrList):
		startIndex = num*(len(attrList))
		self.name_sub = ".. " + self.NAME_SUB.format(self.evalType, num) + " raw:: html\n\n\t" + \
			"<a href=#{0}>{1}</a>\n\n".format(self.name.lower(), self.name)
		# span_overlap_OPE = "<span class='result rank{0}'>{1:.1f}</span>".format(self.rank_overlap_OPE.get('ALL'), self.overlap.get('ALL'))
		# # span_failure = "/{0:.1f}".format(self.failure.get('ALL')) + "</span>"
		# sub = ".. " + self.RESULT_SUB.format(startIndex) + " raw:: html\n\n\t" + span_overlap + "<br />" + span_failure + "\n"
		# self.result_sub = {'ALL' : sub}
		self.result_sub = dict()
		for i in range(len(attrList)):
			attr = attrList[i]
			name = attr.name
			span_overlap = "<span class='result rank{0}'>{1:.1f}</span>".format(
				self.rank_overlap[name], self.overlap[name])
			# span_overlap_SRE = "<span class='result rank{0}'>{1:.1f}</span>".format(
			# 	self.rank_overlap_SRE[name], self.overlap_SRE[name])
			# span_overlap_TRE = "<span class='result rank{0}'>{1:.1f}</span>".format(
			# 	self.rank_overlap_TRE[name], self.overlap_TRE[name])
			# span_failure = "/{0:.1f}".format(self.failure.get(name)) + "</span>"
			sub = ".. " + self.RESULT_SUB.format(self.evalType, startIndex + i) + " raw:: html\n\n\t" + span_overlap + "\n"
			self.result_sub[attr.name] = sub

	@staticmethod
	def getOverlapLines():
		overlap_OPE = open(PATH_BENCH + SRC_OVERLAP_OPE_FILE)
		overlap_SRE = open(PATH_BENCH + SRC_OVERLAP_SRE_FILE)
		overlap_TRE = open(PATH_BENCH + SRC_OVERLAP_TRE_FILE)
		overlapline_OPE = overlap_OPE.readlines()
		overlapline_SRE = overlap_SRE.readlines()
		overlapline_TRE = overlap_TRE.readlines()
		return overlapline_OPE, overlapline_SRE, overlapline_TRE

	@staticmethod
	def getFailureLines():
		failureFile = open(PATH_BENCH + SRC_FAILURE_FILE)
		failurelines = failureFile.readlines()
		return failurelines

	@staticmethod
	def getResultList():
		overlapline_OPE, overlapline_SRE, overlapline_TRE = SphinxBenchmarkResult.getOverlapLines()
		# failurelines = SphinxBenchmarkResult.getFailureLines()

		# if not len(overlaplines) == len(failurelines):
		# 	sys.exit("number of overlap & failure doesn't match")

		attrList = SphinxAttribute.getAttributeList()
		attrList.append(SphinxAttribute('ALL\tall', -1))
		attrList.sort()
		
		resultList_OPE = []
		resultList_SRE = []
		resultList_TRE = []
		for i in range(len(overlapline_OPE)):
			result_OPE = SphinxBenchmarkResult(overlapline_OPE[i], 'OPE', attrList, i) 
			resultList_OPE.append(result_OPE)
			result_SRE = SphinxBenchmarkResult(overlapline_SRE[i], 'SRE', attrList, i) 
			resultList_SRE.append(result_SRE)
			result_TRE = SphinxBenchmarkResult(overlapline_TRE[i], 'TRE', attrList, i) 
			resultList_TRE.append(result_TRE)

		SphinxBenchmarkResult.initRank(resultList_OPE, attrList)
		SphinxBenchmarkResult.initRank(resultList_SRE, attrList)
		SphinxBenchmarkResult.initRank(resultList_TRE, attrList)
		resultList = sorted(resultList_OPE, key=lambda SphinxBenchmarkResult: SphinxBenchmarkResult.rank_overlap['ALL'])
		for i in range(len(resultList)):
			resultList[i].initSub(i, attrList)
		resultList = sorted(resultList_SRE, key=lambda SphinxBenchmarkResult: SphinxBenchmarkResult.rank_overlap['ALL'])
		for i in range(len(resultList)):
			resultList[i].initSub(i, attrList)
		resultList = sorted(resultList_TRE, key=lambda SphinxBenchmarkResult: SphinxBenchmarkResult.rank_overlap['ALL'])
		for i in range(len(resultList)):
			resultList[i].initSub(i, attrList)
		return resultList_OPE, resultList_SRE, resultList_TRE

	@staticmethod
	def initRank(resultList, attrList):
		for attr in attrList:
			rankList = sorted(resultList, 
				key=lambda SphinxBenchmarkResult: SphinxBenchmarkResult.overlap.get(attr.name), reverse=True)
			for i in range(len(rankList)):
				rankList[i].rank_overlap[attr.name] = i + 1



class SphinxBenchmarkFigure:
	TYPE_LIST = ['OPE', 'SRE', 'TRE']
	SEQ_LIST = [50, 100]
	PREFIX = "SRER_w90"
	NAME_SUB = "|fig_name{0:03d}|"
	IMAGE_SUB = "|fig_image{0:03d}|"
	PDF_SUB = "|fig_pdf{0:03d}|"
	IMG_BIG_HEIGHT = 280
	IMG_HEIGHT = 180
	##attributes
	# name
	# name_sub
	# image_sub
	# pdf_sub

	def __init__(self, num, attr=None):
		if attr is None:
			self.name = "**Overall**"
			self.initImageAndPdfSub("", num)
		else:
			name = attr.name
			desc = attr.desc.split(" - ")[0]
			self.name = "**{0}**".format(name) + ": " + desc
			self.initImageAndPdfSub("_"+name, num)
		self.initNameSub(self.name, num)

	def initNameSub(self, name, num):
		self.name_sub = ".. "+self.NAME_SUB.format(num)+" replace:: "+name + "\n"
		
	def initImageAndPdfSub(self, name, num):
		count = num * (len(self.TYPE_LIST) * len(self.SEQ_LIST) + 1)
		img_sub = ".. "+self.IMAGE_SUB.format(count) + " image:: /v1.1/{0}{1}.png\n".format(self.PREFIX, name)
		img_sub += "\t:height: {0}px\n".format(self.IMG_BIG_HEIGHT)
		pdf_sub = ".. " + self.PDF_SUB.format(count) + " raw:: html\n\n\t" + "<a class='download-pdf' href=\"./v1.1/{0}{1}.pdf\">[pdf]</a><br />\n".format(self.PREFIX, name)
		self.image_sub = [img_sub]
		self.pdf_sub = [pdf_sub]
		count = count + 1
		for seq in self.SEQ_LIST:
			for _type in self.TYPE_LIST:
				img_sub = ".. "+self.IMAGE_SUB.format(count)+ " image:: /v1.1/{0}{1}sq{2}.png\n".format(_type, seq, name)
				img_sub += "\t:height: {0}px\n".format(self.IMG_HEIGHT)
				pdf_sub = ".. " + self.PDF_SUB.format(count) + " raw:: html\n\n\t" + "<a class='download-pdf' href=\"./v1.1/{0}{1}sq{2}.pdf\">[pdf]</a><br />\n".format(_type, seq, name)
				self.image_sub.append(img_sub)
				self.pdf_sub.append(pdf_sub)
				count = count + 1

	@staticmethod
	def getFigureList():
		attrList = SphinxAttribute.getAttributeList()
		figureList = [SphinxBenchmarkFigure(0)]
		for i in range(len(attrList)):
			attr = attrList[i]
			figure = SphinxBenchmarkFigure(i + 1, attr)
			figureList.append(figure)

		return figureList

class SphinxBenchmarkFigureV10:
	TYPE_LIST = ['OPE', 'SRE', 'TRE']
	SRC_OVERLAP = "/v1.0/{0}overlap_{1}.png\n"
	SRC_ERROR = "/v1.0/{0}error_{1}.png\n"
	NAME_SUB = "|v10_name{0:03d}|"
	IMAGE_OVERLAP_SUB = "|v10_overlap{0:03d}|"
	IMAGE_ERROR_SUB = "|v10_error{0:03d}|"
	IMG_HEIGHT = 180
	##attributes
	# name
	# name_sub
	# image_overlap_sub
	# image_error_sub

	def __init__(self, num, attr=None):
		if attr is None:
			self.name = "**Overall**"
			self.initImageSub("", num)
		else:
			name = attr.name
			desc = attr.desc.split(" - ")[0]
			self.name = "**{0}**".format(name) + ": " + desc
			self.initImageSub(name+"_", num)
		self.initNameSub(self.name, num)

	def initNameSub(self, name, num):
		self.name_sub = ".. "+self.NAME_SUB.format(num)+" replace:: "+name + "\n"
		
	def initImageSub(self, name, num):
		count = num * len(self.TYPE_LIST)
		self.image_overlap_sub = []
		self.image_error_sub = []
		for _type in self.TYPE_LIST:
			img_overlap_sub = ".. "+self.IMAGE_OVERLAP_SUB.format(count)+ " image:: "+self.SRC_OVERLAP.format(name, _type)
			#img_overlap_sub += "\t:height: {0}px\n".format(self.IMG_HEIGHT)
			img_error_sub = ".. "+self.IMAGE_ERROR_SUB.format(count)+ " image:: "+self.SRC_ERROR.format(name, _type)
			self.image_overlap_sub.append(img_overlap_sub)
			self.image_error_sub.append(img_error_sub)
			count = count + 1

	@staticmethod
	def getFigureList():
		attrList = SphinxAttribute.getAttributeList()
		figureList = [SphinxBenchmarkFigureV10(0)]
		for i in range(len(attrList)):
			attr = attrList[i]
			figure = SphinxBenchmarkFigureV10(i + 1, attr)
			figureList.append(figure)

		return figureList