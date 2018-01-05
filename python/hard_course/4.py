import os

result_dirs = list()
# os.chdir("main/")
# print(os.getcwd())

for current_dir, dirs, files in os.walk("main/"):
    for file in files:
        if file[-3:] == ".py":
            if current_dir not in result_dirs:
                result_dirs.append(current_dir)


result_dirs.sort()

with open("new_file.txt", "w") as f:
    for dir in result_dirs:
        f.write(dir + "\n")
