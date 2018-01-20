from collections import Counter
from tkinter import *
from tkinter import messagebox

# lst is a variable used to mainly contain the message alphabets.
lst = []
def encode(enc):
    counts = Counter(enc)
    temp = []

    for i in counts: # Cutting alphabets from the msg and appending it into [lst].
        temp += (str(counts[i]) + i)
        y = (i, counts[i])
        lst.append(y)


    messagebox.showinfo("Compressed", temp)



# Decoding the input MSG.
def decode(x):
    q = ""
    for character, count in x:
        q += character * count
    return q

def printmethods():
    compressed = encode(entry1.get())
    decomp = decode(lst)
    messagebox.showinfo("Decompresses", decomp)


''' Ui Components,
    here i used simple user interface to preview compilation of code. '''
root = Tk()
root.title('RLE')
mLabel=Label(root,text="RLE Compression").grid(columnspan=2)
label1=Label(root,text="Enter Word").grid(row=1,column=0,sticky=W)

entry1=Entry(root)
entry1.grid(row=1,column=1)
button1=Button(root,text="Compress",command=printmethods).grid(row=3,columnspan=2)
root.mainloop()
