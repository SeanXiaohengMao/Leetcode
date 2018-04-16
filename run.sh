#!/bin/bash

git pull
git add Mao/. shadow/. q.py run.sh README.md
python q.py
git commit -m "Questions Answered"
git push
python q.py