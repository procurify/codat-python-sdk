# codat_python_sdk.SettingsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**settings_get**](SettingsApi.md#settings_get) | **GET** /settings | Fetch your settings
[**settings_integrations_integration_id_get**](SettingsApi.md#settings_integrations_integration_id_get) | **GET** /settings/integrations/{integrationId} | Fetch your organisations integration settings
[**settings_integrations_integration_id_patch**](SettingsApi.md#settings_integrations_integration_id_patch) | **PATCH** /settings/integrations/{integrationId} | Update your organisations integration settings
[**settings_patch**](SettingsApi.md#settings_patch) | **PATCH** /settings | Update your settings


# **settings_get**
> CodatPublicApiModelsClientsClientSettingsModel settings_get()

Fetch your settings

### Example

* Api Key Authentication (API Key Auth):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import settings_api
from codat_python_sdk.model.codat_public_api_models_clients_client_settings_model import CodatPublicApiModelsClientsClientSettingsModel
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

# Enter a context with an instance of the API client
with codat_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = settings_api.SettingsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Fetch your settings
        api_response = api_instance.settings_get()
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling SettingsApi->settings_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CodatPublicApiModelsClientsClientSettingsModel**](CodatPublicApiModelsClientsClientSettingsModel.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_integrations_integration_id_get**
> CodatPublicApiModelsClientsIntegrationSettingsModel settings_integrations_integration_id_get(integration_id)

Fetch your organisations integration settings

### Example

* Api Key Authentication (API Key Auth):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import settings_api
from codat_python_sdk.model.codat_public_api_models_clients_integration_settings_model import CodatPublicApiModelsClientsIntegrationSettingsModel
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

# Enter a context with an instance of the API client
with codat_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = settings_api.SettingsApi(api_client)
    integration_id = "integrationId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Fetch your organisations integration settings
        api_response = api_instance.settings_integrations_integration_id_get(integration_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling SettingsApi->settings_integrations_integration_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **str**|  |

### Return type

[**CodatPublicApiModelsClientsIntegrationSettingsModel**](CodatPublicApiModelsClientsIntegrationSettingsModel.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_integrations_integration_id_patch**
> CodatPublicApiModelsClientsIntegrationSettingsModel settings_integrations_integration_id_patch(integration_id)

Update your organisations integration settings

### Example

* Api Key Authentication (API Key Auth):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import settings_api
from codat_python_sdk.model.codat_public_api_models_clients_integration_settings_patch_model import CodatPublicApiModelsClientsIntegrationSettingsPatchModel
from codat_python_sdk.model.codat_public_api_models_clients_integration_settings_model import CodatPublicApiModelsClientsIntegrationSettingsModel
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

# Enter a context with an instance of the API client
with codat_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = settings_api.SettingsApi(api_client)
    integration_id = "integrationId_example" # str | 
    codat_public_api_models_clients_integration_settings_patch_model = CodatPublicApiModelsClientsIntegrationSettingsPatchModel(
        one_time_sync="one_time_sync_example",
    ) # CodatPublicApiModelsClientsIntegrationSettingsPatchModel |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update your organisations integration settings
        api_response = api_instance.settings_integrations_integration_id_patch(integration_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling SettingsApi->settings_integrations_integration_id_patch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update your organisations integration settings
        api_response = api_instance.settings_integrations_integration_id_patch(integration_id, codat_public_api_models_clients_integration_settings_patch_model=codat_public_api_models_clients_integration_settings_patch_model)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling SettingsApi->settings_integrations_integration_id_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **str**|  |
 **codat_public_api_models_clients_integration_settings_patch_model** | [**CodatPublicApiModelsClientsIntegrationSettingsPatchModel**](CodatPublicApiModelsClientsIntegrationSettingsPatchModel.md)|  | [optional]

### Return type

[**CodatPublicApiModelsClientsIntegrationSettingsModel**](CodatPublicApiModelsClientsIntegrationSettingsModel.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_patch**
> CodatPublicApiModelsClientsClientSettingsModel settings_patch()

Update your settings

### Example

* Api Key Authentication (API Key Auth):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import settings_api
from codat_python_sdk.model.codat_public_api_models_clients_client_settings_patch_model import CodatPublicApiModelsClientsClientSettingsPatchModel
from codat_python_sdk.model.codat_public_api_models_clients_client_settings_model import CodatPublicApiModelsClientsClientSettingsModel
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

# Enter a context with an instance of the API client
with codat_python_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = settings_api.SettingsApi(api_client)
    codat_public_api_models_clients_client_settings_patch_model = CodatPublicApiModelsClientsClientSettingsPatchModel(
        one_time_sync="one_time_sync_example",
    ) # CodatPublicApiModelsClientsClientSettingsPatchModel |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update your settings
        api_response = api_instance.settings_patch(codat_public_api_models_clients_client_settings_patch_model=codat_public_api_models_clients_client_settings_patch_model)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling SettingsApi->settings_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **codat_public_api_models_clients_client_settings_patch_model** | [**CodatPublicApiModelsClientsClientSettingsPatchModel**](CodatPublicApiModelsClientsClientSettingsPatchModel.md)|  | [optional]

### Return type

[**CodatPublicApiModelsClientsClientSettingsModel**](CodatPublicApiModelsClientsClientSettingsModel.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

