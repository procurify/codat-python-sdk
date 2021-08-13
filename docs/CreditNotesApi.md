# codat_python_sdk.CreditNotesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_company_id_connections_connection_id_push_credit_notes_credit_note_id_put**](CreditNotesApi.md#companies_company_id_connections_connection_id_push_credit_notes_credit_note_id_put) | **PUT** /companies/{companyId}/connections/{connectionId}/push/creditNotes/{creditNoteId} | Posts an updated credit note to the accounting package for a given company.
[**companies_company_id_connections_connection_id_push_credit_notes_post**](CreditNotesApi.md#companies_company_id_connections_connection_id_push_credit_notes_post) | **POST** /companies/{companyId}/connections/{connectionId}/push/creditNotes | 
[**companies_company_id_data_credit_notes_credit_note_id_get**](CreditNotesApi.md#companies_company_id_data_credit_notes_credit_note_id_get) | **GET** /companies/{companyId}/data/creditNotes/{creditNoteId} | Gets a single creditNote corresponding to the supplied Id
[**companies_company_id_data_credit_notes_get**](CreditNotesApi.md#companies_company_id_data_credit_notes_get) | **GET** /companies/{companyId}/data/creditNotes | Gets a list of all credit notes for a company, with pagination

# **companies_company_id_connections_connection_id_push_credit_notes_credit_note_id_put**
> CodatDataContractsDatasetsCreditNotePushOperation companies_company_id_connections_connection_id_push_credit_notes_credit_note_id_put(company_id, connection_id, credit_note_id, body=body, timeout_in_minutes=timeout_in_minutes, force_update=force_update)

Posts an updated credit note to the accounting package for a given company.

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
api_instance = codat_python_sdk.CreditNotesApi(codat_python_sdk.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
credit_note_id = 'credit_note_id_example' # str | 
body = codat_python_sdk.CodatDataContractsDatasetsCreditNote() # CodatDataContractsDatasetsCreditNote |  (optional)
timeout_in_minutes = 56 # int |  (optional)
force_update = false # bool |  (optional) (default to false)

try:
    # Posts an updated credit note to the accounting package for a given company.
    api_response = api_instance.companies_company_id_connections_connection_id_push_credit_notes_credit_note_id_put(company_id, connection_id, credit_note_id, body=body, timeout_in_minutes=timeout_in_minutes, force_update=force_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditNotesApi->companies_company_id_connections_connection_id_push_credit_notes_credit_note_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **connection_id** | [**str**](.md)|  | 
 **credit_note_id** | **str**|  | 
 **body** | [**CodatDataContractsDatasetsCreditNote**](CodatDataContractsDatasetsCreditNote.md)|  | [optional] 
 **timeout_in_minutes** | **int**|  | [optional] 
 **force_update** | **bool**|  | [optional] [default to false]

### Return type

[**CodatDataContractsDatasetsCreditNotePushOperation**](CodatDataContractsDatasetsCreditNotePushOperation.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_connection_id_push_credit_notes_post**
> CodatDataContractsDatasetsCreditNotePushOperation companies_company_id_connections_connection_id_push_credit_notes_post(company_id, connection_id, body=body, timeout_in_minutes=timeout_in_minutes)



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
api_instance = codat_python_sdk.CreditNotesApi(codat_python_sdk.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = codat_python_sdk.CodatDataContractsDatasetsCreditNote() # CodatDataContractsDatasetsCreditNote |  (optional)
timeout_in_minutes = 56 # int |  (optional)

try:
    api_response = api_instance.companies_company_id_connections_connection_id_push_credit_notes_post(company_id, connection_id, body=body, timeout_in_minutes=timeout_in_minutes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditNotesApi->companies_company_id_connections_connection_id_push_credit_notes_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **connection_id** | [**str**](.md)|  | 
 **body** | [**CodatDataContractsDatasetsCreditNote**](CodatDataContractsDatasetsCreditNote.md)|  | [optional] 
 **timeout_in_minutes** | **int**|  | [optional] 

### Return type

[**CodatDataContractsDatasetsCreditNotePushOperation**](CodatDataContractsDatasetsCreditNotePushOperation.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_data_credit_notes_credit_note_id_get**
> CodatDataContractsDatasetsCreditNote companies_company_id_data_credit_notes_credit_note_id_get(company_id, credit_note_id)

Gets a single creditNote corresponding to the supplied Id

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
api_instance = codat_python_sdk.CreditNotesApi(codat_python_sdk.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
credit_note_id = 'credit_note_id_example' # str | 

try:
    # Gets a single creditNote corresponding to the supplied Id
    api_response = api_instance.companies_company_id_data_credit_notes_credit_note_id_get(company_id, credit_note_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditNotesApi->companies_company_id_data_credit_notes_credit_note_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **credit_note_id** | **str**|  | 

### Return type

[**CodatDataContractsDatasetsCreditNote**](CodatDataContractsDatasetsCreditNote.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_data_credit_notes_get**
> CodatDataContractsDatasetsCreditNotePagedResponseModel companies_company_id_data_credit_notes_get(company_id, page, page_size=page_size, query=query, order_by=order_by)

Gets a list of all credit notes for a company, with pagination

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
api_instance = codat_python_sdk.CreditNotesApi(codat_python_sdk.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
page = 1 # int |  (default to 1)
page_size = 100 # int |  (optional) (default to 100)
query = 'query_example' # str |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    # Gets a list of all credit notes for a company, with pagination
    api_response = api_instance.companies_company_id_data_credit_notes_get(company_id, page, page_size=page_size, query=query, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CreditNotesApi->companies_company_id_data_credit_notes_get: %s\n" % e)
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

[**CodatDataContractsDatasetsCreditNotePagedResponseModel**](CodatDataContractsDatasetsCreditNotePagedResponseModel.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

