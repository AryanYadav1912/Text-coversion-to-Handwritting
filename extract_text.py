import pywhatkit as kit
import PyPDF2 as pp
a=pp.PdfFileReader("progit.pdf")
print(a.documentInfo)
print(a.getNumPages())
str=""
for i in range(8,10):
    str +=a.getPage(i).extractText()

with open("text.txt","w",encoding="utf-8") as f:
    f.write(str)



'''hand=open("text.txt","r")
st=hand.read()
kit.text_to_handwriting(st,"handwriting.png",[20,10,0])'''

with open('text.txt', 'r') as fobj:
    text = fobj.read()

kit.text_to_handwriting(text, 'assignment.png',  rgb=[0, 0, 255]) # Default is set to Blue color