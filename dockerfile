FROM python:3.9.10-alpine

WORKDIR /app

COPY ./requirements.txt ./requirements.txt

RUN python3 -m pip install --upgrade pip wheel setuptools; \
    pip3 install -r requirements.txt

COPY . .

EXPOSE 80

CMD [ "./entrypoint.sh"]