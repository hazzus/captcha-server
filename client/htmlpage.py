class HtmlPage:
    head = '''
    <head>
        <title>Captcha-server</title>
    </head>
    '''
    body = ''

    def form_page(self, src, address):
        self.body = '''
        <img src="''' + src + '''" align=middle>
        <form method="post" action="''' + address + '''">
            <input type="text" name="answer">
            <input type="submit">
        </form>
        '''

    def error_page(self, code, content):
        self.body = '<h1>' + str(code) + content + '</h1>'

    def construct(self):
        return '<html>' + self.head + '<body>' + self.body + '</body></html>'

    def save(self):
        path = 'captcha.html'
        if len(self.body) > 0:
            with open(path, 'w+') as file:
                file.write(self.construct())
            return path
        else:
            print('Empty body')
