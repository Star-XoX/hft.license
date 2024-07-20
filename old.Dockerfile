FROM python:3.9-slim

# Create a virtual environment
RUN python3 -m venv /venv

# Activate the virtual environment
ENV PATH="/venv/bin:$PATH"

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the Python script
COPY script.py .

# Run the Python script
CMD ["python", "script.py"]