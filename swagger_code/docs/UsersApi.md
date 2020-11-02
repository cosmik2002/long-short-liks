# swagger_client.UsersApi

All URIs are relative to *http://localhost:5000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_long_to_short_put**](UsersApi.md#api_long_to_short_put) | **PUT** /api/long_to_short | shotter link, return short link
[**api_short_postfix_get**](UsersApi.md#api_short_postfix_get) | **GET** /api/{short_postfix} | redirect to long link
[**api_statistic_short_postfix_get**](UsersApi.md#api_statistic_short_postfix_get) | **GET** /api/statistic/{short_postfix} | statistic to short link


# **api_long_to_short_put**
> api_long_to_short_put(long_url=long_url)

shotter link, return short link

shotter link, return short link

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
long_url = 'long_url_example' # str | long link (optional)

try:
    # shotter link, return short link
    api_instance.api_long_to_short_put(long_url=long_url)
except ApiException as e:
    print("Exception when calling UsersApi->api_long_to_short_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **long_url** | **str**| long link | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_short_postfix_get**
> api_short_postfix_get(short_postfix)

redirect to long link

search long link and redirect

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
short_postfix = 'short_postfix_example' # str | short_postfix for long link

try:
    # redirect to long link
    api_instance.api_short_postfix_get(short_postfix)
except ApiException as e:
    print("Exception when calling UsersApi->api_short_postfix_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **short_postfix** | **str**| short_postfix for long link | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: redirect

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_statistic_short_postfix_get**
> api_statistic_short_postfix_get(short_postfix)

statistic to short link

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi()
short_postfix = 'short_postfix_example' # str | short_postfix for long link

try:
    # statistic to short link
    api_instance.api_statistic_short_postfix_get(short_postfix)
except ApiException as e:
    print("Exception when calling UsersApi->api_statistic_short_postfix_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **short_postfix** | **str**| short_postfix for long link | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

