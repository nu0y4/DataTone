def gpt2(data:str):
    import requests

    req = requests.post(burp0_url, headers=burp0_headers, json=burp0_json).content
    return req.decode('utf8')
