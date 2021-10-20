# codat_python_sdk.ConnectionApi

All URIs are relative to *http://localhost*

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

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import connection_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = codat_python_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: API Key Auth
configuration.api_key['API Key Auth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['API Key Auth'] = 'Bearer'

# Configure OAuth2 access token for authorization: Codat Login
configuration = codat_python_sdk.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with codat_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = connection_api.ConnectionApi(api_client)
    company_id = "companyId_example" # str | 
    connection_id = "connectionId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Disconnect and delete a data source from a company
        api_response = api_instance.companies_company_id_connections_connection_id_delete(company_id, connection_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling ConnectionApi->companies_company_id_connections_connection_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **connection_id** | **str**|  |

### Return type

**bool**

### Authorization

[API Key Auth](../README.md#API Key Auth), [Codat Login](../README.md#Codat Login)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_connection_id_get**
> CodatPublicApiModelsCompanyDataConnection companies_company_id_connections_connection_id_get(company_id, connection_id)

Retrieve a single data source connected to a single company, including its connection status

### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import connection_api
from codat_python_sdk.model.codat_public_api_models_company_data_connection import CodatPublicApiModelsCompanyDataConnection
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = codat_python_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: API Key Auth
configuration.api_key['API Key Auth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['API Key Auth'] = 'Bearer'

# Configure OAuth2 access token for authorization: Codat Login
configuration = codat_python_sdk.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with codat_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = connection_api.ConnectionApi(api_client)
    company_id = "companyId_example" # str | 
    connection_id = "connectionId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a single data source connected to a single company, including its connection status
        api_response = api_instance.companies_company_id_connections_connection_id_get(company_id, connection_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling ConnectionApi->companies_company_id_connections_connection_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **connection_id** | **str**|  |

### Return type

[**CodatPublicApiModelsCompanyDataConnection**](CodatPublicApiModelsCompanyDataConnection.md)

### Authorization

[API Key Auth](../README.md#API Key Auth), [Codat Login](../README.md#Codat Login)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_connection_id_patch**
> CodatPublicApiModelsCompanyDataConnection companies_company_id_connections_connection_id_patch(company_id, connection_id)

Disconnect a data source from a company

This revokes a company’s access to a data source, but the data connection is still listed as a part of a company's  data connection(s). The status value in the request body should be \"Unlinked\" (case sensitive). Data connections  can only be unlinked if in the Linked or Deauthorized state.

### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import connection_api
from codat_python_sdk.model.codat_public_api_models_company_patch_data_connection_model import CodatPublicApiModelsCompanyPatchDataConnectionModel
from codat_python_sdk.model.codat_public_api_models_company_data_connection import CodatPublicApiModelsCompanyDataConnection
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = codat_python_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: API Key Auth
configuration.api_key['API Key Auth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['API Key Auth'] = 'Bearer'

# Configure OAuth2 access token for authorization: Codat Login
configuration = codat_python_sdk.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with codat_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = connection_api.ConnectionApi(api_client)
    company_id = "companyId_example" # str | 
    connection_id = "connectionId_example" # str | 
    codat_public_api_models_company_patch_data_connection_model = CodatPublicApiModelsCompanyPatchDataConnectionModel(
        status="status_example",
    ) # CodatPublicApiModelsCompanyPatchDataConnectionModel |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Disconnect a data source from a company
        api_response = api_instance.companies_company_id_connections_connection_id_patch(company_id, connection_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling ConnectionApi->companies_company_id_connections_connection_id_patch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Disconnect a data source from a company
        api_response = api_instance.companies_company_id_connections_connection_id_patch(company_id, connection_id, codat_public_api_models_company_patch_data_connection_model=codat_public_api_models_company_patch_data_connection_model)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling ConnectionApi->companies_company_id_connections_connection_id_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **connection_id** | **str**|  |
 **codat_public_api_models_company_patch_data_connection_model** | [**CodatPublicApiModelsCompanyPatchDataConnectionModel**](CodatPublicApiModelsCompanyPatchDataConnectionModel.md)|  | [optional]

### Return type

[**CodatPublicApiModelsCompanyDataConnection**](CodatPublicApiModelsCompanyDataConnection.md)

### Authorization

[API Key Auth](../README.md#API Key Auth), [Codat Login](../README.md#Codat Login)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_get**
> CodatPublicApiModelsCompanyDataConnectionPagedResponseModel companies_company_id_connections_get(company_id, page)

Retrieve all data sources connected to a single company, including their connection statuses

### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import connection_api
from codat_python_sdk.model.codat_public_api_models_company_data_connection_paged_response_model import CodatPublicApiModelsCompanyDataConnectionPagedResponseModel
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = codat_python_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: API Key Auth
configuration.api_key['API Key Auth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['API Key Auth'] = 'Bearer'

# Configure OAuth2 access token for authorization: Codat Login
configuration = codat_python_sdk.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with codat_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = connection_api.ConnectionApi(api_client)
    company_id = "companyId_example" # str | 
    page = 1 # int | 
    page_size = 100 # int |  (optional) if omitted the server will use the default value of 100
    query = "query_example" # str |  (optional)
    order_by = "orderBy_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve all data sources connected to a single company, including their connection statuses
        api_response = api_instance.companies_company_id_connections_get(company_id, page)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling ConnectionApi->companies_company_id_connections_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve all data sources connected to a single company, including their connection statuses
        api_response = api_instance.companies_company_id_connections_get(company_id, page, page_size=page_size, query=query, order_by=order_by)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling ConnectionApi->companies_company_id_connections_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **page** | **int**|  |
 **page_size** | **int**|  | [optional] if omitted the server will use the default value of 100
 **query** | **str**|  | [optional]
 **order_by** | **str**|  | [optional]

### Return type

[**CodatPublicApiModelsCompanyDataConnectionPagedResponseModel**](CodatPublicApiModelsCompanyDataConnectionPagedResponseModel.md)

### Authorization

[API Key Auth](../README.md#API Key Auth), [Codat Login](../README.md#Codat Login)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_post**
> CodatPublicApiModelsCompanyDataConnection companies_company_id_connections_post(company_id)

Connect a data source to a company

This creates a new data connection in the PendingAuth state. You can get a list of data connections (platformKeys)  supported by Codat from GET /integrations.

### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import connection_api
from codat_python_sdk.model.codat_public_api_models_company_data_connection import CodatPublicApiModelsCompanyDataConnection
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = codat_python_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: API Key Auth
configuration.api_key['API Key Auth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['API Key Auth'] = 'Bearer'

# Configure OAuth2 access token for authorization: Codat Login
configuration = codat_python_sdk.Configuration(
    host = "http://localhost"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with codat_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = connection_api.ConnectionApi(api_client)
    company_id = "companyId_example" # str | 
    body = "body_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Connect a data source to a company
        api_response = api_instance.companies_company_id_connections_post(company_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling ConnectionApi->companies_company_id_connections_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Connect a data source to a company
        api_response = api_instance.companies_company_id_connections_post(company_id, body=body)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling ConnectionApi->companies_company_id_connections_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **body** | **str**|  | [optional]

### Return type

[**CodatPublicApiModelsCompanyDataConnection**](CodatPublicApiModelsCompanyDataConnection.md)

### Authorization

[API Key Auth](../README.md#API Key Auth), [Codat Login](../README.md#Codat Login)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

