#!/bin/bash

whoami
date
echo "Current shell: $SHELL"
echo "Bash version: $BASH_VERSION"

# Documentation:
man ls

ls -lah .

echo "User: $USER"
echo "Numbers: {1..5}"
echo "Today: $(date)"

command -v bash
command -v python3

history | tail -n 10
