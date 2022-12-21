from tkinter import filedialog

def openfilename(): #toopen file via file dialog rather than path name
    path = filedialog.askopenfilename()
    return path

def reverse_complement(filename):
    original = open(filename).read()
    reverse = ""
    i = len(original) - 1
    while i >= 0:
        reverse += original[i]
        i-=1
    new_seq = ""
    for i in reverse:
        if (i == 'A'):
            new_seq += 'T'
        elif (i == 'T'):
            new_seq += 'A'
        elif (i == 'G'):
            new_seq += 'C'
        elif (i == 'C'):
            new_seq += 'G'
    output = open("revc_output.txt", "w")
    output.write(reverse)

file = openfilename()
reverse_complement(file)