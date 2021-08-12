# swagger_client.BankAccountsApi

All URIs are relative to */*

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
> CodatDataContractsDatasetsBankTransactionPagedResponseModel companies_company_id_connections_connection_id_data_bank_accounts_account_id_bank_transactions_get(company_id, connection_id, account_id, page, page_size=page_size, query=query, order_by=order_by)

Gets bank transactions for a given bank account ID

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
api_instance = swagger_client.BankAccountsApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
account_id = 'account_id_example' # str | 
page = 1 # int |  (default to 1)
page_size = 100 # int |  (optional) (default to 100)
query = 'query_example' # str |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    # Gets bank transactions for a given bank account ID
    api_response = api_instance.companies_company_id_connections_connection_id_data_bank_accounts_account_id_bank_transactions_get(company_id, connection_id, account_id, page, page_size=page_size, query=query, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankAccountsApi->companies_company_id_connections_connection_id_data_bank_accounts_account_id_bank_transactions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **connection_id** | [**str**](.md)|  | 
 **account_id** | **str**|  | 
 **page** | **int**|  | [default to 1]
 **page_size** | **int**|  | [optional] [default to 100]
 **query** | **str**|  | [optional] 
 **order_by** | **str**|  | [optional] 

### Return type

[**CodatDataContractsDatasetsBankTransactionPagedResponseModel**](CodatDataContractsDatasetsBankTransactionPagedResponseModel.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_connection_id_data_bank_accounts_account_id_get**
> CodatDataContractsDatasetsBankAccount companies_company_id_connections_connection_id_data_bank_accounts_account_id_get(company_id, connection_id, account_id)

Gets the bank account with a given ID

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
api_instance = swagger_client.BankAccountsApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
account_id = 'account_id_example' # str | 

try:
    # Gets the bank account with a given ID
    api_response = api_instance.companies_company_id_connections_connection_id_data_bank_accounts_account_id_get(company_id, connection_id, account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankAccountsApi->companies_company_id_connections_connection_id_data_bank_accounts_account_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **connection_id** | [**str**](.md)|  | 
 **account_id** | **str**|  | 

### Return type

[**CodatDataContractsDatasetsBankAccount**](CodatDataContractsDatasetsBankAccount.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_connection_id_data_bank_accounts_get**
> CodatDataContractsDatasetsBankAccountPagedResponseModel companies_company_id_connections_connection_id_data_bank_accounts_get(company_id, connection_id, page, page_size=page_size, query=query, order_by=order_by)

Gets the list of bank accounts for a given connection

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
api_instance = swagger_client.BankAccountsApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
page = 1 # int |  (default to 1)
page_size = 100 # int |  (optional) (default to 100)
query = 'query_example' # str |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    # Gets the list of bank accounts for a given connection
    api_response = api_instance.companies_company_id_connections_connection_id_data_bank_accounts_get(company_id, connection_id, page, page_size=page_size, query=query, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankAccountsApi->companies_company_id_connections_connection_id_data_bank_accounts_get: %s\n" % e)
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

[**CodatDataContractsDatasetsBankAccountPagedResponseModel**](CodatDataContractsDatasetsBankAccountPagedResponseModel.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_connection_id_options_bank_accounts_account_id_bank_transactions_get**
> CodatDataContractsPushPushOption companies_company_id_connections_connection_id_options_bank_accounts_account_id_bank_transactions_get(company_id, connection_id, account_id)

Gets the options of pushing bank account transactions.

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
api_instance = swagger_client.BankAccountsApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
account_id = 'account_id_example' # str | 

try:
    # Gets the options of pushing bank account transactions.
    api_response = api_instance.companies_company_id_connections_connection_id_options_bank_accounts_account_id_bank_transactions_get(company_id, connection_id, account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankAccountsApi->companies_company_id_connections_connection_id_options_bank_accounts_account_id_bank_transactions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **connection_id** | [**str**](.md)|  | 
 **account_id** | **str**|  | 

### Return type

[**CodatDataContractsPushPushOption**](CodatDataContractsPushPushOption.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_connection_id_push_bank_accounts_account_id_bank_transactions_post**
> CodatDataContractsDatasetsBankTransactionsPushOperation companies_company_id_connections_connection_id_push_bank_accounts_account_id_bank_transactions_post(company_id, connection_id, account_id, body=body, allow_sync_on_push_complete=allow_sync_on_push_complete, timeout_in_minutes=timeout_in_minutes)

Posts bank transactions to the accounting package for a given company.

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
api_instance = swagger_client.BankAccountsApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
account_id = 'account_id_example' # str | 
body = swagger_client.CodatDataContractsDatasetsBankTransactions() # CodatDataContractsDatasetsBankTransactions |  (optional)
allow_sync_on_push_complete = true # bool |  (optional) (default to true)
timeout_in_minutes = 56 # int |  (optional)

try:
    # Posts bank transactions to the accounting package for a given company.
    api_response = api_instance.companies_company_id_connections_connection_id_push_bank_accounts_account_id_bank_transactions_post(company_id, connection_id, account_id, body=body, allow_sync_on_push_complete=allow_sync_on_push_complete, timeout_in_minutes=timeout_in_minutes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankAccountsApi->companies_company_id_connections_connection_id_push_bank_accounts_account_id_bank_transactions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **connection_id** | [**str**](.md)|  | 
 **account_id** | **str**|  | 
 **body** | [**CodatDataContractsDatasetsBankTransactions**](CodatDataContractsDatasetsBankTransactions.md)|  | [optional] 
 **allow_sync_on_push_complete** | **bool**|  | [optional] [default to true]
 **timeout_in_minutes** | **int**|  | [optional] 

### Return type

[**CodatDataContractsDatasetsBankTransactionsPushOperation**](CodatDataContractsDatasetsBankTransactionsPushOperation.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_connection_id_push_bank_accounts_post**
> CodatDataContractsDatasetsBankStatementAccountPushOperation companies_company_id_connections_connection_id_push_bank_accounts_post(company_id, connection_id, body=body, allow_sync_on_push_complete=allow_sync_on_push_complete, timeout_in_minutes=timeout_in_minutes)

Posts a new bank account to the accounting package for a given company.

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
api_instance = swagger_client.BankAccountsApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = swagger_client.CodatDataContractsDatasetsBankStatementAccount() # CodatDataContractsDatasetsBankStatementAccount |  (optional)
allow_sync_on_push_complete = true # bool |  (optional) (default to true)
timeout_in_minutes = 56 # int |  (optional)

try:
    # Posts a new bank account to the accounting package for a given company.
    api_response = api_instance.companies_company_id_connections_connection_id_push_bank_accounts_post(company_id, connection_id, body=body, allow_sync_on_push_complete=allow_sync_on_push_complete, timeout_in_minutes=timeout_in_minutes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankAccountsApi->companies_company_id_connections_connection_id_push_bank_accounts_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **connection_id** | [**str**](.md)|  | 
 **body** | [**CodatDataContractsDatasetsBankStatementAccount**](CodatDataContractsDatasetsBankStatementAccount.md)|  | [optional] 
 **allow_sync_on_push_complete** | **bool**|  | [optional] [default to true]
 **timeout_in_minutes** | **int**|  | [optional] 

### Return type

[**CodatDataContractsDatasetsBankStatementAccountPushOperation**](CodatDataContractsDatasetsBankStatementAccountPushOperation.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_data_bank_accounts_account_id_get**
> CodatDataContractsDatasetsBankStatementAccount companies_company_id_data_bank_accounts_account_id_get(company_id, account_id, query=query)

Gets the bank account for given account ID.

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
api_instance = swagger_client.BankAccountsApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
account_id = 'account_id_example' # str | 
query = 'query_example' # str |  (optional)

try:
    # Gets the bank account for given account ID.
    api_response = api_instance.companies_company_id_data_bank_accounts_account_id_get(company_id, account_id, query=query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankAccountsApi->companies_company_id_data_bank_accounts_account_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **account_id** | **str**|  | 
 **query** | **str**|  | [optional] 

### Return type

[**CodatDataContractsDatasetsBankStatementAccount**](CodatDataContractsDatasetsBankStatementAccount.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_data_bank_accounts_account_id_transactions_get**
> CodatDataContractsDatasetsBankStatementLinePagedResponseModel companies_company_id_data_bank_accounts_account_id_transactions_get(company_id, account_id, page, page_size=page_size, query=query, order_by=order_by)

Gets the latest bank transactions for given account ID and company.

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
api_instance = swagger_client.BankAccountsApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
account_id = 'account_id_example' # str | 
page = 1 # int |  (default to 1)
page_size = 100 # int |  (optional) (default to 100)
query = 'query_example' # str |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    # Gets the latest bank transactions for given account ID and company.
    api_response = api_instance.companies_company_id_data_bank_accounts_account_id_transactions_get(company_id, account_id, page, page_size=page_size, query=query, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankAccountsApi->companies_company_id_data_bank_accounts_account_id_transactions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **account_id** | **str**|  | 
 **page** | **int**|  | [default to 1]
 **page_size** | **int**|  | [optional] [default to 100]
 **query** | **str**|  | [optional] 
 **order_by** | **str**|  | [optional] 

### Return type

[**CodatDataContractsDatasetsBankStatementLinePagedResponseModel**](CodatDataContractsDatasetsBankStatementLinePagedResponseModel.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

