#!/bin/bash

LIB_DIR="${PWD}"


# Installing commit message hook
rm -f .git/hooks/commit-msg
ln -s -f ${LIB_DIR}/githooks/commit_message.py .git/hooks/commit-msg

# Installing pre-commit message hook
rm -f .git/hooks/pre-commit
ln -s -f ${LIB_DIR}/githooks/pre_commit.py .git/hooks/pre-commit

# Setting up permissions
chmod +x .git/hooks/*

rm -rf .git/hooks/${LIB_DIR}/githooks
ln -s -f ${LIB_DIR}/githooks .git/hooks/githooks

echo "Git hooks installed successfully !"