import http.client
import json

connect = http.client.HTTPSConnection("jsonplaceholder.typicode.com")
header = {'Content-Type': 'application/json'}
user = {'name': 'ali', 'age':33}
connect.request('post', "/users", json.dumps(user), header)
request = connect.getresponse()
if  (request.status == 201):
    print("Employee add successfully")
elif (request.status == 400):
    print(request.reason)
    print("Please completed all fields")
else: print(request.reason)

connect.close()