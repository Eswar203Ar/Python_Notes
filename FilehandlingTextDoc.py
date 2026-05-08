try :
    file = open("D:\\input.txt",mode = 'r')
    print("File opened")
    data = file.read()
    print(data)
    file.close()
    print("File closed")
except FileNotFoundError:
    print("Exception : Invalid File Name")