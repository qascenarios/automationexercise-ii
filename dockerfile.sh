#!/bin/bash

# Exit immediately if any command fails
set -e

# Docker image name
IMAGE_NAME="topdandy/automationexercise-ii:latest"

# Local directory for Allure results
ALLURE_RESULTS_DIR="$(pwd)/allure-results"

echo "🧹 Removing previous Allure results..."
rm -rf "$ALLURE_RESULTS_DIR"

# Recreate results directory
mkdir -p "$ALLURE_RESULTS_DIR"

# Run tests inside Docker container
docker run --rm \
  -v "$ALLURE_RESULTS_DIR:/app/allure-results" \
  "$IMAGE_NAME"

echo "Test execution completed"

# Launch Allure report server
echo "Launching Allure report..."
allure serve "$ALLURE_RESULTS_DIR"
