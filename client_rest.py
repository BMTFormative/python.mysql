import http.client
import json

connect = http.client.HTTPSConnection("jsonplaceholder.typicode.com")
connect.request('GET', "/users")
request = connect.getresponse()
print("Status=%s / Message%s" % (request.status, request.reason))
txt = request.read().decode('utf-8')
tab = json.loads(txt)
for u in tab:
    print("%s (%s)" % (u["name"],u["address"]["city"]))

connect.close()