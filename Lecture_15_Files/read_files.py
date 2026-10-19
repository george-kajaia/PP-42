# file = open("test.txt", "r" )
# try:
#     line = file.read()    
#     print(line.strip())
# finally:
#     file.close()



# file = open("test.txt", "r" )
# try:
#     line = file.readline()    
#     while line:
#         print(line.strip())
#         line = file.readline()
# finally:
#     file.close()



file = open("test.txt", "r" )
try:
    lines = file.readlines()    
    for x in lines:
        print(x.strip())
finally:
    file.close()

