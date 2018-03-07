import requests as r
import webbrowser
from htmlpage import HtmlPage

SERVER_ADDRESS = 'http://localhost:8080/'

# TODO normal client


def save(pic):
    path = 'saved_captcha.png'
    with open(path, 'wb') as file:
        file.write(pic)
    return path


def ask():
    user = r.get(SERVER_ADDRESS)
    path = save(user.content)
    page = HtmlPage()
    page.form_page(path, SERVER_ADDRESS)
    index = page.save()
    webbrowser.open(index)


if __name__ == '__main__':
    ask()
