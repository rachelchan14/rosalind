from tkinter import filedialog

def openfilename(): #toopen file via file dialog rather than path name
    path = filedialog.askopenfilename()
    return path

def countingDNAnucleotides(filename):
    nucleotides = open(filename).read()
    output = open("dna_output.txt", "w")
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
    bases = ['A', 'C', 'G', 'T']
    list = []
    for i in bases:
        list.append(str(nucleotides.count(i)))
    output.write(" ".join(list))
        #count = kind of like get but in non-dictionary version

file = openfilename()
countingDNAnucleotides(file)