
import requests, threading

desc = "Deletes a webhook"
params = {
    "webhook_url" : "the URL of the webhook you want to delete"
}

def run(webhook_url):
    requests.delete(webhook_url)

if __name__ == "__main__":
    config = {}
    for param in params:
        config[param] = input("Enter "+params[param]+": ")
    run(**config)
