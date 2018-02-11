import random as r
from PIL import Image, ImageDraw, ImageFont

MX = 120
MY = 60


class captcha:
    __code = ''
    __image = Image.new('RGBA', (MX, MY), (255, 255, 255, 255))

    def __init__(self):
        self.__create_captcha_code()
        self.__draw_captcha()

    def __create_captcha_code(self):
        alphabet = '1234567890abdefghijklmnpqrstvxyz'
        length = r.randint(4, 7)
        for i in range(length):
            self.__code += r.choice(alphabet)

    def __draw_captcha(self):
        def draw_lines():
            lines_amount = r.randint(1, 3)
            for j in range(lines_amount):
                color = (r.randint(0, 255), r.randint(0, 255), r.randint(0, 255), 128)
                d.line([0, r.randint(0, MY), MX, r.randint(0, MY)], fill=color)
                d.line([r.randint(0, MX), 0, r.randint(0, MX), MY], fill=color)

        def draw_dots():
            dots_amount = r.randint(0, 500)
            for i in range(dots_amount):
                color = (r.randint(0, 255), r.randint(0, 255), r.randint(0, 255), 255)
                d.point([r.randint(0, MX), r.randint(0, MX)], color)

        d = ImageDraw.Draw(self.__image)
        font = ImageFont.truetype('fonts/times-new-roman.ttf', 30)
        x = r.randint(10, 25)
        y = r.randint(10, 25)
        draw_lines()
        draw_dots()
        # разный шрифт, размер и угол для букв
        d.text((x, y), self.__code, font=font, fill=(0, 0, 0, 255))
        draw_lines()
        draw_dots()
        del d

    def get_image(self):
        return self.__image

    def get_code(self):
        return self.__code
