import PyPDF2, pyttsx3

pdfreader = PyPDF2.PdfFileReader(open('file_name.pdf', 'rb'))
speaker = pyttsx3.init()

for page_num in range(pdfreader.numPages):
    text = pdfreader.getPage(page_num).extractText()
    clean_text = text.strip().replace('\n', ' ')

speaker.save_to_file(clean_text, 'test_file.mp3')
speaker.runAndWait()
speaker.stop()
