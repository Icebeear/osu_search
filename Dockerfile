FROM python:3.11.2 

SHELL ["/bin/bash", "-c"]

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

RUN pip install --upgrade pip  

WORKDIR /osu_search

RUN mkdir -p /osu_search

COPY . /osu_search

RUN pip install -r requirements.txt

# COPY wait-for-it.sh /usr/local/bin/wait-for-it.sh

# RUN chmod +x /usr/local/bin/wait-for-it.sh

WORKDIR /osu_search/app 

EXPOSE 8000  