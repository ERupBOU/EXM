import exifread
import mutagen
import magic
import PyPDF2

def metack(image_path):
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
        return {"error": "Не удалось прочитать метаданные аудиофайла."}

def get_file_type(file_path):
    file_type = magic.from_file(file_path, mime=True)
    return file_type

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

def main_menu():
    while True:
        print("Выберите действие:")
        print("1. Получить метаданные изображения (EXIF)")
        print("2. Получить метаданные аудиофайла (Mutagen)")
        print("3. Определить тип файла (python-magic)")
        print("4. Получить метаданные PDF-файла (PyPDF2)")
        print("5. Вернуться в главное меню")
        print("6. Выйти")

        choice = input("[?] Введите номер действия: ")

        if choice == "1":
            image_path = input("Введите путь к изображению: ")
            image_metadata = get_image_metadata(image_path)
            print("Метаданные изображения:")
            for key, value in image_metadata.items():
                print(f"{key}: {value}")
        elif choice == "2":
            audio_path = input("Введите путь к аудиофайлу: ")
            audio_metadata = get_audio_metadata(audio_path)
            if "error" in audio_metadata:
                print(audio_metadata["error"])
            else:
                print("Метаданные аудиофайла:")
                for key, value in audio_metadata.items():
                    print(f"{key}: {value}")
        elif choice == "3":
            file_path = input("Введите путь к файлу: ")
            file_type = get_file_type(file_path)
            print(f"Тип файла: {file_type}")
        elif choice == "4":
            pdf_path = input("Введите путь к PDF-файлу: ")
            pdf_metadata = get_pdf_metadata(pdf_path)
            print("Метаданные PDF-файла:")
            print(f"Автор: {pdf_metadata['author']}")
            print(f"Название: {pdf_metadata['title']}")
            print(f"Создатель: {pdf_metadata['creator']}")
            print(f"Дата создания: {pdf_metadata['creation_date']}")
        elif choice == "5":
            return
        elif choice == "6":
            print("Выход из программы...")
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")

if __name__ == "__main__":
    main_menu()