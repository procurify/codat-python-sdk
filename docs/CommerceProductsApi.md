# swagger_client.CommerceProductsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_company_id_connections_connection_id_data_commerce_products_get**](CommerceProductsApi.md#companies_company_id_connections_connection_id_data_commerce_products_get) | **GET** /companies/{companyId}/connections/{connectionId}/data/commerce-products | Gets the latest commerce products for a company, with pagination
[**companies_company_id_connections_connection_id_data_commerce_products_product_id_get**](CommerceProductsApi.md#companies_company_id_connections_connection_id_data_commerce_products_product_id_get) | **GET** /companies/{companyId}/connections/{connectionId}/data/commerce-products/{productId} | Gets the specified commerce product for a given company

# **companies_company_id_connections_connection_id_data_commerce_products_get**
> CodatDataContractsDatasetsCommerceProductPagedResponseModel companies_company_id_connections_connection_id_data_commerce_products_get(company_id, connection_id, page, page_size=page_size, query=query, order_by=order_by)

Gets the latest commerce products for a company, with pagination

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
api_instance = swagger_client.CommerceProductsApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
page = 1 # int |  (default to 1)
page_size = 100 # int |  (optional) (default to 100)
query = 'query_example' # str |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    # Gets the latest commerce products for a company, with pagination
    api_response = api_instance.companies_company_id_connections_connection_id_data_commerce_products_get(company_id, connection_id, page, page_size=page_size, query=query, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommerceProductsApi->companies_company_id_connections_connection_id_data_commerce_products_get: %s\n" % e)
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

[**CodatDataContractsDatasetsCommerceProductPagedResponseModel**](CodatDataContractsDatasetsCommerceProductPagedResponseModel.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_connection_id_data_commerce_products_product_id_get**
> CodatDataContractsDatasetsCommerceProduct companies_company_id_connections_connection_id_data_commerce_products_product_id_get(company_id, connection_id, product_id)

Gets the specified commerce product for a given company

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
api_instance = swagger_client.CommerceProductsApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
product_id = 'product_id_example' # str | 

try:
    # Gets the specified commerce product for a given company
    api_response = api_instance.companies_company_id_connections_connection_id_data_commerce_products_product_id_get(company_id, connection_id, product_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommerceProductsApi->companies_company_id_connections_connection_id_data_commerce_products_product_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **connection_id** | [**str**](.md)|  | 
 **product_id** | **str**|  | 

### Return type

[**CodatDataContractsDatasetsCommerceProduct**](CodatDataContractsDatasetsCommerceProduct.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

