import os

class FileEdit:

    def open_file(self, file_path):
        file = open(file_path, "r")
        content = file.read()
        file.close()

        return content


    def edit_file(self, file_path, text):
        file = open(file_path, "w")
        file.write(text)
        file.close()

    def delete_file(self, file_path):
        if os.path.exists(file_path):
            os.remove(file_path)
        else:
            raise Exception("File not found")

