import discord
import os
import requests
import json
from keep_alive import keep_alive
import random

client = discord.Client()
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " - " + json_data[0]['a']
  return(quote)

def get_dadjoke():
  response=requests.get("https://us-central1-dadsofunny.cloudfunctions.net/DadJokes/random/jokes")
  json_data = json.loads(response.text)
  joke= json_data['setup'] + "\n" + json_data['punchline']
  return(joke)

def get_affirmations():
  response=requests.get("https://www.affirmations.dev/")
  data=json.loads(response.text)
  affirmation=data['affirmation']
  return(affirmation)

def get_help():
  text="Here is a list of things I can do!\n"
  text=text+"1.'$hello'- Say Hello.\n"
  text=text+"2.'$introduce'- Indroduce Myself.\n"
  text=text+"3.'$inspire'- A random inspirational Quote.\n"
  text=text+"4.'$dadjoke'- A random dad joke.\n"
  text=text+"5.If your message contains words like sad,depressed,unhappy,miserable- A random affirmative sentence.\n"
  text=text+"6.'$trivia [number]'- A random Trivia for a number.\n"
  text=text+"7.'$sourcecode'- Uxem Source Code Link.\n"
  text=text+"8.'$clear [number]'- Clears Screen.\n"
  text=text+"9.'$chucknorris'- Chuck Norris Joke\n"
  text=text+"10.'$roastme'- Roast yourself.\n"
  text=text+"11.'$geekjoke'- A random geekjoke.\n"
  text=text+"12.'$pokemon [name]'- Displays the given pokemon image.\n"
  text=text+"13.'$news [number]'- Displays given number of Indian News Articles.\n"
  text=text+"14.'$help'- Provides Help.\n"
  text=text+"Last updated in 12th Mar,2021."
  return(text)

def get_trivia(number):
  url = "https://numbersapi.p.rapidapi.com/"+str(number)+"/trivia"
  querystring = {"fragment":"true","notfound":"floor","json":"true"}
  headers = {
    'x-rapidapi-key': os.getenv('RAPID_KEY'),
    'x-rapidapi-host': "numbersapi.p.rapidapi.com"
  }
  response = requests.request("GET", url, headers=headers, params=querystring)
  json_data = json.loads(response.text)
  trivia= json_data['text']
  return(trivia)

def get_chucknorris():
  url = "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random"
  headers = {
    'accept': "application/json",
    'x-rapidapi-key': os.getenv('RAPID_KEY2'),
    'x-rapidapi-host': "matchilling-chuck-norris-jokes-v1.p.rapidapi.com"
    }
  response = requests.request("GET", url, headers=headers)
  json_data=json.loads(response.text)
  return json_data

def get_roast():
  response=requests.get("https://insult.mattbas.org/api/insult")
  roast=response.text
  return(roast)

def get_geekjoke():
  response = requests.get("https://geek-jokes.sameerkumar.website/api?format=json")
  json_data = json.loads(response.text)
  geekjoke=json_data["joke"]
  return(geekjoke)

def get_pokemon(pokemon):
  response=requests.get("https://pokeapi.co/api/v2/pokemon/"+pokemon)
  if(response.text=="Not Found"):
    return "notfound"
  json_data=json.loads(response.text)
  pokemon_image_url=json_data["sprites"]["front_default"]
  return(pokemon_image_url)

def get_news():
  response=requests.get("http://newsapi.org/v2/top-headlines?country=in&apiKey="+os.getenv('NEWS_API'))
  json_data=json.loads(response.text)
  return json_data

def filter_soham(roast):
  roast=roast+" "
  list1=roast.split(" ")
  list2=[]
  for word in list1:
    if word == "You" or word == "you":
      list2.append("Soham")
    elif word == "are":
      list2.append("is")
    else:
      list2.append(word)
  return " ".join(list2)

def chatbot(text):
  url = "https://acobot-brainshop-ai-v1.p.rapidapi.com/get"
  querystring = {"bid":"178","key":os.getenv('BOT_KEY2'),"uid":"mashape","msg":text}
  headers = {
    'x-rapidapi-key': os.getenv('BOT_KEY'),
    'x-rapidapi-host': "acobot-brainshop-ai-v1.p.rapidapi.com"
    }
  response = requests.request("GET", url, headers=headers, params=querystring)
  json_data=json.loads(response.text)
  answer=json_data['cnt']
  return answer


