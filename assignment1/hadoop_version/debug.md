encountered error when using “hadoop dfs -ls /":
connection refused

Diagnose:
You can check the status of a service with
service <service-name> status
and you can restart a service with
service <service-name> restart

e.g. ```service hadoop-hdfs-namenode```, the output is
Hadoop namenode is dead and pid file exists showing status FAILED

Solution:
http://kshitish-bigdata.blogspot.com/2015/02/hadoop-namenode-is-dead-and-pid-file.html
First stop all Hadoop daemons/services and then re-format namenode. After reformatting the namenode try starting all daemons again and check the status. If all daemons are running OK then you are done. 

The procedure are as follows:
1. 
```
for  service in /etc/init.d/hadoop-hdfs-*; do $service stop; done;
```
2.
```
for  service in /etc/init.d/hadoop-hdfs-*; do $service status; done;
```
3. Remove cache
```sudo rm -rf /var/lib/hadoop-hdfs/cache/*```
4. Reformat namenode
```sudo -u hdfs hdfs namenode -format```
5.
``` 
for  service in /etc/init.d/hadoop-hdfs-*; do $service start; done;
```
