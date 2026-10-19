# file = open("data.txt", "w")
# try:
#     list = ["1 This is a test line\n", "2 This is a test line\n", "3 This is a test line\n"]
#     line = file.writelines(list)
#     print(line);
# finally:
#     file.close()


# file = open("data.txt", "w")
# try:    
#     line = file.write("abc")
#     print(line);
# finally:
#     file.close()


# file = open("data.txt", "a")
# try:    
#     line = file.write("\n123")
#     print(file.readable(), file.writable());
# finally:
#     file.close()


# file = open("data.txt", "r+")
# try:
#     line = file.write("\n123")
#     print(file.readable(), file.writable());
#     file.seek(0)
#     lines = file.readlines()
#     print(lines)
# finally:
#     file.close()


# file = open("data.txt", "a+")
# try:
#     line = file.write("\n123")
#     print(file.readable(), file.writable());
#     file.seek(0)
#     lines = file.readlines()
#     print(lines)
# finally:
#     file.close()


with open("data.txt", "r") as file:
    data = file.read()
print(data) 