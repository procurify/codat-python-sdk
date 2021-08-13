# codat_python_sdk.SettingsApi

All URIs are relative to */*

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
api_instance = codat_python_sdk.SettingsApi(codat_python_sdk.ApiClient(configuration))

try:
    # Fetch your settings
    api_response = api_instance.settings_get()
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_integrations_integration_id_get**
> CodatPublicApiModelsClientsIntegrationSettingsModel settings_integrations_integration_id_get(integration_id)

Fetch your organisations integration settings

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
api_instance = codat_python_sdk.SettingsApi(codat_python_sdk.ApiClient(configuration))
integration_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Fetch your organisations integration settings
    api_response = api_instance.settings_integrations_integration_id_get(integration_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->settings_integrations_integration_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | [**str**](.md)|  | 

### Return type

[**CodatPublicApiModelsClientsIntegrationSettingsModel**](CodatPublicApiModelsClientsIntegrationSettingsModel.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_integrations_integration_id_patch**
> CodatPublicApiModelsClientsIntegrationSettingsModel settings_integrations_integration_id_patch(integration_id, body=body)

Update your organisations integration settings

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
api_instance = codat_python_sdk.SettingsApi(codat_python_sdk.ApiClient(configuration))
integration_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = codat_python_sdk.CodatPublicApiModelsClientsIntegrationSettingsPatchModel() # CodatPublicApiModelsClientsIntegrationSettingsPatchModel |  (optional)

try:
    # Update your organisations integration settings
    api_response = api_instance.settings_integrations_integration_id_patch(integration_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->settings_integrations_integration_id_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | [**str**](.md)|  | 
 **body** | [**CodatPublicApiModelsClientsIntegrationSettingsPatchModel**](CodatPublicApiModelsClientsIntegrationSettingsPatchModel.md)|  | [optional] 

### Return type

[**CodatPublicApiModelsClientsIntegrationSettingsModel**](CodatPublicApiModelsClientsIntegrationSettingsModel.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_patch**
> CodatPublicApiModelsClientsClientSettingsModel settings_patch(body=body)

Update your settings

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
api_instance = codat_python_sdk.SettingsApi(codat_python_sdk.ApiClient(configuration))
body = codat_python_sdk.CodatPublicApiModelsClientsClientSettingsPatchModel() # CodatPublicApiModelsClientsClientSettingsPatchModel |  (optional)

try:
    # Update your settings
    api_response = api_instance.settings_patch(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->settings_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CodatPublicApiModelsClientsClientSettingsPatchModel**](CodatPublicApiModelsClientsClientSettingsPatchModel.md)|  | [optional] 

### Return type

[**CodatPublicApiModelsClientsClientSettingsModel**](CodatPublicApiModelsClientsClientSettingsModel.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

