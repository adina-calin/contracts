FROM python:3.8-buster
RUN apt-get update && apt-get install libgraphviz-dev graphviz --assume-yes
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
ADD . /ev_contracte
WORKDIR /ev_contracte
RUN pip install -e .
