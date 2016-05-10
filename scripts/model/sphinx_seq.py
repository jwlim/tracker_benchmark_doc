from config import *

class SphinxSequence:
    IMG_WIDTH = 100
    IMG_HEIGHT = 75
    LINK_SUB = "|links{0:03d}|"
    IMG_SUB = "|image{0:03d}|"
    ATTR_SUB = "|attrs{0:03d}|"
    ## attributes
    # name  : sequence name
    # image : image substitution
    # link  : link substitution
    # attrs : attributes list
    # attrs_sub : attrs's substitution


    def __init__(self, line, num):
        seq = line.strip().split('\t')
        self.name = seq[0]
        self.initLink(seq[0], num)
        self.initImage(seq[0], num)
        self.initAttrs(seq[1], num)

    def initLink(self, name, num):
        substitution = ".. "+ self.LINK_SUB.format(num) +" replace:: " + name + "_\n"
        downloadLink = "./seq/" + name + ".zip\n"
        self.link = substitution + ".. _" + name + ": " + downloadLink 

    def initImage(self, name, num):
        substitution = ".. "+ self.IMG_SUB.format(num) +" image:: /seq/" + name + ".png\n"
        #substitution += "\t:width: {0}px\n".format(self.IMG_WIDTH)
        #substitution += "\t:height: {0}px\n".format(self.IMG_HEIGHT)
        self.image = substitution

    def initAttrs(self, attrs, num):
        self.attrs = attrs.split(', ')
        substitution = ".. "+ self.ATTR_SUB.format(num) +" replace:: " + attrs + "\n"
        self.attrs_sub = substitution

    def __lt__(self, other):
        return self.name < other.name

    @staticmethod
    def getSeqLines(seqNum):
        seqName = "seq{0}".format(seqNum + 1)
        path = PATH_DATA + seqName + "/"
        srcItemFile = open(path + SRC_ITEM_FILE)
        itemLines = srcItemFile.readlines()
        return itemLines

    @staticmethod
    def getSeqList(seqNum, startIndex):
        itemLines = SphinxSequence.getSeqLines(seqNum)
        seqList = []
        for i in range(len(itemLines)):
            item = SphinxSequence(itemLines[i], i+startIndex)
            seqList.append(item)
        return seqList
