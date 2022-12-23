from tkinter import filedialog

def openfilename():
    path = filedialog.askopenfilename()
    return path

codon_table = {'GCU':'A','GCC':'A','GCA':'A','GCG':'A','CGU':'R','CGC':'R','CGA':'R','CGG':'R','AGA':'R','AGG':'R','UCU':'S','UCC':'S','UCA':'S','UCG':'S','AGU':'S','AGC':'S','AUU':'I','AUC':'I','AUA':'I','AUU':'I','AUC':'I','AUA':'I','UUA':'L','UUG':'L','CUU':'L','CUC':'L','CUA':'L','CUG':'L','GGU':'G','GGC':'G','GGA':'G','GGG':'G','GUU':'V','GUC':'V','GUA':'V','GUG':'V','ACU':'T','ACC':'T','ACA':'T','ACG':'T','CCU':'P','CCC':'P','CCA':'P','CCG':'P','AAU':'N','AAC':'N','GAU':'D','GAC':'D','UGU':'C','UGC':'C','CAA':'Q','CAG':'Q','GAA':'E','GAG':'E','CAU':'H','CAC':'H','AAA':'K','AAG':'K','UUU':'F','UUC':'F','UAU':'Y','UAC':'Y','AUG':'M','UGG':'W','UAG':'','UGA':'','UAA':'' }

def translate(filename):
    file = open(filename).read()
    start_index = file.find("AUG")
    proteins = []
    for i in range(start_index, len(file), 3):
        if (file[i:i+3] in codon_table):
            proteins.append(codon_table[file[i:i+3]])
    output = open("prot.txt", "w")
    output.write("".join(proteins))

file = openfilename()
translate(file)