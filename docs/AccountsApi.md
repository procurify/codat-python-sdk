# codat_python_sdk.AccountsApi

All URIs are relative to *http://localhost*

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

* Api Key Authentication (API Key Auth):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import accounts_api
from codat_python_sdk.model.codat_public_api_models_metadata_account_categories_model import CodatPublicApiModelsMetadataAccountCategoriesModel
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
    api_instance = accounts_api.AccountsApi(api_client)
    company_id = "companyId_example" # str | 
    connection_id = "connectionId_example" # str | 
    account_id = "accountId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.companies_company_id_connections_connection_id_metadata_accounts_account_id_categories_get(company_id, connection_id, account_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling AccountsApi->companies_company_id_connections_connection_id_metadata_accounts_account_id_categories_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **connection_id** | **str**|  |
 **account_id** | **str**|  |

### Return type

[**CodatPublicApiModelsMetadataAccountCategoriesModel**](CodatPublicApiModelsMetadataAccountCategoriesModel.md)

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

# **companies_company_id_connections_connection_id_metadata_accounts_account_id_categories_patch**
> CodatPublicApiModelsMetadataAccountCategoriesModel companies_company_id_connections_connection_id_metadata_accounts_account_id_categories_patch(company_id, connection_id, account_id)



### Example

* Api Key Authentication (API Key Auth):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import accounts_api
from codat_python_sdk.model.codat_public_api_models_metadata_account_categories_model import CodatPublicApiModelsMetadataAccountCategoriesModel
from codat_python_sdk.model.codat_public_api_models_metadata_patch_single_account_category_model import CodatPublicApiModelsMetadataPatchSingleAccountCategoryModel
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
    api_instance = accounts_api.AccountsApi(api_client)
    company_id = "companyId_example" # str | 
    connection_id = "connectionId_example" # str | 
    account_id = "accountId_example" # str | 
    codat_public_api_models_metadata_patch_single_account_category_model = CodatPublicApiModelsMetadataPatchSingleAccountCategoryModel(
        confirmed=CodatPublicApiModelsMetadataConfirmedAccountCategoryModel(
            type="type_example",
            subtype="subtype_example",
            detail_type="detail_type_example",
        ),
    ) # CodatPublicApiModelsMetadataPatchSingleAccountCategoryModel |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.companies_company_id_connections_connection_id_metadata_accounts_account_id_categories_patch(company_id, connection_id, account_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling AccountsApi->companies_company_id_connections_connection_id_metadata_accounts_account_id_categories_patch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.companies_company_id_connections_connection_id_metadata_accounts_account_id_categories_patch(company_id, connection_id, account_id, codat_public_api_models_metadata_patch_single_account_category_model=codat_public_api_models_metadata_patch_single_account_category_model)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling AccountsApi->companies_company_id_connections_connection_id_metadata_accounts_account_id_categories_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **connection_id** | **str**|  |
 **account_id** | **str**|  |
 **codat_public_api_models_metadata_patch_single_account_category_model** | [**CodatPublicApiModelsMetadataPatchSingleAccountCategoryModel**](CodatPublicApiModelsMetadataPatchSingleAccountCategoryModel.md)|  | [optional]

### Return type

[**CodatPublicApiModelsMetadataAccountCategoriesModel**](CodatPublicApiModelsMetadataAccountCategoriesModel.md)

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

# **companies_company_id_connections_connection_id_metadata_accounts_categories_get**
> CodatPublicApiModelsMetadataAccountCategoriesModelPagedResponseModel companies_company_id_connections_connection_id_metadata_accounts_categories_get(company_id, connection_id, )



### Example

* Api Key Authentication (API Key Auth):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import accounts_api
from codat_python_sdk.model.codat_public_api_models_metadata_account_categories_model_paged_response_model import CodatPublicApiModelsMetadataAccountCategoriesModelPagedResponseModel
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
    api_instance = accounts_api.AccountsApi(api_client)
    company_id = "companyId_example" # str | 
    connection_id = "connectionId_example" # str | 
    page_size = 100 # int |  (optional) if omitted the server will use the default value of 100
    query = "query_example" # str |  (optional)
    order_by = "orderBy_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.companies_company_id_connections_connection_id_metadata_accounts_categories_get(company_id, connection_id, )
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling AccountsApi->companies_company_id_connections_connection_id_metadata_accounts_categories_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.companies_company_id_connections_connection_id_metadata_accounts_categories_get(company_id, connection_id, page_size=page_size, query=query, order_by=order_by)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling AccountsApi->companies_company_id_connections_connection_id_metadata_accounts_categories_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **connection_id** | **str**|  |
 **page** | **int**|  | defaults to 1
 **page_size** | **int**|  | [optional] if omitted the server will use the default value of 100
 **query** | **str**|  | [optional]
 **order_by** | **str**|  | [optional]

