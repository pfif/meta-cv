FROM ubuntu:14.04

RUN apt-get -y update; apt-get -y install apt-transport-https curl python3.4 build-essential python3-pip libpq-dev 

RUN sh -c 'curl https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -'
RUN sh -c 'curl https://storage.googleapis.com/download.dartlang.org/linux/debian/dart_stable.list > /etc/apt/sources.list.d/dart_stable.list'
RUN apt-get -y update; apt-get -y install dart

RUN pip3 install uwsgi pylint

RUN pip3 install django==1.9 psycopg2==2.6

ADD . /var/django/metacvserver/

WORKDIR /var/django/metacvserver/

RUN mkdir -p /var/django/metacvserver_compiledjs/cv/
RUN /usr/lib/dart/bin/dart2js -vm --out=/var/django/metacvserver_compiledjs/cv/themaintemplate_bootstrap.js cv/static/cv/themaintemplate_bootstrap.dart
