#!/bin/bash

# User Creation Script
# Usage: ./adduser.sh <username>
# This script creates a user, sets password, and configures home directory

# Check if running as root or with sudo
if [ "$EUID" -ne 0 ]; then
    echo "This script must be run as root or with sudo"
    echo "Usage: sudo ./adduser.sh <username>"
    exit 1
fi

# Check if username is provided
if [ $# -eq 0 ]; then
    echo "Error: No username provided"
    echo "Usage: sudo ./adduser.sh <username>"
    exit 1
fi

USERNAME=$1

# Check if user already exists
if id "$USERNAME" &>/dev/null; then
    echo "Error: User '$USERNAME' already exists"
    exit 1
fi

echo "Creating user: $USERNAME"

# Create user with home directory
useradd -m -s /bin/bash "$USERNAME"

if [ $? -eq 0 ]; then
    echo "✓ User '$USERNAME' created successfully"
else
    echo "✗ Failed to create user '$USERNAME'"
    exit 1
fi

# Set password for the user
echo "Setting password for user '$USERNAME'"
passwd "$USERNAME"

if [ $? -eq 0 ]; then
    echo "✓ Password set successfully for '$USERNAME'"
else
    echo "✗ Failed to set password for '$USERNAME'"
    exit 1
fi

# Add user to sudo group (optional - uncomment if needed)
# usermod -aG sudo "$USERNAME"
# echo "✓ Added '$USERNAME' to sudo group"

# Set proper ownership of home directory
chown -R "$USERNAME:$USERNAME" "/home/$USERNAME"


usermod -d "/home/$USERNAME" "$USERNAME"

if [ $? -eq 0 ]; then
    echo "✓ Home directory ownership set correctly"
else
    echo "✗ Failed to set home directory ownership"
fi

# set sudo permission
usermod -aG sudo "$USERNAME"

# Display user information
echo ""
echo "User creation completed successfully!"
echo "Username: $USERNAME"
echo "Home directory: /home/$USERNAME"
echo "Shell: /bin/bash"
echo ""
echo "To switch to this user, run: su - $USERNAME"
echo "To check user groups, run: groups $USERNAME"