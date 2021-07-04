#!/bin/sh

basedir=`cd $(dirname $0); pwd -P`
date
cd $basedir

eval `ssh-agent`
ssh-add .ssh/deploy

rm -rf tmp
git clone https://gitlab.com/zhekasmirnov/horizon-cloud-config.git --depth 1 tmp

/bin/cp -rf tmp/* .

python3 iccn-pack.py

git checkout --orphan  new_branch
git add -A
git commit -am "update"
git branch -D master
git branch -m master
git push -f origin master
