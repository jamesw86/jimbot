from PIL import Image, ImageFont, ImageDraw, ImageOps
import datetime
import tempfile
from datetime import timedelta

def getDays():
    td = datetime.datetime.now() - datetime.datetime(2020, 4, 1) 
    days = td.days
    return days


date_text = "Day " + str(getDays()) + " of lockdown:"

im = Image.open('egg_offer.jpg')
im = ImageOps.pad(im, (im.size[0],im.size[1]+50), color='white', centering=(0.5,1))
draw = ImageDraw.Draw(im)

# use a truetype font
font = ImageFont.truetype("arial.ttf", 30)

draw.text((10, 15), date_text, font=font, fill="black")

im.save("Day" + str(getDays()) + ".jpg")
print("Image saved as: " + "Day" + str(getDays()) + ".jpg")
