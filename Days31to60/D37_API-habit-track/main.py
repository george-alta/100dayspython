from datetime import datetime
from config import TOKEN, USERNAME
import requests

GRAPH = 'graph1'
pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    'id': 'graph1',
    'name': 'days training',
    'unit': 'minutes',
    'type': 'int',
    'color': 'sora',
    'timezone': 'NZ'
}

headers = {
    'X-USER-TOKEN': TOKEN
}
# the token needs to be sent as part of the header
# response = requests.post(
#     url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# post a pixel
now = datetime.now()
today = now.strftime("%Y%m%d")
minutes = str(input(f"How Many minutes did you trained today? {today}: "))
json_pixel = {
    'date': today,
    'quantity': minutes

}
pixel_url = f"{graph_endpoint}/{GRAPH}"
print(pixel_url)
response = requests.post(
    url=pixel_url, json=json_pixel, headers=headers)
print(response.text)


# {"message":"Please retry this request. Your request for some APIs will be rejected 25% of the time because you are not a Pixela supporter. If you are interested in being a Pixela supporter, please see: https://github.com/a-know/Pixela/wiki/How-to-support-Pixela-by-Patreon-%EF%BC%8F-Use-Limited-Features","isSuccess":false,"isRejected":true}
