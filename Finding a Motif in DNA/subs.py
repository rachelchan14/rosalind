from tkinter import filedialog

def openfilename():
    path = filedialog.askopenfilename()
    return path

def subs(filename):
    file = open(filename).readlines()
    index = []
    seq = file[0]
    target = file[1].strip('\n')
    i = 0
    while (i < len(seq)):
        if (seq[i:i+len(target)] == target):
            index.append(str(i+1))
        i+=1
    output = open("subs.txt", "w")
    output.write(" ".join(index))

file = openfilename()
subs(file)