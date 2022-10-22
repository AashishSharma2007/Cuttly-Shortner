import urllib 
import requests
import json

#TODO: past you cuttly api key here.
key = ''
url = urllib.parse.quote(input('Type URL: '));
name = input('Custom Name: ')
r = requests.get('https://cutt.ly/api/api.php?key={}&short={}&name={}'.format(key,url,name))

data = json.loads(r.text)['url']

if data['status'] == 7:
    file = open('links.json','a+')
    #TODO: Fix this, This is not writing in json file
    file.write(r.text)
    file.close()
    print('Short Link: ' + data['shortLink'])
else : print(f'Something went wrong\nError Code {data["status"]}\nhttps://notes.io/qjye5')
input()
