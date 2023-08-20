def gpt2(data:str):
    import requests

    burp0_url = "https://api.binjie.fun:443/api/generateStream?refer__1360=n4%2Bx0DcDBD9DgD1QDsDOImHcWsU3x%2BhD"
    burp0_headers = {"Sec-Ch-Ua": "\"Chromium\";v=\"109\", \"Not_A Brand\";v=\"99\"",
                     "Accept": "application/json, text/plain, */*", "Content-Type": "application/json",
                     "Sec-Ch-Ua-Mobile": "?0",
                     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.120 Safari/537.36",
                     "Sec-Ch-Ua-Platform": "\"Windows\"", "Origin": "https://c.binjie.fun",
                     "Sec-Fetch-Site": "same-site", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty",
                     "Referer": "https://c.binjie.fun/", "Accept-Encoding": "gzip, deflate",
                     "Accept-Language": "zh-CN,zh;q=0.9"}
    burp0_json = {"network": True, "prompt": data, "stream": False, "system": "",
                  "userId": "#/chat/1692026957621", "withoutContext": False}
    req = requests.post(burp0_url, headers=burp0_headers, json=burp0_json).content
    return req.decode('utf8')