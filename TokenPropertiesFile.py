import json, requests

for i in range(0, 100000):
    url = requests.get("https://api.otherside.xyz/lands/{tokenId}".format(tokenId=i))
    text = url.text
    
    if text == 'Specified token has not been minted':
        continue

    data = json.loads(text)

    with open('./nftdata/{tokenId}.json'.format(tokenId=i),'w') as jsonFile:
        json.dump(data, jsonFile)