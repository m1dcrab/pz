from PIL import Image, ImageFilter
from requests import get
import io

img1_link = 'https://psv4.userapi.com/s/v1/d/vhrr86J3my2CUKCXB_OgwQVgZFCTnp9PgA0nvxrdAg_C4H9Bk495sZTyQ1Bwt4fHR6cW05xX_5yu7h91tVncJJOajAjJ2VGUkTrwQX-JrCdKdvlt/image1.png'
img2_link = 'https://psv4.userapi.com/s/v1/d/lZJxaRrX6zv82dZ0Gd4pceVvcd8MtVi9KbcUVNb7tUT5EECf3JOVYF0SaetO6CGapSDYFTORo6A6Zub_ZbDbDebuj1SwQtW15_CKuu1VdGzBMwOQlN_LjA/image2.png'

def parse_img(link):
    return Image.open(io.BytesIO(get(link).content))

img = parse_img(img1_link)
img2 = parse_img(img2_link)

edited_img = img.crop((63, 67, 150, 150)).resize((300,300),0).rotate(180,expand=True)

triangle = img2.getchannel('G')
blank = img2.point(lambda _: 0)
mask = Image.composite(img2, blank, triangle)

edited_img.paste(img2.resize((300,300),0),(0,0),mask.resize((300,300),0).convert('L'))
edited_img.filter(ImageFilter.EMBOSS).convert('RGB').save('edited_img.tif')


