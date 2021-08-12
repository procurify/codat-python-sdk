# swagger_client.BankStatementsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_company_id_data_bank_statements_accounts_get**](BankStatementsApi.md#companies_company_id_data_bank_statements_accounts_get) | **GET** /companies/{companyId}/data/bankStatements/accounts | Gets the latest bank statements for a company, with pagination
[**companies_company_id_data_bank_statements_get**](BankStatementsApi.md#companies_company_id_data_bank_statements_get) | **GET** /companies/{companyId}/data/bankStatements | Gets the latest bank statements for a company, with pagination

# **companies_company_id_data_bank_statements_accounts_get**
> list[CodatDataContractsDatasetsBankStatementAccount] companies_company_id_data_bank_statements_accounts_get(company_id, query=query)

Gets the latest bank statements for a company, with pagination

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
api_instance = swagger_client.BankStatementsApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
query = 'query_example' # str |  (optional)

try:
    # Gets the latest bank statements for a company, with pagination
    api_response = api_instance.companies_company_id_data_bank_statements_accounts_get(company_id, query=query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankStatementsApi->companies_company_id_data_bank_statements_accounts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **query** | **str**|  | [optional] 

### Return type

[**list[CodatDataContractsDatasetsBankStatementAccount]**](CodatDataContractsDatasetsBankStatementAccount.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_data_bank_statements_get**
> CodatDataContractsDatasetsBankStatementLinePagedResponseModel companies_company_id_data_bank_statements_get(company_id, page, account_id=account_id, page_size=page_size, query=query, order_by=order_by)

Gets the latest bank statements for a company, with pagination

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
api_instance = swagger_client.BankStatementsApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
page = 1 # int |  (default to 1)
account_id = 'account_id_example' # str |  (optional)
page_size = 100 # int |  (optional) (default to 100)
query = 'query_example' # str |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    # Gets the latest bank statements for a company, with pagination
    api_response = api_instance.companies_company_id_data_bank_statements_get(company_id, page, account_id=account_id, page_size=page_size, query=query, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankStatementsApi->companies_company_id_data_bank_statements_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **page** | **int**|  | [default to 1]
 **account_id** | **str**|  | [optional] 
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

