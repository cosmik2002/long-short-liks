# swagger-client
This is a simple API

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
long_url = 'long_url_example' # str | long link (optional)

try:
    # shotter link, return short link
    api_instance.api_long_to_short_put(long_url=long_url)
except ApiException as e:
    print("Exception when calling UsersApi->api_long_to_short_put: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:5000*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*UsersApi* | [**api_long_to_short_put**](docs/UsersApi.md#api_long_to_short_put) | **PUT** /api/long_to_short | shotter link, return short link
*UsersApi* | [**api_short_postfix_get**](docs/UsersApi.md#api_short_postfix_get) | **GET** /api/{short_postfix} | redirect to long link
*UsersApi* | [**api_statistic_short_postfix_get**](docs/UsersApi.md#api_statistic_short_postfix_get) | **GET** /api/statistic/{short_postfix} | statistic to short link


## Documentation For Models



## Documentation For Authorization

 All endpoints do not require authorization.


## Author

you@your-company.com

