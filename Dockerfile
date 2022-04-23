FROM python:3.9.12-buster

RUN pip install requests

RUN git clone https://github.com/RoastBeefer00/chuck-norris.git 

CMD ["python", "./chuck-norris/chucknorris.py"]
