
#TASK 1:Read a File and Handle Errors

filename = "sample.txt"
try:
    with open(filename,"rt") as fh:
        content = fh.read()
except FileNotFoundError:
    print("error: The file",filename, "was not found.")
else:
    print("Reading file content")
    print("line1:",content.split("\n")[0])
    print("line2:",content.split("\n")[1])