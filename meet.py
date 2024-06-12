import exifread
import mutagen
import magic
import PyPDF2

def metack():
    while True:
        print("Select an action:")
        print("1. Work with image metadata (EXIF)")
        print("2. Work with audio metadata (Mutagen)")
        print("3. Determine file type (python-magic)")
        print("4. Work with PDF metadata (PyPDF2)")
        print("5. Exit")

        choice = input("[?] Enter the number of the action: ")

        if choice == "1":
            handle_image_metadata()
        elif choice == "2":
            handle_audio_metadata()
        elif choice == "3":
            handle_file_type()
        elif choice == "4":
            handle_pdf_metadata()
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

def handle_image_metadata():
    file_path = input("Enter the path to the image: ")
    with open(file_path, 'rb') as f:
        tags = exifread.process_file(f)
        print("Image metadata:")
        for tag in tags.keys():
            if tag not in ('JPEGThumbnail', 'EXIF MakerNote'):
                print(f"{tag}: {tags[tag]}")

def handle_audio_metadata():
    file_path = input("Enter the path to the audio file: ")
    audio = mutagen.File(file_path)
    if audio is not None:
        print("Audio file metadata:")
        for key, value in audio.items():
            print(f"{key}: {value}")
    else:
        print("Failed to read the audio file metadata.")

def handle_file_type():
    file_path = input("Enter the path to the file: ")
    file_type = magic.from_file(file_path, mime=True)
    print(f"File type: {file_type}")

def handle_pdf_metadata():
    file_path = input("Enter the path to the PDF file: ")
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        metadata = pdf_reader.metadata
        print("PDF file metadata:")
        print(f"Author: {metadata.author}")
        print(f"Title: {metadata.title}")
        print(f"Creator: {metadata.creator}")
        print(f"Creation date: {metadata.creation_date}")