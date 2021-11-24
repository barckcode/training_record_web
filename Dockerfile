FROM python:3.9

WORKDIR /app

COPY ./app/ /app
COPY ./requirements.txt /app/requirements.txt

RUN pip3 install -r requirements.txt

CMD [ "flask", "run", "--host=0.0.0.0" ]
