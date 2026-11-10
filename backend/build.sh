#!/usr/bin/env bash
# Build script for Render / cloud deployment
set -o errexit

pip install --upgrade pip
pip install -r requirements.txt
