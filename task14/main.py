import os
import shutil
from datetime import datetime

class FileSorter:
    FILE_TYPES = {
        "images": [".png", ".jpg", ".jpeg", ".gif", ".bmp"],
        "videos": [".mp4", ".avi", ".mov", ".mkv", ".flv"],
        "documents": [".docx", ".pdf", ".xls", ".xlsx", ".txt"],
        "audio": [".mp3", ".wav", ".ogg", ".aac"],
        "fonts": [".ttf", ".otf", ".woff", ".woff2"]
    }

    def __init__(self, input_directory, output_directory):
        self.input_directory = input_directory
        self.output_directory = output_directory

    def get_target_folder(self, file_extension):
        """Возвращает папку для конкретного типа файла"""
        return next((folder for folder, extensions in self.FILE_TYPES.items() if file_extension in extensions), None)

    def rename_file_with_timestamp(self, file_extension):
        """Переименовывает файл, добавляя текущую дату и время."""
        current_time = datetime.now().strftime("%Y_%m_%d_%H_%M")
        return f"{current_time}{file_extension}"

    def create_directory(self, path):
        """Создаёт директорию, если она не существует."""
        os.makedirs(path, exist_ok=True)

    def sort_files(self):
        """Сортирует файлы из папки input_directory в подкаталоги output_directory."""
        self.create_directory(self.output_directory)

        for file_name in os.listdir(self.input_directory):
            file_path = os.path.join(self.input_directory, file_name)

            if os.path.isdir(file_path):
                continue

            file_extension = os.path.splitext(file_name)[1].lower()

            target_folder = self.get_target_folder(file_extension)
            if not target_folder:
                print(f"Тип файла {file_name} не поддерживается. Пропускаем.")
                continue

            target_path = os.path.join(self.output_directory, target_folder)
            self.create_directory(target_path)

            new_file_name = self.rename_file_with_timestamp(file_extension)
            new_file_path = os.path.join(target_path, new_file_name)
            shutil.move(file_path, new_file_path)

            print(f"Файл {file_name} перемещён в {target_folder} как {new_file_name}.")

if __name__ == "__main__":
    input_dir = "uploads"
    output_dir = "sorted_files"

    if not os.path.exists(input_dir):
        print(f"Папка {input_dir} не найдена! Создайте её и добавьте файлы для сортировки.")
    else:
        sorter = FileSorter(input_dir, output_dir)
        sorter.sort_files()
        print("\nСортировка завершена.")
