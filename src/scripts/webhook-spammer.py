
import requests, threading

desc = "Spams a webhook"
params = {
    "webhook_url" : "the URL of the webhook you want to spam",
    "content" : "the text you want it to be spammed with"
}

def run(webhook_url, content):
    print('\nSpamming webhook. Press CTRL+C to stop.')
    while True:
        try:
            requests.post(webhook_url, json={'content':content})
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    config = {}
    for param in params:
        config[param] = input("Enter "+params[param]+": ")
    run(**config)
