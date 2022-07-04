import PyPDF2
"""
PDF(Portable Document Format) is the file format developed by Adobe in the 1990s. 
At the present time, we all are familiared with its huge popularity in read-only 
documents.
Here, in this code I will be going to use PyPDF2 module for following things:

1) Extracting text
2) Copying pages
3) Rotating pages
4) Encrypting pdf

"""
def main():
    print(("""which of the following would you like to do on a pdf document?
1) Extracting text

2) Rotating pages

3) Encrypting pdf 

4) Quit
"""))
    try:

        user_selecion = int(input("Enter your response? "))
    
        if user_selecion == 1:
            extract()

        elif user_selecion == 2:
            rotatePages()
        
        elif user_selecion == 3:
            encrypt()

        elif user_selecion == 4:
            quit()

        else:
            print("Invalid selection\n")

    except Exception as e:
        print(e)

def extract():
    filename = input("Enter the name of your file? ")
    try:
        with open(filename, "rb") as file_in_progress:
            pdf_reader = PyPDF2.PdfFileReader(file_in_progress)
            # page = pdf_reader.getPage(0)
            # texts = page.extractText()
            number_pages = pdf_reader.numPages
            count = 0
            while count < number_pages:
                texts =" "
                page = pdf_reader.getPage(count)
                count += 1
                texts = page.extractText()
                print("Page number:",count)
                print(texts)
            file_in_progress.close()

    except Exception as e:
        print("Your file does not exit\n")
        print(e)

def rotatePages():
    print("""This feature will only rotate the first page of the pdf document in a clockwise.""")
    extension = ".pdf"
    filename = input("Enter the name of your file? ")
    filename += extension

    try:
        with open(filename, "rb") as file_in_progress:
            pdf_reader = PyPDF2.PdfFileReader(file_in_progress)
            pdf_writer = PyPDF2.PdfFileWriter()

            page = pdf_reader.getPage(0)
            degree = int(input("Enter the degree of the rotation(eg. 90, 180, 270): "))
            page.rotateClockwise(degree)

            pdf_writer.addPage(page)

            name_of_new_file = input("Name of the new file: ")
            name_of_new_file += extension

            result = open(name_of_new_file, "wb")
            pdf_writer.write(result)
            result.close()
            print("A new file has been created in same working directory as",result.name,"\n")

    except Exception as e:
        print("Something went wrong\n")
        print(e)


def encrypt():
    extension = ".pdf"
    filename = input("Enter the name of your file? ")
    filename += extension
    
    try:
        with open(filename, "rb") as file_in_progress:
            pdf_reader = PyPDF2.PdfFileReader(file_in_progress)
            pdf_writer = PyPDF2.PdfFileWriter()
            for page_numbers in range(pdf_reader.numPages):
                pdf_writer.addPage(pdf_reader.getPage(page_numbers))

            password = input("Enter the password for the new file: ")
            pdf_writer.encrypt(password)

            name_of_new_file = input("Name of the new file: ")
            name_of_new_file += extension

            result = open(name_of_new_file, "wb")
            pdf_writer.write(result)
            result.close()
            print("A new file has been created in same working directory as",result.name,"\n")

    except Exception as e:
        print("Something went wrong\n")
        print(e)


if "__main__" == __name__:
    while True:
        main()
