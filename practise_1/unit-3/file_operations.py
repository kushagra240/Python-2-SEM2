def write_text_file(file_name, text):
    with open(file_name, "w", encoding="utf-8") as file_handle:
        file_handle.write(text)


def read_text_file(file_name):
    with open(file_name, "r", encoding="utf-8") as file_handle:
        return file_handle.read()
