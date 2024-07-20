# Use an official Ubuntu 22.04 image as the base
FROM ubuntu:22.04

RUN apt-get update && apt-get install -y git python3 python3-pip

WORKDIR /xox

COPY placeholder.py /placeholder.py

ENTRYPOINT ["python", "/placeholder.py"]

CMD ["tail", "-f", "/dev/null"]

