#!/usr/bin/python3
import pprint
import re

import discord
from discord.ext import commands
from discord.ext.commands import Context
from pubg_python import PUBG, Shard

from config import Config
from weapons import Weapons


conf = Config()
pubg_api = PUBG(conf.pubg_api, Shard.PC_NA)
# client = discord.Client()
bot = commands.Bot(command_prefix='$')
_weapons = Weapons()


@bot.command()
async def weapons(ctx: Context, player_name: str = '',
                  sorting_stat: str = 'XPTotal',
                  weapon_name: str = ''):
    """Look up a player's weapon stats and print them to discord."""
    print('You are in the weapons function')
    p_name = _player_name(ctx.author, player_name)

    weapons = pubg_api.weapon_mastery(player_id(p_name)).get()
    
    if weapon_name != '':
        try:
            weapon_key = _weapons.get_weapon_key(weapon_name)
            weapon_info = weapons.weapon_summaries[weapon_key]
            message = block_message(
                    {
                        _weapons.key_to_name(weapon_key): weapon_info
                    })
        except KeyError:
            message = 'Unknown weapon'
    else:
        print(weapons.weapon_summaries['Item_Weapon_Groza_C']['XPTotal'])
         
        _top_weapons = top_weapons(weapons, sort=sorting_stat)
        pprint.pprint(_top_weapons)
        
        message = block_message(_top_weapons)
        if len(message) > 2000:
            message = block_message(_top_weapons[0])
        await ctx.send('{}\n{}'.format(p_name, message))


def top_weapons(weapons, how_many: int = 2, sort: str = 'XPTotal'):
    weapons_list = []
    # pprint.pprint(weapon_summaries)
    for weapon_summary in weapons.weapon_summaries:
        summary = weapons.weapon_summaries[weapon_summary]
        print(weapon_summary)
        weapon_name = _weapons.key_to_name(weapon_summary)
        
        new_weapon = {weapon_name: summary}
        print(weapon_name)
        if len(weapons_list) == 0:
                weapons_list.append(new_weapon)
                continue
        # pprint.pprint(weapons_list)
        for weapon_obj in weapons_list:
            for item in weapon_obj:
                weapon = weapon_obj[item]
                if sort == 'XPTotal':
                    value = summary[sort]
                    value_in_list = weapon[sort]
                else:
                    value = summary['StatsTotal'][sort]
                    value_in_list = weapon['StatsTotal'][sort]
                print('New value: {}, value in list: {}'.format(value, value_in_list))
                if value >= value_in_list:
                    if len(weapons_list) >= how_many:
                        pprint.pprint(weapons_list)
                        pprint.pprint('weapon: {}'.format(weapon_obj))
                        
                        weapons_list.remove(weapon_obj)
                    weapons_list.append(new_weapon)
                    break
    return weapons_list


def _player_name(author, name: str) -> str:
    return author.name if name == '' else name


def block_message(obj: object, format_string: str = '```{}```') -> str:
    """Format an object and return the string output."""
    message = pprint.pformat(obj)
    return format_string.format(message)
 

def player_id(player_name: str) -> int:
    """Returns the player ID from a player name."""
    return pubg_api.players().filter(player_names=[player_name])[0].id


@bot.command()
async def player(ctx: Context, player_name: str = ''):
    """Display PUBG player's stats to Discord."""
    print('You are in the player function')
    p_name = _player_name(ctx.author, player_name)

    season_data = pubg_api.seasons('lifetime', player_id=p_name).get()
    """
    players = pubg_api.players().filter(player_names=[player_name])
    pprint.pprint(players.__dict__)
    msg = []
    if len(players) == 0:
        await ctx.send('Player not found')
    for player in players:
        msg.append(player.id)
    """
    pprint.pprint(season_data.season.__dict__)
    # await ctx.send(msg)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.event
async def on_message(message):
    print((f'{message.channel}: {message.author}: {message.author.name}: '
            '{message.content}'))
    if message.author == bot.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    await bot.process_commands(message)

# client.run(conf.token)
bot.run(conf.token)

