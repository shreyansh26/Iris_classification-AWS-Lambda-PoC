# {
#     "data": [
#         [6.5, 3.0, 5.8, 2.2],
#         [6.1, 2.8, 4.7, 1.2]
#     ]
# }

import requests

url = 'https://ti53furxkb.execute-api.us-east-1.amazonaws.com/test/classify'

myobj = {
    "data": [
        [6.5, 3.0, 5.8, 2.2],
        [6.1, 2.8, 4.7, 1.2]
    ]
}

x = requests.post(url, json = myobj)

print(x.text)