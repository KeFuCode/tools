import json, requests

url = requests.get("https://api.otherside.xyz/lands/20")
text = url.text

if text == 'Specified token has not been minted':
    print('not been minted')
    exit(0)

# print(type(text))
# <class 'str'>

data = json.loads(text)

# print(type(data))
# <class 'dict'>
 
attributes = data['attributes']



    