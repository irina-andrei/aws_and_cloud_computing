#!/bin/bash

# cloning the app files to the instance
git clone https://github.com/LSF970/sparta_test_app.git

# tell the os what version of nodejs you want
curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -

# install nodejs
sudo apt install nodejs -y

# install process manager
sudo npm install pm2 -g

# go to the app folder
cd ./sparta_test_app/app

# install your app
npm install

# run the app
node app.js