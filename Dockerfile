FROM php:7.3.14-apache 
# [PowerShell]
# docker build --tag=assess:latest
# docker run  -v D:\Users\Michael\Documents\assess.io:/var/www/html -p 8000:8000 -p 80:80 -it assess:latest /bin/bash

RUN apt-get update

ADD laravel.conf /etc/apache2/sites-available
RUN a2dissite 000-default
RUN a2ensite laravel
RUN a2enmod rewrite
