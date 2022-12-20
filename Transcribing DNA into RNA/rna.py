def openfilename():
    path = filedialog.askopenfilename()
    return path

def transcribe(filename):
    nucleotides = open(filename).read()
    output = open("rna_output.txt", "w")
    replaced = nucleotides.replace('T', 'U')
    output.write(replaced)
