#!/bin/bash

git pull
cp RDcopy README.md
python q.py
git add --all
git commit -m "Questions Answered"
git push