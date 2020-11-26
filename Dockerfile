FROM python:3

ARG bot_token

WORKDIR /usr/src/app

COPY main.py .

RUN python -m pip install aiogram

USER nobody

ENV BOT_TOKEN=$bot_token

CMD ["python", "/usr/src/app/main.py"]
