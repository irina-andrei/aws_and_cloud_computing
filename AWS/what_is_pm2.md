# What is PM2?

PM2 = Process manager for Node.js applications. It gives more control over node processes.

PM2 is available as an NPM package, so you can install it through npm or yarn:
```
$ npm install pm2
# or
$ yarn add pm2
```

After installing PM2, run npx pm2 --version to see the installed version:
```
$ npx pm2 --version
5.1.2
```
If you don't want to prefix the pm2 command with npm every time, you can install it globally:
```
$ npm install -g pm2
# or
$ yarn global add pm2
```

<br>

### Why is it useful? 
PM2 is useful because it allows you to manage and monitor your Node.js applications in a production environment. 

**Benefits:**

* It can keep your applications alive forever, even if they crash or encounter errors. PM2 will automatically restart them and maintain a stable service.
* It can load balance your applications across multiple CPU cores, improving performance and scalability.
* It can watch and reload your applications whenever you make changes to the code, without any downtime or service interruption.
* It can log and display various metrics and information about your applications, such as CPU usage, memory usage, requests per minute, errors, etc.
* It can integrate with other tools and platforms, such as Keymetrics, Docker, Kubernetes, Nginx etc to provide a complete solution for deploying and managing Node.js applications.

<br>

### Some of the commands we can use to interact with node processes:

```
pm2 start app.js
```
=> This command will start the app in the background. It monitors your application and keeps it running indefinitely.

```
pm2 start app.js --name "my app"
```
=> PM2 defaults to the name of the entry file as the app's name, but you can use a more recognizable name through the --name option. This name is what you'll use to reference the application in many pm2 subcommands.

```
$ pm2 restart app
```
=>  The restart subcommand is also available for manually restarting your application at any time.

```
$ pm2-dev start app.js
```
=> It can be quite tedious to restart your application server in development every time you change the source files. Using the pm2-dev binary to start your application can take care of that concern automatically.

<br>

### How you can manage processes using PM2

To list your running applications:
```
pm2 list
```
This prints a table describing the state of all running applications with columns for:

* the app name and id
* CPU and memory usage
* number of restarts (↺)
* uptime
* process id
* the mode (fork or cluster)


You can also sort the output table according to a metric of your choice:
```
$ pm2 list --sort [name|id|pid|memory|cpu|status|uptime][:asc|desc]
# such as
$ pm2 list --sort uptime:desc
```

Another way to keep tabs on your running applications is through the built-in terminal dashboard (accessed through the monit subcommand). This allows you to view live data on resource usage and logs for each of your applications.
```
$ pm2 monit
```
<br>

#### Sources:
- [A Complete Guide to PM2](https://blog.appsignal.com/2022/03/09/a-complete-guide-to-nodejs-process-management-with-pm2.html)