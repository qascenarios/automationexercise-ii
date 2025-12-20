# Use a slim Python base image
FROM python:3.11-slim

# Install dependencies for Playwright
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        curl \
        git \
        libnss3 \
        libatk1.0-0 \
        libatk-bridge2.0-0 \
        libcups2 \
        libdrm2 \
        libxkbcommon0 \
        libxcomposite1 \
        libxdamage1 \
        libxrandr2 \
        libgbm1 \
        libgtk-3-0 \
        libasound2 \
        libpangocairo-1.0-0 \
        fonts-liberation \
        wget \
        && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy dependency file first
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright browsers (Chromium only to reduce size)
RUN playwright install chromium

# Copy project files
COPY . .

# Clean old allure-results
RUN rm -rf allure-results

# Default command: run tests
CMD ["pytest", "--alluredir=allure-results"]
