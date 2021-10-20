# codat_python_sdk.ProfileApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**profile_api_key_put**](ProfileApi.md#profile_api_key_put) | **PUT** /profile/apiKey | Refresh the existing API key for your clients.
[**profile_get**](ProfileApi.md#profile_get) | **GET** /profile | Fetch your organisations company profile
[**profile_put**](ProfileApi.md#profile_put) | **PUT** /profile | Update your organisations company profile
[**profile_sync_settings_get**](ProfileApi.md#profile_sync_settings_get) | **GET** /profile/syncSettings | 
[**profile_sync_settings_post**](ProfileApi.md#profile_sync_settings_post) | **POST** /profile/syncSettings | 


# **profile_api_key_put**
> CodatPublicApiModelsCompanyProfileModel profile_api_key_put()

Refresh the existing API key for your clients.

### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import profile_api
from codat_python_sdk.model.codat_public_api_models_company_profile_model import CodatPublicApiModelsCompanyProfileModel
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
    api_instance = profile_api.ProfileApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Refresh the existing API key for your clients.
        api_response = api_instance.profile_api_key_put()
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling ProfileApi->profile_api_key_put: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CodatPublicApiModelsCompanyProfileModel**](CodatPublicApiModelsCompanyProfileModel.md)

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

# **profile_get**
> CodatPublicApiModelsCompanyProfileModel profile_get()

Fetch your organisations company profile

### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import profile_api
from codat_python_sdk.model.codat_public_api_models_company_profile_model import CodatPublicApiModelsCompanyProfileModel
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
    api_instance = profile_api.ProfileApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Fetch your organisations company profile
        api_response = api_instance.profile_get()
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling ProfileApi->profile_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CodatPublicApiModelsCompanyProfileModel**](CodatPublicApiModelsCompanyProfileModel.md)

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

# **profile_put**
> CodatPublicApiModelsCompanyProfileModel profile_put()

Update your organisations company profile

If you are using the Codat 'link site' this information will be visible there.

### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import profile_api
from codat_python_sdk.model.codat_public_api_models_company_profile_model import CodatPublicApiModelsCompanyProfileModel
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
    api_instance = profile_api.ProfileApi(api_client)
    codat_public_api_models_company_profile_model = CodatPublicApiModelsCompanyProfileModel(
        name="name_example",
        logo_url="logo_url_example",
        icon_url="icon_url_example",
        redirect_url="redirect_url_example",
        white_list_urls=[
            "white_list_urls_example",
        ],
        api_key="api_key_example",
        alert_auth_header="alert_auth_header_example",
        confirm_company_name=True,
    ) # CodatPublicApiModelsCompanyProfileModel |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update your organisations company profile
        api_response = api_instance.profile_put(codat_public_api_models_company_profile_model=codat_public_api_models_company_profile_model)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling ProfileApi->profile_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **codat_public_api_models_company_profile_model** | [**CodatPublicApiModelsCompanyProfileModel**](CodatPublicApiModelsCompanyProfileModel.md)|  | [optional]

### Return type

[**CodatPublicApiModelsCompanyProfileModel**](CodatPublicApiModelsCompanyProfileModel.md)

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

# **profile_sync_settings_get**
> CodatClientsApiClientContractClientSyncSettings profile_sync_settings_get()



### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import profile_api
from codat_python_sdk.model.codat_clients_api_client_contract_client_sync_settings import CodatClientsApiClientContractClientSyncSettings
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
    api_instance = profile_api.ProfileApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.profile_sync_settings_get()
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling ProfileApi->profile_sync_settings_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CodatClientsApiClientContractClientSyncSettings**](CodatClientsApiClientContractClientSyncSettings.md)

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

# **profile_sync_settings_post**
> profile_sync_settings_post()



### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import profile_api
from codat_python_sdk.model.codat_clients_api_client_contract_client_sync_settings import CodatClientsApiClientContractClientSyncSettings
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
    api_instance = profile_api.ProfileApi(api_client)
    codat_clients_api_client_contract_client_sync_settings = CodatClientsApiClientContractClientSyncSettings(
        client_id="client_id_example",
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
    ) # CodatClientsApiClientContractClientSyncSettings |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.profile_sync_settings_post(codat_clients_api_client_contract_client_sync_settings=codat_clients_api_client_contract_client_sync_settings)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling ProfileApi->profile_sync_settings_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **codat_clients_api_client_contract_client_sync_settings** | [**CodatClientsApiClientContractClientSyncSettings**](CodatClientsApiClientContractClientSyncSettings.md)|  | [optional]

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

