# swagger_client.CommerceDisputesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_company_id_connections_connection_id_data_commerce_disputes_dispute_id_get**](CommerceDisputesApi.md#companies_company_id_connections_connection_id_data_commerce_disputes_dispute_id_get) | **GET** /companies/{companyId}/connections/{connectionId}/data/commerce-disputes/{disputeId} | Gets the specified commerce dispute for a given company
[**companies_company_id_connections_connection_id_data_commerce_disputes_get**](CommerceDisputesApi.md#companies_company_id_connections_connection_id_data_commerce_disputes_get) | **GET** /companies/{companyId}/connections/{connectionId}/data/commerce-disputes | Gets the latest commerce disputes for a company, with pagination

# **companies_company_id_connections_connection_id_data_commerce_disputes_dispute_id_get**
> CodatDataContractsDatasetsCommerceDispute companies_company_id_connections_connection_id_data_commerce_disputes_dispute_id_get(company_id, connection_id, dispute_id)

Gets the specified commerce dispute for a given company

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
api_instance = swagger_client.CommerceDisputesApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
dispute_id = 'dispute_id_example' # str | 

try:
    # Gets the specified commerce dispute for a given company
    api_response = api_instance.companies_company_id_connections_connection_id_data_commerce_disputes_dispute_id_get(company_id, connection_id, dispute_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommerceDisputesApi->companies_company_id_connections_connection_id_data_commerce_disputes_dispute_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **connection_id** | [**str**](.md)|  | 
 **dispute_id** | **str**|  | 

### Return type

[**CodatDataContractsDatasetsCommerceDispute**](CodatDataContractsDatasetsCommerceDispute.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_connection_id_data_commerce_disputes_get**
> CodatDataContractsDatasetsCommerceDisputePagedResponseModel companies_company_id_connections_connection_id_data_commerce_disputes_get(company_id, connection_id, page, page_size=page_size, query=query, order_by=order_by)

Gets the latest commerce disputes for a company, with pagination

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
api_instance = swagger_client.CommerceDisputesApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
page = 1 # int |  (default to 1)
page_size = 100 # int |  (optional) (default to 100)
query = 'query_example' # str |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    # Gets the latest commerce disputes for a company, with pagination
    api_response = api_instance.companies_company_id_connections_connection_id_data_commerce_disputes_get(company_id, connection_id, page, page_size=page_size, query=query, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommerceDisputesApi->companies_company_id_connections_connection_id_data_commerce_disputes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **connection_id** | [**str**](.md)|  | 
 **page** | **int**|  | [default to 1]
 **page_size** | **int**|  | [optional] [default to 100]
 **query** | **str**|  | [optional] 
 **order_by** | **str**|  | [optional] 

### Return type

[**CodatDataContractsDatasetsCommerceDisputePagedResponseModel**](CodatDataContractsDatasetsCommerceDisputePagedResponseModel.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

