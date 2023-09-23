import requests
import json
from PIL import Image, ImageFont, ImageDraw
import textwrap
import glob, random


r = requests.get("https://api.themotivate365.com/stoic-quote")
data = r.json()
author = data['author']
quote = data['quote']

text = quote
text2 = author

images = glob.glob("./backgrounds/*.jpg")
random_image = random.choice(images)

MAX_W, MAX_H = 1000, 1200
img = Image.open(random_image).resize((MAX_W, MAX_H))
draw = ImageDraw.Draw(img)

font = ImageFont.truetype('Roboto-Black.ttf', size=80)


textwrapped = textwrap.wrap(text, width=25)
textwrapped2 = textwrap.wrap(text2, width=40)

#draw.text((0,y-150), '\n'.join(textwrapped), fill="white", font=font)


w = draw.textlength(text, font)
h = draw.textlength(text, font)
w2 = draw.textlength(text2, font)
h2 = draw.textlength(text2, font)

x = (MAX_W-800)/2
y = (MAX_H)/2

x2 = (MAX_W-w2)/2
y2 = (MAX_H-300)/2



res = len(quote.split())


if len(textwrapped2) == 0:
    if res >= 40:
        draw.text((0, 100), '\n'.join(textwrapped), fill="white", font=font, stroke_width=3, stroke_fill='black')
        draw.text((0, 0), "Unknown", fill="white", font=font, stroke_width=3, stroke_fill='black')

    elif res >= 30:
        draw.text((0, 200), '\n'.join(textwrapped), fill="white", font=font, stroke_width=3, stroke_fill='black')
        draw.text((0, 50), "Unknown", fill="white", font=font, stroke_width=3, stroke_fill='black')
    else:
        draw.text((0, 500), '\n'.join(textwrapped), fill="white", font=font, stroke_width=3, stroke_fill='black')
        draw.text((0, 300), "Unknown", fill="white", font=font, stroke_width=3, stroke_fill='black')
else:
    pass

if res >= 60:
    print("longer than 60")

if res >= 40:
    draw.text((0, 100), '\n'.join(textwrapped), fill="white", font=font, stroke_width=3, stroke_fill='black')
    draw.text((0, 0), '\n'.join(textwrapped2), fill="white", font=font, stroke_width=3, stroke_fill='black')

elif res >= 30:
    draw.text((0, 200), '\n'.join(textwrapped), fill="white", font=font, stroke_width=3, stroke_fill='black')
    draw.text((0, 50), '\n'.join(textwrapped2), fill="white", font=font, stroke_width=3, stroke_fill='black')
else:
    draw.text((0, 500), '\n'.join(textwrapped), fill="white", font=font, stroke_width=3, stroke_fill='black')
    draw.text((0,300), '\n'.join(textwrapped2), fill="white", font=font, stroke_width=3, stroke_fill='black')


img.save('H.png')
