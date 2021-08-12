# swagger_client.BillsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_company_id_connections_connection_id_data_bills_bill_id_attachments_attachment_id_download_get**](BillsApi.md#companies_company_id_connections_connection_id_data_bills_bill_id_attachments_attachment_id_download_get) | **GET** /companies/{companyId}/connections/{connectionId}/data/bills/{billId}/attachments/{attachmentId}/download | 
[**companies_company_id_connections_connection_id_data_bills_bill_id_attachments_attachment_id_get**](BillsApi.md#companies_company_id_connections_connection_id_data_bills_bill_id_attachments_attachment_id_get) | **GET** /companies/{companyId}/connections/{connectionId}/data/bills/{billId}/attachments/{attachmentId} | 
[**companies_company_id_connections_connection_id_data_bills_bill_id_attachments_get**](BillsApi.md#companies_company_id_connections_connection_id_data_bills_bill_id_attachments_get) | **GET** /companies/{companyId}/connections/{connectionId}/data/bills/{billId}/attachments | 
[**companies_company_id_connections_connection_id_push_bills_bill_id_attachments_post**](BillsApi.md#companies_company_id_connections_connection_id_push_bills_bill_id_attachments_post) | **POST** /companies/{companyId}/connections/{connectionId}/push/bills/{billId}/attachments | 
[**companies_company_id_connections_connection_id_push_bills_bill_id_put**](BillsApi.md#companies_company_id_connections_connection_id_push_bills_bill_id_put) | **PUT** /companies/{companyId}/connections/{connectionId}/push/bills/{billId} | Posts an updated bill to the accounting package for a given company.
[**companies_company_id_connections_connection_id_push_bills_post**](BillsApi.md#companies_company_id_connections_connection_id_push_bills_post) | **POST** /companies/{companyId}/connections/{connectionId}/push/bills | Posts a new bill to the accounting package for a given company.
[**companies_company_id_data_bills_bill_id_get**](BillsApi.md#companies_company_id_data_bills_bill_id_get) | **GET** /companies/{companyId}/data/bills/{billId} | 
[**companies_company_id_data_bills_get**](BillsApi.md#companies_company_id_data_bills_get) | **GET** /companies/{companyId}/data/bills | Gets the latest bills for a company, with pagination

# **companies_company_id_connections_connection_id_data_bills_bill_id_attachments_attachment_id_download_get**
> companies_company_id_connections_connection_id_data_bills_bill_id_attachments_attachment_id_download_get(company_id, connection_id, bill_id, attachment_id)



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
api_instance = swagger_client.BillsApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
bill_id = 'bill_id_example' # str | 
attachment_id = 'attachment_id_example' # str | 

try:
    api_instance.companies_company_id_connections_connection_id_data_bills_bill_id_attachments_attachment_id_download_get(company_id, connection_id, bill_id, attachment_id)
except ApiException as e:
    print("Exception when calling BillsApi->companies_company_id_connections_connection_id_data_bills_bill_id_attachments_attachment_id_download_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **connection_id** | [**str**](.md)|  | 
 **bill_id** | **str**|  | 
 **attachment_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_connection_id_data_bills_bill_id_attachments_attachment_id_get**
> CodatDataContractsDatasetsAttachmentsDatasetAttachment companies_company_id_connections_connection_id_data_bills_bill_id_attachments_attachment_id_get(company_id, connection_id, bill_id, attachment_id)



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
api_instance = swagger_client.BillsApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
bill_id = 'bill_id_example' # str | 
attachment_id = 'attachment_id_example' # str | 

try:
    api_response = api_instance.companies_company_id_connections_connection_id_data_bills_bill_id_attachments_attachment_id_get(company_id, connection_id, bill_id, attachment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillsApi->companies_company_id_connections_connection_id_data_bills_bill_id_attachments_attachment_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **connection_id** | [**str**](.md)|  | 
 **bill_id** | **str**|  | 
 **attachment_id** | **str**|  | 

### Return type

[**CodatDataContractsDatasetsAttachmentsDatasetAttachment**](CodatDataContractsDatasetsAttachmentsDatasetAttachment.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_connection_id_data_bills_bill_id_attachments_get**
> CodatDataContractsDatasetsAttachmentsDataset companies_company_id_connections_connection_id_data_bills_bill_id_attachments_get(company_id, connection_id, bill_id)



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
api_instance = swagger_client.BillsApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
bill_id = 'bill_id_example' # str | 

try:
    api_response = api_instance.companies_company_id_connections_connection_id_data_bills_bill_id_attachments_get(company_id, connection_id, bill_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillsApi->companies_company_id_connections_connection_id_data_bills_bill_id_attachments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **connection_id** | [**str**](.md)|  | 
 **bill_id** | **str**|  | 

### Return type

[**CodatDataContractsDatasetsAttachmentsDataset**](CodatDataContractsDatasetsAttachmentsDataset.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_connection_id_push_bills_bill_id_attachments_post**
> companies_company_id_connections_connection_id_push_bills_bill_id_attachments_post(company_id, connection_id, bill_id)



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
api_instance = swagger_client.BillsApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
bill_id = 'bill_id_example' # str | 

try:
    api_instance.companies_company_id_connections_connection_id_push_bills_bill_id_attachments_post(company_id, connection_id, bill_id)
except ApiException as e:
    print("Exception when calling BillsApi->companies_company_id_connections_connection_id_push_bills_bill_id_attachments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **connection_id** | [**str**](.md)|  | 
 **bill_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_connection_id_push_bills_bill_id_put**
> CodatDataContractsDatasetsBillPushOperation companies_company_id_connections_connection_id_push_bills_bill_id_put(company_id, connection_id, bill_id, body=body, timeout_in_minutes=timeout_in_minutes, force_update=force_update)

Posts an updated bill to the accounting package for a given company.

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
api_instance = swagger_client.BillsApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
bill_id = 'bill_id_example' # str | 
body = swagger_client.CodatDataContractsDatasetsBill() # CodatDataContractsDatasetsBill |  (optional)
timeout_in_minutes = 56 # int |  (optional)
force_update = false # bool |  (optional) (default to false)

try:
    # Posts an updated bill to the accounting package for a given company.
    api_response = api_instance.companies_company_id_connections_connection_id_push_bills_bill_id_put(company_id, connection_id, bill_id, body=body, timeout_in_minutes=timeout_in_minutes, force_update=force_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillsApi->companies_company_id_connections_connection_id_push_bills_bill_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **connection_id** | [**str**](.md)|  | 
 **bill_id** | **str**|  | 
 **body** | [**CodatDataContractsDatasetsBill**](CodatDataContractsDatasetsBill.md)|  | [optional] 
 **timeout_in_minutes** | **int**|  | [optional] 
 **force_update** | **bool**|  | [optional] [default to false]

### Return type

[**CodatDataContractsDatasetsBillPushOperation**](CodatDataContractsDatasetsBillPushOperation.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_connection_id_push_bills_post**
> CodatDataContractsDatasetsBillPushOperation companies_company_id_connections_connection_id_push_bills_post(company_id, connection_id, body=body, timeout_in_minutes=timeout_in_minutes)

Posts a new bill to the accounting package for a given company.

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
api_instance = swagger_client.BillsApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = swagger_client.CodatDataContractsDatasetsBill() # CodatDataContractsDatasetsBill |  (optional)
timeout_in_minutes = 56 # int |  (optional)

try:
    # Posts a new bill to the accounting package for a given company.
    api_response = api_instance.companies_company_id_connections_connection_id_push_bills_post(company_id, connection_id, body=body, timeout_in_minutes=timeout_in_minutes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillsApi->companies_company_id_connections_connection_id_push_bills_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **connection_id** | [**str**](.md)|  | 
 **body** | [**CodatDataContractsDatasetsBill**](CodatDataContractsDatasetsBill.md)|  | [optional] 
 **timeout_in_minutes** | **int**|  | [optional] 

### Return type

[**CodatDataContractsDatasetsBillPushOperation**](CodatDataContractsDatasetsBillPushOperation.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_data_bills_bill_id_get**
> CodatDataContractsDatasetsBill companies_company_id_data_bills_bill_id_get(company_id, bill_id)



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
api_instance = swagger_client.BillsApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
bill_id = 'bill_id_example' # str | 

try:
    api_response = api_instance.companies_company_id_data_bills_bill_id_get(company_id, bill_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillsApi->companies_company_id_data_bills_bill_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **bill_id** | **str**|  | 

### Return type

[**CodatDataContractsDatasetsBill**](CodatDataContractsDatasetsBill.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_data_bills_get**
> CodatDataContractsDatasetsBillPagedResponseModel companies_company_id_data_bills_get(company_id, page, page_size=page_size, query=query, order_by=order_by)

Gets the latest bills for a company, with pagination

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
api_instance = swagger_client.BillsApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
page = 1 # int |  (default to 1)
page_size = 100 # int |  (optional) (default to 100)
query = 'query_example' # str |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    # Gets the latest bills for a company, with pagination
    api_response = api_instance.companies_company_id_data_bills_get(company_id, page, page_size=page_size, query=query, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillsApi->companies_company_id_data_bills_get: %s\n" % e)
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

[**CodatDataContractsDatasetsBillPagedResponseModel**](CodatDataContractsDatasetsBillPagedResponseModel.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

