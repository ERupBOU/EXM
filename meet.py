import exifread
import mutagen
import PyPDF2

def get_image_metadata(image_path):
    with open(image_path, 'rb') as f:
        tags = exifread.process_file(f)
        metadata = {}
        for tag in tags.keys():
            if tag not in ('JPEGThumbnail', 'EXIF MakerNote'):
                metadata[tag] = tags[tag]
    return metadata

def get_audio_metadata(audio_path):
    audio = mutagen.File(audio_path)
    if audio is not None:
        return dict(audio)
    else:
        return {"error": "Failed to read audio file metadata."}

def get_pdf_metadata(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        metadata = pdf_reader.metadata
        return {
            "author": metadata.author,
            "title": metadata.title,
            "creator": metadata.creator,
            "creation_date": metadata.creation_date
        }

def metack():
    while True:
        print("Select an action:")
        print("1. Get image metadata (EXIF)")
        print("2. Get audio file metadata (Mutagen)")
        print("3. Get PDF metadata (PyPDF2)")
        print("4. Return to main menu")
        print("5. Exit")

        choice = input("[?] Enter the action number: ")

        if choice == "1":
            image_path = input("Enter the path to the image: ")
            image_metadata = get_image_metadata(image_path)
            print("Image metadata:")
            for key, value in image_metadata.items():
                print(f"{key}: {value}")
        elif choice == "2":
            audio_path = input("Enter the path to the audio file: ")
            audio_metadata = get_audio_metadata(audio_path)
            if "error" in audio_metadata:
                print(audio_metadata["error"])
            else:
                print("Audio file metadata:")
                for key, value in audio_metadata.items():
                    print(f"{key}: {value}")
        elif choice == "3":
            pdf_path = input("Enter the path to the PDF file: ")
            pdf_metadata = get_pdf_metadata(pdf_path)
            print("PDF file metadata:")
            print(f"Author: {pdf_metadata['author']}")
            print(f"Title: {pdf_metadata['title']}")
            print(f"Creator: {pdf_metadata['creator']}")
            print(f"Creation date: {pdf_metadata['creation_date']}")
        elif choice == "4":
            return
        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")
