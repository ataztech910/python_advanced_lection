import os
 
print(os.name)
print(os.environ)
print(os.getenv("TMPDIR"))
print(os.getcwd())
# os.chdir(r"C:\Users\mike\Documents") сменит директорию
os.mkdir("test")
os.rmdir("test")

# path = r'C:\Users\me\Documents\pytest\2014\02\19' создаст вложенный набор
# os.makedirs(path)

# os.remove("test.txt") удалит файл

# os.rename("test.txt", "pytest.txt") переименует файл
# os.startfile(r'C:\Users\me\Documents\labels.pdf') - запустит файл

path = r'/Users/alicefromwonderland/Desktop/study/my-presentations/python_advanced_26_04_2021/'
 
for root, dirs, files in os.walk(path):
    print(root)

fileDir = os.path.exists(r'C:\Python27\Tools\pynche\ChipViewer.py')
print(fileDir)
print( os.path.join(r'C:\Python27\Tools\pynche', 'ChipViewer.py') )
print( os.path.split(r'C:\Python27\Tools\pynche\ChipViewer.py') )