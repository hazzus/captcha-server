from captcha import *
import requests as r

u = r.get('http://localhost:8080')
print(u.text)
ans = input()
u = r.post('http://localhost:8080', data=ans)
print(u.text)