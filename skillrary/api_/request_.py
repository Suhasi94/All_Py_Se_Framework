import requests
import os
import json
import jsonpath

# url = "https://www.google.com/"
# data = requests.get(url)
# print(data)
# print(type(data))
# print(data.status_code)
# print(data.content)
# print(data.headers)
# print(data.url)
# print(data.cookies)
# print(data.encoding)
# print(data.text)
os.chdir(r"C:\Users\User\OneDrive\Desktop\python_rmg_07")
# with open("demo.json","w") as f:
#     json.dump({"name": "abc", "id": 20},f)

# v_pointer = open("demo.json","r")
# data = v_pointer.read()
# print(data)
# print(type(data))
# json_data = json.loads(data)
# print(type(json_data))

##################### Response
# url1 = "https://reqres.in/api/users?page=2"
# v_res = requests.get(url1)
# v_content = v_res.text
# print(v_content) # will return json
# v_statuscode = v_res.status_code
# v_json_data = json.loads(v_content)
# print(v_json_data)
# v_per_page = jsonpath.jsonpath(v_json_data,'perpage')
# v_data_elements = jsonpath.jsonpath(v_json_data,'data')
# print(v_data_elements)
# print(len(v_data_elements[0]))
# assert v_statuscode == 200

############## post - create

url2 = "https://reqres.in/api/users"
f_pointer = open("demo.json")
v_input_data = f_pointer.read()
v_input_data_json = json.loads(v_input_data) # deserialize json into python
print("--InputData--")
print(v_input_data_json) #in python
# #execute the rest post api
# v_response = requests.post(url2,v_input_data_json)
# print("---Response Code---")
# print(v_response.text) # the response will be in json format
# #response code of the request
# v_responsecode = v_response.status_code
# print("----Response Code---")
# print(v_responsecode)
# #converting the response data into which is in json into py
# json_data = json.loads(v_response.text)
# print(json_data)
# # get the id of the response of the students value
# v_id = jsonpath.jsonpath(json_data,"id")
# print(v_id[0])
# # assert condition
# assert v_responsecode == 201
### till execute the rest api it is samre

##### put
v_response = requests.put("https://reqres.in/api/users/2",v_input_data_json)
print("---Response Code---")
print(v_response.text) # the response will be in json format
#response code of the request
v_responsecode = v_response.status_code
print("----Response Code---")
print(v_responsecode)
#converting the response data into which is in json into py
json_data = json.loads(v_response.text)
print(json_data)
## json data

v_name_input = v_input_data_json['name']
v_job_input = v_input_data_json["id"]
print(v_name_input)
print(v_job_input)
v_name = jsonpath.jsonpath(json_data,"name")
v_job = jsonpath.jsonpath(json_data,"id")
v_updatedAt = jsonpath.jsonpath(json_data,"updatedAt")
print(v_name[0])
print(v_job[0])
print(v_updatedAt[0])