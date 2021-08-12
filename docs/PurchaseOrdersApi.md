# swagger_client.PurchaseOrdersApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_company_id_connections_connection_id_push_purchase_orders_post**](PurchaseOrdersApi.md#companies_company_id_connections_connection_id_push_purchase_orders_post) | **POST** /companies/{companyId}/connections/{connectionId}/push/purchaseOrders | Posts a new purchase order to the accounting package for a given company.
[**companies_company_id_connections_connection_id_push_purchase_orders_purchase_order_id_put**](PurchaseOrdersApi.md#companies_company_id_connections_connection_id_push_purchase_orders_purchase_order_id_put) | **PUT** /companies/{companyId}/connections/{connectionId}/push/purchaseOrders/{purchaseOrderId} | Posts an updated purchase order to the accounting package for a given company.
[**companies_company_id_data_purchase_orders_get**](PurchaseOrdersApi.md#companies_company_id_data_purchase_orders_get) | **GET** /companies/{companyId}/data/purchaseOrders | 
[**companies_company_id_data_purchase_orders_purchase_order_id_get**](PurchaseOrdersApi.md#companies_company_id_data_purchase_orders_purchase_order_id_get) | **GET** /companies/{companyId}/data/purchaseOrders/{purchaseOrderId} | 

# **companies_company_id_connections_connection_id_push_purchase_orders_post**
> CodatDataContractsDatasetsPurchaseOrderPushOperation companies_company_id_connections_connection_id_push_purchase_orders_post(company_id, connection_id, body=body, timeout_in_minutes=timeout_in_minutes)

Posts a new purchase order to the accounting package for a given company.

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
api_instance = swagger_client.PurchaseOrdersApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = swagger_client.CodatDataContractsDatasetsPurchaseOrder() # CodatDataContractsDatasetsPurchaseOrder |  (optional)
timeout_in_minutes = 56 # int |  (optional)

try:
    # Posts a new purchase order to the accounting package for a given company.
    api_response = api_instance.companies_company_id_connections_connection_id_push_purchase_orders_post(company_id, connection_id, body=body, timeout_in_minutes=timeout_in_minutes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PurchaseOrdersApi->companies_company_id_connections_connection_id_push_purchase_orders_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **connection_id** | [**str**](.md)|  | 
 **body** | [**CodatDataContractsDatasetsPurchaseOrder**](CodatDataContractsDatasetsPurchaseOrder.md)|  | [optional] 
 **timeout_in_minutes** | **int**|  | [optional] 

### Return type

[**CodatDataContractsDatasetsPurchaseOrderPushOperation**](CodatDataContractsDatasetsPurchaseOrderPushOperation.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_connection_id_push_purchase_orders_purchase_order_id_put**
> CodatDataContractsDatasetsPurchaseOrderPushOperation companies_company_id_connections_connection_id_push_purchase_orders_purchase_order_id_put(company_id, connection_id, purchase_order_id, body=body, timeout_in_minutes=timeout_in_minutes, force_update=force_update)

Posts an updated purchase order to the accounting package for a given company.

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
api_instance = swagger_client.PurchaseOrdersApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
purchase_order_id = 'purchase_order_id_example' # str | 
body = swagger_client.CodatDataContractsDatasetsPurchaseOrder() # CodatDataContractsDatasetsPurchaseOrder |  (optional)
timeout_in_minutes = 56 # int |  (optional)
force_update = false # bool |  (optional) (default to false)

try:
    # Posts an updated purchase order to the accounting package for a given company.
    api_response = api_instance.companies_company_id_connections_connection_id_push_purchase_orders_purchase_order_id_put(company_id, connection_id, purchase_order_id, body=body, timeout_in_minutes=timeout_in_minutes, force_update=force_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PurchaseOrdersApi->companies_company_id_connections_connection_id_push_purchase_orders_purchase_order_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **connection_id** | [**str**](.md)|  | 
 **purchase_order_id** | **str**|  | 
 **body** | [**CodatDataContractsDatasetsPurchaseOrder**](CodatDataContractsDatasetsPurchaseOrder.md)|  | [optional] 
 **timeout_in_minutes** | **int**|  | [optional] 
 **force_update** | **bool**|  | [optional] [default to false]

### Return type

[**CodatDataContractsDatasetsPurchaseOrderPushOperation**](CodatDataContractsDatasetsPurchaseOrderPushOperation.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_data_purchase_orders_get**
> CodatDataContractsDatasetsPurchaseOrderPagedResponseModel companies_company_id_data_purchase_orders_get(company_id, page, page_size=page_size, query=query, order_by=order_by)



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
api_instance = swagger_client.PurchaseOrdersApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
page = 1 # int |  (default to 1)
page_size = 100 # int |  (optional) (default to 100)
query = 'query_example' # str |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    api_response = api_instance.companies_company_id_data_purchase_orders_get(company_id, page, page_size=page_size, query=query, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PurchaseOrdersApi->companies_company_id_data_purchase_orders_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **page** | **int**|  | [default to 1]
 **page_size** | **int**|  | [optional] [default to 100]
 **query** | **str**|  | [optional] 
 **order_by** | **str**|  | [optional] 

### Return type

[**CodatDataContractsDatasetsPurchaseOrderPagedResponseModel**](CodatDataContractsDatasetsPurchaseOrderPagedResponseModel.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_data_purchase_orders_purchase_order_id_get**
> CodatDataContractsDatasetsPurchaseOrder companies_company_id_data_purchase_orders_purchase_order_id_get(company_id, purchase_order_id)



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
api_instance = swagger_client.PurchaseOrdersApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
purchase_order_id = 'purchase_order_id_example' # str | 

try:
    api_response = api_instance.companies_company_id_data_purchase_orders_purchase_order_id_get(company_id, purchase_order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PurchaseOrdersApi->companies_company_id_data_purchase_orders_purchase_order_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **purchase_order_id** | **str**|  | 

### Return type

[**CodatDataContractsDatasetsPurchaseOrder**](CodatDataContractsDatasetsPurchaseOrder.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