### Return type

[**CodatPublicApiModelsMetadataAccountCategoriesModelPagedResponseModel**](CodatPublicApiModelsMetadataAccountCategoriesModelPagedResponseModel.md)

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

# **companies_company_id_connections_connection_id_metadata_accounts_categories_patch**
> [CodatPublicApiModelsMetadataAccountCategoriesModel] companies_company_id_connections_connection_id_metadata_accounts_categories_patch(company_id, connection_id)



### Example

* Api Key Authentication (API Key Auth):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import accounts_api
from codat_python_sdk.model.codat_public_api_models_metadata_account_categories_model import CodatPublicApiModelsMetadataAccountCategoriesModel
from codat_python_sdk.model.codat_public_api_models_metadata_patch_account_categories_model import CodatPublicApiModelsMetadataPatchAccountCategoriesModel
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
    api_instance = accounts_api.AccountsApi(api_client)
    company_id = "companyId_example" # str | 
    connection_id = "connectionId_example" # str | 
    codat_public_api_models_metadata_patch_account_categories_model = CodatPublicApiModelsMetadataPatchAccountCategoriesModel(
        categories=[
            CodatPublicApiModelsMetadataPatchAccountCategoryModel(
                account_ref=CodatPublicApiModelsMetadataPatchAccountRefModel(
                    id="id_example",
                ),
                confirmed=CodatPublicApiModelsMetadataConfirmedAccountCategoryModel(
                    type="type_example",
                    subtype="subtype_example",
                    detail_type="detail_type_example",
                ),
            ),
        ],
    ) # CodatPublicApiModelsMetadataPatchAccountCategoriesModel |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.companies_company_id_connections_connection_id_metadata_accounts_categories_patch(company_id, connection_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling AccountsApi->companies_company_id_connections_connection_id_metadata_accounts_categories_patch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.companies_company_id_connections_connection_id_metadata_accounts_categories_patch(company_id, connection_id, codat_public_api_models_metadata_patch_account_categories_model=codat_public_api_models_metadata_patch_account_categories_model)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling AccountsApi->companies_company_id_connections_connection_id_metadata_accounts_categories_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **connection_id** | **str**|  |
 **codat_public_api_models_metadata_patch_account_categories_model** | [**CodatPublicApiModelsMetadataPatchAccountCategoriesModel**](CodatPublicApiModelsMetadataPatchAccountCategoriesModel.md)|  | [optional]

### Return type

[**[CodatPublicApiModelsMetadataAccountCategoriesModel]**](CodatPublicApiModelsMetadataAccountCategoriesModel.md)

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

# **companies_company_id_connections_connection_id_push_accounts_post**
> CodatDataContractsDatasetsAccountPushOperation companies_company_id_connections_connection_id_push_accounts_post(company_id, connection_id)

Posts an individual account for a given company.

### Example

