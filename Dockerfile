# Use an official Ubuntu 22.04 image as the base
FROM ubuntu:22.04

RUN apt-get update && apt-get install -y git

# Clone your repository
RUN git clone git@github.com:Star-XoX/hft.license.git

WORKDIR /hft.license

# Create a virtual environment
RUN python3 -m venv /venv

# Activate the virtual environment
ENV PATH="/venv/bin:$PATH"

# Install dependencies
RUN pip install -r requirements.txt

# Run the Python script
CMD ["python", "script.py"]
