import file_operations as fo


fo.write_text_file("sample_text.txt", "Hello from file operations")
print(fo.read_text_file("sample_text.txt"))
