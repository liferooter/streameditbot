# Stream editor bot (@streameditbot)
## What's this?
It's Telegram bot for executing some Unix text processing commands on messages
in groups.
## How can I do with it...
## ...as user
You can add this bot to your group and execute sed, awk, grep and some other
Unix commands on messages in this chat
## ...as developer
I distribute this code under Unlicense license, so you can do what you want.\
You can fork it. You can contribute to it. You can sell it. You can use its
code in your projects. You can deploy my bot's copy on your server. You can
do anything. This code is not mine, it's yours.
## Requirements
- Python 3
- Docker
## How to deploy this bot on my server?
I don't recommend you to do it, but if you want to get yet another useless
copy of already existing bot,
you shoud:
1. Get Telegram bot token from @BotFather

2. Clone my repo
    ```shell script
    git clone https://github.com/liferooter/streameditbot
    ```
3. Build docker image 
    ```shell script
    docker build -t streameditbot_img .
    ```
4. Deploy docker
    ```shell script
    docker run --name streameditbot \
               -e BOT_TOKEN="your-bot-token" \
               streameditbot_img
    ```

## Is there this bot in Docker Hub?
No.