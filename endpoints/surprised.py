from io import BytesIO

from PIL import Image, ImageDraw
from flask import send_file

from utils.endpoint import Endpoint, setup
from utils.textutils import wrap


@setup
class Surprised(Endpoint):
    params = ['text']

    def generate(self, avatars, text, usernames):
        base = Image.open(self.assets.get('assets/surprised/surprised.bmp')).convert('RGBA')
        font = self.assets.get_font('assets/fonts/robotoregular.ttf', size=36)
        try:
            text1, text2 = text.split(',')
        except ValueError:
            text1, text2 = 'tries to use surprised without splitting by comma,the command breaks'.split(',')
        text1 = wrap(font, 'me: ' + text1, 650)
        text2 = wrap(font, 'also me: ' + text2, 650)
        canv = ImageDraw.Draw(base)
        canv.text((20, 20), text1, font=font, fill='White')
        canv.text((20, 140), text2, font=font, fill='White')
        base = base.convert('RGB')

        b = BytesIO()
        base.save(b, format='jpeg')
        b.seek(0)
        return send_file(b, mimetype='image/jpeg')
