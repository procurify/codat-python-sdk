# swagger_client.ProfileApi

All URIs are relative to */*

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
api_instance = swagger_client.ProfileApi(swagger_client.ApiClient(configuration))

try:
    # Refresh the existing API key for your clients.
    api_response = api_instance.profile_api_key_put()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfileApi->profile_api_key_put: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CodatPublicApiModelsCompanyProfileModel**](CodatPublicApiModelsCompanyProfileModel.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profile_get**
> CodatPublicApiModelsCompanyProfileModel profile_get()

Fetch your organisations company profile

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
api_instance = swagger_client.ProfileApi(swagger_client.ApiClient(configuration))

try:
    # Fetch your organisations company profile
    api_response = api_instance.profile_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfileApi->profile_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CodatPublicApiModelsCompanyProfileModel**](CodatPublicApiModelsCompanyProfileModel.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profile_put**
> CodatPublicApiModelsCompanyProfileModel profile_put(body=body)

Update your organisations company profile

If you are using the Codat 'link site' this information will be visible there.

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
api_instance = swagger_client.ProfileApi(swagger_client.ApiClient(configuration))
body = swagger_client.CodatPublicApiModelsCompanyProfileModel() # CodatPublicApiModelsCompanyProfileModel |  (optional)

try:
    # Update your organisations company profile
    api_response = api_instance.profile_put(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfileApi->profile_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CodatPublicApiModelsCompanyProfileModel**](CodatPublicApiModelsCompanyProfileModel.md)|  | [optional] 

### Return type

[**CodatPublicApiModelsCompanyProfileModel**](CodatPublicApiModelsCompanyProfileModel.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profile_sync_settings_get**
> CodatClientsApiClientContractClientSyncSettings profile_sync_settings_get()



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
api_instance = swagger_client.ProfileApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.profile_sync_settings_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProfileApi->profile_sync_settings_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CodatClientsApiClientContractClientSyncSettings**](CodatClientsApiClientContractClientSyncSettings.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **profile_sync_settings_post**
> profile_sync_settings_post(body=body)



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
api_instance = swagger_client.ProfileApi(swagger_client.ApiClient(configuration))
body = swagger_client.CodatClientsApiClientContractClientSyncSettings() # CodatClientsApiClientContractClientSyncSettings |  (optional)

try:
    api_instance.profile_sync_settings_post(body=body)
except ApiException as e:
    print("Exception when calling ProfileApi->profile_sync_settings_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CodatClientsApiClientContractClientSyncSettings**](CodatClientsApiClientContractClientSyncSettings.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

