import os
print("#########################################")
print("#            FILE HANDLEING             #")
print("(#########################################")
while(True):
def ins():
    print("1. create new file")
    print("2. write the text in file")
    print("3. list the files")
    print("4. delete the file")
    print("5. rename the file")
    print("6. stop the program")
ins()
c=int(input('enter ur choice: '))
def create_file():
    name=input('enter the file name: ')
    with open(name+",txt","w")as file:
        file.write("welcome")
    print(name,"created sucessfully...")
def write_file():
    name=input('enter the file name to write: ')
    text=input('type the content: ')
    with open(name+",txt","a")as file:
        file.write("welcome")
    print(name,"created sucessfully...")

while(True):
    ins()
    match c:
        case 1:
            print("creating file")
            create_file()
        case 2:
            print("edit")
            write_file()
        case 3:
            print("list file")
            files_list=os.listdir(".")
            print(files_list)
        case 4:
            print("delete file")
            n=input("type the file name to delete: ")
            os.remove
    case 5:
        print("rename")
    case 6:
        print("stop the program")
def create_file():
    name=input('enter the file name: ')
    with open(name+".txt","w")as file:
        file.write("welcome")
    print(name,"created sucessfully..")
match c:
    case 1:
        print("creating file")
        create_file()
    case 2:
        print("edit")
        write_file()
    case 3:
        print("list file")
        files_list=os.listdir(".")
        print(files_list)
    case 4:
        print("delete file")
    case 5:
        print("rename")
    case 6:
        print("stop the program")