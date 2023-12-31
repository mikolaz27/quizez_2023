FROM python:3.11-rc-slim

RUN apt update
RUN mkdir /quiz

WORKDIR /quiz

COPY ./src  ./src
COPY ./commands ./commands
COPY ./requirements.txt ./requirements.txt

RUN  pip install -r ./requirements.txt

CMD ["bash"]


