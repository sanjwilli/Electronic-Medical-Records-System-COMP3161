# Electronic-Medical-Records-System-COMP3161

A web application for a hospitals patients record keeping system

## Getting Started

This system uses a MySQL database in order to keep the data, you'll need Mysql on your system. Our prefered system to use is a linux based system.

## Prerequisites

```
Python
Mysql
Flask
```

## Installing

### Python 2.7

Open the command line and do the following:

```
$ wget --no-check-certificate https://www.python.org/ftp/python/2.7.11/Python-2.7.11.tgz
$ tar -xzf Python-2.7.11.tgz
$ cd Python-2.7.11
```
You DON'T have to specify Python 2.7.11 you can choose the lastest version of python 2 which is what I highly recommend.

### Mysql 

NOTE MySQL should already be installed in the virtual environment but in the case it is not.

```
$ sudo apt-get update
$ sudo apt-get install mysql-server
```
### Flask

Normally I would recommend creating your own virtual environment but there is one already in this GitHub so the following should NOT be done. But in the case that it is not working please delete the "venv" file and do the following 

```
$ cd Electronic-Medical-Records-System-COMP3161/
$ virtualenv venv
```
If there isn't a requirements.txt file please do the following

```
$ pip install flask
```

## Running the System

Open the command line and find the file. If there is no requirements.txt file then skip the second line below.

```
$ source venv/bin/activate
$ pip install -r requirements.txt
```
Now you open a new command line terminal and start Mysql. When Mysql is open please do the following

```
mysql> source /path/to/file/Electronic-Medical-Records-System-COMP3161/hospital_final3.sql
```
Your database has been created with only one (1) data and that is the administration Information. Where you should be able to login to the as admin with the following

```
username: admin0001
password: pass1234
```
