# codat_python_sdk.CommerceInfoApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_company_id_connections_connection_id_data_commerce_info_get**](CommerceInfoApi.md#companies_company_id_connections_connection_id_data_commerce_info_get) | **GET** /companies/{companyId}/connections/{connectionId}/data/commerce-info | Gets the latest basic info for a commerce company.

# **companies_company_id_connections_connection_id_data_commerce_info_get**
> CodatDataContractsDatasetsCommerceCompanyInfo companies_company_id_connections_connection_id_data_commerce_info_get(company_id, connection_id)

Gets the latest basic info for a commerce company.

### Example
```python
from __future__ import print_function
import time
import codat_python_sdk
from codat_python_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: API Key Auth
configuration = codat_python_sdk.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = codat_python_sdk.CommerceInfoApi(codat_python_sdk.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Gets the latest basic info for a commerce company.
    api_response = api_instance.companies_company_id_connections_connection_id_data_commerce_info_get(company_id, connection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommerceInfoApi->companies_company_id_connections_connection_id_data_commerce_info_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **connection_id** | [**str**](.md)|  | 

### Return type

[**CodatDataContractsDatasetsCommerceCompanyInfo**](CodatDataContractsDatasetsCommerceCompanyInfo.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

