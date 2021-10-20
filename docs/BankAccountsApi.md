# codat_python_sdk.BankAccountsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_company_id_connections_connection_id_data_bank_accounts_account_id_bank_transactions_get**](BankAccountsApi.md#companies_company_id_connections_connection_id_data_bank_accounts_account_id_bank_transactions_get) | **GET** /companies/{companyId}/connections/{connectionId}/data/bankAccounts/{accountId}/bankTransactions | Gets bank transactions for a given bank account ID
[**companies_company_id_connections_connection_id_data_bank_accounts_account_id_get**](BankAccountsApi.md#companies_company_id_connections_connection_id_data_bank_accounts_account_id_get) | **GET** /companies/{companyId}/connections/{connectionId}/data/bankAccounts/{accountId} | Gets the bank account with a given ID
[**companies_company_id_connections_connection_id_data_bank_accounts_get**](BankAccountsApi.md#companies_company_id_connections_connection_id_data_bank_accounts_get) | **GET** /companies/{companyId}/connections/{connectionId}/data/bankAccounts | Gets the list of bank accounts for a given connection
[**companies_company_id_connections_connection_id_options_bank_accounts_account_id_bank_transactions_get**](BankAccountsApi.md#companies_company_id_connections_connection_id_options_bank_accounts_account_id_bank_transactions_get) | **GET** /companies/{companyId}/connections/{connectionId}/options/bankAccounts/{accountId}/bankTransactions | Gets the options of pushing bank account transactions.
[**companies_company_id_connections_connection_id_push_bank_accounts_account_id_bank_transactions_post**](BankAccountsApi.md#companies_company_id_connections_connection_id_push_bank_accounts_account_id_bank_transactions_post) | **POST** /companies/{companyId}/connections/{connectionId}/push/bankAccounts/{accountId}/bankTransactions | Posts bank transactions to the accounting package for a given company.
[**companies_company_id_connections_connection_id_push_bank_accounts_post**](BankAccountsApi.md#companies_company_id_connections_connection_id_push_bank_accounts_post) | **POST** /companies/{companyId}/connections/{connectionId}/push/bankAccounts | Posts a new bank account to the accounting package for a given company.
[**companies_company_id_data_bank_accounts_account_id_get**](BankAccountsApi.md#companies_company_id_data_bank_accounts_account_id_get) | **GET** /companies/{companyId}/data/bankAccounts/{accountId} | Gets the bank account for given account ID.
[**companies_company_id_data_bank_accounts_account_id_transactions_get**](BankAccountsApi.md#companies_company_id_data_bank_accounts_account_id_transactions_get) | **GET** /companies/{companyId}/data/bankAccounts/{accountId}/transactions | Gets the latest bank transactions for given account ID and company.


# **companies_company_id_connections_connection_id_data_bank_accounts_account_id_bank_transactions_get**
> CodatDataContractsDatasetsBankTransactionPagedResponseModel companies_company_id_connections_connection_id_data_bank_accounts_account_id_bank_transactions_get(company_id, connection_id, account_id, )

Gets bank transactions for a given bank account ID

### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import bank_accounts_api
from codat_python_sdk.model.codat_data_contracts_datasets_bank_transaction_paged_response_model import CodatDataContractsDatasetsBankTransactionPagedResponseModel
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
    api_instance = bank_accounts_api.BankAccountsApi(api_client)
    company_id = "companyId_example" # str | 
    connection_id = "connectionId_example" # str | 
    account_id = "accountId_example" # str | 
    page_size = 100 # int |  (optional) if omitted the server will use the default value of 100
    query = "query_example" # str |  (optional)
    order_by = "orderBy_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets bank transactions for a given bank account ID
        api_response = api_instance.companies_company_id_connections_connection_id_data_bank_accounts_account_id_bank_transactions_get(company_id, connection_id, account_id, )
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling BankAccountsApi->companies_company_id_connections_connection_id_data_bank_accounts_account_id_bank_transactions_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets bank transactions for a given bank account ID
        api_response = api_instance.companies_company_id_connections_connection_id_data_bank_accounts_account_id_bank_transactions_get(company_id, connection_id, account_id, page_size=page_size, query=query, order_by=order_by)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling BankAccountsApi->companies_company_id_connections_connection_id_data_bank_accounts_account_id_bank_transactions_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **connection_id** | **str**|  |
 **account_id** | **str**|  |
 **page** | **int**|  | defaults to 1
 **page_size** | **int**|  | [optional] if omitted the server will use the default value of 100
 **query** | **str**|  | [optional]
 **order_by** | **str**|  | [optional]

### Return type

[**CodatDataContractsDatasetsBankTransactionPagedResponseModel**](CodatDataContractsDatasetsBankTransactionPagedResponseModel.md)

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

# **companies_company_id_connections_connection_id_data_bank_accounts_account_id_get**
> CodatDataContractsDatasetsBankAccount companies_company_id_connections_connection_id_data_bank_accounts_account_id_get(company_id, connection_id, account_id)

Gets the bank account with a given ID

### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import bank_accounts_api
from codat_python_sdk.model.codat_data_contracts_datasets_bank_account import CodatDataContractsDatasetsBankAccount
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
    api_instance = bank_accounts_api.BankAccountsApi(api_client)
    company_id = "companyId_example" # str | 
    connection_id = "connectionId_example" # str | 
    account_id = "accountId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Gets the bank account with a given ID
        api_response = api_instance.companies_company_id_connections_connection_id_data_bank_accounts_account_id_get(company_id, connection_id, account_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling BankAccountsApi->companies_company_id_connections_connection_id_data_bank_accounts_account_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **connection_id** | **str**|  |
 **account_id** | **str**|  |

### Return type

[**CodatDataContractsDatasetsBankAccount**](CodatDataContractsDatasetsBankAccount.md)

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

# **companies_company_id_connections_connection_id_data_bank_accounts_get**
> CodatDataContractsDatasetsBankAccountPagedResponseModel companies_company_id_connections_connection_id_data_bank_accounts_get(company_id, connection_id, )

Gets the list of bank accounts for a given connection

### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import bank_accounts_api
from codat_python_sdk.model.codat_data_contracts_datasets_bank_account_paged_response_model import CodatDataContractsDatasetsBankAccountPagedResponseModel
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
    api_instance = bank_accounts_api.BankAccountsApi(api_client)
    company_id = "companyId_example" # str | 
    connection_id = "connectionId_example" # str | 
    page_size = 100 # int |  (optional) if omitted the server will use the default value of 100
    query = "query_example" # str |  (optional)
    order_by = "orderBy_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets the list of bank accounts for a given connection
        api_response = api_instance.companies_company_id_connections_connection_id_data_bank_accounts_get(company_id, connection_id, )
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling BankAccountsApi->companies_company_id_connections_connection_id_data_bank_accounts_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets the list of bank accounts for a given connection
        api_response = api_instance.companies_company_id_connections_connection_id_data_bank_accounts_get(company_id, connection_id, page_size=page_size, query=query, order_by=order_by)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling BankAccountsApi->companies_company_id_connections_connection_id_data_bank_accounts_get: %s\n" % e)
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

[**CodatDataContractsDatasetsBankAccountPagedResponseModel**](CodatDataContractsDatasetsBankAccountPagedResponseModel.md)

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

# **companies_company_id_connections_connection_id_options_bank_accounts_account_id_bank_transactions_get**
> CodatDataContractsPushPushOption companies_company_id_connections_connection_id_options_bank_accounts_account_id_bank_transactions_get(company_id, connection_id, account_id)

Gets the options of pushing bank account transactions.

### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import bank_accounts_api
from codat_python_sdk.model.codat_data_contracts_push_push_option import CodatDataContractsPushPushOption
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
    api_instance = bank_accounts_api.BankAccountsApi(api_client)
    company_id = "companyId_example" # str | 
    connection_id = "connectionId_example" # str | 
    account_id = "accountId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Gets the options of pushing bank account transactions.
        api_response = api_instance.companies_company_id_connections_connection_id_options_bank_accounts_account_id_bank_transactions_get(company_id, connection_id, account_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling BankAccountsApi->companies_company_id_connections_connection_id_options_bank_accounts_account_id_bank_transactions_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **connection_id** | **str**|  |
 **account_id** | **str**|  |

### Return type

[**CodatDataContractsPushPushOption**](CodatDataContractsPushPushOption.md)

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

# **companies_company_id_connections_connection_id_push_bank_accounts_account_id_bank_transactions_post**
> CodatDataContractsDatasetsBankTransactionsPushOperation companies_company_id_connections_connection_id_push_bank_accounts_account_id_bank_transactions_post(company_id, connection_id, account_id)

Posts bank transactions to the accounting package for a given company.

### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import bank_accounts_api
from codat_python_sdk.model.codat_data_contracts_datasets_bank_transactions import CodatDataContractsDatasetsBankTransactions
from codat_python_sdk.model.codat_data_contracts_datasets_bank_transactions_push_operation import CodatDataContractsDatasetsBankTransactionsPushOperation
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
    api_instance = bank_accounts_api.BankAccountsApi(api_client)
    company_id = "companyId_example" # str | 
    connection_id = "connectionId_example" # str | 
    account_id = "accountId_example" # str | 
    allow_sync_on_push_complete = True # bool |  (optional) if omitted the server will use the default value of True
    timeout_in_minutes = 1 # int |  (optional)
    codat_data_contracts_datasets_bank_transactions = CodatDataContractsDatasetsBankTransactions(
        account_id="account_id_example",
        transactions=[
            CodatDataContractsDatasetsBankStatementLine(
                id="id_example",
                date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                description="description_example",
                reconciled=True,
                amount=3.14,
                balance=3.14,
                transaction_type=CodatDataContractsDatasetsTransactionType("Unknown"),
                modified_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                source_modified_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
            ),
        ],
        contract_version="contract_version_example",
    ) # CodatDataContractsDatasetsBankTransactions |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Posts bank transactions to the accounting package for a given company.
        api_response = api_instance.companies_company_id_connections_connection_id_push_bank_accounts_account_id_bank_transactions_post(company_id, connection_id, account_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling BankAccountsApi->companies_company_id_connections_connection_id_push_bank_accounts_account_id_bank_transactions_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Posts bank transactions to the accounting package for a given company.
        api_response = api_instance.companies_company_id_connections_connection_id_push_bank_accounts_account_id_bank_transactions_post(company_id, connection_id, account_id, allow_sync_on_push_complete=allow_sync_on_push_complete, timeout_in_minutes=timeout_in_minutes, codat_data_contracts_datasets_bank_transactions=codat_data_contracts_datasets_bank_transactions)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling BankAccountsApi->companies_company_id_connections_connection_id_push_bank_accounts_account_id_bank_transactions_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **connection_id** | **str**|  |
 **account_id** | **str**|  |
 **allow_sync_on_push_complete** | **bool**|  | [optional] if omitted the server will use the default value of True
 **timeout_in_minutes** | **int**|  | [optional]
 **codat_data_contracts_datasets_bank_transactions** | [**CodatDataContractsDatasetsBankTransactions**](CodatDataContractsDatasetsBankTransactions.md)|  | [optional]

### Return type

[**CodatDataContractsDatasetsBankTransactionsPushOperation**](CodatDataContractsDatasetsBankTransactionsPushOperation.md)

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

# **companies_company_id_connections_connection_id_push_bank_accounts_post**
> CodatDataContractsDatasetsBankStatementAccountPushOperation companies_company_id_connections_connection_id_push_bank_accounts_post(company_id, connection_id)

Posts a new bank account to the accounting package for a given company.

### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import bank_accounts_api
from codat_python_sdk.model.codat_data_contracts_datasets_bank_statement_account_push_operation import CodatDataContractsDatasetsBankStatementAccountPushOperation
from codat_python_sdk.model.codat_data_contracts_datasets_bank_statement_account import CodatDataContractsDatasetsBankStatementAccount
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
    api_instance = bank_accounts_api.BankAccountsApi(api_client)
    company_id = "companyId_example" # str | 
    connection_id = "connectionId_example" # str | 
    allow_sync_on_push_complete = True # bool |  (optional) if omitted the server will use the default value of True
    timeout_in_minutes = 1 # int |  (optional)
    codat_data_contracts_datasets_bank_statement_account = CodatDataContractsDatasetsBankStatementAccount(
        id="id_example",
        account_name="account_name_example",
        from_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        to_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        nominal_code="nominal_code_example",
        sort_code="sort_code_example",
        account_number="account_number_example",
        iban="iban_example",
        currency="currency_example",
        balance=3.14,
        available_balance=3.14,
        modified_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        source_modified_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        overdraft_limit=3.14,
        institution="institution_example",
    ) # CodatDataContractsDatasetsBankStatementAccount |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Posts a new bank account to the accounting package for a given company.
        api_response = api_instance.companies_company_id_connections_connection_id_push_bank_accounts_post(company_id, connection_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling BankAccountsApi->companies_company_id_connections_connection_id_push_bank_accounts_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Posts a new bank account to the accounting package for a given company.
        api_response = api_instance.companies_company_id_connections_connection_id_push_bank_accounts_post(company_id, connection_id, allow_sync_on_push_complete=allow_sync_on_push_complete, timeout_in_minutes=timeout_in_minutes, codat_data_contracts_datasets_bank_statement_account=codat_data_contracts_datasets_bank_statement_account)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling BankAccountsApi->companies_company_id_connections_connection_id_push_bank_accounts_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **connection_id** | **str**|  |
 **allow_sync_on_push_complete** | **bool**|  | [optional] if omitted the server will use the default value of True
 **timeout_in_minutes** | **int**|  | [optional]
 **codat_data_contracts_datasets_bank_statement_account** | [**CodatDataContractsDatasetsBankStatementAccount**](CodatDataContractsDatasetsBankStatementAccount.md)|  | [optional]

### Return type

[**CodatDataContractsDatasetsBankStatementAccountPushOperation**](CodatDataContractsDatasetsBankStatementAccountPushOperation.md)

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

# **companies_company_id_data_bank_accounts_account_id_get**
> CodatDataContractsDatasetsBankStatementAccount companies_company_id_data_bank_accounts_account_id_get(company_id, account_id)

Gets the bank account for given account ID.

### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import bank_accounts_api
from codat_python_sdk.model.codat_data_contracts_datasets_bank_statement_account import CodatDataContractsDatasetsBankStatementAccount
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
    api_instance = bank_accounts_api.BankAccountsApi(api_client)
    company_id = "companyId_example" # str | 
    account_id = "accountId_example" # str | 
    query = "query_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets the bank account for given account ID.
        api_response = api_instance.companies_company_id_data_bank_accounts_account_id_get(company_id, account_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling BankAccountsApi->companies_company_id_data_bank_accounts_account_id_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets the bank account for given account ID.
        api_response = api_instance.companies_company_id_data_bank_accounts_account_id_get(company_id, account_id, query=query)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling BankAccountsApi->companies_company_id_data_bank_accounts_account_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **account_id** | **str**|  |
 **query** | **str**|  | [optional]

### Return type

[**CodatDataContractsDatasetsBankStatementAccount**](CodatDataContractsDatasetsBankStatementAccount.md)

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

# **companies_company_id_data_bank_accounts_account_id_transactions_get**
> CodatDataContractsDatasetsBankStatementLinePagedResponseModel companies_company_id_data_bank_accounts_account_id_transactions_get(company_id, account_id, )

Gets the latest bank transactions for given account ID and company.

### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import bank_accounts_api
from codat_python_sdk.model.codat_data_contracts_datasets_bank_statement_line_paged_response_model import CodatDataContractsDatasetsBankStatementLinePagedResponseModel
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
    api_instance = bank_accounts_api.BankAccountsApi(api_client)
    company_id = "companyId_example" # str | 
    account_id = "accountId_example" # str | 
    page_size = 100 # int |  (optional) if omitted the server will use the default value of 100
    query = "query_example" # str |  (optional)
    order_by = "orderBy_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets the latest bank transactions for given account ID and company.
        api_response = api_instance.companies_company_id_data_bank_accounts_account_id_transactions_get(company_id, account_id, )
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling BankAccountsApi->companies_company_id_data_bank_accounts_account_id_transactions_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets the latest bank transactions for given account ID and company.
        api_response = api_instance.companies_company_id_data_bank_accounts_account_id_transactions_get(company_id, account_id, page_size=page_size, query=query, order_by=order_by)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling BankAccountsApi->companies_company_id_data_bank_accounts_account_id_transactions_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **account_id** | **str**|  |
 **page** | **int**|  | defaults to 1
 **page_size** | **int**|  | [optional] if omitted the server will use the default value of 100
 **query** | **str**|  | [optional]
 **order_by** | **str**|  | [optional]

### Return type

[**CodatDataContractsDatasetsBankStatementLinePagedResponseModel**](CodatDataContractsDatasetsBankStatementLinePagedResponseModel.md)

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

