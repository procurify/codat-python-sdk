# swagger_client.InvoicesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_company_id_connections_connection_id_data_invoices_invoice_id_attachments_attachment_id_download_get**](InvoicesApi.md#companies_company_id_connections_connection_id_data_invoices_invoice_id_attachments_attachment_id_download_get) | **GET** /companies/{companyId}/connections/{connectionId}/data/invoices/{invoiceId}/attachments/{attachmentId}/download | 
[**companies_company_id_connections_connection_id_data_invoices_invoice_id_attachments_attachment_id_get**](InvoicesApi.md#companies_company_id_connections_connection_id_data_invoices_invoice_id_attachments_attachment_id_get) | **GET** /companies/{companyId}/connections/{connectionId}/data/invoices/{invoiceId}/attachments/{attachmentId} | 
[**companies_company_id_connections_connection_id_data_invoices_invoice_id_attachments_get**](InvoicesApi.md#companies_company_id_connections_connection_id_data_invoices_invoice_id_attachments_get) | **GET** /companies/{companyId}/connections/{connectionId}/data/invoices/{invoiceId}/attachments | 
[**companies_company_id_connections_connection_id_push_invoices_invoice_id_attachment_post**](InvoicesApi.md#companies_company_id_connections_connection_id_push_invoices_invoice_id_attachment_post) | **POST** /companies/{companyId}/connections/{connectionId}/push/invoices/{invoiceId}/attachment | 
[**companies_company_id_connections_connection_id_push_invoices_invoice_id_put**](InvoicesApi.md#companies_company_id_connections_connection_id_push_invoices_invoice_id_put) | **PUT** /companies/{companyId}/connections/{connectionId}/push/invoices/{invoiceId} | Posts an updated invoice to the accounting package for a given company.
[**companies_company_id_connections_connection_id_push_invoices_post**](InvoicesApi.md#companies_company_id_connections_connection_id_push_invoices_post) | **POST** /companies/{companyId}/connections/{connectionId}/push/invoices | Posts a new invoice to the accounting package for a given company.
[**companies_company_id_data_invoices_get**](InvoicesApi.md#companies_company_id_data_invoices_get) | **GET** /companies/{companyId}/data/invoices | Gets the latest invoices for a company, with pagination
[**companies_company_id_data_invoices_invoice_id_get**](InvoicesApi.md#companies_company_id_data_invoices_invoice_id_get) | **GET** /companies/{companyId}/data/invoices/{invoiceId} | 
[**companies_company_id_data_invoices_invoice_id_pdf_get**](InvoicesApi.md#companies_company_id_data_invoices_invoice_id_pdf_get) | **GET** /companies/{companyId}/data/invoices/{invoiceId}/pdf | 

# **companies_company_id_connections_connection_id_data_invoices_invoice_id_attachments_attachment_id_download_get**
> companies_company_id_connections_connection_id_data_invoices_invoice_id_attachments_attachment_id_download_get(company_id, connection_id, invoice_id, attachment_id)



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
api_instance = swagger_client.InvoicesApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
invoice_id = 'invoice_id_example' # str | 
attachment_id = 'attachment_id_example' # str | 

try:
    api_instance.companies_company_id_connections_connection_id_data_invoices_invoice_id_attachments_attachment_id_download_get(company_id, connection_id, invoice_id, attachment_id)
except ApiException as e:
    print("Exception when calling InvoicesApi->companies_company_id_connections_connection_id_data_invoices_invoice_id_attachments_attachment_id_download_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **connection_id** | [**str**](.md)|  | 
 **invoice_id** | **str**|  | 
 **attachment_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_connection_id_data_invoices_invoice_id_attachments_attachment_id_get**
> CodatDataContractsDatasetsAttachmentsDatasetAttachment companies_company_id_connections_connection_id_data_invoices_invoice_id_attachments_attachment_id_get(company_id, connection_id, invoice_id, attachment_id)



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
api_instance = swagger_client.InvoicesApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
invoice_id = 'invoice_id_example' # str | 
attachment_id = 'attachment_id_example' # str | 

try:
    api_response = api_instance.companies_company_id_connections_connection_id_data_invoices_invoice_id_attachments_attachment_id_get(company_id, connection_id, invoice_id, attachment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->companies_company_id_connections_connection_id_data_invoices_invoice_id_attachments_attachment_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **connection_id** | [**str**](.md)|  | 
 **invoice_id** | **str**|  | 
 **attachment_id** | **str**|  | 

### Return type

[**CodatDataContractsDatasetsAttachmentsDatasetAttachment**](CodatDataContractsDatasetsAttachmentsDatasetAttachment.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_connection_id_data_invoices_invoice_id_attachments_get**
> CodatDataContractsDatasetsAttachmentsDataset companies_company_id_connections_connection_id_data_invoices_invoice_id_attachments_get(company_id, connection_id, invoice_id)



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
api_instance = swagger_client.InvoicesApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
invoice_id = 'invoice_id_example' # str | 

try:
    api_response = api_instance.companies_company_id_connections_connection_id_data_invoices_invoice_id_attachments_get(company_id, connection_id, invoice_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->companies_company_id_connections_connection_id_data_invoices_invoice_id_attachments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **connection_id** | [**str**](.md)|  | 
 **invoice_id** | **str**|  | 

### Return type

[**CodatDataContractsDatasetsAttachmentsDataset**](CodatDataContractsDatasetsAttachmentsDataset.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_connection_id_push_invoices_invoice_id_attachment_post**
> companies_company_id_connections_connection_id_push_invoices_invoice_id_attachment_post(company_id, connection_id, invoice_id)



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
api_instance = swagger_client.InvoicesApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
invoice_id = 'invoice_id_example' # str | 

try:
    api_instance.companies_company_id_connections_connection_id_push_invoices_invoice_id_attachment_post(company_id, connection_id, invoice_id)
except ApiException as e:
    print("Exception when calling InvoicesApi->companies_company_id_connections_connection_id_push_invoices_invoice_id_attachment_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **connection_id** | [**str**](.md)|  | 
 **invoice_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_connection_id_push_invoices_invoice_id_put**
> CodatDataContractsDatasetsInvoicePushOperation companies_company_id_connections_connection_id_push_invoices_invoice_id_put(company_id, connection_id, invoice_id, body=body, timeout_in_minutes=timeout_in_minutes, force_update=force_update)

Posts an updated invoice to the accounting package for a given company.

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
api_instance = swagger_client.InvoicesApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
invoice_id = 'invoice_id_example' # str | 
body = swagger_client.CodatDataContractsDatasetsInvoice() # CodatDataContractsDatasetsInvoice |  (optional)
timeout_in_minutes = 56 # int |  (optional)
force_update = false # bool |  (optional) (default to false)

try:
    # Posts an updated invoice to the accounting package for a given company.
    api_response = api_instance.companies_company_id_connections_connection_id_push_invoices_invoice_id_put(company_id, connection_id, invoice_id, body=body, timeout_in_minutes=timeout_in_minutes, force_update=force_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->companies_company_id_connections_connection_id_push_invoices_invoice_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **connection_id** | [**str**](.md)|  | 
 **invoice_id** | **str**|  | 
 **body** | [**CodatDataContractsDatasetsInvoice**](CodatDataContractsDatasetsInvoice.md)|  | [optional] 
 **timeout_in_minutes** | **int**|  | [optional] 
 **force_update** | **bool**|  | [optional] [default to false]

### Return type

[**CodatDataContractsDatasetsInvoicePushOperation**](CodatDataContractsDatasetsInvoicePushOperation.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_connection_id_push_invoices_post**
> CodatDataContractsDatasetsInvoicePushOperation companies_company_id_connections_connection_id_push_invoices_post(company_id, connection_id, body=body, timeout_in_minutes=timeout_in_minutes)

Posts a new invoice to the accounting package for a given company.

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
api_instance = swagger_client.InvoicesApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = swagger_client.CodatDataContractsDatasetsInvoice() # CodatDataContractsDatasetsInvoice |  (optional)
timeout_in_minutes = 56 # int |  (optional)

try:
    # Posts a new invoice to the accounting package for a given company.
    api_response = api_instance.companies_company_id_connections_connection_id_push_invoices_post(company_id, connection_id, body=body, timeout_in_minutes=timeout_in_minutes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->companies_company_id_connections_connection_id_push_invoices_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **connection_id** | [**str**](.md)|  | 
 **body** | [**CodatDataContractsDatasetsInvoice**](CodatDataContractsDatasetsInvoice.md)|  | [optional] 
 **timeout_in_minutes** | **int**|  | [optional] 

### Return type

[**CodatDataContractsDatasetsInvoicePushOperation**](CodatDataContractsDatasetsInvoicePushOperation.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_data_invoices_get**
> CodatDataContractsDatasetsInvoicePagedResponseModel companies_company_id_data_invoices_get(company_id, page, page_size=page_size, query=query, order_by=order_by)

Gets the latest invoices for a company, with pagination

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
api_instance = swagger_client.InvoicesApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
page = 1 # int |  (default to 1)
page_size = 100 # int |  (optional) (default to 100)
query = 'query_example' # str |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    # Gets the latest invoices for a company, with pagination
    api_response = api_instance.companies_company_id_data_invoices_get(company_id, page, page_size=page_size, query=query, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->companies_company_id_data_invoices_get: %s\n" % e)
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

[**CodatDataContractsDatasetsInvoicePagedResponseModel**](CodatDataContractsDatasetsInvoicePagedResponseModel.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_data_invoices_invoice_id_get**
> CodatDataContractsDatasetsInvoice companies_company_id_data_invoices_invoice_id_get(company_id, invoice_id)



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
api_instance = swagger_client.InvoicesApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
invoice_id = 'invoice_id_example' # str | 

try:
    api_response = api_instance.companies_company_id_data_invoices_invoice_id_get(company_id, invoice_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->companies_company_id_data_invoices_invoice_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **invoice_id** | **str**|  | 

### Return type

[**CodatDataContractsDatasetsInvoice**](CodatDataContractsDatasetsInvoice.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_data_invoices_invoice_id_pdf_get**
> companies_company_id_data_invoices_invoice_id_pdf_get(company_id, invoice_id)



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
api_instance = swagger_client.InvoicesApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
invoice_id = 'invoice_id_example' # str | 

try:
    api_instance.companies_company_id_data_invoices_invoice_id_pdf_get(company_id, invoice_id)
except ApiException as e:
    print("Exception when calling InvoicesApi->companies_company_id_data_invoices_invoice_id_pdf_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **invoice_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

