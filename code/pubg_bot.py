#!/usr/bin/python3
import pprint
import re

import discord
from discord.ext import commands
from pubg_python import PUBG, Shard

from config import Config


conf = Config()
pubg_api = PUBG(conf.pubg_api, Shard.PC_NA)
# client = discord.Client()
bot = commands.Bot(command_prefix='$')

weapon_hash = {
        'ak': 'Item_Weapon_AK47_C',
        'ak47': 'Item_Weapon_AK47_C',
        'aug': 'Item_Weapon_AUG_C',
        'awm': 'Item_Weapon_AWM_C',
        's686': 'Item_Weapon_Berreta686_C',
        '686': 'Item_Weapon_Berreta686_C',
        'doublebarrel': 'Item_Weapon_Berreta686_C',
        'beryl': 'Item_Weapon_BerylM762_C',
        'berylm762': 'Item_Weapon_BerylM762_C',
        'beryl762': 'Item_Weapon_BerylM762_C',
        'ppbizon': 'Item_Weapon_BizonPP19_C',
        'ppbison': 'Item_Weapon_BizonPP19_C',
        'bizonpp': 'Item_Weapon_BizonPP19_C',
        'bisonpp': 'Item_Weapon_BizonPP19_C',
        'crossbow': 'Item_Weapon_Crossbow_C',
        'xbow': 'Item_Weapon_Crossbow_C',
        'bestguninthegame': 'Item_Weapon_Crossbow_C',
        'bestweaponinthegame': 'Item_Weapon_Crossbow_C',
        'goat': 'Item_Weapon_Crossbow_C',
        'dp28': 'Item_Weapon_DP28_C',
        'dinnerplate28': 'Item_Weapon_DP28_C',
        'dinnerplate': 'Item_Weapon_DP28_C',
        'pizzagun': 'Item_Weapon_DP28_C',
        'glock': 'Item_Weapon_G18_C',
        'g18': 'Item_Weapon_G18_C',
        'g36c': 'Item_Weapon_G36C_C',
        'g36': 'Item_Weapon_G36C_C',
        'groza': 'Item_Weapon_Groza_C',
        'hk416': 'Item_Weapon_HK416_C',
        'm4a1': 'Item_Weapon_HK416_C',
        'm4': 'Item_Weapon_HK416_C',
        'ct': 'Item_Weapon_HK416_C',
        'kar98k': 'Item_Weapon_Kar98k_C',
        'kar98': 'Item_Weapon_Kar98k_C',
        'kar9': 'Item_Weapon_Kar98k_C',
        'k9': 'Item_Weapon_Kar98k_C',
        'karbine': 'Item_Weapon_Kar98k_C',
        'carbine': 'Item_Weapon_Kar98k_C',
        'car9': 'Item_Weapon_Kar98k_C',
        'm16a4': 'Item_Weapon_M16A4_C',
        'm16': 'Item_Weapon_M16A4_C',
        '1911': 'Item_Weapon_M1911_C',
        'm1911': 'Item_Weapon_M1911_C',
        'm249': 'Item_Weapon_M249_C',
        'eatsvehiclesforbreakfast': 'Item_Weapon_M249_C',
        'breakfast': 'Item_Weapon_M249_C',
        'ammogobbler': 'Item_Weapon_M249_C',
        'm9': 'Item_Weapon_M9_C',
        'p92': 'Item_Weapon_M9_C',
        '92': 'Item_Weapon_M9_C',
        'm24': 'Item_Weapon_M24_C',
        '24': 'Item_Weapon_M24_C',
        'twofour': 'Item_Weapon_M24_C',
        'mtwofour': 'Item_Weapon_M24_C',
        'mp5k': 'Item_Weapon_MP5K_C',
        'mp5': 'Item_Weapon_MP5K_C',
        'mp': 'Item_Weapon_MP5K_C',
        'vikendigun': 'Item_Weapon_MP5K_C',
        'mini14': 'Item_Weapon_Mini14_C',
        'mini': 'Item_Weapon_Mini14_C',
        'min': 'Item_Weapon_Mini14_C',
        'mk14': 'Item_Weapon_Mk14_C',
        'mk': 'Item_Weapon_Mk14_C',
        'mutant': 'Item_Weapon_Mk47Mutant_C',
        'mk47': 'Item_Weapon_Mk47Mutant_C',
        'mk47mutant': 'Item_Weapon_Mk47Mutant_C',
        'mutant47': 'Item_Weapon_Mk47Mutant_C',
        'mkmutant': 'Item_Weapon_Mk47Mutant_C',
        'nagant': 'Item_Weapon_NagantM1895_C',
        '1895': 'Item_Weapon_NagantM1895_C',
        'nagantm1895': 'Item_Weapon_NagantM1895_C',
        'nagant1895': 'Item_Weapon_NagantM1895_C',
        'm1895': 'Item_Weapon_NagantM1895_C',
        'revolver': 'Item_Weapon_NagantM1895_C',
        'revolver762': 'Item_Weapon_NagantM1895_C',
        'rhino': 'Item_Weapon_Rhino_C',
        'miramar revolver': 'Item_Weapon_Rhino_C',
        'revolver45': 'Item_Weapon_Rhino_C',
        'chiapparhino': 'Item_Weapon_Rhino_C',
        'chiappa': 'Item_Weapon_Rhino_C',
        'scar': 'Item_Weapon_SCAR-L_C',
        'scarl': 'Item_Weapon_SCAR-L_C',
        'skarl': 'Item_Weapon_SCAR-L_C',
        'skar': 'Item_Weapon_SCAR-L_C',
        'sks': 'Item_Weapon_SKS_C',
        'sk': 'Item_Weapon_SKS_C',
        'saiga': 'Item_Weapon_Saiga12_C',
        'sega': 'Item_Weapon_Saiga12_C',
        'segagenesis': 'Item_Weapon_Saiga12_C',
        'dear6lb8ozbabyjesusgivethisguntomewhenihotdrop':
            'Item_Weapon_Saiga12_C',
        'sawnoff': 'Item_Weapon_Sawnoff_C',
        'sawedoff': 'Item_Weapon_Sawnoff_C',
        'tommy': 'Item_Weapon_Thompson_C',
        'thommy': 'Item_Weapon_Thompson_C',
        'tommygun': 'Item_Weapon_Thompson_C',
        'thommygun': 'Item_Weapon_Thompson_C',
        'thompson': 'Item_Weapon_Thompson_C',
        'thomson': 'Item_Weapon_Thompson_C',
        'ump': 'Item_Weapon_UMP_C',
        'ump45': 'Item_Weapon_UMP_C',
        'ump9': 'Item_Weapon_UMP_C',
        'uzi': 'Item_Weapon_UZI_C',
        'usi': 'Item_Weapon_UZI_C',
        'vss': 'Item_Weapon_VSS_C',
        'psst': 'Item_Weapon_VSS_C',
        'whothefuckisshootingatme': 'Item_Weapon_VSS_C',
        'whereisthisguy': 'Item_Weapon_VSS_C',
        'vector': 'Item_Weapon_Vector_C',
        'vector45': 'Item_Weapon_Vector_C',
        'vector9': 'Item_Weapon_Vector_C',
        'vector9m': 'Item_Weapon_Vector_C',
        'vector9mm': 'Item_Weapon_Vector_C',
        'win1894': 'Item_Weapon_Win1894_C',
        'win': 'Item_Weapon_Win1894_C',
        'winny': 'Item_Weapon_Win1894_C',
        'winny1894': 'Item_Weapon_Win1894_C',
        'winchester': 'Item_Weapon_Winchester_C',
        'skorp': 'Item_Weapon_vz61Skorpian_C',
        'scorp': 'Item_Weapon_vz61Skorpian_C',
        'skorpian': 'Item_Weapon_vz61Skorpian_C',
        'scorpian': 'Item_Weapon_vz61Skorpian_C',
        'vz61skorpian': 'Item_Weapon_vz61Skorpian_C',
        'vz61': 'Item_Weapon_vz61Skorpian_C',
        'vz': 'Item_Weapon_vz61Skorpian_C'
}


@bot.command()
async def weapons(ctx, player_name: str, weapon_name: str = ''):
    """Look up a player's weapon stats and print them to discord."""
    print('You are in the weapons function')
    weapons = pubg_api.weapon_mastery(player_id(player_name)).get()
    
    if weapon_name != '':
        try:
            name = weapon_name.strip().replace(' ', '').replace('.', ''
                    ).replace('-', '').lower()
            weapon_key = weapon_hash[name]
            weapon_info = weapons.weapon_summaries[weapon_key]
            msg = pprint.pformat(weapon_info)
            await ctx.send('```{}```'.format(msg))

        except KeyError:
            await ctx.send('Unknown weapon')
    else:
        print(weapons.weapon_summaries)


def player_id(player_name: str) -> int:
    return pubg_api.players().filter(player_names=[player_name])[0].id

@bot.command()
async def player(ctx, player_name: str):
    print('You are in the player function')
    season_data = pubg_api.seasons('lifetime', player_id=player_name).get()
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

