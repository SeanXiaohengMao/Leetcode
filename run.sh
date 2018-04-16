#!/bin/bash

git pull
git add Mao/. shadow/. q.py run.sh
python q.py
git commit -m "Questions Answered"
git push
python q.py