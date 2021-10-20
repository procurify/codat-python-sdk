# codat_python_sdk.IntegrationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**integrations_bank_settings_get**](IntegrationsApi.md#integrations_bank_settings_get) | **GET** /integrations/bankSettings | 
[**integrations_bank_settings_put**](IntegrationsApi.md#integrations_bank_settings_put) | **PUT** /integrations/bankSettings | 
[**integrations_credentials_platform_key_delete**](IntegrationsApi.md#integrations_credentials_platform_key_delete) | **DELETE** /integrations/credentials/{platformKey} | Delete credentials used to authenticate with an accounting platform
[**integrations_credentials_platform_key_get**](IntegrationsApi.md#integrations_credentials_platform_key_get) | **GET** /integrations/credentials/{platformKey} | Fetch credentials required to authenticate with an accounting platform.
[**integrations_credentials_platform_key_put**](IntegrationsApi.md#integrations_credentials_platform_key_put) | **PUT** /integrations/credentials/{platformKey} | Update credentials required to authenticate with an accounting platform
[**integrations_get**](IntegrationsApi.md#integrations_get) | **GET** /integrations | 
[**integrations_platform_key_branding_get**](IntegrationsApi.md#integrations_platform_key_branding_get) | **GET** /integrations/{platformKey}/branding | 
[**integrations_platform_key_enabled_put**](IntegrationsApi.md#integrations_platform_key_enabled_put) | **PUT** /integrations/{platformKey}/enabled | 
[**integrations_platform_key_get**](IntegrationsApi.md#integrations_platform_key_get) | **GET** /integrations/{platformKey} | 


# **integrations_bank_settings_get**
> CodatClientsApiClientContractBankSettingsDataset integrations_bank_settings_get()



### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import integrations_api
from codat_python_sdk.model.codat_clients_api_client_contract_bank_settings_dataset import CodatClientsApiClientContractBankSettingsDataset
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
    api_instance = integrations_api.IntegrationsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.integrations_bank_settings_get()
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling IntegrationsApi->integrations_bank_settings_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CodatClientsApiClientContractBankSettingsDataset**](CodatClientsApiClientContractBankSettingsDataset.md)

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

# **integrations_bank_settings_put**
> CodatClientsApiClientContractBankSettingsDataset integrations_bank_settings_put()



### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import integrations_api
from codat_python_sdk.model.codat_clients_api_client_contract_bank_settings_dataset import CodatClientsApiClientContractBankSettingsDataset
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
    api_instance = integrations_api.IntegrationsApi(api_client)
    codat_clients_api_client_contract_bank_settings_dataset = CodatClientsApiClientContractBankSettingsDataset(
        bank_settings=[
            CodatClientsApiClientContractBankSetting(
                name="name_example",
                source_guid="source_guid_example",
                bank_integrations=[
                    CodatClientsApiClientContractBankIntegration(
                        name="name_example",
                        integration_guid="integration_guid_example",
                        selected=True,
                    ),
                ],
            ),
        ],
    ) # CodatClientsApiClientContractBankSettingsDataset |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.integrations_bank_settings_put(codat_clients_api_client_contract_bank_settings_dataset=codat_clients_api_client_contract_bank_settings_dataset)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling IntegrationsApi->integrations_bank_settings_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **codat_clients_api_client_contract_bank_settings_dataset** | [**CodatClientsApiClientContractBankSettingsDataset**](CodatClientsApiClientContractBankSettingsDataset.md)|  | [optional]

### Return type

[**CodatClientsApiClientContractBankSettingsDataset**](CodatClientsApiClientContractBankSettingsDataset.md)

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

# **integrations_credentials_platform_key_delete**
> dict integrations_credentials_platform_key_delete(platform_key)

Delete credentials used to authenticate with an accounting platform

### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import integrations_api
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
    api_instance = integrations_api.IntegrationsApi(api_client)
    platform_key = "platformKey_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete credentials used to authenticate with an accounting platform
        api_response = api_instance.integrations_credentials_platform_key_delete(platform_key)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling IntegrationsApi->integrations_credentials_platform_key_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  |

### Return type

**dict**

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

# **integrations_credentials_platform_key_get**
> dict integrations_credentials_platform_key_get(platform_key)

Fetch credentials required to authenticate with an accounting platform.

Used to determine presence and version of credentials. Due to masking the credentials returned cannot be used  to access the API.

### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import integrations_api
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
    api_instance = integrations_api.IntegrationsApi(api_client)
    platform_key = "platformKey_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch credentials required to authenticate with an accounting platform.
        api_response = api_instance.integrations_credentials_platform_key_get(platform_key)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling IntegrationsApi->integrations_credentials_platform_key_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  |

### Return type

**dict**

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

# **integrations_credentials_platform_key_put**
> dict integrations_credentials_platform_key_put(platform_key)

Update credentials required to authenticate with an accounting platform

### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import integrations_api
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
    api_instance = integrations_api.IntegrationsApi(api_client)
    platform_key = "platformKey_example" # str | 
    request_body = {
        "key": "key_example",
    } # {str: (str,)} |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update credentials required to authenticate with an accounting platform
        api_response = api_instance.integrations_credentials_platform_key_put(platform_key)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling IntegrationsApi->integrations_credentials_platform_key_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update credentials required to authenticate with an accounting platform
        api_response = api_instance.integrations_credentials_platform_key_put(platform_key, request_body=request_body)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling IntegrationsApi->integrations_credentials_platform_key_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  |
 **request_body** | **{str: (str,)}**|  | [optional]

### Return type

**dict**

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

# **integrations_get**
> CodatPublicApiModelsPlatformCredentialsPlatformSourceModelPagedResponseModel integrations_get()



### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import integrations_api
from codat_python_sdk.model.codat_public_api_models_platform_credentials_platform_source_model_paged_response_model import CodatPublicApiModelsPlatformCredentialsPlatformSourceModelPagedResponseModel
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
    api_instance = integrations_api.IntegrationsApi(api_client)
    page_size = 100 # int |  (optional) if omitted the server will use the default value of 100
    query = "query_example" # str |  (optional)
    order_by = "orderBy_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.integrations_get()
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling IntegrationsApi->integrations_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.integrations_get(page_size=page_size, query=query, order_by=order_by)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling IntegrationsApi->integrations_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | defaults to 1
 **page_size** | **int**|  | [optional] if omitted the server will use the default value of 100
 **query** | **str**|  | [optional]
 **order_by** | **str**|  | [optional]

### Return type

[**CodatPublicApiModelsPlatformCredentialsPlatformSourceModelPagedResponseModel**](CodatPublicApiModelsPlatformCredentialsPlatformSourceModelPagedResponseModel.md)

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

# **integrations_platform_key_branding_get**
> CodatPublicApiModelsClientsIntegrationBrandingModel integrations_platform_key_branding_get(platform_key)



### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import integrations_api
from codat_python_sdk.model.codat_public_api_models_clients_integration_branding_model import CodatPublicApiModelsClientsIntegrationBrandingModel
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
    api_instance = integrations_api.IntegrationsApi(api_client)
    platform_key = "platformKey_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.integrations_platform_key_branding_get(platform_key)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling IntegrationsApi->integrations_platform_key_branding_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  |

### Return type

[**CodatPublicApiModelsClientsIntegrationBrandingModel**](CodatPublicApiModelsClientsIntegrationBrandingModel.md)

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

# **integrations_platform_key_enabled_put**
> CodatPublicApiModelsPlatformCredentialsPlatformSourceModel integrations_platform_key_enabled_put(platform_key)



### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import integrations_api
from codat_python_sdk.model.codat_public_api_models_platform_credentials_platform_source_model import CodatPublicApiModelsPlatformCredentialsPlatformSourceModel
from codat_python_sdk.model.codat_public_api_models_platform_credentials_enabled_args import CodatPublicApiModelsPlatformCredentialsEnabledArgs
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
    api_instance = integrations_api.IntegrationsApi(api_client)
    platform_key = "platformKey_example" # str | 
    codat_public_api_models_platform_credentials_enabled_args = CodatPublicApiModelsPlatformCredentialsEnabledArgs(
        enabled=True,
    ) # CodatPublicApiModelsPlatformCredentialsEnabledArgs |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.integrations_platform_key_enabled_put(platform_key)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling IntegrationsApi->integrations_platform_key_enabled_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.integrations_platform_key_enabled_put(platform_key, codat_public_api_models_platform_credentials_enabled_args=codat_public_api_models_platform_credentials_enabled_args)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling IntegrationsApi->integrations_platform_key_enabled_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  |
 **codat_public_api_models_platform_credentials_enabled_args** | [**CodatPublicApiModelsPlatformCredentialsEnabledArgs**](CodatPublicApiModelsPlatformCredentialsEnabledArgs.md)|  | [optional]

### Return type

[**CodatPublicApiModelsPlatformCredentialsPlatformSourceModel**](CodatPublicApiModelsPlatformCredentialsPlatformSourceModel.md)

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

# **integrations_platform_key_get**
> CodatPublicApiModelsPlatformCredentialsPlatformSourceModel integrations_platform_key_get(platform_key)



### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import integrations_api
from codat_python_sdk.model.codat_public_api_models_platform_credentials_platform_source_model import CodatPublicApiModelsPlatformCredentialsPlatformSourceModel
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
    api_instance = integrations_api.IntegrationsApi(api_client)
    platform_key = "platformKey_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.integrations_platform_key_get(platform_key)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling IntegrationsApi->integrations_platform_key_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  |

### Return type

[**CodatPublicApiModelsPlatformCredentialsPlatformSourceModel**](CodatPublicApiModelsPlatformCredentialsPlatformSourceModel.md)

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

