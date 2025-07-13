FROM python:3.10-slim

# Install dependencies
RUN apt update && apt upgrade -y && \
    apt-get install -y git curl wget ffmpeg bash neofetch python3-pip software-properties-common && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python packages
COPY requirements.txt .
RUN pip install --upgrade pip wheel && \
    pip install --no-cache-dir -r requirements.txt

# Set working directory
WORKDIR /app
COPY . .

# Expose port
EXPOSE 8000

# Run the bot and Flask API
CMD flask run -h 0.0.0.0 -p 8000 & python3 -m devgagan
