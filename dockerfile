FROM python:3.9.10-alpine

WORKDIR /app

COPY ./requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 80

CMD [ "./entrypoint.sh"]