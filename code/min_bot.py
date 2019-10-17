#!/usr/bin/python3

import discord

from config import Config


conf = Config()
client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    print(f'{message.channel}: {message.author}: {message.author.name}: {message.content}')
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


client.run(conf.token)
