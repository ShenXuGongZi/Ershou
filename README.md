
![](http://img.shields.io/codeclimate/coverage/github/triAGENS/ashikawa-core.svg)  ![](http://img.shields.io/badge/Python-2.7-green.svg)
![](http://img.shields.io/pypi/l/Django.svg)

###中文说明请看 [http://shenxugongzi.github.io/Ershou/](http://shenxugongzi.github.io/Ershou/)

### Sites for Ubuntu installation guide here refers to other systems, please refer to 

Web.py framework based on the production of this site is divided into two parts, the data crawling and web show. Database using sqlite 

Please refer to how to install web.py 

<pre> http://webpy.org/install </pre> 

### Gripping portion 

Get a directory folder file is responsible for crawling Information 

Before crawling you should install the following dependencies: 


<pre> requests, pyquery </pre> 


After installing the implementation: 


<pre> python Get.py </pre> 


You can grab data 


The server can use crontab timing crawl, the source file has been written only as follows sh 

Get.sh edit the file in the root directory 


<pre> vim get.sh </pre> 


Modify your path 


<pre> python /home/yourfile/get.py </pre> 


Then join the crontab 


<pre> crontab -e </pre> 


<pre> * / 10 * * * * sh /home/yourfile/get.sh </pre> 


Can be. 

Note: It is recommended to delete the database file to re-crawl. 


### Show the part 


Start the application needs to be installed gunicorn 


<pre> pip install gunicorn </pre> 


Start the service after installing 


<pre> gunicorn -w 8 app: ershou </pre> 

After starting the service default port is 8000 by default only allow 127.0.0.1 access is only allowed to access the machine. Debugging when you can add the following parameters 

<pre> gunicorn -w 8 0.0.0.0:8000 app: ershou </pre> 

So that you can visit any address. 

Nginx configuration, the xmiao.org replacement for your own domain name on it. 

<pre> 
server {
   listen 80; 
   server_name xmiao.org www.xmiao.org; 
   access_log /var/log/nginx/example.log; 

   location / {
       proxy_pass http://127.0.0.1:8000; 

       proxy_set_header Host $ host; 
       proxy_set_header X-Real-IP $ remote_addr; 
       proxy_set_header X-Forwarded-For $ proxy_add_x_forwarded_for; 
   } 
} 

server {
     listen 80; 
     server_name ershou.miaowu.asia; 

     location / {
         rewrite ^ http: //www.xmiao.org$request_uri permanent;? 
     } 
} 
</pre>
