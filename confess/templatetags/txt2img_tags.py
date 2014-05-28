from django.conf import settings
from django import template
from PIL import Image, ImageDraw, ImageFont
from os import chdir, path



register = template.Library()

def txt2img(text,bg="#ffffff",fg="#000000",font="Tinos-Regular.TTF",FontSize=14):
    font_dir = settings.MEDIA_ROOT+"/text2img/"   # Set the directory to store the images
    img_name = str(text)+".png" # Remove hashes
    if path.exists(str(font_dir)+str(img_name)):
        pass
    else:
        font_size = FontSize
        fnt = ImageFont.truetype(font_dir+font, font_size)
        w, h= fnt.getsize(text)
        img = Image.new('RGBA', (w, h), bg)
        draw = ImageDraw.Draw(img)
        draw.fontmode = "0" 
        draw.text((0,0), text, font=fnt, fill=fg)
        img.save(font_dir+img_name,"PNG",quality=100)
    imgtag = '<img src="'+settings.MEDIA_URL+'txt2img/'+img_name+'" alt="'+text+'" />'
    return imgtag
register.tag(txt2img)





