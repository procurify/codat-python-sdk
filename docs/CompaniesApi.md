# codat_python_sdk.CompaniesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_company_id_delete**](CompaniesApi.md#companies_company_id_delete) | **DELETE** /companies/{companyId} | Deletes a company, this is not reversible.
[**companies_company_id_get**](CompaniesApi.md#companies_company_id_get) | **GET** /companies/{companyId} | Fetch metadata on a single company.
[**companies_company_id_put**](CompaniesApi.md#companies_company_id_put) | **PUT** /companies/{companyId} | Update a company with a new name
[**companies_company_id_settings_get**](CompaniesApi.md#companies_company_id_settings_get) | **GET** /companies/{companyId}/settings | Fetch settings on a single company.
[**companies_company_id_settings_put**](CompaniesApi.md#companies_company_id_settings_put) | **PUT** /companies/{companyId}/settings | Update settings on a single company.
[**companies_company_id_sync_settings_get**](CompaniesApi.md#companies_company_id_sync_settings_get) | **GET** /companies/{companyId}/syncSettings | 
[**companies_company_id_sync_settings_post**](CompaniesApi.md#companies_company_id_sync_settings_post) | **POST** /companies/{companyId}/syncSettings | 
[**companies_get**](CompaniesApi.md#companies_get) | **GET** /companies | Fetch a list of all companies metadata with accounting links on the Codat platform
[**companies_post**](CompaniesApi.md#companies_post) | **POST** /companies | Initiate the process of onboarding a new company on the Codat platform


# **companies_company_id_delete**
> companies_company_id_delete(company_id)

Deletes a company, this is not reversible.

### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import companies_api
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
    api_instance = companies_api.CompaniesApi(api_client)
    company_id = "companyId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Deletes a company, this is not reversible.
        api_instance.companies_company_id_delete(company_id)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling CompaniesApi->companies_company_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |

### Return type

void (empty response body)

### Authorization

[API Key Auth](../README.md#API Key Auth), [Codat Login](../README.md#Codat Login)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_get**
> CodatPublicApiModelsCompanyCompany companies_company_id_get(company_id)

Fetch metadata on a single company.

### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import companies_api
from codat_python_sdk.model.codat_public_api_models_company_company import CodatPublicApiModelsCompanyCompany
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
    api_instance = companies_api.CompaniesApi(api_client)
    company_id = "companyId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch metadata on a single company.
        api_response = api_instance.companies_company_id_get(company_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling CompaniesApi->companies_company_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |

### Return type

[**CodatPublicApiModelsCompanyCompany**](CodatPublicApiModelsCompanyCompany.md)

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

# **companies_company_id_put**
> CodatPublicApiModelsCompanyCompany companies_company_id_put(company_id)

Update a company with a new name

### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import companies_api
from codat_python_sdk.model.codat_public_api_models_company_company import CodatPublicApiModelsCompanyCompany
from codat_python_sdk.model.codat_clients_api_client_contract_company import CodatClientsApiClientContractCompany
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
    api_instance = companies_api.CompaniesApi(api_client)
    company_id = "companyId_example" # str | 
    codat_clients_api_client_contract_company = CodatClientsApiClientContractCompany(
        id="id_example",
        client_id="client_id_example",
        client_name="client_name_example",
        name="name_example",
        last_sync=dateutil_parser('1970-01-01T00:00:00.00Z'),
        data_connections=[
            CodatClientsApiClientContractDataConnection(
                id="id_example",
                company_id="company_id_example",
                client_id="client_id_example",
                status="status_example",
                supported_data_path=CodatClientsApiClientContractSupportedDataPath(
                    supported_data_path_id=1,
                    supported_data_path_name="supported_data_path_name_example",
                    source_guid="source_guid_example",
                    source_name="source_name_example",
                    source_type="source_type_example",
                    source_display_name="source_display_name_example",
                    integration_guid="integration_guid_example",
                    integration_name="integration_name_example",
                    is_offline_connector=True,
                    service_ref="service_ref_example",
                    requires_credentials=True,
                    integration_display_name="integration_display_name_example",
                    integration_type="integration_type_example",
                ),
                redirect_url="redirect_url_example",
                created_on_utc=dateutil_parser('1970-01-01T00:00:00.00Z'),
                last_sync=dateutil_parser('1970-01-01T00:00:00.00Z'),
                delete_requested=True,
                deleted=True,
                deleted_utc=dateutil_parser('1970-01-01T00:00:00.00Z'),
            ),
        ],
        shard_id=1,
        created_on_utc=dateutil_parser('1970-01-01T00:00:00.00Z'),
        delete_requested=True,
        deleted=True,
        created_by_user_id="created_by_user_id_example",
        created_by_user_name="created_by_user_name_example",
    ) # CodatClientsApiClientContractCompany |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a company with a new name
        api_response = api_instance.companies_company_id_put(company_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling CompaniesApi->companies_company_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a company with a new name
        api_response = api_instance.companies_company_id_put(company_id, codat_clients_api_client_contract_company=codat_clients_api_client_contract_company)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling CompaniesApi->companies_company_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **codat_clients_api_client_contract_company** | [**CodatClientsApiClientContractCompany**](CodatClientsApiClientContractCompany.md)|  | [optional]

### Return type

[**CodatPublicApiModelsCompanyCompany**](CodatPublicApiModelsCompanyCompany.md)

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

# **companies_company_id_settings_get**
> CodatPublicApiModelsCompanyCompanySettings companies_company_id_settings_get(company_id)

Fetch settings on a single company.

### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import companies_api
from codat_python_sdk.model.codat_public_api_models_company_company_settings import CodatPublicApiModelsCompanyCompanySettings
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
    api_instance = companies_api.CompaniesApi(api_client)
    company_id = "companyId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch settings on a single company.
        api_response = api_instance.companies_company_id_settings_get(company_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling CompaniesApi->companies_company_id_settings_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |

### Return type

[**CodatPublicApiModelsCompanyCompanySettings**](CodatPublicApiModelsCompanyCompanySettings.md)

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

# **companies_company_id_settings_put**
> CodatPublicApiModelsCompanyCompanySettings companies_company_id_settings_put(company_id)

Update settings on a single company.

### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import companies_api
from codat_python_sdk.model.codat_clients_api_client_contract_company_settings import CodatClientsApiClientContractCompanySettings
from codat_python_sdk.model.codat_public_api_models_company_company_settings import CodatPublicApiModelsCompanyCompanySettings
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
    api_instance = companies_api.CompaniesApi(api_client)
    company_id = "companyId_example" # str | 
    codat_clients_api_client_contract_company_settings = CodatClientsApiClientContractCompanySettings(
        company_id="company_id_example",
        offline_connector_install=True,
        one_time_sync="one_time_sync_example",
    ) # CodatClientsApiClientContractCompanySettings |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update settings on a single company.
        api_response = api_instance.companies_company_id_settings_put(company_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling CompaniesApi->companies_company_id_settings_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update settings on a single company.
        api_response = api_instance.companies_company_id_settings_put(company_id, codat_clients_api_client_contract_company_settings=codat_clients_api_client_contract_company_settings)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling CompaniesApi->companies_company_id_settings_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **codat_clients_api_client_contract_company_settings** | [**CodatClientsApiClientContractCompanySettings**](CodatClientsApiClientContractCompanySettings.md)|  | [optional]

### Return type

[**CodatPublicApiModelsCompanyCompanySettings**](CodatPublicApiModelsCompanyCompanySettings.md)

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

# **companies_company_id_sync_settings_get**
> CodatClientsApiClientContractCompanySyncSettings companies_company_id_sync_settings_get(company_id)



### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import companies_api
from codat_python_sdk.model.codat_clients_api_client_contract_company_sync_settings import CodatClientsApiClientContractCompanySyncSettings
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
    api_instance = companies_api.CompaniesApi(api_client)
    company_id = "companyId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.companies_company_id_sync_settings_get(company_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling CompaniesApi->companies_company_id_sync_settings_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |

### Return type

[**CodatClientsApiClientContractCompanySyncSettings**](CodatClientsApiClientContractCompanySyncSettings.md)

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

# **companies_company_id_sync_settings_post**
> companies_company_id_sync_settings_post(company_id)



### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import companies_api
from codat_python_sdk.model.codat_clients_api_client_contract_company_sync_settings import CodatClientsApiClientContractCompanySyncSettings
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
    api_instance = companies_api.CompaniesApi(api_client)
    company_id = "companyId_example" # str | 
    codat_clients_api_client_contract_company_sync_settings = CodatClientsApiClientContractCompanySyncSettings(
        company_id="company_id_example",
        settings=[
            CodatClientsApiClientContractSyncSetting(
                data_type="data_type_example",
                fetch_on_first_link=True,
                sync_schedule=1,
                sync_order=1,
                sync_from_utc=dateutil_parser('1970-01-01T00:00:00.00Z'),
                sync_from_window=1,
                months_to_sync=1,
            ),
        ],
        overrides_defaults=True,
    ) # CodatClientsApiClientContractCompanySyncSettings |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.companies_company_id_sync_settings_post(company_id)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling CompaniesApi->companies_company_id_sync_settings_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.companies_company_id_sync_settings_post(company_id, codat_clients_api_client_contract_company_sync_settings=codat_clients_api_client_contract_company_sync_settings)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling CompaniesApi->companies_company_id_sync_settings_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **codat_clients_api_client_contract_company_sync_settings** | [**CodatClientsApiClientContractCompanySyncSettings**](CodatClientsApiClientContractCompanySyncSettings.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[API Key Auth](../README.md#API Key Auth), [Codat Login](../README.md#Codat Login)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_get**
> CodatPublicApiModelsCompanyCompanyPagedResponseModel companies_get()

Fetch a list of all companies metadata with accounting links on the Codat platform

### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import companies_api
from codat_python_sdk.model.codat_public_api_models_company_company_paged_response_model import CodatPublicApiModelsCompanyCompanyPagedResponseModel
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
    api_instance = companies_api.CompaniesApi(api_client)
    page_size = 100 # int |  (optional) if omitted the server will use the default value of 100
    query = "query_example" # str |  (optional)
    order_by = "orderBy_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Fetch a list of all companies metadata with accounting links on the Codat platform
        api_response = api_instance.companies_get()
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling CompaniesApi->companies_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch a list of all companies metadata with accounting links on the Codat platform
        api_response = api_instance.companies_get(page_size=page_size, query=query, order_by=order_by)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling CompaniesApi->companies_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | defaults to 1
 **page_size** | **int**|  | [optional] if omitted the server will use the default value of 100
 **query** | **str**|  | [optional]
 **order_by** | **str**|  | [optional]

### Return type

[**CodatPublicApiModelsCompanyCompanyPagedResponseModel**](CodatPublicApiModelsCompanyCompanyPagedResponseModel.md)

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

# **companies_post**
> CodatPublicApiModelsCompanyCompany companies_post()

Initiate the process of onboarding a new company on the Codat platform

### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import companies_api
from codat_python_sdk.model.codat_public_api_models_company_add_company_model import CodatPublicApiModelsCompanyAddCompanyModel
from codat_python_sdk.model.codat_public_api_models_company_company import CodatPublicApiModelsCompanyCompany
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
    api_instance = companies_api.CompaniesApi(api_client)
    codat_public_api_models_company_add_company_model = CodatPublicApiModelsCompanyAddCompanyModel(
        name="name_example",
        platform_type="platform_type_example",
        created_by_user_id="created_by_user_id_example",
    ) # CodatPublicApiModelsCompanyAddCompanyModel |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Initiate the process of onboarding a new company on the Codat platform
        api_response = api_instance.companies_post(codat_public_api_models_company_add_company_model=codat_public_api_models_company_add_company_model)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling CompaniesApi->companies_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **codat_public_api_models_company_add_company_model** | [**CodatPublicApiModelsCompanyAddCompanyModel**](CodatPublicApiModelsCompanyAddCompanyModel.md)|  | [optional]

### Return type

[**CodatPublicApiModelsCompanyCompany**](CodatPublicApiModelsCompanyCompany.md)

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

