from datetime import datetime
from config import TOKEN, USERNAME
import requests

headers = {
    'X-USER-TOKEN': TOKEN
}
now = datetime.now()
today = now.strftime("%Y%m%d")
print(today)

# how to delete a pixel (2022 - 09 - 11)
pixel_url = f'https://pixe.la/v1/users/{USERNAME}/graphs/graph1/20220911'
response = requests.delete(url=pixel_url, headers=headers)
print(response.text)
