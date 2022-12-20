from tkinter import filedialog
from test import x

def openfilename():
    path = filedialog.askopenfilename()
    return path

def countingDNAnucleotides(filename):
    nucleotides = open(filename).read()
    # my solution: 
    # my_dict = {}
    # for i in nucleotides:
    #     if (i == '\n'):
    #         continue
    #     my_dict[i] = my_dict.get(i, 0) + 1
    # ordered = sorted(my_dict.items())
    # dict(ordered)
    # for value in ordered:
    #     print (value[1], end = " ")
    
    # cleaner solution:
    print(nucleotides.count('A'), nucleotides.count('C'), nucleotides.count('G'), nucleotides.count('T')) #kind of like get but in non-dictionary version
