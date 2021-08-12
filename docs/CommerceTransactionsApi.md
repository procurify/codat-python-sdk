# swagger_client.CommerceTransactionsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_company_id_connections_connection_id_data_commerce_transactions_get**](CommerceTransactionsApi.md#companies_company_id_connections_connection_id_data_commerce_transactions_get) | **GET** /companies/{companyId}/connections/{connectionId}/data/commerce-transactions | Gets the latest commerce transactions for a company, with pagination
[**companies_company_id_connections_connection_id_data_commerce_transactions_transaction_id_get**](CommerceTransactionsApi.md#companies_company_id_connections_connection_id_data_commerce_transactions_transaction_id_get) | **GET** /companies/{companyId}/connections/{connectionId}/data/commerce-transactions/{transactionId} | Gets the specified commerce transaction for a given company

# **companies_company_id_connections_connection_id_data_commerce_transactions_get**
> CodatDataContractsDatasetsCommerceTransactionPagedResponseModel companies_company_id_connections_connection_id_data_commerce_transactions_get(company_id, connection_id, page, page_size=page_size, query=query, order_by=order_by)

Gets the latest commerce transactions for a company, with pagination

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
api_instance = swagger_client.CommerceTransactionsApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
page = 1 # int |  (default to 1)
page_size = 100 # int |  (optional) (default to 100)
query = 'query_example' # str |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    # Gets the latest commerce transactions for a company, with pagination
    api_response = api_instance.companies_company_id_connections_connection_id_data_commerce_transactions_get(company_id, connection_id, page, page_size=page_size, query=query, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommerceTransactionsApi->companies_company_id_connections_connection_id_data_commerce_transactions_get: %s\n" % e)
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

[**CodatDataContractsDatasetsCommerceTransactionPagedResponseModel**](CodatDataContractsDatasetsCommerceTransactionPagedResponseModel.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_connection_id_data_commerce_transactions_transaction_id_get**
> CodatDataContractsDatasetsCommerceTransaction companies_company_id_connections_connection_id_data_commerce_transactions_transaction_id_get(company_id, connection_id, transaction_id)

Gets the specified commerce transaction for a given company

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
api_instance = swagger_client.CommerceTransactionsApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
transaction_id = 'transaction_id_example' # str | 

try:
    # Gets the specified commerce transaction for a given company
    api_response = api_instance.companies_company_id_connections_connection_id_data_commerce_transactions_transaction_id_get(company_id, connection_id, transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommerceTransactionsApi->companies_company_id_connections_connection_id_data_commerce_transactions_transaction_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **connection_id** | [**str**](.md)|  | 
 **transaction_id** | **str**|  | 

### Return type

[**CodatDataContractsDatasetsCommerceTransaction**](CodatDataContractsDatasetsCommerceTransaction.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

