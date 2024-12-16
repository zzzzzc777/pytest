import requests
headers = {"Content-Type": "text/xml"}
datas = """<?xml version="1.0"?>
<methodCall>
    <methodName>examples.getStateName</methodName>
    <params>
        <param>
            <value><i4>41</i4></value>
        </param>
    </params>
</methodCall>"""
r = requests.post("http://httpbin.org/post", data=datas, headers=headers)
print(r.text)