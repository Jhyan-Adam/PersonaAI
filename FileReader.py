import re
import datetime
import tensorflow as tf
import numpy as np

# Variables Declaration
batchSizeS = 3
batchNumberS = 31
batchSizeR = 6
batchNumberR = 29
rcvrBatchCntr = 0
sdrBatchCntr = 0
receiverBatches = np.empty(shape=(batchNumberR, batchSizeR), dtype=object)
senderBatches = np.empty(shape=(batchNumberS, batchSizeS), dtype=object)

def batchMaker(filepath):
    with open(filepath, encoding="utf-8") as chatFile:
        lines = chatFile.readlines()
        rowIdxR = 0
        colIdxR = 0
        rowIdxS = 0
        colIdxS = 0
        for line in lines:
            if not "<Media omitted>" in line:
                if colIdxS == batchSizeS:
                    colIdxS = 0
                    rowIdxS += 1
                if colIdxR == batchSizeR:
                    colIdxR = 0
                    rowIdxR += 1

                if rowIdxR < batchNumberR:
                    if "Jhyan:" in line:
                        global receiverBatches
                        receiverBatches[rowIdxR, colIdxR] = line
                        colIdxR += 1

                if rowIdxS < batchNumberS:
                    if "Misha:" in line:
                        global senderBatches
                        senderBatches[rowIdxS, colIdxS] = line
                        colIdxS += 1

        print(receiverBatches)
        print("######break######")
        print(senderBatches)

batchMaker("./Chat.txt")
# lineSplitter("./Chat.txt")
