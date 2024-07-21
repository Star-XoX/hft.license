# Use an official Ubuntu 22.04 image as the base
FROM ubuntu:22.04

RUN apt-get update && apt-get install -y git python3 python3-pip  cron

RUN (crontab -l ; echo "* * * * * nohup python3 -u /xox/hft.license/script.py > /xox/hft.license/out.script &") | crontab -


WORKDIR /xox

COPY placeholder.py /placeholder.py

CMD ["python3", "/placeholder.py"]

# CMD ["tail", "-f", "/dev/null"]

