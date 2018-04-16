#!/bin/bash

git pull
git add Mao/. shadow/. q.py run.sh
git commit -m "Questions Answered"
git push
python q.py