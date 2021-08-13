# codat_python_sdk.CommerceOrdersApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_company_id_connections_connection_id_data_commerce_orders_get**](CommerceOrdersApi.md#companies_company_id_connections_connection_id_data_commerce_orders_get) | **GET** /companies/{companyId}/connections/{connectionId}/data/commerce-orders | Gets the latest commerce orders for a company, with pagination
[**companies_company_id_connections_connection_id_data_commerce_orders_order_id_get**](CommerceOrdersApi.md#companies_company_id_connections_connection_id_data_commerce_orders_order_id_get) | **GET** /companies/{companyId}/connections/{connectionId}/data/commerce-orders/{orderId} | Gets the specified commerce order for a given company

# **companies_company_id_connections_connection_id_data_commerce_orders_get**
> CodatDataContractsDatasetsCommerceOrderPagedResponseModel companies_company_id_connections_connection_id_data_commerce_orders_get(company_id, connection_id, page, page_size=page_size, query=query, order_by=order_by)

Gets the latest commerce orders for a company, with pagination

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
api_instance = codat_python_sdk.CommerceOrdersApi(codat_python_sdk.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
page = 1 # int |  (default to 1)
page_size = 100 # int |  (optional) (default to 100)
query = 'query_example' # str |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    # Gets the latest commerce orders for a company, with pagination
    api_response = api_instance.companies_company_id_connections_connection_id_data_commerce_orders_get(company_id, connection_id, page, page_size=page_size, query=query, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommerceOrdersApi->companies_company_id_connections_connection_id_data_commerce_orders_get: %s\n" % e)
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

[**CodatDataContractsDatasetsCommerceOrderPagedResponseModel**](CodatDataContractsDatasetsCommerceOrderPagedResponseModel.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_connection_id_data_commerce_orders_order_id_get**
> CodatDataContractsDatasetsCommerceOrder companies_company_id_connections_connection_id_data_commerce_orders_order_id_get(company_id, connection_id, order_id)

Gets the specified commerce order for a given company

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
api_instance = codat_python_sdk.CommerceOrdersApi(codat_python_sdk.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
order_id = 'order_id_example' # str | 

try:
    # Gets the specified commerce order for a given company
    api_response = api_instance.companies_company_id_connections_connection_id_data_commerce_orders_order_id_get(company_id, connection_id, order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommerceOrdersApi->companies_company_id_connections_connection_id_data_commerce_orders_order_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **connection_id** | [**str**](.md)|  | 
 **order_id** | **str**|  | 

### Return type

[**CodatDataContractsDatasetsCommerceOrder**](CodatDataContractsDatasetsCommerceOrder.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

