# codat_python_sdk.SuppliersApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_attachment_id_download_get**](SuppliersApi.md#companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_attachment_id_download_get) | **GET** /companies/{companyId}/connections/{connectionId}/data/suppliers/{supplierId}/attachments/{attachmentId}/download | 
[**companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_attachment_id_get**](SuppliersApi.md#companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_attachment_id_get) | **GET** /companies/{companyId}/connections/{connectionId}/data/suppliers/{supplierId}/attachments/{attachmentId} | 
[**companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_get**](SuppliersApi.md#companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_get) | **GET** /companies/{companyId}/connections/{connectionId}/data/suppliers/{supplierId}/attachments | 
[**companies_company_id_connections_connection_id_push_suppliers_post**](SuppliersApi.md#companies_company_id_connections_connection_id_push_suppliers_post) | **POST** /companies/{companyId}/connections/{connectionId}/push/suppliers | 
[**companies_company_id_data_suppliers_get**](SuppliersApi.md#companies_company_id_data_suppliers_get) | **GET** /companies/{companyId}/data/suppliers | Gets the latest suppliers for a company, with pagination
[**companies_company_id_data_suppliers_supplier_id_get**](SuppliersApi.md#companies_company_id_data_suppliers_supplier_id_get) | **GET** /companies/{companyId}/data/suppliers/{supplierId} | Gets a single supplier corresponding to the supplied Id

# **companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_attachment_id_download_get**
> companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_attachment_id_download_get(company_id, connection_id, supplier_id, attachment_id)



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
api_instance = codat_python_sdk.SuppliersApi(codat_python_sdk.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
supplier_id = 'supplier_id_example' # str | 
attachment_id = 'attachment_id_example' # str | 

try:
    api_instance.companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_attachment_id_download_get(company_id, connection_id, supplier_id, attachment_id)
except ApiException as e:
    print("Exception when calling SuppliersApi->companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_attachment_id_download_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **connection_id** | [**str**](.md)|  | 
 **supplier_id** | **str**|  | 
 **attachment_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_attachment_id_get**
> CodatDataContractsDatasetsAttachmentsDatasetAttachment companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_attachment_id_get(company_id, connection_id, supplier_id, attachment_id)



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
api_instance = codat_python_sdk.SuppliersApi(codat_python_sdk.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
supplier_id = 'supplier_id_example' # str | 
attachment_id = 'attachment_id_example' # str | 

try:
    api_response = api_instance.companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_attachment_id_get(company_id, connection_id, supplier_id, attachment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SuppliersApi->companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_attachment_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **connection_id** | [**str**](.md)|  | 
 **supplier_id** | **str**|  | 
 **attachment_id** | **str**|  | 

### Return type

[**CodatDataContractsDatasetsAttachmentsDatasetAttachment**](CodatDataContractsDatasetsAttachmentsDatasetAttachment.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_get**
> CodatDataContractsDatasetsAttachmentsDataset companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_get(company_id, connection_id, supplier_id)



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
api_instance = codat_python_sdk.SuppliersApi(codat_python_sdk.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
supplier_id = 'supplier_id_example' # str | 

try:
    api_response = api_instance.companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_get(company_id, connection_id, supplier_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SuppliersApi->companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **connection_id** | [**str**](.md)|  | 
 **supplier_id** | **str**|  | 

### Return type

[**CodatDataContractsDatasetsAttachmentsDataset**](CodatDataContractsDatasetsAttachmentsDataset.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_connection_id_push_suppliers_post**
> CodatDataContractsDatasetsSupplierPushOperation companies_company_id_connections_connection_id_push_suppliers_post(company_id, connection_id, body=body, timeout_in_minutes=timeout_in_minutes)



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
api_instance = codat_python_sdk.SuppliersApi(codat_python_sdk.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = codat_python_sdk.CodatDataContractsDatasetsSupplier() # CodatDataContractsDatasetsSupplier |  (optional)
timeout_in_minutes = 56 # int |  (optional)

try:
    api_response = api_instance.companies_company_id_connections_connection_id_push_suppliers_post(company_id, connection_id, body=body, timeout_in_minutes=timeout_in_minutes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SuppliersApi->companies_company_id_connections_connection_id_push_suppliers_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **connection_id** | [**str**](.md)|  | 
 **body** | [**CodatDataContractsDatasetsSupplier**](CodatDataContractsDatasetsSupplier.md)|  | [optional] 
 **timeout_in_minutes** | **int**|  | [optional] 

### Return type

[**CodatDataContractsDatasetsSupplierPushOperation**](CodatDataContractsDatasetsSupplierPushOperation.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_data_suppliers_get**
> CodatDataContractsDatasetsSupplierPagedResponseModel companies_company_id_data_suppliers_get(company_id, page, page_size=page_size, query=query, order_by=order_by)

Gets the latest suppliers for a company, with pagination

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
api_instance = codat_python_sdk.SuppliersApi(codat_python_sdk.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
page = 1 # int |  (default to 1)
page_size = 100 # int |  (optional) (default to 100)
query = 'query_example' # str |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    # Gets the latest suppliers for a company, with pagination
    api_response = api_instance.companies_company_id_data_suppliers_get(company_id, page, page_size=page_size, query=query, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SuppliersApi->companies_company_id_data_suppliers_get: %s\n" % e)
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

[**CodatDataContractsDatasetsSupplierPagedResponseModel**](CodatDataContractsDatasetsSupplierPagedResponseModel.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_data_suppliers_supplier_id_get**
> CodatDataContractsDatasetsSupplier companies_company_id_data_suppliers_supplier_id_get(company_id, supplier_id)

Gets a single supplier corresponding to the supplied Id

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
api_instance = codat_python_sdk.SuppliersApi(codat_python_sdk.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
supplier_id = 'supplier_id_example' # str | 

try:
    # Gets a single supplier corresponding to the supplied Id
    api_response = api_instance.companies_company_id_data_suppliers_supplier_id_get(company_id, supplier_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SuppliersApi->companies_company_id_data_suppliers_supplier_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **supplier_id** | **str**|  | 

### Return type

[**CodatDataContractsDatasetsSupplier**](CodatDataContractsDatasetsSupplier.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

