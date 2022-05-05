from PyPDF2 import PdfFileReader


def get_pagenums(file_path):
    reader = PdfFileReader(file_path)

    if reader.isEncrypted:
        reader.decrypt('')
    page_num = reader.getNumPages()
    return page_num
