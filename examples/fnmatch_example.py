import fnmatch, os

for file in os.listdir('.'):
    if fnmatch.fnmatch(file, '*.html'):
        print (file)