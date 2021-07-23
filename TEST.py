import numpy as np
import re
import Vectoriser

from numpy.core.arrayprint import str_format

class TESTCode:
    t = re.findall("[\w]+", "😬")
    print(t)
    if len(t)<2:
        bigramTokens = np.empty(shape=len(t)-1, dtype=np.dtype('U100'))
        for i in range(len(t)-1):
            bigramTokens[i] = t[i] + " " + t[i+1]
        print(bigramTokens)

class TEST():
    obj = TESTCode()