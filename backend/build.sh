#!/usr/bin/env bash
# Build script for Render deployment
set -o errexit

pip install --upgrade pip
pip install -r requirements.txt

# Download spacy model (required by ATS router)
python -m spacy download en_core_web_sm || true
