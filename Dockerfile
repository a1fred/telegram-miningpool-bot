FROM python:alpine3.6

RUN mkdir /app
WORKDIR /app
COPY . /app/

RUN pip3 install --no-cache-dir pipenv && pipenv install

CMD ["pipenv", "run", "python", "main.py"]
