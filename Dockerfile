# Use an official Ubuntu 22.04 image as the base
FROM ubuntu:22.04

RUN apt-get update && apt-get install -y git python3 python3-pip python3.10-venv

# Clone your repository

RUN git clone https://github.com/Star-XoX/hft.license.git

WORKDIR /hft.license

# Create a virtual environment
RUN python3 -m venv /venv

# Activate the virtual environment
ENV PATH="/venv/bin:$PATH"

# Install dependencies
RUN pip install -r requirements.txt

# Run the Python script
# CMD ["python", "script.py"]

RUN chmod +x start.sh
CMD ["python", "placeholder.py"]
# ENTRYPOINT ["./start.sh"]

