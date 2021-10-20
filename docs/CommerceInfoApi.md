# codat_python_sdk.CommerceInfoApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_company_id_connections_connection_id_data_commerce_info_get**](CommerceInfoApi.md#companies_company_id_connections_connection_id_data_commerce_info_get) | **GET** /companies/{companyId}/connections/{connectionId}/data/commerce-info | Gets the latest basic info for a commerce company.


# **companies_company_id_connections_connection_id_data_commerce_info_get**
> CodatDataContractsDatasetsCommerceCompanyInfo companies_company_id_connections_connection_id_data_commerce_info_get(company_id, connection_id)

Gets the latest basic info for a commerce company.

### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import commerce_info_api
from codat_python_sdk.model.codat_data_contracts_datasets_commerce_company_info import CodatDataContractsDatasetsCommerceCompanyInfo
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

# Configure OAuth2 access token for authorization: Codat Login
configuration = codat_python_sdk.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with codat_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = commerce_info_api.CommerceInfoApi(api_client)
    company_id = "companyId_example" # str | 
    connection_id = "connectionId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Gets the latest basic info for a commerce company.
        api_response = api_instance.companies_company_id_connections_connection_id_data_commerce_info_get(company_id, connection_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling CommerceInfoApi->companies_company_id_connections_connection_id_data_commerce_info_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **connection_id** | **str**|  |

### Return type

[**CodatDataContractsDatasetsCommerceCompanyInfo**](CodatDataContractsDatasetsCommerceCompanyInfo.md)

### Authorization

[API Key Auth](../README.md#API Key Auth), [Codat Login](../README.md#Codat Login)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

