# wan-ip-check
Easy tool to run as a container and notify a webhook when your WAN IP changes.

# Usage
## docker-compose
1. Setup your .env file as described below
1. Clone this repo
1. docker-compose up -d
## docker without compose 
1. Setup .env file
1. docker run -d --restart unless-stopped -v ${PWD}/.env:/app/.env jski/wan-ip-check:latest

# .env file
You need the following variables:
- webhook_url (where you want to send the notification)
- check_site (the site to check your IP, by default I use "http://4.ipquail.com/ip")
- system_name (name to pass along with the webhook so you know which machine you're notifying from)
- check_interval (time in seconds to pass between checks, by default I use "3600")