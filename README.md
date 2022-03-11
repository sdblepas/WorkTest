# WorkTest
---
My Todo api, This api uses python FastAPI and MongoDB.

![example workflow](https://github.com/idokrn/WorkTest/blob/main/.github/workflows/build.yaml/badge.svg)


# Getting started
___
Clone this repository with
``` bash
git clone https://github.com/idokrn/WorkTest.git && cd WorkTest
```

Login to my Jfrog artifact registry

``` bash
docker login idokrn.jfrog.io -u anonymous
```

Bring the API up
``` bash
docker-compose up -d
```

Now you can verify the deployment by accessing the api docs [Here](http://localhost/docs)


