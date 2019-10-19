#!/usr/bin/python3
from typing import List


class StatOptions(object):
    def __init__(self):
        self.top_level = self.get_options(['xptotal', 'tiercurrent',
                                           'levelcurrent', 'statstotal',
                                           'medals'])
        self.stats = {
            'damageplayer': 'DamagePlayer',
            'damage': 'DamagePlayer',
            'totaldamage': 'DamagePlayer',
            'defeats': 'Defeats',
            'totaldefeats': 'Defeats',
            'defeat': 'Defeats',
            'totaldefeat': 'Defeats',
            'totalgroggies': 'Groggies',
            'groggies': 'Groggies',
            'totalgroggie': 'Groggies',
            'groggie': 'Groggies',
            'totalheadshots': 'HeadShots',
            'headshots': 'HeadShots',
            'totalheadshot': 'HeadShots',
            'headshot': 'HeadShots',
            'kills': 'Kills',
            'totalkills': 'Kills',
            'totalkill': 'Kills',
            'kill': 'Kills',
            'longrangedefeats': 'LongRangeDefeats',
            'longrangedefeat': 'LongRangeDefeats',
            'longrange': 'LongRangeDefeats',
            'long': 'LongRangeDefeats',
            'longestdefeat': 'LongestDefeat',
            'longdefeat': 'LongestDefeat',
            'mostdamageplayerinagame': 'MostDamagePlayerInAGame',
            'mostdamage': 'MostDamagePlayerInAGame',
            'mostdmg': 'MostDamagePlayerInAGame',
            'mostdefeatsinagame': 'MostDefeatsInAGame',
            'mostdefeatinagame': 'MostDefeatsInAGame',
            'mostdefeats': 'MostDefeatsInAGame',
            'mostdefeat': 'MostDefeatsInAGame',
            'mostgroggiesinagame': 'MostGroggiesInAGame',
            'mostgroggieinagame': 'MostGroggiesInAGame',
            'mostgroggies': 'MostGroggiesInAGame',
            'mostgroggie': 'MostGroggiesInAGame',
            'mostheadshotsingame': 'MostHeadShotsInAGame',
            'mostheadshotingame': 'MostHeadShotsInAGame',
            'mostheadshots': 'MostHeadShotsInAGame',
            'mostheadshot': 'MostHeadShotsInAGame',
            'mostkillsinagame': 'MostKillsInAGame',
            'mostkillinagame': 'MostKillsInAGame',
            'mostkills': 'MostKillsInAGame',
            'mostkill': 'MostKillsInAGame',
            'levelcurrent': 'LevelCurrent',
            'level': 'LevelCurrent',
            'medals': 'Medals',
            'statstotal': 'StatsTotal',
            'stats': 'StatsTotal',
            'tiercurrent': 'TierCurrent',
            'tier': 'TierCurrent',
            'xptotal': 'XPTotal',
            'xp': 'XPTotal'
        }
        
    def _clean(self, string: str) -> str:
        """Returns a cleaned str to use in the stat map."""
        return string.lower().strip().replace(' ', '')
        
    def get_option(self, stat: str) -> str:
        """Returns the stat in correct casing.
        
        Args:
            stat: The stat to obtain. Casing does not matter.
        Raises:
            KeyError: If the provided stat is not in the map.
        """
        try:
            return self.stats[self._clean(stat)]
        except KeyError:
            raise KeyError
    
    def get_options(self, stats: List[str]) -> List[str]:
        """Returns a list of stats in correct casing.
        
        Args:
            stats: The list of stat options. Casing does not matter.
        """
        out = []
        for stat in stats:
            try:
                out.append(self.get_option(stat))
            except KeyError:
                continue
                
                
                
                
                
                
                
                
                
                