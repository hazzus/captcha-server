import requests as r

u = r.get('http://localhost:8080')
with open('saved_captcha.png', 'wb') as file:
    file.write(u.content)
ans = input()
u = r.post('http://localhost:8080', data=ans)
print(u.status_code)
