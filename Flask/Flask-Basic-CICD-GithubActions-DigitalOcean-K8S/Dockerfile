FROM ubuntu:20.04

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN apt-get update -y && apt-get install -y python3-pip 

# We copy just the requirements.txt first to leverage Docker cache
ADD requirements.txt /app/

WORKDIR /app

RUN /bin/bash -c "pip3 install --no-cache-dir -r requirements.txt"

ADD /app/ /app/

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "wsgi:app"]