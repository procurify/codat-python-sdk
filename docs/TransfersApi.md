# swagger_client.TransfersApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_company_id_connections_connection_id_data_transfers_get**](TransfersApi.md#companies_company_id_connections_connection_id_data_transfers_get) | **GET** /companies/{companyId}/connections/{connectionId}/data/transfers | Gets the transfers for a given company.
[**companies_company_id_connections_connection_id_data_transfers_transfer_id_get**](TransfersApi.md#companies_company_id_connections_connection_id_data_transfers_transfer_id_get) | **GET** /companies/{companyId}/connections/{connectionId}/data/transfers/{transferId} | Gets the specified transfer for a given company.
[**companies_company_id_connections_connection_id_push_transfers_post**](TransfersApi.md#companies_company_id_connections_connection_id_push_transfers_post) | **POST** /companies/{companyId}/connections/{connectionId}/push/transfers | Posts a new transfer to the accounting package for a given company.

# **companies_company_id_connections_connection_id_data_transfers_get**
> CodatDataContractsDatasetsTransferPagedResponseModel companies_company_id_connections_connection_id_data_transfers_get(company_id, connection_id, page, page_size=page_size, query=query, order_by=order_by)

Gets the transfers for a given company.

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
api_instance = swagger_client.TransfersApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
page = 1 # int |  (default to 1)
page_size = 100 # int |  (optional) (default to 100)
query = 'query_example' # str |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    # Gets the transfers for a given company.
    api_response = api_instance.companies_company_id_connections_connection_id_data_transfers_get(company_id, connection_id, page, page_size=page_size, query=query, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransfersApi->companies_company_id_connections_connection_id_data_transfers_get: %s\n" % e)
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

[**CodatDataContractsDatasetsTransferPagedResponseModel**](CodatDataContractsDatasetsTransferPagedResponseModel.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_connection_id_data_transfers_transfer_id_get**
> CodatDataContractsDatasetsTransfer companies_company_id_connections_connection_id_data_transfers_transfer_id_get(company_id, connection_id, transfer_id)

Gets the specified transfer for a given company.

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
api_instance = swagger_client.TransfersApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
transfer_id = 'transfer_id_example' # str | 

try:
    # Gets the specified transfer for a given company.
    api_response = api_instance.companies_company_id_connections_connection_id_data_transfers_transfer_id_get(company_id, connection_id, transfer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransfersApi->companies_company_id_connections_connection_id_data_transfers_transfer_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **connection_id** | [**str**](.md)|  | 
 **transfer_id** | **str**|  | 

### Return type

[**CodatDataContractsDatasetsTransfer**](CodatDataContractsDatasetsTransfer.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_connection_id_push_transfers_post**
> CodatDataContractsDatasetsTransferPushOperation companies_company_id_connections_connection_id_push_transfers_post(company_id, connection_id, body=body, timeout_in_minutes=timeout_in_minutes)

Posts a new transfer to the accounting package for a given company.

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
api_instance = swagger_client.TransfersApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = swagger_client.CodatDataContractsDatasetsTransfer() # CodatDataContractsDatasetsTransfer |  (optional)
timeout_in_minutes = 56 # int |  (optional)

try:
    # Posts a new transfer to the accounting package for a given company.
    api_response = api_instance.companies_company_id_connections_connection_id_push_transfers_post(company_id, connection_id, body=body, timeout_in_minutes=timeout_in_minutes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransfersApi->companies_company_id_connections_connection_id_push_transfers_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **connection_id** | [**str**](.md)|  | 
 **body** | [**CodatDataContractsDatasetsTransfer**](CodatDataContractsDatasetsTransfer.md)|  | [optional] 
 **timeout_in_minutes** | **int**|  | [optional] 

### Return type

[**CodatDataContractsDatasetsTransferPushOperation**](CodatDataContractsDatasetsTransferPushOperation.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

