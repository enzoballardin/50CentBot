import requests
import json
import tweepy
import os
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import sys


def lambda_handler(event, context):
    # TODO implement
    result = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL')

    #print(result)
    #print(result.text)


    response = json.loads(result.text)['USD']
    dolHigh =  float(response['high'])
    dolLow = float(response['low'])

    dol = (dolHigh + dolLow) / 4
    dol = "%.2f" % dol

    print(dol)

    texto = "R$ {}".format(dol)

    print(texto)


    #Define parametros
    
    img = Image.open('50-cent.jpg')
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('impact.ttf', 112)

    [x, y] = 90, 210

    #Coloca borda no texto
    fillcolor ='white'
    shadowcolor = 'black'
    draw.text((x-5, y-5), texto, font=font, fill=shadowcolor)
    draw.text((x+5, y-5), texto, font=font, fill=shadowcolor)
    draw.text((x-5, y+5), texto, font=font, fill=shadowcolor)
    draw.text((x+5, y+5), texto, font=font, fill=shadowcolor)

    # Escreve o texto por cima da borda
    draw.text((x, y), texto, font=font, fill=fillcolor)


    #Salva  a imagem
    img.save('/tmp/output.jpg')




    # Consumer keys and access tokens, used for OAuth
    consumer_key = ''
    consumer_secret = ''
    access_token = ''
    access_token_secret = ''
    
    # OAuth process, using the keys and tokens
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    
    # Creation of the actual interface, using authentication
    api = tweepy.API(auth)

    # Send the tweet.
    api.update_with_media('/tmp/output.jpg', texto)

    return {
            'statusCode': 200,
            'body': json.dumps('Hello from Lambda!')
        }

