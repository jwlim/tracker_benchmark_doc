from config import *
from model.sphinx_seq import *
from model.sphinx_attr import *
from writing_table import *

def make():
	startIndex = 0
	allSeqitems = []
	for i in range(NUM_SEQ_SET):
		seqItems = SphinxSequence.getSeqList(i, startIndex)
		seqName = "seq{0}".format(i + 1)
		makeSeqFiles(seqName, seqItems, startIndex)
		allSeqitems += seqItems
		startIndex += len(seqItems)
	attrList = SphinxAttribute.getAttributeList()
	makeAttrFiles(attrList, allSeqitems)
	
def makeSeqFiles(seqName, items, startIndex):
	print "for {0} seqs".format(len(items))
	path = PATH_DATA + seqName + "/"
	makeSeqSubsFile(path, items)
	path = "/datasets/" + seqName + "/"
	makeSeqRstFile(path, seqName, items, startIndex)

def makeAttrFiles(attrList, allSeqitems):
	print "for {0} attrs".format(len(attrList))
	makeAttrSubsFiles(attrList, allSeqitems)
	makeAttrRstFile(len(attrList))

def makeSeqSubsFile(path, items):
	linkFile = open(path + SUB_LINK_FILE, 'w')
	imageFile = open(path + SUB_IMAGE_FILE, 'w')
	attrFile = open(path + SUB_ATTR_FILE, 'w')

	for item in items:
		linkFile.write(item.link + "\n")
		imageFile.write(item.image + "\n")
		attrFile.write(item.attrs_sub)

	print "\t" + path + SUB_LINK_FILE + " created."
	print "\t" + path + SUB_IMAGE_FILE + " created."
	print "\t" + path + SUB_ATTR_FILE + " created."
	linkFile.close()
	imageFile.close()
	attrFile.close()	

def makeSeqRstFile(path, seqName, items, startIndex):
	dataFile = open(PATH_SRC + DATASET_SEQ_FILE.format(seqName), 'w')
	includePrefix = ".. include :: "
	dataFile.write(includePrefix + path + SUB_LINK_FILE + "\n")
	dataFile.write(includePrefix + path + SUB_IMAGE_FILE + "\n")
	dataFile.write(includePrefix + path + SUB_ATTR_FILE + "\n\n")
	itemsNum = len(items)
	room = len(SphinxSequence.LINK_SUB.format(0))
	roomList = [room] * 7
	column = len(roomList)
	table = WritingTable(roomList, dataFile)
	table.writeRow()
	while(itemsNum >= column):
		table.writeSequences(startIndex, column)
		itemsNum -= column
		startIndex += column

	if(itemsNum > 0):
		table.writeSequences(startIndex, itemsNum)
	print "\t" + PATH_SRC + DATASET_SEQ_FILE.format(seqName) + " created."

def makeAttrSubsFiles(attrs, items):
	attrFile = open(PATH_ATTR + ATTR_FILE, 'w')
	attrListFile = open(PATH_ATTR + ATTR_SEQ_LIST_FILE, 'w')
	descFile = open(PATH_ATTR + DESC_FILE, 'w')
	for i in range(len(attrs)):
		attrs[i].getAttrList(items, i)
		attrFile.write(attrs[i].name_sub)
		descFile.write(attrs[i].desc_sub)
		attrListFile.write(attrs[i].list_sub)
	print "\t" + PATH_ATTR + ATTR_FILE + " created."
	print "\t" + PATH_ATTR + ATTR_SEQ_LIST_FILE + " created."
	print "\t" + PATH_ATTR + DESC_FILE + " created."
	attrFile.close()
	attrListFile.close()
	descFile.close()

def makeAttrRstFile(attrsNum):
	path = "/datasets/attributes/"
	attrFile = open(PATH_SRC + DATASET_ATTR_FILE, 'w')
	includePrefix = ".. include:: "
	attrFile.write(includePrefix + path + ATTR_FILE + "\n")
	attrFile.write(includePrefix + path + ATTR_SEQ_LIST_FILE + "\n")
	attrFile.write(includePrefix + path + DESC_FILE + "\n\n")

	room = len(SphinxAttribute.NAME_SUB.format(0))
	roomList = [room, 50]
	table = WritingTable(roomList, attrFile)
	table.writeAttrHeader()
	for i in range(attrsNum):
		table.writeAttribute(i)
	print "\t" + PATH_SRC + DATASET_ATTR_FILE + " created."
	attrFile.close()



