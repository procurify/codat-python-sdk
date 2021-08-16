# codat_python_sdk.MetricsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**metrics_companies_get**](MetricsApi.md#metrics_companies_get) | **GET** /metrics/companies | 


# **metrics_companies_get**
> CodatPublicApiModelsClientsClientCompanyMetricsModel metrics_companies_get()



### Example

* Api Key Authentication (API Key Auth):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import metrics_api
from codat_python_sdk.model.codat_public_api_models_clients_client_company_metrics_model import CodatPublicApiModelsClientsClientCompanyMetricsModel
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = codat_python_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: API Key Auth
configuration.api_key['API Key Auth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['API Key Auth'] = 'Bearer'

# Enter a context with an instance of the API client
with codat_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = metrics_api.MetricsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.metrics_companies_get()
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
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


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

