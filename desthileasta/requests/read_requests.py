import requests
import json

def call_requests(token, per_page,page):
  url = "https://webhook.site/token/{}/requests?per_page={}&page={}".format(token, per_page, page)
  headers = {'accept': 'application/json', 'api-key': token}
  response  = requests.get(url, headers=headers)
  count_selected, count_option_list, count_option_wizard, is_last_page = 0, 0, 0, True
  if response.status_code == 200:
    json_data = response.json()
    is_last_page = json_data["is_last_page"]
    content = [row["content"] for row in json_data["data"]]
    selected = [json.loads(item)["selected"] for item in content]    
    count_selected = len(selected)
    count_option_list = selected.count('list')
    count_option_wizard = selected.count('wizard')
  else:
    print('Error:', response.status_code)
  return count_selected, count_option_list, count_option_wizard, is_last_page

token = "5c669060-58a5-42a0-8cbd-76abd33e468e"

is_last_page = False
page = 0
total_selected, total_option_list, total_option_wizard = 0, 0, 0 
while not(is_last_page):
  page += 1
  count_selected, count_option_list, count_option_wizard, is_last_page = call_requests(token, 50, page)
  total_selected += count_selected
  total_option_list += count_option_list
  total_option_wizard += count_option_wizard
  print("page {}".format(page))
  print(count_selected)
  print(count_option_list)
  print(count_option_wizard)

print("totales")
print(total_selected)
print(total_option_list)
print(total_option_wizard)
print(is_last_page)


""" url = 'https://webhook.site/token/414559c2-a5ad-47c3-82ac-18155e56f4d9/requests?per_page=50&page=1'
headers = {'accept': 'application/json', 'api-key': '414559c2-a5ad-47c3-82ac-18155e56f4d9'}
response  = requests.get(url, headers=headers)
if response.status_code == 200:
  json_data = response.json()
  if(json_data["is_last_page"]):
    print("is last page")
  else:
    print("not is last page")
  
  
  content = [row["content"] for row in json_data["data"]]
  selected = [json.loads(item)["selected"] for item in content]
  
  count_selected = len(selected)
  count_option_list = selected.count('list')
  count_option_wizard = selected.count('wizard')
  
  print("Respuestas: {}, list: {}, wizard: {}".format(count_selected, count_option_list, count_option_wizard))
  print(json_data)
else:
  print('Error:', response.status_code) """