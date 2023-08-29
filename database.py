import requests
import re
import urllib.parse

# Get PCGamingWiki PageID from title
def get_pageid_from_title(title):
    try:
        return requests.get('https://www.pcgamingwiki.com/w/api.php?action=cargoquery&format=json&tables=Infobox_game&fields=Infobox_game._pageName%3DPage%2CInfobox_game._pageID%3DPageID&where=Infobox_game._pageName%3D%22{}%22'.format(urllib.parse.quote(title))).json()['cargoquery'][0]['title']['PageID']
    except:
        raise Exception('Invalid title given')

# Get PCGamingWiki PageID from steam appid
def get_pageid_from_steam_appid(appid):
    try:
        return requests.get('https://www.pcgamingwiki.com/w/api.php?action=cargoquery&tables=Infobox_game&fields=Infobox_game._pageID%3DPageID%2CInfobox_game.Steam_AppID&where=Infobox_game.Steam_AppID%20HOLDS%20%22{}%22&format=json'.format(appid)).json()['cargoquery'][0]['title']['PageID']
    except:
        raise Exception('Invalid steam appid given')

# Get PCGamingWiki PageID from gog productid
def get_pageid_from_gog_productid(productid):
    try:
        return requests.get('https://www.pcgamingwiki.com/w/api.php?action=cargoquery&tables=Infobox_game&fields=Infobox_game._pageID%3DPageID%2CInfobox_game.GOGcom_ID&where=Infobox_game.GOGcom_ID%20HOLDS%20%22{}%22&format=jsonfm'.format(productid)).json()['cargoquery'][0]['title']['PageID']
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
    
def get_save_location_from_title(title):
    pageid = get_pageid_from_steam_appid(title)
    wiki_text = get_wiki_text_from_pageId(pageid)
    return get_save_location_from_wiki_text(wiki_text)

def get_save_location_from_steam_appid(appid):
    pageid = get_pageid_from_steam_appid(appid)
    wiki_text = get_wiki_text_from_pageId(pageid)
    return get_save_location_from_wiki_text(wiki_text)

def get_save_location_from_gog_productid(productid):
    pageid = get_pageid_from_gog_productid(productid)
    wiki_text = get_wiki_text_from_pageId(pageid)
    return get_save_location_from_wiki_text(wiki_text)

def get_game_names():
    try:
        return requests.get('https://www.pcgamingwiki.com/w/api.php?action=cargoquery&format=json&tables=Infobox_game&fields=_pageName%3DPage').json()
    except:
        raise Exception('Failed to get game names')
    
