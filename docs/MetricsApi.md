# swagger_client.MetricsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**metrics_companies_get**](MetricsApi.md#metrics_companies_get) | **GET** /metrics/companies | 

# **metrics_companies_get**
> CodatPublicApiModelsClientsClientCompanyMetricsModel metrics_companies_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: API Key Auth
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MetricsApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.metrics_companies_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->metrics_companies_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CodatPublicApiModelsClientsClientCompanyMetricsModel**](CodatPublicApiModelsClientsClientCompanyMetricsModel.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

