import os

print(os.getcwd())
print(os.path.curdir)
print(os.path.join("fuNke","code"))
print(os.path.isabs(os.getcwd()))
print(os.path.abspath('.'))
print(os.path.basename(os.path.abspath('.')))
print(os.path.dirname(os.path.abspath('.')))

localfile = open("C:\\Users\\vibhu.ranjan\\Desktop\\bhaiya's info.txt");
file_content = localfile.read();
print(file_content)