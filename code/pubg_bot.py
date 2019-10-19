#!/usr/bin/python3
import pprint
# import re
from typing import List

# import discord
from discord.ext import commands
from discord.ext.commands import Context
from pubg_python import PUBG, Shard

from config import Config
from stat_options import StatOptions
from weapons import Weapons


conf = Config()
pubg_api = PUBG(conf.pubg_api, Shard.PC_NA)
# client = discord.Client()
bot = commands.Bot(command_prefix='$')
_weapons = Weapons()
stat_options = StatOptions()

@bot.command()
async def weapon(ctx: Context, weapon_name: str = '', player_name: str = ''):
    """Look up a specific weapon and print its stats to Discord."""
    print('You are in the weapon function')
    p_name = _player_name(ctx.author, player_name)
    author = ctx.author.name

    pubg_player_id = player_id(p_name)
    if pubg_player_id == -1:
        await ctx.send('Player Unknown')

    if weapon_name != '':
        try:
            weapons = pubg_api.weapon_mastery(pubg_player_id).get()
            weapon_key = _weapons.get_weapon_key(weapon_name)
        except KeyError:
            message = 'Unknown weapon'
            await ctx.send(message)
        weapon_info = weapons.weapon_summaries[weapon_key]
        standardized_weapon_name = _weapons.key_to_name(weapon_key)
        weapon = {standardized_weapon_name: weapon_info}
        
        message = build_discord_message(p_name, author, weapon)
        await ctx.send(message)
    else:
        await weapons(ctx, player_name)


@bot.command()
async def weapons(ctx: Context,
                  sorting_stats: str = 'XPTotal, Defeats, Kills, Groggies',
                  player_name: str = ''):
    """Look up a player's weapon stats and print them to Discord."""
    print('You are in the weapons function')
    p_name = _player_name(ctx.author, player_name)
    author = ctx.author.name
    stats = stat_options.get_options(sorting_stats.split(','))

    pubg_player_id = player_id(p_name)
    if pubg_player_id == -1:
        await ctx.send('Player Unknown')
    
    weapons = pubg_api.weapon_mastery(pubg_player_id).get()
    _top_weapons = top_weapons(weapons, sort=stats[0])
    reduced_weapons = top_weapons_reduced(_top_weapons, stats)
    
    message = build_discord_message(p_name, author, reduced_weapons)
    await ctx.send(message)


def build_discord_message(player_name: str, author: str, weapons_dict: dict,
                          max_message_length: int = 2000) -> str:
    """Returns a formatted message that can be posted to Discord."""
    pprint.pprint(weapons_dict)
    output_obj = build_obj(player_name, weapons_dict)
    message = block_message(output_obj)
    if len(message) > max_message_length:
        output_obj = build_obj(player_name, weapons_dict[0])
        message = block_message(output_obj)
    return '{}\n{}'.format(author, message)


def build_obj(player_name: str, obj: object):
    """Returns a dict containing an object and the player name."""
    return {player_name: obj}


def top_weapons(weapons, how_many: int = 5, sort: str = 'XPTotal'):
    weapons_list = []
    standard_stat = stat_options.get_option(sort)
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
                if standard_stat == 'XPTotal':
                    value = summary[standard_stat]
                    value_in_list = weapon[standard_stat]
                else:
                    value = summary['StatsTotal'][standard_stat]
                    value_in_list = weapon['StatsTotal'][standard_stat]
                if value >= value_in_list:
                    if len(weapons_list) >= how_many:
                        pprint.pprint(weapons_list)
                        pprint.pprint('weapon: {}'.format(weapon_obj))
                        
                        weapons_list.remove(weapon_obj)
                    weapons_list.append(new_weapon)
                    break
    return weapons_list


def top_weapons_reduced(weapons: dict, stats: List[str]) -> dict:
    """Returns a dict of weapon stats."""
    weapons_out = []

    for weapon in weapons:
        key = [key_ for key_ in weapon.keys()][0]
        new_weapon = { key: {} }
        for stat in stats:
            try:
                standard_stat = stat_options.get_option(stat)
            except KeyError:
                continue
            if standard_stat in stat_options.top_level:
                new_weapon[key][standard_stat] = weapon[key][standard_stat]
            else:
                try:
                    new_weapon[key]['StatsTotal'][standard_stat] = \
                            weapon[key]['StatsTotal'][standard_stat]
                except KeyError:
                    new_weapon[key]['StatsTotal'] = {}
                    new_weapon[key]['StatsTotal'][standard_stat] = \
                            weapon[key]['StatsTotal'][standard_stat]
        weapons_out.append(new_weapon)
    return weapons_out


def _player_name(author, name: str) -> str:
    return author.name if name == '' else name


def block_message(obj: object, format_string: str = '```json\n{}```') -> str:
    """Format an object and return the string output."""
    message = pprint.pformat(obj)
    print(message)
    return format_string.format(message)
 

def player_id(player_name: str) -> int:
    """Returns the player ID from a player name.
    
    If the player_id is not found then return the player id as -1.
    """
    try:
        player_id = pubg_api.players().filter(player_names=[player_name])[0].id
    except NotFoundError:
        player_id = -1

    return player_id


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

