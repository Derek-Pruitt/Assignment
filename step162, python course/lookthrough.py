# Author        Derek Pruitt

# Python        3.8.3

# Assignment for school



file_List = ('information.docx','Hello.txt','myImage.png',\
             'myMovie.mpg','World.txt','data.pdf','myPhoto.jpeg')
for value in file_List:
    if value.endswith(".txt"):
        print(value)

