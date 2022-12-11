
import requests

desc = "Generates a Discord.GG invite but for friend requests."
params = {
    "token" : "your Discord authentication token",
}

def run(token):
    headers = { "accept" : "*/*", "accept-encoding" : "gzip, deflate", "accept-language" : "en-US", "authorization" : token, "dnt" : "1", "referer" : "https://discord.com/channels/@me", "sec-ch-ua-mobile" : "?0", "sec-ch-ua-platform" : "\"Windows\"", "sec-fetch-dest" : "empty", "sec-fetch-mode" : "cors", "sec-fetch-site" : "same-origin", "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36", "x-debug-options" : "bugReporterEnabled", "x-discord-locale" : "en-US" }
    invite = requests.post("https://discord.com/api/v9/users/@me/invites", headers=headers, json={}).json()
    print(f"\nFriend invite generated!\nLink: https://discord.gg/{invite['code']}\nThis invite has a maximum of 5 uses.")

if __name__ == "__main__":
    config = {}
    for param in params:
        config[param] = input("Enter "+params[param]+": ")
    run(**config)
