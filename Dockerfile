FROM python:3

WORKDIR /Users/roastbeefer/docker/chucknorris

RUN pip install requests

COPY . .

CMD ["python", "./chucknorris.py"]
