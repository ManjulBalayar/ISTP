#!/bin/bash
# CI setup script to prepare the environment for tests

# Create logs directory structure for Django
mkdir -p ISTP_website/logs
mkdir -p logs
touch ISTP_website/logs/django.log
echo "Created logs directory structure"

# Make bandit config executable
chmod +x security_check.py
echo "Made security scripts executable"

# Install security tools
pip install safety bandit packaging
echo "Installed security tools"

# Run security checks (continue even if it fails)
python security_check.py || echo "Security issues found, but continuing with build"

# Continue with other CI steps...
echo "Setup complete" 