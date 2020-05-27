#!/bin/bash
CONTAINER_NAME='mlspec/mlspeclib-action-samples-train'

pipenv update mlspeclib
pipenv lock -r > requirements.txt

git add .
git commit -a -m 'updating requirements'
git push

docker build --no-cache -t $CONTAINER_NAME .
docker push $CONTAINER_NAME

python3 -m unittest tests/test*
python3 -m unittest integration/test*


