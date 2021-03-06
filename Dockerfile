FROM python:3

WORKDIR /usr/src/app

COPY src/main.py .
COPY bin/sandbox.sh .
COPY LICENSE .

RUN python -m pip install aiogram
RUN useradd bot -d /nonexisting

# USER bot

CMD ["python", "/usr/src/app/main.py"]
