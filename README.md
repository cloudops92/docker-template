# docker-template

![](https://github.com/zero-templates/docker-template/workflows/docker-template-ci/badge.svg)

The basic docker example, building greeting python application into docker container. 

## Build

###### Build Docker image
This command build the docker image with name `docker-template_hello-docker`.
~~~~
$ docker-compose build
~~~~

###### Running docker image
~~~~
$ docker run docker-template_hello-docker
~~~~

###### Greet your self
~~~~
$ docker run docker-template_hello-docker <your_name>
~~~~


## Overview

- **Build Pipeline**: <https://github.com/lazy-leo/docker-template/actions/new>
- **Maintainer**: lazzy.leoo@gmail.com