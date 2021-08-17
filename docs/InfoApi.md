# codat_python_sdk.InfoApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_company_id_data_info_get**](InfoApi.md#companies_company_id_data_info_get) | **GET** /companies/{companyId}/data/info | Gets the latest basic info for a company.
[**companies_company_id_data_info_post**](InfoApi.md#companies_company_id_data_info_post) | **POST** /companies/{companyId}/data/info | Initiates the process of synchronising basic info for a company


# **companies_company_id_data_info_get**
> CodatDataContractsDatasetsCompanyDataset companies_company_id_data_info_get(company_id)

Gets the latest basic info for a company.

### Example

* Api Key Authentication (API Key Auth):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import info_api
from codat_python_sdk.model.codat_data_contracts_datasets_company_dataset import CodatDataContractsDatasetsCompanyDataset
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
    api_instance = info_api.InfoApi(api_client)
    company_id = "companyId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Gets the latest basic info for a company.
        api_response = api_instance.companies_company_id_data_info_get(company_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling InfoApi->companies_company_id_data_info_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |

### Return type

[**CodatDataContractsDatasetsCompanyDataset**](CodatDataContractsDatasetsCompanyDataset.md)

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

# **companies_company_id_data_info_post**
> CodatPublicApiModelsDataDataSet companies_company_id_data_info_post(company_id)

Initiates the process of synchronising basic info for a company

### Example

* Api Key Authentication (API Key Auth):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import info_api
from codat_python_sdk.model.codat_public_api_models_data_data_set import CodatPublicApiModelsDataDataSet
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
    api_instance = info_api.InfoApi(api_client)
    company_id = "companyId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Initiates the process of synchronising basic info for a company
        api_response = api_instance.companies_company_id_data_info_post(company_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling InfoApi->companies_company_id_data_info_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |

### Return type

[**CodatPublicApiModelsDataDataSet**](CodatPublicApiModelsDataDataSet.md)

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

