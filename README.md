# 50CentBot
50CentBot is a bot that posts an image on Twitter everyday, with the daily exchange rate for "50 cents" of american dollars in brazilian real.
It was inspired in a bad joke about the name "50cent"...

![Screenshot](/50centbot.png)
Format: ![Alt Text](url)

## How it works
###API and libs
I am using PIL's Image, ImageFont and ImageDraw to open, write on and save the image.
I used Tweepy to integrate Twitter and Python.
Also using requests and json.


###Code
The whole bot is a single function that is supposed to run once a day. It first requests the daily USD-BRL exchange rate using:

```python
requests.get('https://economia.awesomeapi.com.br/all/USD-BRL')
```
This returns a json object, which contains between its values the higher and lower exchange rates.
The code than calculates the average between this values, takes half (50 cents) and stores it as a string.


###Writing in the image
PIL opens the image, writes the string on the choosen coordinates, and saves it.

Then, the twitter API runs and connects to the twitter account, and posts the image with the desired caption.
The image with the text is deleted and the code keeps only the base image so a new image is created, posted and immediately deleted everyday.

###Hosting and triggering
The bot runs from AWS Lambda, which was setted to run once a day at approximately 11PM.

## Check it out!
https://twitter.com/Dia50cent
