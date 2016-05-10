from model.sphinx_attr import *
from model.sphinx_seq import *
from model.sphinx_benchmark import *

class WritingTable:
	EMPTY = "|EMPTY|"
	#attributes
	#roomList : room list (number of " ")
	#column : number of column (number of rooms)
	#dataFile : file to write
	
	def __init__(self, roomList, dataFile):
		self.roomList = roomList
		self.column = len(roomList)
		self.dataFile = dataFile

	def write(self, string):
		self.dataFile.write(string)

	def writeEmpty(self):
		self.write("|")
		for i in range(self.column):
				self.write((" " * self.roomList[i]) +"|")
		self.write("\n")

	def writeRow(self):
		self.write("+")
		for i in range(self.column):
				self.write(("-" * self.roomList[i]) +"+")
		self.write("\n")

	def writeHeader(self):
		self.write("+")
		for i in range(self.column):
				self.write(("=" * self.roomList[i]) +"+")
		self.write("\n")

	def writeColumns(self, columns):
		cols = len(columns)
		if cols > self.column:
			sys.exit("Number of columns exceeded : {0} > {1}\n{2}".format(cols, self.column, columns))

		self.write("|")
		for i in range(self.column):
			if i < cols:
				if columns[i] == self.EMPTY:
					self.write(" "*self.roomList[i]+"|")			
				else:
					length = len(columns[i])
					if length > self.roomList[i]:
						sys.exit("Length of column('{0}') exceed room({1})".format(columns[i], self.roomList[i]))
					self.write(columns[i] + " "*(self.roomList[i] - length) + "|")
			else:
				self.write(" "*self.roomList[i]+"|")
		self.write("\n")

	def writeSequences(self, start, dataNum):
		imageColumns = []
		linkColumns = []
		attrColumns = []
		for i in range(dataNum):
			imageColumns.append(SphinxSequence.IMG_SUB.format(start+i))
			linkColumns.append(SphinxSequence.LINK_SUB.format(start+i))
			attrColumns.append(SphinxSequence.ATTR_SUB.format(start+i))
		self.writeColumns(imageColumns)
		self.writeEmpty()
		self.writeColumns(linkColumns)
		self.writeEmpty()
		self.writeColumns(attrColumns)
		self.writeEmpty()
		self.writeRow()

	def writeAttrHeader(self):
		self.writeRow()
		columns = ['NAME', 'Description']
		self.writeColumns(columns)
		self.writeHeader()

	def writeAttribute(self, i):
		columns = [SphinxAttribute.NAME_SUB.format(i), SphinxAttribute.DESC_SUB.format(i)]
		self.writeColumns(columns)
		self.writeEmpty()
		columns = [self.EMPTY, SphinxAttribute.LIST_SUB.format(i)]
		self.writeColumns(columns)
		self.writeRow()

	def writeBenchHeader(self):
		self.writeRow()
		columns = ['NAME', 'CODE', 'REFERENCE']
		self.writeColumns(columns)
		self.writeHeader()

	def writeBenchmark(self, i):
		columns = [SphinxBenchmark.NAME_SUB.format(i), SphinxBenchmark.CODE_SUB.format(i), SphinxBenchmark.REFERENCE_SUB.format(i)]
		self.writeColumns(columns)
		self.writeRow()

	def writeResultHeader(self, evalType, attrList):		
		columns = ['**{0}**'.format(evalType), '**ALL**']
		attrList.sort()
		for attr in attrList:
			columns.append(attr.name)
		self.writeRow()
		self.writeColumns(columns)
		self.writeHeader()

	def writeResult(self, num, attrNum, evalType):
		startIndex = num * attrNum
		columns = [SphinxBenchmarkResult.NAME_SUB.format(evalType, num)]
		for i in range(attrNum):
			columns.append(SphinxBenchmarkResult.RESULT_SUB.format(evalType, startIndex + i))
		self.writeColumns(columns)
		self.writeRow()

	def writeFigureHeader(self):
		self.writeRow()
		columns = ['SRER (TB-50)']
		for _type in SphinxBenchmarkFigure.TYPE_LIST:
			columns.append("{0} (50/100)".format(_type))
		self.writeColumns(columns)
		self.writeRow()

	def writeFigure(self, num):
		typeNum = len(SphinxBenchmarkFigure.TYPE_LIST)
		seqNum = len(SphinxBenchmarkFigure.SEQ_LIST)
		startIndex = num * (typeNum * seqNum + 1)		
		count = startIndex + 1

		imgColumns = [SphinxBenchmarkFigure.NAME_SUB.format(num)]
		pdfColumns = [self.EMPTY]
		for i in range(typeNum):
			imgColumns.append(SphinxBenchmarkFigure.IMAGE_SUB.format(count))
			pdfColumns.append(SphinxBenchmarkFigure.PDF_SUB.format(count))
			count = count + 1
		self.writeColumns(imgColumns)
		self.writeEmpty()
		self.writeColumns(pdfColumns)
		self.writeEmpty()

		imgColumns = [SphinxBenchmarkFigure.IMAGE_SUB.format(startIndex)]
		pdfColumns = [SphinxBenchmarkFigure.PDF_SUB.format(startIndex)]
		for i in range(typeNum):
			imgColumns.append(SphinxBenchmarkFigure.IMAGE_SUB.format(count))
			pdfColumns.append(SphinxBenchmarkFigure.PDF_SUB.format(count))
			count = count + 1
		self.writeColumns(imgColumns)
		self.writeEmpty()
		self.writeColumns(pdfColumns)

		self.writeRow()

	def writeV10OverlapHeader(self):
		self.writeRow()
		columns = ['**SUCCESS**']
		for _type in SphinxBenchmarkFigureV10.TYPE_LIST:
			columns.append(_type)
		self.writeColumns(columns)
		#self.writeEmpty()
		self.writeColumns(['|br|'])
		self.writeColumns(['**PLOTS**'])
		self.writeRow()

	def writeV10ErrorHeader(self):
		self.writeRow()
		columns = ['**PRECISION**']
		for _type in SphinxBenchmarkFigureV10.TYPE_LIST:
			columns.append(_type)
		self.writeColumns(columns)
		#self.writeEmpty()
		self.writeColumns(['|br|'])
		self.writeColumns(['**PLOTS**'])
		self.writeRow()

	def writeV10Overlap(self, num):
		typeNum = len(SphinxBenchmarkFigureV10.TYPE_LIST)
		startIndex = num * typeNum
		columns = [SphinxBenchmarkFigureV10.NAME_SUB.format(num)]
		for i in range(typeNum):
			columns.append(SphinxBenchmarkFigureV10.IMAGE_OVERLAP_SUB.format(startIndex + i))
		self.writeColumns(columns)
		self.writeRow()

	def writeV10Error(self, num):
		typeNum = len(SphinxBenchmarkFigureV10.TYPE_LIST)
		startIndex = num * typeNum
		columns = [SphinxBenchmarkFigureV10.NAME_SUB.format(num)]
		for i in range(typeNum):
			columns.append(SphinxBenchmarkFigureV10.IMAGE_ERROR_SUB.format(startIndex + i))
		self.writeColumns(columns)
		self.writeRow()









