# Notes on 5 October - User Data


What we did today:

-- Started up an Instance with Ubuntu 18.04 (1e9)

```shell
sudo apt update
sudo apt upgrade -y
sudo apt install nginx -y

# optional
cd /etc/nginx/sites-available
sudo nano default
#

sudo apt install sed
sudo sed -i "s/try_files \$uri \$uri\/ =404;/proxy_pass http:\/\/localhost:3000\/;/" /etc/nginx/sites-available/default

# sed => allows us to replace certain parts of a file using a command line
# -i for interactive
# in between the "" will be what we need to replace
# changing this => telling nginx to serve a particular port as default.

sudo systemctl restart nginx
sudo systemctl enable nginx

```
```shell
sudo nano nrp_provision.sh
sudo chmod 755 nrp_provision.sh
./nrp_provision.sh
```

ADVANCED - USER DATA
- either upload script file or write the codes manually in the 'User Data' box
-  https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html

<br>

# 1. SCRIPT for User Data on a new Instance (with Ubuntu 18.04 1e9)

```shell
#!/bin/bash
apt update -y
apt upgrade -y
apt install nginx -y
apt install sed
sed -i "s/try_files \$uri \$uri\/ =404;/proxy_pass http:\/\/localhost:3000\/;/" /etc/nginx/sites-available/default
systemctl restart nginx
systemctl enable nginx
curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -
apt install nodejs -y
npm install pm2 -g
apt install git -y
git clone https://github.com/LSF970/sparta_test_app.git repo
cd repo
cd app
npm install
pm2 start app.js
```

<br>

# 2. From AMI (with app + nginx installed), start Instance with this code in User Data:

```shell
#!/bin/bash
cd /home/ubuntu/repo/app
# This would start from root, so it needs the full address.
sudo systemctl restart nginx
npm install
pm2 start app.js
```

You could create 10-15 Instances from the AMI and all will have a running app (with different IPs).