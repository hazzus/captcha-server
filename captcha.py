import random as r
from PIL import Image, ImageDraw, ImageFont


class captcha:
    MY = 60
    __code = ''
    __font = ImageFont.truetype('fonts/times-new-roman.ttf', 30)

    @staticmethod
    def __random_color():
        return r.randint(0, 255), r.randint(0, 255), r.randint(0, 255), 255

    def __init__(self):
        self.__create_captcha_code()
        self.MX = len(self.__code) * 30 + 50
        self.__background = self.__random_color()
        self.__image = Image.new('RGBA', (self.MX, self.MY), self.__background)
        self.__draw_captcha()

    def __create_captcha_code(self):
        alphabet = '1234567890abdefghijklmnpqrstvxyz'
        length = r.randint(4, 7)
        for i in range(length):
            self.__code += r.choice(alphabet)

    def __draw_captcha(self):
        def draw_lines():
            lines_amount = r.randint(2, 5)
            for j in range(lines_amount):
                color = self.__random_color()
                d.line([0, r.randint(0, self.MY), self.MX, r.randint(0, self.MY)], fill=color)
                d.line([r.randint(0, self.MX), 0, r.randint(0, self.MX), self.MY], fill=color)

        def draw_dots():
            dots_amount = r.randint(0, 500)
            for i in range(dots_amount):
                color = (r.randint(0, 255), r.randint(0, 255), r.randint(0, 255), 255)
                d.point([r.randint(0, self.MX), r.randint(0, self.MX)], color)

        def turn(s, x, y, a):
            temp = Image.new('RGBA', (30, 40), self.__background)
            temp_draw = ImageDraw.Draw(temp)
            temp_draw.text((10, 0), s, font=self.__font, fill=(0, 0, 0, 255))
            temp = temp.rotate(a, )
            self.__image.paste(temp, (x, y), temp)

        d = ImageDraw.Draw(self.__image)
        x = r.randint(10, 25)
        y = r.randint(5, 20)
        draw_lines()
        draw_dots()
        for symbol in self.__code:
            angle = r.randint(-30, 30)
            turn(symbol, x, y, angle)
            x += 30
        # TODO алгоритм искажения изображений
        draw_lines()
        draw_dots()
        del d

    def get_image(self):
        image = self.__image
        self.clear_image()
        return image

    def get_code(self):
        return self.__code

    def clear_image(self):
        self.__image = Image.new('RGBA', (self.MX, self.MY), (255, 255, 255, 255))