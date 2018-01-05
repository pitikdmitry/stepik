with open("dataset_24465_4.txt", "r") as file_read, open("new_file.txt", "w") as file_write:
    for line in reversed(file_read.readlines()):
        file_write.write(line)
