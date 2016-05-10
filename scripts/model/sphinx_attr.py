from config import *

class SphinxAttribute:
	## attributes
	# name : attr's name
	# desc : attr's desc
	# list : seq's list
	# name_sub : name's substitution for sphinx
	# desc_sub : desc's substitution for sphinx
	# list_sub : seq's list substitution 

	NAME_SUB = "|Attr{0:03d}|"
	DESC_SUB = "|Desc{0:03d}|"
	LIST_SUB = "|List{0:03d}|"

	def __init__(self, line, num):
		attr = line.strip().split('\t')
		self.initName(attr[0], num)
		self.initDesc(attr[1], num)

	def initName(self, name, num):
		self.name = name
		self.name_sub = ".. " + self.NAME_SUB.format(num) + " replace:: " + name + "\n"

	def initDesc(self, desc, num):
		self.desc = desc
		self.desc_sub = ".. " + self.DESC_SUB.format(num) + " replace:: " + desc + "\n"

	def getAttrList(self, seqs, num):
		result = []
		for seq in seqs:
			if self.name in seq.attrs:
				result.append(seq.name)
		self.list = result.sort()
		string = ", ".join(str(x) for x in result)
		self.list_sub = ".. " + self.LIST_SUB.format(num) + " replace:: " + string + "\n\n"

	def __lt__(self, other):
		return self.name < other.name

	@staticmethod
	def getAttributeLines():
		srcAttrFile = open(PATH_ATTR + SRC_ATTRIBUTE_FILE)
		attrLines = srcAttrFile.readlines()
		return attrLines

	@staticmethod
	def getAttributeList():
		attrLines = SphinxAttribute.getAttributeLines()
		attrList = []
		for i in range(len(attrLines)):
			attr = SphinxAttribute(attrLines[i], i)
			attrList.append(attr)
		return attrList
