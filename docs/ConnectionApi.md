# codat_python_sdk.ConnectionApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_company_id_connections_connection_id_delete**](ConnectionApi.md#companies_company_id_connections_connection_id_delete) | **DELETE** /companies/{companyId}/connections/{connectionId} | Disconnect and delete a data source from a company
[**companies_company_id_connections_connection_id_get**](ConnectionApi.md#companies_company_id_connections_connection_id_get) | **GET** /companies/{companyId}/connections/{connectionId} | Retrieve a single data source connected to a single company, including its connection status
[**companies_company_id_connections_connection_id_patch**](ConnectionApi.md#companies_company_id_connections_connection_id_patch) | **PATCH** /companies/{companyId}/connections/{connectionId} | Disconnect a data source from a company
[**companies_company_id_connections_get**](ConnectionApi.md#companies_company_id_connections_get) | **GET** /companies/{companyId}/connections | Retrieve all data sources connected to a single company, including their connection statuses
[**companies_company_id_connections_post**](ConnectionApi.md#companies_company_id_connections_post) | **POST** /companies/{companyId}/connections | Connect a data source to a company

# **companies_company_id_connections_connection_id_delete**
> bool companies_company_id_connections_connection_id_delete(company_id, connection_id)

Disconnect and delete a data source from a company

This revokes and removes a data connection from being listed as a company's connection(s).

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
api_instance = codat_python_sdk.ConnectionApi(codat_python_sdk.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Disconnect and delete a data source from a company
    api_response = api_instance.companies_company_id_connections_connection_id_delete(company_id, connection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionApi->companies_company_id_connections_connection_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **connection_id** | [**str**](.md)|  | 

### Return type

**bool**

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_connection_id_get**
> CodatPublicApiModelsCompanyDataConnection companies_company_id_connections_connection_id_get(company_id, connection_id)

Retrieve a single data source connected to a single company, including its connection status

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
api_instance = codat_python_sdk.ConnectionApi(codat_python_sdk.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Retrieve a single data source connected to a single company, including its connection status
    api_response = api_instance.companies_company_id_connections_connection_id_get(company_id, connection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionApi->companies_company_id_connections_connection_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **connection_id** | [**str**](.md)|  | 

### Return type

[**CodatPublicApiModelsCompanyDataConnection**](CodatPublicApiModelsCompanyDataConnection.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_connection_id_patch**
> CodatPublicApiModelsCompanyDataConnection companies_company_id_connections_connection_id_patch(company_id, connection_id, body=body)

Disconnect a data source from a company

This revokes a company’s access to a data source, but the data connection is still listed as a part of a company's  data connection(s). The status value in the request body should be \"Unlinked\" (case sensitive). Data connections  can only be unlinked if in the Linked or Deauthorized state.

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
api_instance = codat_python_sdk.ConnectionApi(codat_python_sdk.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = codat_python_sdk.CodatPublicApiModelsCompanyPatchDataConnectionModel() # CodatPublicApiModelsCompanyPatchDataConnectionModel |  (optional)

try:
    # Disconnect a data source from a company
    api_response = api_instance.companies_company_id_connections_connection_id_patch(company_id, connection_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionApi->companies_company_id_connections_connection_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **connection_id** | [**str**](.md)|  | 
 **body** | [**CodatPublicApiModelsCompanyPatchDataConnectionModel**](CodatPublicApiModelsCompanyPatchDataConnectionModel.md)|  | [optional] 

### Return type

[**CodatPublicApiModelsCompanyDataConnection**](CodatPublicApiModelsCompanyDataConnection.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_get**
> CodatPublicApiModelsCompanyDataConnectionPagedResponseModel companies_company_id_connections_get(company_id, page, page_size=page_size, query=query, order_by=order_by)

Retrieve all data sources connected to a single company, including their connection statuses

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
api_instance = codat_python_sdk.ConnectionApi(codat_python_sdk.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
page = 1 # int |  (default to 1)
page_size = 100 # int |  (optional) (default to 100)
query = 'query_example' # str |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    # Retrieve all data sources connected to a single company, including their connection statuses
    api_response = api_instance.companies_company_id_connections_get(company_id, page, page_size=page_size, query=query, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionApi->companies_company_id_connections_get: %s\n" % e)
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

[**CodatPublicApiModelsCompanyDataConnectionPagedResponseModel**](CodatPublicApiModelsCompanyDataConnectionPagedResponseModel.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_post**
> CodatPublicApiModelsCompanyDataConnection companies_company_id_connections_post(company_id, body=body)

Connect a data source to a company

This creates a new data connection in the PendingAuth state. You can get a list of data connections (platformKeys)  supported by Codat from GET /integrations.

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
api_instance = codat_python_sdk.ConnectionApi(codat_python_sdk.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = 'body_example' # str |  (optional)

try:
    # Connect a data source to a company
    api_response = api_instance.companies_company_id_connections_post(company_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionApi->companies_company_id_connections_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **body** | [**str**](str.md)|  | [optional] 

### Return type

[**CodatPublicApiModelsCompanyDataConnection**](CodatPublicApiModelsCompanyDataConnection.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

