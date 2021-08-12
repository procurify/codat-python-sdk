# swagger_client.IntegrationsApi

All URIs are relative to */*

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
api_instance = swagger_client.IntegrationsApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.integrations_bank_settings_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->integrations_bank_settings_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CodatClientsApiClientContractBankSettingsDataset**](CodatClientsApiClientContractBankSettingsDataset.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **integrations_bank_settings_put**
> CodatClientsApiClientContractBankSettingsDataset integrations_bank_settings_put(body=body)



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
api_instance = swagger_client.IntegrationsApi(swagger_client.ApiClient(configuration))
body = swagger_client.CodatClientsApiClientContractBankSettingsDataset() # CodatClientsApiClientContractBankSettingsDataset |  (optional)

try:
    api_response = api_instance.integrations_bank_settings_put(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->integrations_bank_settings_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CodatClientsApiClientContractBankSettingsDataset**](CodatClientsApiClientContractBankSettingsDataset.md)|  | [optional] 

### Return type

[**CodatClientsApiClientContractBankSettingsDataset**](CodatClientsApiClientContractBankSettingsDataset.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **integrations_credentials_platform_key_delete**
> CodatPublicApiModelsPlatformCredentialsPlatformCredentials integrations_credentials_platform_key_delete(platform_key)

Delete credentials used to authenticate with an accounting platform

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
api_instance = swagger_client.IntegrationsApi(swagger_client.ApiClient(configuration))
platform_key = 'platform_key_example' # str | 

try:
    # Delete credentials used to authenticate with an accounting platform
    api_response = api_instance.integrations_credentials_platform_key_delete(platform_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->integrations_credentials_platform_key_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 

### Return type

[**CodatPublicApiModelsPlatformCredentialsPlatformCredentials**](CodatPublicApiModelsPlatformCredentialsPlatformCredentials.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **integrations_credentials_platform_key_get**
> CodatPublicApiModelsPlatformCredentialsPlatformCredentials integrations_credentials_platform_key_get(platform_key)

Fetch credentials required to authenticate with an accounting platform.

Used to determine presence and version of credentials. Due to masking the credentials returned cannot be used  to access the API.

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
api_instance = swagger_client.IntegrationsApi(swagger_client.ApiClient(configuration))
platform_key = 'platform_key_example' # str | 

try:
    # Fetch credentials required to authenticate with an accounting platform.
    api_response = api_instance.integrations_credentials_platform_key_get(platform_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->integrations_credentials_platform_key_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 

### Return type

[**CodatPublicApiModelsPlatformCredentialsPlatformCredentials**](CodatPublicApiModelsPlatformCredentialsPlatformCredentials.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **integrations_credentials_platform_key_put**
> CodatPublicApiModelsPlatformCredentialsPlatformCredentials integrations_credentials_platform_key_put(platform_key, body=body)

Update credentials required to authenticate with an accounting platform

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
api_instance = swagger_client.IntegrationsApi(swagger_client.ApiClient(configuration))
platform_key = 'platform_key_example' # str | 
body = NULL # dict(str, str) |  (optional)

try:
    # Update credentials required to authenticate with an accounting platform
    api_response = api_instance.integrations_credentials_platform_key_put(platform_key, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->integrations_credentials_platform_key_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 
 **body** | [**dict(str, str)**](dict.md)|  | [optional] 

### Return type

[**CodatPublicApiModelsPlatformCredentialsPlatformCredentials**](CodatPublicApiModelsPlatformCredentialsPlatformCredentials.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **integrations_get**
> CodatPublicApiModelsPlatformCredentialsPlatformSourceModelPagedResponseModel integrations_get(page, page_size=page_size, query=query, order_by=order_by)



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
api_instance = swagger_client.IntegrationsApi(swagger_client.ApiClient(configuration))
page = 1 # int |  (default to 1)
page_size = 100 # int |  (optional) (default to 100)
query = 'query_example' # str |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    api_response = api_instance.integrations_get(page, page_size=page_size, query=query, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->integrations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [default to 1]
 **page_size** | **int**|  | [optional] [default to 100]
 **query** | **str**|  | [optional] 
 **order_by** | **str**|  | [optional] 

### Return type

[**CodatPublicApiModelsPlatformCredentialsPlatformSourceModelPagedResponseModel**](CodatPublicApiModelsPlatformCredentialsPlatformSourceModelPagedResponseModel.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **integrations_platform_key_branding_get**
> CodatPublicApiModelsClientsIntegrationBrandingModel integrations_platform_key_branding_get(platform_key)



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
api_instance = swagger_client.IntegrationsApi(swagger_client.ApiClient(configuration))
platform_key = 'platform_key_example' # str | 

try:
    api_response = api_instance.integrations_platform_key_branding_get(platform_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->integrations_platform_key_branding_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 

### Return type

[**CodatPublicApiModelsClientsIntegrationBrandingModel**](CodatPublicApiModelsClientsIntegrationBrandingModel.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **integrations_platform_key_enabled_put**
> CodatPublicApiModelsPlatformCredentialsPlatformSourceModel integrations_platform_key_enabled_put(platform_key, body=body)



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
api_instance = swagger_client.IntegrationsApi(swagger_client.ApiClient(configuration))
platform_key = 'platform_key_example' # str | 
body = swagger_client.CodatPublicApiModelsPlatformCredentialsEnabledArgs() # CodatPublicApiModelsPlatformCredentialsEnabledArgs |  (optional)

try:
    api_response = api_instance.integrations_platform_key_enabled_put(platform_key, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->integrations_platform_key_enabled_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 
 **body** | [**CodatPublicApiModelsPlatformCredentialsEnabledArgs**](CodatPublicApiModelsPlatformCredentialsEnabledArgs.md)|  | [optional] 

### Return type

[**CodatPublicApiModelsPlatformCredentialsPlatformSourceModel**](CodatPublicApiModelsPlatformCredentialsPlatformSourceModel.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **integrations_platform_key_get**
> CodatPublicApiModelsPlatformCredentialsPlatformSourceModel integrations_platform_key_get(platform_key)



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
api_instance = swagger_client.IntegrationsApi(swagger_client.ApiClient(configuration))
platform_key = 'platform_key_example' # str | 

try:
    api_response = api_instance.integrations_platform_key_get(platform_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationsApi->integrations_platform_key_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **platform_key** | **str**|  | 

### Return type

[**CodatPublicApiModelsPlatformCredentialsPlatformSourceModel**](CodatPublicApiModelsPlatformCredentialsPlatformSourceModel.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

