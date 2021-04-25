import urllib.request

webUrl = urllib.request.urlopen('https://google.com')

print (str(webUrl.getcode()))
print (str(webUrl.read()))