import requests

url = 'https://randomuser.me/api/?gender=female'
query_params = {'gender':'female'}
header = {'x':'x_id'}
#calling an API
response = requests.get(url, params=query_params)

#calling with API endpoint
# response1 = requests.get('https://api.thecatapi.com/v1/breeds')

#getting response signal
# print(response)

#printing the http code
print(response.status_code)

#printing result as test format(list)
# print(response.text)
# print(response1.text)


# print(response.request.method)
# print(response.request.headers)
# print(response.headers)
# print(response.reason)

# print(response.content)
print(response.json())

