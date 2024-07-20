# Use an official Ubuntu 22.04 image as the base
# FROM ubuntu:22.04
# FROM ubuntu:22.04-slim
FROM ubuntu:22.04-minimal

RUN apt-get update && apt-get install -y git python3 python3-pip

WORKDIR /xox

COPY placeholder.py /placeholder.py

CMD ["python3", "/placeholder.py"]

# CMD ["tail", "-f", "/dev/null"]

