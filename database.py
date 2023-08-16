import requests
import re

# Get PCGamingWiki PageID from steam appid
def get_pageid_from_steam_appid(appid):
    return requests.get('https://www.pcgamingwiki.com/w/api.php?action=cargoquery&tables=Infobox_game&fields=Infobox_game._pageID%3DPageID%2CInfobox_game.Steam_AppID&where=Infobox_game.Steam_AppID%20HOLDS%20%22{}%22&format=json'.format(appid)).json()['cargoquery'][0]['title']['PageID']

# Get PCGamingWiki PageID from gog appid
def get_pageid_from_gog_appid(appid):
    return requests.get('https://www.pcgamingwiki.com/w/api.php?action=cargoquery&tables=Infobox_game&fields=Infobox_game._pageID%3DPageID%2CInfobox_game.GOGcom_ID&where=Infobox_game.GOGcom_ID%20HOLDS%20%22{}%22&format=jsonfm'.format(appid)).json()['cargoquery'][0]['title']['PageID']

# Get PCGamingWiki Text from PageID
def get_wiki_text_from_pageId(pageId):
    return requests.get('https://www.pcgamingwiki.com/w/api.php?action=parse&format=json&pageid={}&prop=wikitext'.format(pageId)).json()['parse']['wikitext']['*']

def get_save_location_from_wiki_text(wiki_text):
    saves = {}
    regex = r"{{Game data\|\n({{Game data/saves\|()\|()}}?)*}}"
    matches = re.findall(regex, wiki_text)
    #parsed = list(map(lambda x: "|".join(x.split("|")[1::]), regex))
    #for loc in parsed:
    #    system, path = loc.split("|", 1)
    #    saves[system] = path
    return matches

def get_save_location_from_steam_appid(appid):
    pageid = get_pageid_from_steam_appid(appid)
    wiki_text = get_wiki_text_from_pageId(pageid)
    return get_save_location_from_wiki_text(wiki_text)

print(get_pageid_from_steam_appid(1462040))
#print(get_wiki_text(146683))
#print(get_save_location_from_wiki_text(get_wiki_text_from_pageId(get_pageid_from_steam_appid(1462040))))
print(get_save_location_from_steam_appid(1462040))