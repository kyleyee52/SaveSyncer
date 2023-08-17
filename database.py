import requests
import re

# Get PCGamingWiki PageID from steam appid
def get_pageid_from_steam_appid(appid):
    try:
        return requests.get('https://www.pcgamingwiki.com/w/api.php?action=cargoquery&tables=Infobox_game&fields=Infobox_game._pageID%3DPageID%2CInfobox_game.Steam_AppID&where=Infobox_game.Steam_AppID%20HOLDS%20%22{}%22&format=json'.format(appid)).json()['cargoquery'][0]['title']['PageID']
    except:
        raise Exception('Invalid steam appid given')

# Get PCGamingWiki PageID from gog appid
def get_pageid_from_gog_appid(appid):
    try:
        return requests.get('https://www.pcgamingwiki.com/w/api.php?action=cargoquery&tables=Infobox_game&fields=Infobox_game._pageID%3DPageID%2CInfobox_game.GOGcom_ID&where=Infobox_game.GOGcom_ID%20HOLDS%20%22{}%22&format=jsonfm'.format(appid)).json()['cargoquery'][0]['title']['PageID']
    except:
        raise Exception('Invalid gog appid given')

# Get PCGamingWiki Text from PageID
def get_wiki_text_from_pageId(pageId):
    try:
        return requests.get('https://www.pcgamingwiki.com/w/api.php?action=parse&format=json&pageid={}&prop=wikitext'.format(pageId)).json()['parse']['wikitext']['*']
    except:
        raise Exception('Invalid PageID given')

# Returns a dictionary of save locations for each platform
def get_save_location_from_wiki_text(wiki_text):
    try:
        saves = {}
        regex = r"({{Game data/saves\|([\w ]*)\|(.*|{{.*}})}})+"
        matches = re.findall(regex, wiki_text)
        for match in matches:
            if match[-1] != '':
                saves[match[1]] = match[2]
        return saves
    except:
        raise Exception('Invalid wiki_text given')

def get_save_location_from_steam_appid(appid):
    pageid = get_pageid_from_steam_appid(appid)
    wiki_text = get_wiki_text_from_pageId(pageid)
    return get_save_location_from_wiki_text(wiki_text)

#print(get_pageid_from_steam_appid(1462040))
#print(get_wiki_text(146683))
#print(get_save_location_from_wiki_text(get_wiki_text_from_pageId(get_pageid_from_steam_appid(1462040))))
print(get_save_location_from_steam_appid(632360))