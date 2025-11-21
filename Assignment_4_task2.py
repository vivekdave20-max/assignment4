#TASK 2:Write and Append Data to a File
f_name= "output.txt"
with open(f_name,"xt") as filehandle:
    filehandle.write(input("enter text to write to the file:"))
print("data successfully writen to",f_name)

with open(f_name, "rt") as filehandle:
    content = filehandle.read()
print("output:",content)

with open(f_name, "at") as filehandle:
    filehandle.write(input("Enter additional text to append:"))
print("data successfully writen to",f_name)

with open(f_name, "rt") as filehandle:
    content = filehandle.read()
print("Final content of", f_name,":\n",content)
