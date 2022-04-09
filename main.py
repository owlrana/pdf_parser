import PyPDF2
import re
#import textract
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# FILENAME IN DIR, PUT INSIDE A LOOP IF REQ FOR MULTIPLE FILES
filename = "DTE1-15June.pdf"

# OPEN FILE AS OBJ
pdfFileObj = open(filename,'rb')


# CONVERTING INTO PyPDF2 OBJECT THAT CAN BE PARSED
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)


# READ ALL PAGES
num_pages = pdfReader.numPages
count = 0
text = ""
while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count +=1
    text += pageObj.extractText()
    

#FIND EACH WORD THROUGH TWO SPACES AND OTHER DELIMITERS USIGN REGEX
raw = re.split(';|,|  |Ł|Ñ|Ó|Ò|\*|\n', text)


#punctuations = '"!@#$%^&*()_+=-][}{;:/?.>,< 0123456789\''

# LIST OF WORDS TO MAINTAIN
myList = []

# WORDS THAT SHOULD NOT BE INCLUDED
blacklisted = ['is', 'to', 'in']

for word in raw:
    curr = ""
    for letter in word:
        if (ord(letter) >= ord('a') and ord(letter) <= ord('z')) or (ord(letter) >= ord('A') and ord(letter) <= ord('Z')):
            curr = curr + letter
    if len(curr) > 1 and curr.lower() not in blacklisted:
        myList.append(curr.title())
    #print(curr, end="   ")

# MAINTAIN COUTN FOR EACH WORD
freq = {}
for word in myList:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

# THROW OUTPUT INTO TEXT FIEL
with open(filename[:-4] + "_freq" + ".txt", 'w') as f:
    # SORT DICT OBJ FIRST
    for w in sorted(freq, key=freq.get, reverse=True):
        line = str(freq[w]) + " = " + str(w) + "\n"
        f.write(line)
        
