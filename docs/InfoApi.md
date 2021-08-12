# swagger_client.InfoApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_company_id_data_info_get**](InfoApi.md#companies_company_id_data_info_get) | **GET** /companies/{companyId}/data/info | Gets the latest basic info for a company.
[**companies_company_id_data_info_post**](InfoApi.md#companies_company_id_data_info_post) | **POST** /companies/{companyId}/data/info | Initiates the process of synchronising basic info for a company

# **companies_company_id_data_info_get**
> CodatDataContractsDatasetsCompanyDataset companies_company_id_data_info_get(company_id)

Gets the latest basic info for a company.

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
api_instance = swagger_client.InfoApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Gets the latest basic info for a company.
    api_response = api_instance.companies_company_id_data_info_get(company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->companies_company_id_data_info_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 

### Return type

[**CodatDataContractsDatasetsCompanyDataset**](CodatDataContractsDatasetsCompanyDataset.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_data_info_post**
> CodatPublicApiModelsDataDataSet companies_company_id_data_info_post(company_id)

Initiates the process of synchronising basic info for a company

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
api_instance = swagger_client.InfoApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Initiates the process of synchronising basic info for a company
    api_response = api_instance.companies_company_id_data_info_post(company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InfoApi->companies_company_id_data_info_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 

### Return type

[**CodatPublicApiModelsDataDataSet**](CodatPublicApiModelsDataDataSet.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

