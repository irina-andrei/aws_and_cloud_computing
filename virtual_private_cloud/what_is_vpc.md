# VPC

VPC = **Virtual Private Cloud**

Most important aspect of VPC is **security**: using a VPC means having greater control over security.

* AWS creates a default VPC for you, and there is a default subnet for each Availability Zone.
* In Azure, these are called *Virtual Networks*, and there is no default VPC or default subnet => more setup involved.
* GCP, same as AWS, creates a default VPC for you. 

<br>

![AltText](Images/diagram1.png)

```placeholder for DIAGRAM```

In a custom VPC:
* You decide whether subnets are public or private and what Availability Zone you want for each subnet.
* SSH only allows login to the VPC, not to specific individual subnets. 

We will have a Public Subnet (A.Z. 1a) and a Private Subnet (A.Z. 1b)

<br>

![AltText](Images/diagram2.png)

```placeholder for DIAGRAM```

<br>

**CIDR Block** = defines the range of IP Addresses allowed (IP allowance).

You can set up a Public Router which will use the Public Route Table to send packets where they are allowed to go. 

**Public Route Table** => makes sure internet gateway will have traffic routed to our Public Subnet.

**Default Route Table** => makes sure traffic (packets) is routed *internally*. Requests for Database still go through this.

* The APP VM will still have a Public IP Address, but the Database VM has no need for a Public IP Address.
* Once you SSH in the App VM, you can use it as a **Jump Box** to SSH into the Database VM. 
* The Database VM does not have a route to the internet, it's the whole point of having a Private Subnet. 
* VPCs can have the same CIDR if they don't need to communicate with each other.
* 2-tier Architecture: front end + back end.
* There will still be some reserved addressess (usually .0 or .1 or .255).



<br>


## My Script for User Data that I used on my existing updated_app_AMI: 


```shell
#!/bin/bash

export DB_HOST=mongodb://10.0.3.52:27017/posts

cd /home/ubuntu/sparta_test_app/app
sudo systemctl restart nginx
npm install

#seed database
echo "Clearing and seeding database..."
node seeds/seed.js
echo " --> Done!"

#install pm2
sudo npm install pm2 -g

#kill previous app background processes
pm2 kill

# start the app in the background
pm2 start app.js

```

<br>

* npm install - checks DB connection

* Security Groups are associated with a specific VPC.

* 3000 is the default port for node.js


## Steps for VPC:

1. On AWS, go to VPC:

![AltText](1.png)

<br>

2. Next, click on Create VPC:

![AltText](2.png)

<br>

3. Next, choose an appropriate name for your VPC and the CIDR block (Range of IP addresses you are allowing):

![AltText](3.png)

<br>
4. Now you can add tags to the VPC. The 'Name' tag will already have been added automatically. If you're happy with everything, press 'Create VPC': 

![AltText](4.png)

<br>
5. It will confirm that the VPC has been created: 

![AltText](5.png)

<br>
6. Next, we will create the Subnets. On the left hand panel, click on Subnets: 

![AltText](6.png)

<br>
7. Click Create Subnets:

![AltText](7.png)

<br>
8. Next, find the correct VPC in the dropdown list:

![AltText](8.png)

<br>
9. We'll create the Public Subnet first. Choose an appropriate name, then the Availability Zone (in our case 1a as we want different AZ) and CIDR 

![AltText](9.png)

<br>
10. Next, 

![AltText](10.png)

<br>
11. Next, 

![AltText](11.png)

<br>
12. Next, 

![AltText](12.png)

<br>
13. Next, 

![AltText](13.png)

<br>
14. Next, 

![AltText](14.png)

<br>
15. Next, 

![AltText](15.png)

<br>
