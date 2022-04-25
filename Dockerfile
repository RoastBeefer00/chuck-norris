FROM python:3.9.12-buster

RUN pip install requests

COPY startup.sh .

CMD ["./startup.sh"]
