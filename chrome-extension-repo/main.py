import requests

cookies = {
    '_ga_M2GBM6BVHH': 'GS1.1.1686630089.1.1.1686630093.0.0.0',
    'HSID': 'AtUj4FSRpANDc99sh',
    'SSID': 'AgGhviIl9SLue5eVf',
    'APISID': '7knRpGeWWOxkUmyC/AuUDJWHtrCAnRJj_d',
    'SAPISID': 'Z71PJQM1baZhg0SF/Ap8cihMOb8feb1O-Q',
    '__Secure-1PAPISID': 'Z71PJQM1baZhg0SF/Ap8cihMOb8feb1O-Q',
    '__Secure-3PAPISID': 'Z71PJQM1baZhg0SF/Ap8cihMOb8feb1O-Q',
    'SEARCH_SAMESITE': 'CgQIwZgB',
    'AEC': 'Ad49MVE2rC442NRUqEeSRmeaYeHLUJOw5Aot1r21GhrRLKZqjtvpae82wI8',
    'SID': 'YwgPTN_pFHoSRFGH6E2cu8WjjKli1ha-3S_9a7AqrxnLS3QmN2tKlpRkRVxVPmUC0u7u3A.',
    '__Secure-1PSID': 'YwgPTN_pFHoSRFGH6E2cu8WjjKli1ha-3S_9a7AqrxnLS3QmH1W9J2D7vNtFK3BC9cNJjw.',
    '__Secure-3PSID': 'YwgPTN_pFHoSRFGH6E2cu8WjjKli1ha-3S_9a7AqrxnLS3Qmd3iT-ctYUkk4eh3qevapvw.',
    '__Secure-1PSIDTS': 'sidts-CjEBPu3jIQWFGqmO9Sq8fr8UcwqJnDaON9TOf6cy9xshcCqy6UPCmuhYznYswKB6hbY-EAA',
    '__Secure-3PSIDTS': 'sidts-CjEBPu3jIQWFGqmO9Sq8fr8UcwqJnDaON9TOf6cy9xshcCqy6UPCmuhYznYswKB6hbY-EAA',
    'NID': '511=ib3mhcMa_PN-xeJ44JUng4PSMCW0htTbgLj7N7TOFrbHkBi7srMI8Sz3lqMFfeFRfUS3L7tWx1ldAv1ZSH-xywC-pf0aIvLFdDFvlzfmqa-CZIkNW0PYPhv61D-v_0LLwhIV-TpDneqeTZgW14kL7frOFPj9Bch1tEIyzQba8xaIA_-1ySH7mC59ajWumUFIPsj4OiFJQLdAGZGQjXNn27lrRKn9Qw9G8AVLVb3C-f9u3aKiYmv-yv4OG4jIFQ',
    '1P_JAR': '2023-07-17-17',
    '_ga': 'GA1.3.1431936535.1686630049',
    '_gid': 'GA1.3.1716260511.1689678015',
    '_gat_gtag_UA_4436568_7': '1',
    '_ga_Q3KJSFNQDY': 'GS1.1.1689678014.4.1.1689678163.0.0.0',
    'SIDCC': 'APoG2W-m63ZnKHj7KqDLguPYFVE1D3zjB5HOgVjqEhfOsXacCcMyY2FVlHM3Bcose-bF9JwAiw',
    '__Secure-1PSIDCC': 'APoG2W9T0vXN0qX7jIz4EX1jUNuYu8fvGj6zcxNN3n9y3XFuJz0UH5TLguX6LEgY8MHmkVyj6A',
    '__Secure-3PSIDCC': 'APoG2W9u9bFjCP5JLEsHPmjFhV3epA9khjs5Uvulag5A1mrlCmEFa0Hnv3-00Trh0vidtsxfRtU',
}

