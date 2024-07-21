# Use an official Ubuntu 22.04 image as the base
FROM ubuntu:22.04

WORKDIR /xox

RUN apt-get update && apt-get install -y git python3 python3-pip cron

RUN timedatectl set-timezone America/New_York

#Setup cron
COPY ./cronjob /etc/cron.d/cronjob
RUN crontab /etc/cron.d/cronjob
RUN chmod 644 /etc/cron.d/cronjob

COPY init.py /init.py

# CMD ["tail", "-f", "/dev/null"]

CMD ["cron", "-f"]