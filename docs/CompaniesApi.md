# codat_python_sdk.CompaniesApi

All URIs are relative to */*

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
api_instance = codat_python_sdk.CompaniesApi(codat_python_sdk.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Deletes a company, this is not reversible.
    api_instance.companies_company_id_delete(company_id)
except ApiException as e:
    print("Exception when calling CompaniesApi->companies_company_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_get**
> CodatPublicApiModelsCompanyCompany companies_company_id_get(company_id)

Fetch metadata on a single company.

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
api_instance = codat_python_sdk.CompaniesApi(codat_python_sdk.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Fetch metadata on a single company.
    api_response = api_instance.companies_company_id_get(company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompaniesApi->companies_company_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 

### Return type

[**CodatPublicApiModelsCompanyCompany**](CodatPublicApiModelsCompanyCompany.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_put**
> CodatPublicApiModelsCompanyCompany companies_company_id_put(company_id, body=body)

Update a company with a new name

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
api_instance = codat_python_sdk.CompaniesApi(codat_python_sdk.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = codat_python_sdk.CodatClientsApiClientContractCompany() # CodatClientsApiClientContractCompany |  (optional)

try:
    # Update a company with a new name
    api_response = api_instance.companies_company_id_put(company_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompaniesApi->companies_company_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **body** | [**CodatClientsApiClientContractCompany**](CodatClientsApiClientContractCompany.md)|  | [optional] 

### Return type

[**CodatPublicApiModelsCompanyCompany**](CodatPublicApiModelsCompanyCompany.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_settings_get**
> CodatPublicApiModelsCompanyCompanySettings companies_company_id_settings_get(company_id)

Fetch settings on a single company.

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
api_instance = codat_python_sdk.CompaniesApi(codat_python_sdk.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Fetch settings on a single company.
    api_response = api_instance.companies_company_id_settings_get(company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompaniesApi->companies_company_id_settings_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 

### Return type

[**CodatPublicApiModelsCompanyCompanySettings**](CodatPublicApiModelsCompanyCompanySettings.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_settings_put**
> CodatPublicApiModelsCompanyCompanySettings companies_company_id_settings_put(company_id, body=body)

Update settings on a single company.

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
api_instance = codat_python_sdk.CompaniesApi(codat_python_sdk.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = codat_python_sdk.CodatClientsApiClientContractCompanySettings() # CodatClientsApiClientContractCompanySettings |  (optional)

try:
    # Update settings on a single company.
    api_response = api_instance.companies_company_id_settings_put(company_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompaniesApi->companies_company_id_settings_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **body** | [**CodatClientsApiClientContractCompanySettings**](CodatClientsApiClientContractCompanySettings.md)|  | [optional] 

### Return type

[**CodatPublicApiModelsCompanyCompanySettings**](CodatPublicApiModelsCompanyCompanySettings.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_sync_settings_get**
> CodatClientsApiClientContractCompanySyncSettings companies_company_id_sync_settings_get(company_id)



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
api_instance = codat_python_sdk.CompaniesApi(codat_python_sdk.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    api_response = api_instance.companies_company_id_sync_settings_get(company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompaniesApi->companies_company_id_sync_settings_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 

### Return type

[**CodatClientsApiClientContractCompanySyncSettings**](CodatClientsApiClientContractCompanySyncSettings.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_sync_settings_post**
> companies_company_id_sync_settings_post(company_id, body=body)



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
api_instance = codat_python_sdk.CompaniesApi(codat_python_sdk.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = codat_python_sdk.CodatClientsApiClientContractCompanySyncSettings() # CodatClientsApiClientContractCompanySyncSettings |  (optional)

try:
    api_instance.companies_company_id_sync_settings_post(company_id, body=body)
except ApiException as e:
    print("Exception when calling CompaniesApi->companies_company_id_sync_settings_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **body** | [**CodatClientsApiClientContractCompanySyncSettings**](CodatClientsApiClientContractCompanySyncSettings.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_get**
> CodatPublicApiModelsCompanyCompanyPagedResponseModel companies_get(page, page_size=page_size, query=query, order_by=order_by)

Fetch a list of all companies metadata with accounting links on the Codat platform

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
api_instance = codat_python_sdk.CompaniesApi(codat_python_sdk.ApiClient(configuration))
page = 1 # int |  (default to 1)
page_size = 100 # int |  (optional) (default to 100)
query = 'query_example' # str |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    # Fetch a list of all companies metadata with accounting links on the Codat platform
    api_response = api_instance.companies_get(page, page_size=page_size, query=query, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompaniesApi->companies_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [default to 1]
 **page_size** | **int**|  | [optional] [default to 100]
 **query** | **str**|  | [optional] 
 **order_by** | **str**|  | [optional] 

### Return type

[**CodatPublicApiModelsCompanyCompanyPagedResponseModel**](CodatPublicApiModelsCompanyCompanyPagedResponseModel.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_post**
> CodatPublicApiModelsCompanyCompany companies_post(body=body)

Initiate the process of onboarding a new company on the Codat platform

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
api_instance = codat_python_sdk.CompaniesApi(codat_python_sdk.ApiClient(configuration))
body = codat_python_sdk.CodatPublicApiModelsCompanyAddCompanyModel() # CodatPublicApiModelsCompanyAddCompanyModel |  (optional)

try:
    # Initiate the process of onboarding a new company on the Codat platform
    api_response = api_instance.companies_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompaniesApi->companies_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CodatPublicApiModelsCompanyAddCompanyModel**](CodatPublicApiModelsCompanyAddCompanyModel.md)|  | [optional] 

### Return type

[**CodatPublicApiModelsCompanyCompany**](CodatPublicApiModelsCompanyCompany.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