headers = {
    'authority': 'chrome.google.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
    # 'cookie': '_ga_M2GBM6BVHH=GS1.1.1686630089.1.1.1686630093.0.0.0; HSID=AtUj4FSRpANDc99sh; SSID=AgGhviIl9SLue5eVf; APISID=7knRpGeWWOxkUmyC/AuUDJWHtrCAnRJj_d; SAPISID=Z71PJQM1baZhg0SF/Ap8cihMOb8feb1O-Q; __Secure-1PAPISID=Z71PJQM1baZhg0SF/Ap8cihMOb8feb1O-Q; __Secure-3PAPISID=Z71PJQM1baZhg0SF/Ap8cihMOb8feb1O-Q; SEARCH_SAMESITE=CgQIwZgB; AEC=Ad49MVE2rC442NRUqEeSRmeaYeHLUJOw5Aot1r21GhrRLKZqjtvpae82wI8; SID=YwgPTN_pFHoSRFGH6E2cu8WjjKli1ha-3S_9a7AqrxnLS3QmN2tKlpRkRVxVPmUC0u7u3A.; __Secure-1PSID=YwgPTN_pFHoSRFGH6E2cu8WjjKli1ha-3S_9a7AqrxnLS3QmH1W9J2D7vNtFK3BC9cNJjw.; __Secure-3PSID=YwgPTN_pFHoSRFGH6E2cu8WjjKli1ha-3S_9a7AqrxnLS3Qmd3iT-ctYUkk4eh3qevapvw.; __Secure-1PSIDTS=sidts-CjEBPu3jIQWFGqmO9Sq8fr8UcwqJnDaON9TOf6cy9xshcCqy6UPCmuhYznYswKB6hbY-EAA; __Secure-3PSIDTS=sidts-CjEBPu3jIQWFGqmO9Sq8fr8UcwqJnDaON9TOf6cy9xshcCqy6UPCmuhYznYswKB6hbY-EAA; NID=511=ib3mhcMa_PN-xeJ44JUng4PSMCW0htTbgLj7N7TOFrbHkBi7srMI8Sz3lqMFfeFRfUS3L7tWx1ldAv1ZSH-xywC-pf0aIvLFdDFvlzfmqa-CZIkNW0PYPhv61D-v_0LLwhIV-TpDneqeTZgW14kL7frOFPj9Bch1tEIyzQba8xaIA_-1ySH7mC59ajWumUFIPsj4OiFJQLdAGZGQjXNn27lrRKn9Qw9G8AVLVb3C-f9u3aKiYmv-yv4OG4jIFQ; 1P_JAR=2023-07-17-17; _ga=GA1.3.1431936535.1686630049; _gid=GA1.3.1716260511.1689678015; _gat_gtag_UA_4436568_7=1; _ga_Q3KJSFNQDY=GS1.1.1689678014.4.1.1689678163.0.0.0; SIDCC=APoG2W-m63ZnKHj7KqDLguPYFVE1D3zjB5HOgVjqEhfOsXacCcMyY2FVlHM3Bcose-bF9JwAiw; __Secure-1PSIDCC=APoG2W9T0vXN0qX7jIz4EX1jUNuYu8fvGj6zcxNN3n9y3XFuJz0UH5TLguX6LEgY8MHmkVyj6A; __Secure-3PSIDCC=APoG2W9u9bFjCP5JLEsHPmjFhV3epA9khjs5Uvulag5A1mrlCmEFa0Hnv3-00Trh0vidtsxfRtU',
    'origin': 'https://chrome.google.com',
    'pragma': 'no-cache',
    'referer': 'https://chrome.google.com/',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'x-client-data': 'CIi2yQEIo7bJAQipncoBCNfoygEIkqHLAQiHoM0BCNy9zQEI58HNAQjvxM0B',
    'x-same-domain': '1',
}

params = {
    'hl': 'en-US',
    'gl': 'CN',
    'pv': '20210820',
    'mce': 'atf,pii,rtr,rlb,gtc,hcn,svp,wtd,hap,nma,dpb,utb,hbh,ebo,hqb,ifm,ndd,ntd,oiu,uga,c3d,ncr,hns,ctm,ac,hot,hsf,hfi,dtp,mac,bga,pon,fcf,rai,hbs,rma,igb,ibg,pot,evt,hib,crw',
    'requestedCounts': 'featured:5:10:false,mcol#top_picks_web-development:7:1:true,infiniteWall:21:0:false',
    'category': 'ext/11-web-development',
    '_reqid': '7368416',
    'rt': 'j',
}

data = 'login=imgchatgtp%40gmail.com&f.req=%5B%5B%5B%22featured%22%2C5%2C10%2C0%5D%2C%5B%22mcol%23top_picks_web-development%22%2C7%2C1%2C1%5D%2C%5B%22infiniteWall%22%2C21%2C0%2C0%5D%5D%2C%22ext%2F11-web-development%22%5D&t=AHUv8HENpG5DiYRWCHdUqLuZ9awKKQmv_w%3A1689678013315&'
proxy={
    'http':'http://127.0.0.1:34891',
    'https':'https://127.0.0.1:34891',
}
response = requests.post('https://chrome.google.com/webstore/ajax/item', params=params, 
cookies=cookies, headers=headers, data=data,proxies=proxy,
timeout=10
)

content = response.text[5:]
# with open('chrome.txt','w',encoding='utf8') as fp:
    # fp.write(content[5:])
import json
js_data = json.loads(content)
print(js_data)