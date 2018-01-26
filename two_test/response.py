import requests

request = requests.get('file:\\\C:\\Users\\puhui\\Desktop\\My Website.html')
print (request.text)
print (type(request.text))