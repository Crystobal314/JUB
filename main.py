import discord
import asyncio

client = discord.Client()
@client.event
async def on_ready():
  print( "Capitaine Salamèche à l’écoute !" )

@client.event
async def on_message (message):
  print(message.content)


client.run( "Njk0NDUxNjg1ODMzMDQ4MDY2.XoL2yg.cKJvUv6PomF41mXz4VQ04AbpxGs" )