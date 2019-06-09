FROM python:3.6-slim-stretch

COPY . /srv/

WORKDIR /srv/

RUN apt-get update &&  apt-get install -y libav-tools

RUN pip install -r requirements.txt

ENV PORT=5005

EXPOSE 5005

CMD ["sh", "run.sh"]
