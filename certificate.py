import os
import cv2
from PIL import ImageFont, ImageDraw, Image

imgPath = 'E:\Projects\Python\Certificates\Template.png'

""" image = cv2.imread(imgPath)
# image = image.putText(image, 'text', (0, 50), font, fontScale, color)
font = cv2.FONT_ITALIC
text = "Hello Joseph!! This is longer!"
W, H = (1600/2,1131//2)

# get boundary of this text
textsize = cv2.getTextSize(text, font, 1, 2)[0] * 5

# get coords based on boundary
textX = (image.shape[1] - textsize[0]) // 2
# textY = (image.shape[0] + textsize[1]) // 2

# add text centered on image
# fontpath = "./AlexBrush-Regular.ttf" 
# fontpath = './simsun.ttc'    
# font = ImageFont.truetype(fontpath, 32)
# image = cv2.putText(image, text, (textX, 250 ), font, 1, (72, 187, 247), 2)
image = Image.open("Template.png")  
  
draw = ImageDraw.Draw(image)
w, h = draw.textsize(text, 80)
  
# use a truetype font  
font = ImageFont.truetype("AlexBrush-Regular.ttf", 80)  
  
draw.text(((W-w/2), (H-h/2)), text, font=font)  
# cv2.imwrite("Test.png", image)
image.save("Test.png") """

keys = [
    ()
]

def Create(name, role): 
    # W, H = (1921, 1358)
    W, H = (3841, 2715)
    fontRatio = H / 1358
    maxCharCount = 42

    fontSize = int(120 * fontRatio)
    msg = name
    folder = "Saves"

    # im = Image.new("RGBA",(W,H),"yellow")
    im = Image.open("Template.png")
    
    draw = ImageDraw.Draw(im)
    myFont = ImageFont.truetype("AlexBrush-Regular.ttf", fontSize)
    w, h = draw.textsize(msg, font=myFont)
    draw.text(((W-w)/2,0.53*H), msg, fill="#F7BB48", font=myFont)

    gap = 0.032
    # draw = ImageDraw.Draw(im)
    fontSize = int(35 * fontRatio)

    if len(role) > maxCharCount:
        msg = f"In recognition of your invaluable support"
        # print(f"Greater ({name})")
    else: 
        msg = f"In recognition of your invaluable support {role}"
    myFont = ImageFont.truetype("Montserrat-Medium.ttf", fontSize)
    w, h = draw.textsize(msg, font=myFont)
    draw.text(((W-w)/2,0.655*H), msg, fill="#FFFFFF", font=myFont)

    if len(role) > maxCharCount:
        msg = role
        myFont = ImageFont.truetype("Montserrat-Medium.ttf", fontSize)
        w, h = draw.textsize(msg, font=myFont)
        draw.text(((W-w)/2,(0.655 + gap)*H), msg, fill="#FFFFFF", font=myFont)

    msg = "at our two-day science olympiad event for 150+ students around the globe"
    myFont = ImageFont.truetype("Montserrat-Medium.ttf", fontSize)
    w, h = draw.textsize(msg, font=myFont)
    if len(role )> maxCharCount:
        draw.text(((W-w)/2,(0.655 + gap * 2)*H), msg, fill="#FFFFFF", font=myFont)
    else:
        draw.text(((W-w)/2,(0.655 + gap)*H), msg, fill="#FFFFFF", font=myFont)
    im = im.convert("RGB");
    im.save(f"{folder}/BVSSO 2022 - {name}.pdf")

names = {"Example Recipient": "as an Organizer"}

# Create("Bhai ka naam", "an Organizer")

# for name in names:
#     Create(name, names[name])

keys = list(names.keys())

for i in range(len(keys)):
    print(f"Creating {i + 1}/{len(keys)} ({keys[i]})")
    Create(keys[i], names[keys[i]])

""" 
Roles are:

Event Head
Organizer
Module Head
Assistant Module Head
Graphic Designer / Media Support
IT Support
Volunteer

Host
Marketing Manager

 """
