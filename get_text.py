import fitz  # PyMuPDF works with the alias 'fitz'
import jieba
import re
import csv

# Open the PDF file
pdf_document = fitz.open("factfulness_chinese.pdf")

# Initialize a string to store the extracted text
extracted_text = ""

# Iterate through the pages until we reach page 15
for page_number in range(len(pdf_document)):
    page = pdf_document[page_number]
    text = page.get_text()
    # if page_number == 54:
    #     break
    extracted_text += text

pdf_document.close()


def extract_unique_words(text):
    # Clean the text from punctuation
    pattern = re.compile(r'[^\u4e00-\u9fff]+')
    clean_text = re.sub(pattern, ' ', text)
    # Segment the text into words using jieba
    words = jieba.lcut(clean_text)
    # Get unique words
    unique_words = list(set(words))
    # Remove empty strings if any
    unique_words = [word for word in unique_words if word.strip()]
    return unique_words

data = extracted_text[1:]

# Call the function and print unique words
unique_words = extract_unique_words(data)
print(unique_words)

file_name = "words_whole_book.csv"

# Writing to a CSV file
with open(file_name, mode='w', newline='') as file:
    writer = csv.writer(file)
    for word in unique_words:
        writer.writerow([word])