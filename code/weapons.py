#!/usr/bin/python3

class Weapons(object):
    def __init__(self):
        self.names = {
                'ak': 'Item_Weapon_AK47_C',
                'akm': 'Item_Weapon_AK47_C',
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
                'pp19bizon': 'Item_Weapon_BizonPP19_C',
                'pp19bison': 'Item_Weapon_BizonPP19_C',
                'pp19': 'Item_Weapon_BizonPP19_C',
                'crossbow': 'Item_Weapon_Crossbow_C',
                'xbow': 'Item_Weapon_Crossbow_C',
                'bestguninthegame': 'Item_Weapon_Crossbow_C',
                'bestweaponinthegame': 'Item_Weapon_Crossbow_C',
                'goat': 'Item_Weapon_Crossbow_C',
                'dp28': 'Item_Weapon_DP28_C',
                'dinnerplate28': 'Item_Weapon_DP28_C',
                'dinnerplate': 'Item_Weapon_DP28_C',
                'pizzagun': 'Item_Weapon_DP28_C',
                'fal': 'Item_Weapon_FNFal_C',
                'slr': 'Item_Weapon_FNFal_C',
                'fnfal': 'Item_Weapon_FNFal_C',
                'glock': 'Item_Weapon_G18_C',
                'g18': 'Item_Weapon_G18_C',
                'g36c': 'Item_Weapon_G36C_C',
                'g36': 'Item_Weapon_G36C_C',
                'groza': 'Item_Weapon_Groza_C',
                'hk416': 'Item_Weapon_HK416_C',
                'm4a1': 'Item_Weapon_HK416_C',
                'm4': 'Item_Weapon_HK416_C',
                'm416': 'Item_Weapon_HK416_C',
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
                'r1895': 'Item_Weapon_NagantM1895_C',
                'nagantm1895': 'Item_Weapon_NagantM1895_C',
                'nagant1895': 'Item_Weapon_NagantM1895_C',
                'm1895': 'Item_Weapon_NagantM1895_C',
                'qbu': 'Item_Weapon_QBU88_C',
                'qbu88': 'Item_Weapon_QBU88_C',
                'qbz': 'Item_Weapon_QBZ95_C',
                'qbz95': 'Item_Weapon_QBZ95_C',
                'revolver': 'Item_Weapon_NagantM1895_C',
                'revolver762': 'Item_Weapon_NagantM1895_C',
                'rhino': 'Item_Weapon_Rhino_C',
                'r45': 'Item_Weapon_Rhino_C',
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
                's12k': 'Item_Weapon_Saiga12_C',
                's12': 'Item_Weapon_Saiga12_C',
                'sega': 'Item_Weapon_Saiga12_C',
                'segagenesis': 'Item_Weapon_Saiga12_C',
                'dear6lbs8ozbabyjesusgivethisguntomewhenihotdrop':
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
                'microuzi': 'Item_Weapon_UZI_C',
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
                'pump': 'Item_Weapon_Winchester_C',
                'pumpshotty': 'Item_Weapon_Winchester_C',
                'pumpshotgun': 'Item_Weapon_Winchester_C',
                'S1897': 'Item_Weapon_Winchester_C',
                '1897': 'Item_Weapon_Winchester_C',
                'skorp': 'Item_Weapon_vz61Skorpion_C',
                'scorp': 'Item_Weapon_vz61Skorpion_C',
                'skorpion': 'Item_Weapon_vz61Skorpion_C',
                'scorpion': 'Item_Weapon_vz61Skorpion_C',
                'vz61skorpion': 'Item_Weapon_vz61Skorpion_C',
                'vz61': 'Item_Weapon_vz61Skorpion_C',
                'vz': 'Item_Weapon_vz61Skorpion_C'
        }

    def key_to_name(self, key):
        keys = {
                'Item_Weapon_AK47_C': 'AKM',
                'Item_Weapon_AUG_C': 'AUG',
                'Item_Weapon_AWM_C': 'AWM',
                'Item_Weapon_Berreta686_C': 'S686',
                'Item_Weapon_BerylM762_C': 'Beryl M762',
                'Item_Weapon_BizonPP19_C': 'PP19 Bizon',
                'Item_Weapon_Crossbow_C': 'Crossbow',
                'Item_Weapon_DP28_C': 'DP-28',
                'Item_Weapon_FNFal_C': 'SLR',
                'Item_Weapon_G18_C': 'P18C',
                'Item_Weapon_G36C_C': 'G36C',
                'Item_Weapon_Groza_C': 'Groza',
                'Item_Weapon_HK416_C': 'M416',
                'Item_Weapon_Kar98k_C': 'Kar98k',
                'Item_Weapon_M16A4_C': 'M16A4',
                'Item_Weapon_M1911_C': 'P1911',
                'Item_Weapon_M249_C': 'M249',
                'Item_Weapon_M9_C': 'P92',
                'Item_Weapon_M24_C': 'M24',
                'Item_Weapon_MP5K_C': 'MP5k',
                'Item_Weapon_Mini14_C': 'Mini14',
                'Item_Weapon_Mk14_C': 'Mk14',
                'Item_Weapon_Mk47Mutant_C': 'MK47 Mutant',
                'Item_Weapon_NagantM1895_C': 'R1895',
                'Item_Weapon_QBU88_C': 'QBU',
                'Item_Weapon_QBZ95_C': 'QBZ',
                'Item_Weapon_Rhino_C': 'R45',
                'Item_Weapon_SCAR-L_C': 'SCAR-L',
                'Item_Weapon_SKS_C': 'SKS',
                'Item_Weapon_Saiga12_C': 'S12K',
                'Item_Weapon_Sawnoff_C': 'Sawed-off',
                'Item_Weapon_Thompson_C': 'Tommy Gun',
                'Item_Weapon_UMP_C': 'UMP 45',
                'Item_Weapon_UZI_C': 'Micro Uzi',
                'Item_Weapon_VSS_C': 'VSS',
                'Item_Weapon_Vector_C': 'Vector',
                'Item_Weapon_Win1894_C': 'Win1894',
                'Item_Weapon_Winchester_C': 'S1897',
                'Item_Weapon_vz61Skorpion_C': 'skorpion'
                }
        try:
            value = keys[key]
        except KeyError:
            value = 'Unknown key'
        return value

    def assault_rifles(self):
        """Returns a list of PUBG API AR names."""
        assault_rifles_list = ['akm', 'aug', 'berylm762', 'g36c', 'groza',
                               'm416', 'm16a4', 'mk47mutant', 'qbz', 'scarl'] 
        return self._build_item_list(assault_rifles_list)

    def sniper_rifles(self):
        """Returns a list of PUBG API SR names."""
        sniper_rifles_list = ['awm', 'kar98k', 'm24', 'win94']
        return self._build_item_list(sniper_rifles_list)

    def shotguns(self):
        """Returns a list of PUBG API shotgun names."""
        # DBS is missing
        shotguns_list = ['s686', 's12k', 'sawedoff', 's1897']
        return self._build_item_list(shotguns_list)

    def sub_machine_guns(self):
        """Returns a list of PUBG API SMG names."""
        smgs_list = ['pp19bizon', 'mp5k', 'tommygun', 'ump45', 'microuzi',
                     'vector']
        return self._build_item_list(shotguns_list)

    def light_machine_guns(self):
        """Returns a list of PUBG API LMG names."""
        lmgs_list = ['dp28', 'm249']
        return self._build_item_list(lmgs_list)

    def designated_marksman_rifles(self):
        """Returns a list of PUBG API DMR names."""
        dmrs_list = ['slr', 'mini14', 'mk14', 'qbu', 'sks', 'vss']
        return self._build_item_list(dmrs_list)

    def pistols(self):      
        """Returns a list of PUBG API Pistol names."""
        # Deagle is missing
        pistols_list = ['p18c', 'p1911', 'p92', 'r1895', 'r45', 'skorpian']
        return self._build_item_list(pistols_list)

    def misc(self):
        """Returns a list of PUBG API misc. item names."""
        misc_list = ['crossbow']
        return self._build_item_list(misc_list)
    
    def get_weapon_key(self, weapon_name: str) -> str:
        name = weapon_name.strip().replace(' ', '').replace('.', ''
                ).replace('-', '').lower()
        return self.names[name]

    def _build_item_list(self, weapon_list):
        """Loop through a list of weapons and find the PUBG API item name."""
        items = []
        for weapon in weapon_list:
            items.append(self.get_weapon_key(weapon))
        return items
