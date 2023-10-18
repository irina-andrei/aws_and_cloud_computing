#!/bin/bash

# cloning the app files to the instance
git clone https://github.com/irina-andrei/ci_cd.git

# tell the os what version of nodejs you want
curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -

# install nodejs
sudo apt install nodejs -y

# install process manager
sudo npm install pm2 -g

# go to the app folder
cd ci_cd/app

# install your app
npm install

# kill any remaining processes
pm2 kill

# run the app
pm2 start app.js

# restart the app
pm2 restart app.js