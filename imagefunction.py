#V1.2 DerUSBstick#0001
async def imagefunction(data, restricted_slots, page:int):
    background = await getbackground(0 if len(data) == 10 else 1)
    if len(data) == 18 and restricted_slots:
        background = await numbers(background, data, page)
    background = await cards(background, data, 0 if len(data) == 10 else 1)
    background = await setpage(background, page)
    return background


async def getbackground(types):
    url = ['https://alekeagle.me/XdYUt-P8Xv.png', 'https://alekeagle.me/wp2mKvzvCD.png']
    async with aiohttp.ClientSession() as cs:
        async with cs.get(url[types]) as res:
            image_bytes = await res.read()
            background = Image.open(io.BytesIO(image_bytes)).convert('RGB') 
    return background

async def getcard(url):
    async with aiohttp.ClientSession() as cs:
        async with cs.get(url) as res:
            image_bytes = await res.read()
            image_card = Image.open(io.BytesIO(image_bytes)).convert('RGB')
            image_card = image_card.resize((80, 110), Image.ANTIALIAS)
    return image_card

async def setpage(image, page):
    font = await getfont(20)
    draw = ImageDraw.Draw(image)
    draw.text((5, 385), f'{page*2-1}', (0,0,0), font=font)
    draw.text((595, 385), f'{page*2}', (0,0,0), font=font)
    return image


async def getfont(size):
    #https://alekeagle.me/c8FR3TicHd.ttf
    font = ImageFont.truetype('Font PATH', size, encoding="unic") #<--- Set the PATH of the font
    return font

async def cards(image, data, option):
    i = 0
    card_pos:list = [
        [(113, 145),(320, 15),(418, 15),(516, 15),(320, 142),(418, 142),(516, 142),(320, 269),(418, 269),(516, 269)],
        [(15,17),(112,17),(210,17),(15,144),(112,144),(210,144),(15,274),(112,274),(210,274),(320,13),(418,13),(516,13),(320,143),(418,143),(516,143),(320,273),(418,273),(516,273)]
    ]
    for z in data:
        if z != None and z[1] != None:
            image_card = await getcard(z[1])
            image.paste(image_card, (card_pos[option][i]))
        i += 1
    return image


async def numbers(image, data, page):
    page -= 2
    i = 0
    numbers_pos:list = [
      [(35, 60),(138, 60),(230, 60),(35, 188),(138, 188),(230, 188),(36, 317),(134, 317),(232, 317),(338, 60),(436, 60),(536, 60),(338, 188),(436, 188),(536, 188),(338, 317),(436, 317),(536, 317)], 
      [(30, 60),(132, 60),(224, 60),(34, 188),(131, 188),(227, 188),(32, 317),(130, 317),(228, 317),(338, 60),(436, 60),(533, 60),(338, 188),(436, 188),(533, 188),(338, 317),(436, 317),(533, 317)], 
      [(30, 60),(130, 60),(224, 60),(31, 188),(131, 188),(230, 188),(32, 317),(130, 317),(228, 317),(338, 60),(436, 60),(533, 60),(338, 188),(436, 188),(533, 188),(340, 317),(436, 317),(533, 317)], 
      [(30, 60),(130, 60),(224, 60),(31, 188),(131, 188),(230, 188),(32, 317),(133, 317),(228, 317),(338, 60),(436, 60),(533, 60),(338, 188),(436, 188),(533, 188),(338, 317),(436, 317),(535, 317)], 
      [(30, 60),(130, 60),(224, 60),(31, 188),(131, 188),(230, 188),(32, 317),(133, 317),(228, 317),(342, 60),(436, 60),(533, 60),(338, 188),(436, 188),(533, 188),(338, 317),(436, 317),(535, 317)], 
      [(30, 60),(130, 60),(224, 60),(31, 188),(131, 188),(230, 188),(32, 317),(133, 317),(228, 317),(342, 60),(436, 60),(533, 60),(338, 188),(436, 188),(533, 188),(338, 317),(436, 317),(535, 317)] 
      ]

    font = await getfont(35)
    draw = ImageDraw.Draw(image)
    for z in data:
        draw.text(numbers_pos[page][i], f'0{z[0]}', (165,165,165), font=font)
        i += 1
    return image



----================Changes================----

1. The list in the function cards() has been fixed. The cards fit now in their slots.

2. The function cards() has been improved. Free Slots wont cause a error anymore