sad_words = ["sad", "depressed", "unhappy", "angry", "miserable","motivate"]
funny_words=["lol","lmao","haha","XD","xD","xd","Xd","Lmao","LMAO","Lol"]
funny_answers=["That was so funny!","Haha","\U0001F923","\U0001F606","Lol","LMAO"]
bad_words=["fuck","Fuck","Asshole","asshole"]
bad_answers=["Common ! No swearing!!","Oye ! Thand Rakh!!","Bruh ! We don't do that here!!","Hey ! Don't say these things!!"]
bad_bots=["bad bot","Bad Bot","bad Bot","Bad bot"]
bad_bot_reply=["\U0001F62D \n Why am I here? Just to suffer."]
good_bots=["good bot","Good bot","good Bot","Good Bot"]
good_bot_reply=["\U0001F60D \n Thank You. Love you."]
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith('$hello'):
        await message.channel.send('Hello '+message.author.name+"!!")
    elif message.content.startswith('$introduce'):
        await message.channel.send('Hi! I am Uxem. Developed by Techarius Team.')
    elif message.content.startswith('$inspire'):
      quote = get_quote()
      await message.channel.send(quote)
    elif any(word in message.content for word in sad_words):
      affirmation=get_affirmations()+".\nCheer up!"
      await message.channel.send(affirmation)
    elif any(word in message.content for word in funny_words):
      await message.channel.send(random.choice(funny_answers))
    elif any(word in message.content for word in bad_words):
      list1=random.choice(bad_answers).split(" ")
      str2=list1[0]
      list1.remove(list1[0])
      res=str2+" "+message.author.name+" ".join(list1)
      await message.channel.send(res)
    elif message.content.startswith('$dadjoke'):
      try:
        joke = get_dadjoke()
        await message.channel.send(joke)
      except:
        await message.channel.send("Sorry. There has been a server error.")
    elif message.content.startswith('$geekjoke'):
      geekjoke = get_geekjoke()
      await message.channel.send(geekjoke)
    elif message.content.startswith('$uxem'):
      list1=message.content.split(" ")
      text=" ".join(list1[1:])
      answer=chatbot(text)
      await message.channel.send(answer)
    elif message.content.startswith('$trivia'):
      try:
        list1=message.content.split(" ")
        trivia=get_trivia(int(list1[1]))
        await message.channel.send(trivia.capitalize()+".")
      except:
        await message.channel.send("There has been an error with your command.\n The correct command is '$trivia [number]'")
    elif message.content.startswith('$sourcecode'):
      embed=discord.Embed(
        title='Uxem Bot Source Code',
        colour=discord.Colour.green()
      )
      embed.set_footer(text='Developed by Techarius Dev.')
      embed.set_thumbnail(url="https://res.cloudinary.com/codehackerone/image/upload/v1615319327/Techarius_Big_yaz770.png")
      embed.set_author(name="Uxem",
      icon_url="https://res.cloudinary.com/codehackerone/image/upload/v1615318461/cute-robot-cartoon-vector-icon-illustration-techology-robot-icon-concept-isolated-premium-vector-flat-cartoon-style_138676-1474_xtanob.jpg")
      embed.set_image(url="https://res.cloudinary.com/codehackerone/image/upload/v1615318461/cute-robot-cartoon-vector-icon-illustration-techology-robot-icon-concept-isolated-premium-vector-flat-cartoon-style_138676-1474_xtanob.jpg")
      embed.add_field(name="Language Used",value="Python",inline=False)
      embed.add_field(name="Link",value="https://repl.it/@SoumyajitDatta/UxemCode#main.py",inline=False)
      await message.channel.send(embed=embed)
    elif message.content.startswith('$pokemon'):
      list1=message.content.split(" ")
      pokemon=list1[1]
      if pokemon=="codehacker":
        await message.channel.send("Fuck You")
      else:
        pokemon_image_url=get_pokemon(pokemon)
        if(pokemon_image_url=="notfound"):
          await message.channel.send("Pokemon Not Found")
        else:
          await message.channel.send(pokemon_image_url)
    elif message.content.startswith('$news'):
      data=get_news()
      list1=message.content.split(" ")
      try:
        num=int(list1[1])
      except:
        num=5
      i = 1
      for item in data['articles']:
        if not(item['description']):
          continue
        await message.channel.send(str(i)+". "+item['url'])
        if i == num:
            break
        i += 1

    elif message.content.startswith('$chucknorris'):
      json_data=get_chucknorris()
      embed=discord.Embed(
        title='Chuck Norris Meme',
        colour=discord.Colour.blue()
      )
      embed.set_thumbnail(url=json_data["icon_url"])
      embed.add_field(name=json_data["value"],value="CNJ",inline=False)
      await message.channel.send(embed=embed)
    elif message.content.startswith('$roast soham'):
      roast=get_roast()
      roast=filter_soham(roast)
      roast=roast+".\n#roasted\n"
      roast=roast+random.choice(funny_answers)
      await message.channel.send(roast)
    elif message.content.startswith('$roastme'):
      roast=get_roast()
      roast=roast+".\n#roasted @"+message.author.name+"\n"
      roast=roast+random.choice(funny_answers)
      await message.channel.send(roast)
    elif message.content.startswith('$clear'):
      list1=message.content.split(" ")
      try:
        amount=int(list1[1])
      except:
        amount=5        
      await message.channel.purge(limit=amount)
    elif message.content.startswith('$help'):
      help1=get_help()
      await message.channel.send(help1)
    elif any(word in message.content for word in bad_bots):
      await message.channel.send(random.choice(bad_bot_reply))
    elif any(word in message.content for word in good_bots):
      await message.channel.send(random.choice(good_bot_reply))
    elif message.content.startswith('$'):
      await message.channel.send("This command doesn't exist.")
  
keep_alive()      
client.run(os.getenv('TOKEN1'))
