import requests

url = "http://127.0.0.1:5000/get_form"

data = {
    "user_name": "Man Man",
    "order_date": "01.01.1999",
    "lead_email": "man.man@gmail.com"
}
response = requests.post(url, data=data)
print(response.json())

data = {
    "order_date": "11.11.1111",
    "user_phone": "+76300900022",
    "lead_email": "vb.vb@gmail.com"
}
response = requests.post(url, data=data)
print(response.json())

data = {
    "user_name": "Some Name",
    "order_date": "31.02.2020",
    "lead_email": "some.name@gmail.com",
    "extra_field": "extra_value"
}
response = requests.post(url, data=data)
print(response.json())