* Api Key Authentication (API Key Auth):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import accounts_api
from codat_python_sdk.model.codat_data_contracts_datasets_account_push_operation import CodatDataContractsDatasetsAccountPushOperation
from codat_python_sdk.model.codat_data_contracts_datasets_account import CodatDataContractsDatasetsAccount
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
    api_instance = accounts_api.AccountsApi(api_client)
    company_id = "companyId_example" # str | 
    connection_id = "connectionId_example" # str | 
    timeout_in_minutes = 1 # int |  (optional)
    codat_data_contracts_datasets_account = CodatDataContractsDatasetsAccount(
        id="id_example",
        nominal_code="nominal_code_example",
        name="name_example",
        description="description_example",
        fully_qualified_category="fully_qualified_category_example",
        fully_qualified_name="fully_qualified_name_example",
        currency="currency_example",
        current_balance=3.14,
        type=CodatDataContractsDatasetsAccountType("Unknown"),
        status=CodatDataContractsDatasetsAccountStatus("Unknown"),
        is_bank_account=True,
        modified_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        source_modified_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        valid_datatype_links=[
            CodatDataContractsDatasetsValidDatatypeLinks(
                _property="_property_example",
                links=[
                    "links_example",
                ],
            ),
        ],
    ) # CodatDataContractsDatasetsAccount |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Posts an individual account for a given company.
        api_response = api_instance.companies_company_id_connections_connection_id_push_accounts_post(company_id, connection_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling AccountsApi->companies_company_id_connections_connection_id_push_accounts_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Posts an individual account for a given company.
        api_response = api_instance.companies_company_id_connections_connection_id_push_accounts_post(company_id, connection_id, timeout_in_minutes=timeout_in_minutes, codat_data_contracts_datasets_account=codat_data_contracts_datasets_account)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling AccountsApi->companies_company_id_connections_connection_id_push_accounts_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **connection_id** | **str**|  |
 **timeout_in_minutes** | **int**|  | [optional]
 **codat_data_contracts_datasets_account** | [**CodatDataContractsDatasetsAccount**](CodatDataContractsDatasetsAccount.md)|  | [optional]

### Return type

[**CodatDataContractsDatasetsAccountPushOperation**](CodatDataContractsDatasetsAccountPushOperation.md)

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

# **companies_company_id_data_accounts_account_id_get**
> CodatPublicApiModelsDataAccountResponse companies_company_id_data_accounts_account_id_get(company_id, account_id)

Gets a single account corresponding to the supplied Id

### Example

* Api Key Authentication (API Key Auth):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import accounts_api
from codat_python_sdk.model.codat_public_api_models_data_account_response import CodatPublicApiModelsDataAccountResponse
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
    api_instance = accounts_api.AccountsApi(api_client)
    company_id = "companyId_example" # str | 
    account_id = "accountId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Gets a single account corresponding to the supplied Id
        api_response = api_instance.companies_company_id_data_accounts_account_id_get(company_id, account_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling AccountsApi->companies_company_id_data_accounts_account_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **account_id** | **str**|  |

### Return type

[**CodatPublicApiModelsDataAccountResponse**](CodatPublicApiModelsDataAccountResponse.md)

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

# **companies_company_id_data_accounts_get**
> CodatDataContractsDatasetsAccountPagedResponseModel companies_company_id_data_accounts_get(company_id, )

Gets the latest chart of accounts for a company

### Example

* Api Key Authentication (API Key Auth):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import accounts_api
from codat_python_sdk.model.codat_data_contracts_datasets_account_paged_response_model import CodatDataContractsDatasetsAccountPagedResponseModel
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
    api_instance = accounts_api.AccountsApi(api_client)
    company_id = "companyId_example" # str | 
    page_size = 100 # int |  (optional) if omitted the server will use the default value of 100
    query = "query_example" # str |  (optional)
    order_by = "orderBy_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets the latest chart of accounts for a company
        api_response = api_instance.companies_company_id_data_accounts_get(company_id, )
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling AccountsApi->companies_company_id_data_accounts_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets the latest chart of accounts for a company
        api_response = api_instance.companies_company_id_data_accounts_get(company_id, page_size=page_size, query=query, order_by=order_by)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling AccountsApi->companies_company_id_data_accounts_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **page** | **int**|  | defaults to 1
 **page_size** | **int**|  | [optional] if omitted the server will use the default value of 100
 **query** | **str**|  | [optional]
 **order_by** | **str**|  | [optional]

### Return type

[**CodatDataContractsDatasetsAccountPagedResponseModel**](CodatDataContractsDatasetsAccountPagedResponseModel.md)

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

# **metadata_accounts_categories_get**
> [CodatPublicApiModelsMetadataValidCategoryType] metadata_accounts_categories_get()



### Example

* Api Key Authentication (API Key Auth):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import accounts_api
from codat_python_sdk.model.codat_public_api_models_metadata_valid_category_type import CodatPublicApiModelsMetadataValidCategoryType
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
    api_instance = accounts_api.AccountsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.metadata_accounts_categories_get()
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling AccountsApi->metadata_accounts_categories_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[CodatPublicApiModelsMetadataValidCategoryType]**](CodatPublicApiModelsMetadataValidCategoryType.md)

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

