# Use an official Ubuntu 22.04 image as the base
FROM ubuntu:22.04

WORKDIR /xox

RUN apt-get update && apt-get install -y git python3 python3-pip  cron

# RUN (crontab -l ; echo "* * * * * nohup python3 -u /xox/hft.license/script.py > /xox/hft.license/out.script &") | crontab -

#Setup cron
COPY ./cronjob /etc/cron.d/cronjob
RUN crontab /etc/cron.d/cronjob
RUN chmod 644 /etc/cron.d/cronjob
RUN touch ./cron.log

COPY placeholder.py /placeholder.py

# RUN ["python3", "/placeholder.py"]

# CMD ["tail", "-f", "/dev/null"]

CMD ["cron", "-f"]