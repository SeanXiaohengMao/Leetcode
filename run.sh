#!/bin/bash

git pull
mv REAMEcopy.md README.md
python q.py
git add --all
git commit -m "Questions Answered"
git push