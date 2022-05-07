import re

pattern = re.compile("H.*?o")
#step 1 : open file 
# advantage using "with as" -> no need to handle error
with open ("foo.txt",mode="r") as file:
#step2 : read line
    for line in file:
        match = re.search(pattern,line)
        if match:
            print(match.group())
    #data=file.read()
#print(data)

def hello(name , age):
    print("hello"+  name + str(age))

hello ("V1",87)

# Method 2: read file line by line
#readline() have white sapce
file1 = open ("foo.txt","r")
while True:
    line = file1.readline()
    if not line:
        break
    print("{}".format(line.strip()))
file1.close()