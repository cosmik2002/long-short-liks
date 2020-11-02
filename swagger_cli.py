from __future__ import print_function

import json
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UsersApi(swagger_client.ApiClient())
long_url = "http://mail.ru"


try:
    # shotter link, return short link
    api_instance.api_long_to_short_put(long_url=long_url)
    short_postfix = json.loads(api_instance.api_client.last_response.data)['short_link'].split('/')[-1]
    api_instance.api_short_postfix_get(short_postfix=short_postfix)
    api_instance.api_statistic_short_postfix_get(short_postfix=short_postfix)
    print(api_instance.api_client.last_response.data)
except ApiException as e:
    print("Exception when calling UsersApi->api_long_to_short_put: %s\n" % e)