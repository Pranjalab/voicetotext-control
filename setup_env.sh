#!/bin/bash

# Function to check if a package is installed
is_installed() {
    dpkg -s "$1" &> /dev/null
}

# Install system dependencies
echo "Checking for required system packages..."

REQUIRED_PACKAGES=("portaudio19-dev" "build-essential" "libasound-dev")
MISSING_PACKAGES=()

for pkg in "${REQUIRED_PACKAGES[@]}"; do
    if ! is_installed "$pkg"; then
        MISSING_PACKAGES+=("$pkg")
    fi
done

if [ ${#MISSING_PACKAGES[@]} -ne 0 ]; then
    echo "The following packages are missing: ${MISSING_PACKAGES[@]}"
    echo "Installing missing packages..."
    sudo apt-get update
    sudo apt-get install -y "${MISSING_PACKAGES[@]}"
else
    echo "All required system packages are already installed."
fi

# Create and activate a Python virtual environment

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null
then
    echo "Python3 is not installed. Please install Python3 and try again."
    exit 1
fi

# Create virtual environment named 'voice_to_text'
echo "Creating virtual environment 'voice_to_text'..."
python3 -m venv voice_to_text

# Activate the virtual environment
echo "Activating virtual environment..."
source voice_to_text/bin/activate

# Upgrade pip inside the virtual environment
echo "Upgrading pip..."
pip install --upgrade pip

# Install required packages from requirements.txt
if [ -f "requirements.txt" ]; then
    echo "Installing required packages..."
    pip install -r requirements.txt
else
    echo "requirements.txt file not found!"
    deactivate
    exit 1
fi

echo "Setup complete! To activate the environment, run: source voice_to_text/bin/activate"
