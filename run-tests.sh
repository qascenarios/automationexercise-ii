#!/bin/bash

# Exit immediately if any command fails
set -e

# Docker image name
IMAGE_NAME="topdandy/automationexercise-ii-mb:latest"

# Allure results directory
ALLURE_RESULTS_DIR="$(pwd)/allure-results"

echo "Cleaning previous Allure results..."
rm -rf "$ALLURE_RESULTS_DIR"
mkdir -p "$ALLURE_RESULTS_DIR"

echo "Running tests in Docker..."
docker run --rm \
  -v "$ALLURE_RESULTS_DIR:/app/allure-results" \
  "$IMAGE_NAME"

echo "Test execution completed"
echo "Allure results generated at: $ALLURE_RESULTS_DIR"

# Detect CI environment
if [[ -z "$CI" ]]; then
  echo "Local environment detected — launching Allure report..."
  allure serve "$ALLURE_RESULTS_DIR"
else
  echo "CI/CD environment detected — skipping Allure server launch"
  echo "Allure results will be available as pipeline artifacts"
fi
