## Request a collection of permitted actions
## Returns a list of authorized actions based on a list of requested actions and resources.

import http.client

conn = http.client.HTTPSConnection("")

payload = "{\"items\":[{\"items\":[{\"permitted\":false,\"method\":\"DELETE\",\"path\":\"/services/environments/test1\"},{\"permitted\":true,\"method\":\"PUT\",\"path\":\"/services/environments/test2\"}]}]}"

headers = { 'content-type': "application/json" }

conn.request("POST", "%7B%7BCONTROLLER_FQDN%7D%7D/api/v1/platform/auth/verify", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))