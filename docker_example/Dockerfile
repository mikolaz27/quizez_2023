FROM python:3.11-rc-slim

RUN apt update
RUN python --version
RUN mkdir "/docker_example"

WORKDIR /docker_example


COPY ./python_docker_hello_world.py ./python_docker_hello_world_in_container.py
COPY ./requirements.txt ./requirements.txt

RUN python -m pip install --upgrade pip & pip install -r ./requirements.txt

CMD ["python", "python_docker_hello_world_in_container.py"]


