import http.client

conn = http.client.HTTPSConnection("")

payload = "{\"metadata\":{\"createTime\":\"2019-07-29T09:12:33.001Z\",\"description\":\"This is a sample description string. It provides information about the resource.\",\"updateTime\":\"2019-07-29T10:12:33.001Z\",\"kind\":\"<collection>-<object>\",\"name\":\"resource-name\",\"links\":{\"rel\":\"/api/v1/services/environments/prod\"},\"displayName\":\"My Display Name\",\"uid\":\"d290f1ee-6c54-4b01-90e6-d701748f0851\",\"tags\":[\"production_public\",\"dev\",\"new_app\",\"us-west-1\",\"emea\"],\"ref\":\"/services/environments/prod\"},\"desiredState\":{\"content\":{\"policy\":{\"enforcementMode\":\"blocking\",\"bot-defense\":{\"settings\":{\"isEnabled\":false}},\"template\":{\"name\":\"POLICY_TEMPLATE_NGINX_BASE\"},\"headers\":[{\"name\":\"*\",\"type\":\"wildcard\",\"decodeValueAsBase64\":\"disabled\"},{\"name\":\"*-bin\",\"type\":\"wildcard\",\"decodeValueAsBase64\":\"required\"},{\"name\":\"Referer\",\"type\":\"explicit\",\"decodeValueAsBase64\":\"disabled\"},{\"name\":\"Authorization\",\"type\":\"explicit\",\"decodeValueAsBase64\":\"disabled\"},{\"name\":\"Transfer-Encoding\",\"type\":\"explicit\",\"decodeValueAsBase64\":\"disabled\"}],\"cookies\":[{\"name\":\"*\",\"type\":\"wildcard\",\"decodeValueAsBase64\":\"disabled\"}],\"applicationLanguage\":\"utf-8\",\"name\":\"mynappolicy\",\"parameters\":[{\"name\":\"*\",\"type\":\"wildcard\",\"decodeValueAsBase64\":\"disabled\"}],\"signatures\":[{\"signatureId\":123458888,\"enabled\":false},{\"signatureId\":200000098,\"enabled\":false},{\"signatureId\":200001475,\"enabled\":false},{\"signatureId\":200002595,\"enabled\":false}]}}}}"

headers = { 'content-type': "application/json" }

conn.request("POST", "%7B%7BCONTROLLER_FQDN%7D%7D/api/v1/security/policies", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))