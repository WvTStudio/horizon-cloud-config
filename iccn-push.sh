#!/bin/sh
# git clone https://gitlab.com/zhekasmirnov/horizon-cloud-config.git --depth 1 tmp
basedir=`cd $(dirname $0); pwd -P`
date
cd $basedir
cd tmp
info=$(git pull | grep 'Already up-to-date')
if  [[ -z $info ]];then
cd ..

/bin/cp -rf tmp/* .

python3 iccn-pack.py

eval `ssh-agent`
ssh-add ./.ssh/deploy

git checkout --orphan  new_branch
git add -A
git commit -am "update"
git branch -D master
git branch -m master
git push -f origin master
else
echo "Nothing to do"
fi
