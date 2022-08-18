import spacy
from PyPDF2 import PdfReader


nlp = spacy.load("en_core_web_sm")



def file_handler(file)->tuple:
    print("Opening this file {}".format(str(file)))

    data = ReadFile(file)
    data = NamedEntity(data)
    data = filter_data(data)
    return data

def ReadFile(filename)-> str:
    print("Reading file", filename)
    reader = PdfReader(filename)
    number_of_pages = len(reader.pages)
    
    # contains all the text from the file
    final_text = ""

    for page in reader.pages:
        text = page.extract_text()
        
        final_text += text

    return final_text




def NamedEntity(text)-> tuple:
    doc = nlp(text)
    #print((doc.ents))

    return (doc.ents)


def filter_data(raw_data):
    data = []
    lst = ['ORDINAL', 'CARDINAL']
    for i in raw_data:
        if i.label_ in lst:
            continue

        else:
            data.append((i.text,i.label_))

    return (data)