import requests
from datetime import datetime

USER_NAME = "nikki007"
PIXELA_TOKEN = "dhjskdhks63278sdnkjsdkls"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "dhjskdhks63278sdnkjsdkls",
    "username": "nikki007",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# creating a user account in pixela
# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config = {
    "id": "graph12",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}
#created graph link
#https://pixe.la/v1/users/nikki007/graphs/graph12.html

#response = requests.post(graph_endpoint, json=graph_config, headers=headers)
#print(response.text)

graph_id = "graph12"

# https://pixe.la//v1/users/<username>/graphs/<graphID>
graph_pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{graph_id}"

today = datetime.now()
#today = datetime(year=2024, month=1, day=29)

print(today.strftime("%Y%m%d"))

graph_pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many Km did you cycle?"),
}

response = requests.post(graph_pixel_endpoint, json=graph_pixel_config, headers=headers)
print(response.text)

update_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{graph_id}/20240130"

new_pixel_data = {
    "quantity": "12.4"
}

#response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
#print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{graph_id}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
