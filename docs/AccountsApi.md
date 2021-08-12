# swagger_client.AccountsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_company_id_connections_connection_id_metadata_accounts_account_id_categories_get**](AccountsApi.md#companies_company_id_connections_connection_id_metadata_accounts_account_id_categories_get) | **GET** /companies/{companyId}/connections/{connectionId}/metadata/accounts/{accountId}/categories | 
[**companies_company_id_connections_connection_id_metadata_accounts_account_id_categories_patch**](AccountsApi.md#companies_company_id_connections_connection_id_metadata_accounts_account_id_categories_patch) | **PATCH** /companies/{companyId}/connections/{connectionId}/metadata/accounts/{accountId}/categories | 
[**companies_company_id_connections_connection_id_metadata_accounts_categories_get**](AccountsApi.md#companies_company_id_connections_connection_id_metadata_accounts_categories_get) | **GET** /companies/{companyId}/connections/{connectionId}/metadata/accounts/categories | 
[**companies_company_id_connections_connection_id_metadata_accounts_categories_patch**](AccountsApi.md#companies_company_id_connections_connection_id_metadata_accounts_categories_patch) | **PATCH** /companies/{companyId}/connections/{connectionId}/metadata/accounts/categories | 
[**companies_company_id_connections_connection_id_push_accounts_post**](AccountsApi.md#companies_company_id_connections_connection_id_push_accounts_post) | **POST** /companies/{companyId}/connections/{connectionId}/push/accounts | Posts an individual account for a given company.
[**companies_company_id_data_accounts_account_id_get**](AccountsApi.md#companies_company_id_data_accounts_account_id_get) | **GET** /companies/{companyId}/data/accounts/{accountId} | Gets a single account corresponding to the supplied Id
[**companies_company_id_data_accounts_get**](AccountsApi.md#companies_company_id_data_accounts_get) | **GET** /companies/{companyId}/data/accounts | Gets the latest chart of accounts for a company
[**metadata_accounts_categories_get**](AccountsApi.md#metadata_accounts_categories_get) | **GET** /metadata/accounts/categories | 

# **companies_company_id_connections_connection_id_metadata_accounts_account_id_categories_get**
> CodatPublicApiModelsMetadataAccountCategoriesModel companies_company_id_connections_connection_id_metadata_accounts_account_id_categories_get(company_id, connection_id, account_id)



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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
account_id = 'account_id_example' # str | 

try:
    api_response = api_instance.companies_company_id_connections_connection_id_metadata_accounts_account_id_categories_get(company_id, connection_id, account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->companies_company_id_connections_connection_id_metadata_accounts_account_id_categories_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **connection_id** | [**str**](.md)|  | 
 **account_id** | **str**|  | 

### Return type

[**CodatPublicApiModelsMetadataAccountCategoriesModel**](CodatPublicApiModelsMetadataAccountCategoriesModel.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_connection_id_metadata_accounts_account_id_categories_patch**
> CodatPublicApiModelsMetadataAccountCategoriesModel companies_company_id_connections_connection_id_metadata_accounts_account_id_categories_patch(company_id, connection_id, account_id, body=body)



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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
account_id = 'account_id_example' # str | 
body = swagger_client.CodatPublicApiModelsMetadataPatchSingleAccountCategoryModel() # CodatPublicApiModelsMetadataPatchSingleAccountCategoryModel |  (optional)

try:
    api_response = api_instance.companies_company_id_connections_connection_id_metadata_accounts_account_id_categories_patch(company_id, connection_id, account_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->companies_company_id_connections_connection_id_metadata_accounts_account_id_categories_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **connection_id** | [**str**](.md)|  | 
 **account_id** | **str**|  | 
 **body** | [**CodatPublicApiModelsMetadataPatchSingleAccountCategoryModel**](CodatPublicApiModelsMetadataPatchSingleAccountCategoryModel.md)|  | [optional] 

### Return type

[**CodatPublicApiModelsMetadataAccountCategoriesModel**](CodatPublicApiModelsMetadataAccountCategoriesModel.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_connection_id_metadata_accounts_categories_get**
> CodatPublicApiModelsMetadataAccountCategoriesModelPagedResponseModel companies_company_id_connections_connection_id_metadata_accounts_categories_get(company_id, connection_id, page, page_size=page_size, query=query, order_by=order_by)



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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
page = 1 # int |  (default to 1)
page_size = 100 # int |  (optional) (default to 100)
query = 'query_example' # str |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    api_response = api_instance.companies_company_id_connections_connection_id_metadata_accounts_categories_get(company_id, connection_id, page, page_size=page_size, query=query, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->companies_company_id_connections_connection_id_metadata_accounts_categories_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **connection_id** | [**str**](.md)|  | 
 **page** | **int**|  | [default to 1]
 **page_size** | **int**|  | [optional] [default to 100]
 **query** | **str**|  | [optional] 
 **order_by** | **str**|  | [optional] 

### Return type

[**CodatPublicApiModelsMetadataAccountCategoriesModelPagedResponseModel**](CodatPublicApiModelsMetadataAccountCategoriesModelPagedResponseModel.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_connection_id_metadata_accounts_categories_patch**
> list[CodatPublicApiModelsMetadataAccountCategoriesModel] companies_company_id_connections_connection_id_metadata_accounts_categories_patch(company_id, connection_id, body=body)



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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = swagger_client.CodatPublicApiModelsMetadataPatchAccountCategoriesModel() # CodatPublicApiModelsMetadataPatchAccountCategoriesModel |  (optional)

try:
    api_response = api_instance.companies_company_id_connections_connection_id_metadata_accounts_categories_patch(company_id, connection_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->companies_company_id_connections_connection_id_metadata_accounts_categories_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **connection_id** | [**str**](.md)|  | 
 **body** | [**CodatPublicApiModelsMetadataPatchAccountCategoriesModel**](CodatPublicApiModelsMetadataPatchAccountCategoriesModel.md)|  | [optional] 

### Return type

[**list[CodatPublicApiModelsMetadataAccountCategoriesModel]**](CodatPublicApiModelsMetadataAccountCategoriesModel.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_connection_id_push_accounts_post**
> CodatDataContractsDatasetsAccountPushOperation companies_company_id_connections_connection_id_push_accounts_post(company_id, connection_id, body=body, timeout_in_minutes=timeout_in_minutes)

Posts an individual account for a given company.

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = swagger_client.CodatDataContractsDatasetsAccount() # CodatDataContractsDatasetsAccount |  (optional)
timeout_in_minutes = 56 # int |  (optional)

try:
    # Posts an individual account for a given company.
    api_response = api_instance.companies_company_id_connections_connection_id_push_accounts_post(company_id, connection_id, body=body, timeout_in_minutes=timeout_in_minutes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->companies_company_id_connections_connection_id_push_accounts_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **connection_id** | [**str**](.md)|  | 
 **body** | [**CodatDataContractsDatasetsAccount**](CodatDataContractsDatasetsAccount.md)|  | [optional] 
 **timeout_in_minutes** | **int**|  | [optional] 

### Return type

[**CodatDataContractsDatasetsAccountPushOperation**](CodatDataContractsDatasetsAccountPushOperation.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_data_accounts_account_id_get**
> CodatPublicApiModelsDataAccountResponse companies_company_id_data_accounts_account_id_get(company_id, account_id)

Gets a single account corresponding to the supplied Id

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
account_id = 'account_id_example' # str | 

try:
    # Gets a single account corresponding to the supplied Id
    api_response = api_instance.companies_company_id_data_accounts_account_id_get(company_id, account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->companies_company_id_data_accounts_account_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **account_id** | **str**|  | 

### Return type

[**CodatPublicApiModelsDataAccountResponse**](CodatPublicApiModelsDataAccountResponse.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_data_accounts_get**
> CodatDataContractsDatasetsAccountPagedResponseModel companies_company_id_data_accounts_get(company_id, page, page_size=page_size, query=query, order_by=order_by)

Gets the latest chart of accounts for a company

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
page = 1 # int |  (default to 1)
page_size = 100 # int |  (optional) (default to 100)
query = 'query_example' # str |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    # Gets the latest chart of accounts for a company
    api_response = api_instance.companies_company_id_data_accounts_get(company_id, page, page_size=page_size, query=query, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->companies_company_id_data_accounts_get: %s\n" % e)
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

[**CodatDataContractsDatasetsAccountPagedResponseModel**](CodatDataContractsDatasetsAccountPagedResponseModel.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metadata_accounts_categories_get**
> list[CodatPublicApiModelsMetadataValidCategoryType] metadata_accounts_categories_get()



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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.metadata_accounts_categories_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->metadata_accounts_categories_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CodatPublicApiModelsMetadataValidCategoryType]**](CodatPublicApiModelsMetadataValidCategoryType.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

