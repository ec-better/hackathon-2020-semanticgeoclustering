


# Preparing for BETTER Hackathon 2020 Exercise 4: Semantic Geo-Clustering with SANSA

The exercise will feature the deployment of <ins>a pre-setup Docker image on Linux OS</ins>. 



# Requirements
* Docker Engine >= 1.13.0
* docker-compose >= 1.10.0
* Around 10 GB of disk space for Docker images
* Around 8 GB of RAM on the hosting computer and 4 GB on the Docker image


## Preparation before the Hackathon

1. Clone the Hackathon Project from here: https://github.com/ec-better/hackathon-2020-semanticgeoclustering

2. The  Hackathon requires installation of Python, SANSA, Hadoop, Apache Spark and Apache Zeppelin. But do not worry! We have installed them all in a docker image, ready to download and use on the go.

3. To use the docker image you will need:
  Docker Engine  >= 1.13.0     Installation Tutorial: https://docs.docker.com/engine/install/
  Docker Compose >= 1.10.0   Installation Tutorial: https://docs.docker.com/compose/install/

4. After Installation, configure Docker:
  ```
sudo usermod -aG docker %username%
```
  This allows to run docker commands without sudo prefix (necessary for running make targets).

Get the hackathon jar file (requires ```wget```):
```
make
```
Start the cluster (this will lead to downloading BDE docker images, will take a while):
```
make up
```
Start the cluster (this will lead to downloading BDE docker images, which will take a while)

To load the data to your cluster simply do:
```
make load-data
```

# Starting page on the day of hackathon
When start-up is done you will be able to access the following interfaces:
* http://localhost:8080/ (Spark Master)
* http://localhost:8088/home (Hue HDFS Filebrowser)
* http://localhost/ (Zeppelin)

Go on and open [Zeppelin](http://localhost), make a new notebook and wait for the moderator to start the session.
![Apache Zeppelin RDF POI](./docs/images/POI.png "Apache Zeppelin Running POI Example")



# Notes
* The instructions from this repo were tested on Ubuntu 18.04 and Macos 10.15.5 with Docker engine 17.03. and Docker engine 19.03.13

* This repository you hold a [docker-compose.yml](./docker-compose.yml) for running Hadoop/Spark cluster locally.
* The cluster also includes [Hue](http://gethue.com/) for navigation and copying file to HDFS.
* The notebooks are created and run using [Apache Zeppelin](https://zeppelin.apache.org/).

To restart Zeppelin without restarting the whole stack:
```
make restart
```
Stop the whole stack:
```
make down
```
### Executing hackathon From Command Line
It is also possible to execute the applications from the command line. Get SANSA-Examples jar and start the cluster if you already have not done it:
```
make
make up
make load-data
```
