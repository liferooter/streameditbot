FROM python:3

WORKDIR /usr/src/app

COPY main.py .

RUN python -m pip install aiogram

USER nobody

CMD ["python", "/usr/src/app/main.py"]
