import math
import random as r
from PIL import Image, ImageDraw, ImageFont


class captcha:
    MY = 60
    __code = ''
    __fonts = ['times-new-roman',
               'droid-sans',
               'dejavu-sans-mono',
               'helvetica',
               'pf-dintext',
               'vialog'
               ]

    @staticmethod
    def __random_color(x, y, transparency):
        return r.randint(x, y), r.randint(x, y), r.randint(x, y), transparency

    def __random_font(self):
        return ImageFont.truetype('fonts/' + self.__fonts[r.randint(0, len(self.__fonts) - 1)]+'.ttf', r.randint(25, 35))

    def __init__(self):
        self.__create_captcha_code()
        self.MX = len(self.__code) * 30 + 50
        self.__background = self.__random_color(128, 255, 255)
        self.__image = Image.new('RGBA', (self.MX, self.MY), self.__background)
        self.__draw_captcha()

    def __create_captcha_code(self):
        alphabet = '12345679abdefghijkmnpqrstvxyz'
        length = r.randint(4, 7)
        for i in range(length):
            self.__code += r.choice(alphabet)

    def __draw_captcha(self):
        def draw_lines():
            lines_amount = r.randint(1, 2)
            for j in range(lines_amount):
                color = self.__random_color(0, 128, 255)
                d.line([0, r.randint(0, self.MY), self.MX, r.randint(0, self.MY)], fill=color)
                d.line([r.randint(0, self.MX), 0, r.randint(0, self.MX), self.MY], fill=color)

        def draw_dots(divider):
            max_am = int(self.MX * self.MY / divider)
            dots_amount = r.randint(max_am, max_am)
            for i in range(dots_amount):
                color = self.__random_color(200, 255, 255)
                d.point([r.randint(0, self.MX), r.randint(0, self.MX)], color)

        def turn(s, x, y, a):
            temp = Image.new('RGBA', (30, 40), self.__background)
            temp_draw = ImageDraw.Draw(temp)
            temp_draw.text((10, 0), s, font=self.__random_font(), fill=self.__random_color(0, 90, 255))
            temp = temp.rotate(a, )
            self.__image.paste(temp, (x, y), temp)

        def make_waves():
            pixels = self.__image.load()
            new_image = Image.new('RGBA', (self.MX, self.MY), self.__background)
            new_pixels = new_image.load()
            amplitude = r.randint(180, 220) / 1000
            frequency = r.randint(80, 120) / 10000
            coefficient = r.randint(0, 1000) / 1000
            w, h = self.__image.size
            for x in range(w):
                for y in range(h):
                    x1 = x
                    y1 = int(y * (1 + amplitude * math.sin(2 * math.pi * x * frequency + 2 * math.pi / coefficient)))
                    if x1 > self.MX - 1:
                        x1 = self.MX -1
                    if x1 < 0:
                        x1 = 0
                    if y1 > self.MY - 1:
                        y1 = self.MY - 1
                    if y1 < 0:
                        y1 = 0
                    new_pixels[x1, y1] = pixels[x, y]
            self.__image = new_image

        d = ImageDraw.Draw(self.__image)
        x = r.randint(10, 25)
        y = r.randint(5, 20)
        draw_dots(10)
        for symbol in self.__code:
            angle = r.randint(-30, 30)
            turn(symbol, x, y, angle)
            x += 30
        make_waves()
        d = ImageDraw.Draw(self.__image)
        draw_lines()
        draw_dots(5)
        del d

    def get_image(self):
        image = self.__image
        self.clear_image()
        return image

    def get_code(self):
        return self.__code

    def clear_image(self):
        self.__image = Image.new('RGBA', (self.MX, self.MY), (255, 255, 255, 255))