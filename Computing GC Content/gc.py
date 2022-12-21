from tkinter import filedialog

def openfilename(): #toopen file via file dialog rather than path name
    path = filedialog.askopenfilename()
    return path

def gc(filename):
    filelines = open(filename).readlines()
    max_gc = 0.0
    max_name = filelines[0][1:]
    line = 0
    while (line < len(filelines)):
        if (filelines[line][0] == '>'):
            name = filelines[line][1:]
            gc = 0
            length = 0
            line+=1
        while (line < len(filelines) and filelines[line][0] != '>'):
            gc = gc + filelines[line].count('G') + filelines[line].count('C')
            length += len(filelines[line]) - 1
            line+=1
        gc_percent = 100.0*gc/(length)
        if (gc_percent > max_gc):
            max_gc = gc_percent
            max_name = name
    output = open("gc_output.txt", "w")
    output.write(max_name)
    output.write(str(max_gc))

file = openfilename()
gc(file)