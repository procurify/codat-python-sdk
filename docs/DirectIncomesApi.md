# codat_python_sdk.DirectIncomesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_company_id_connections_connection_id_data_direct_incomes_direct_income_id_get**](DirectIncomesApi.md#companies_company_id_connections_connection_id_data_direct_incomes_direct_income_id_get) | **GET** /companies/{companyId}/connections/{connectionId}/data/directIncomes/{directIncomeId} | Gets the specified direct income for a given company and connection.
[**companies_company_id_connections_connection_id_data_direct_incomes_get**](DirectIncomesApi.md#companies_company_id_connections_connection_id_data_direct_incomes_get) | **GET** /companies/{companyId}/connections/{connectionId}/data/directIncomes | Gets the direct incomes for a given company.
[**companies_company_id_connections_connection_id_push_direct_incomes_post**](DirectIncomesApi.md#companies_company_id_connections_connection_id_push_direct_incomes_post) | **POST** /companies/{companyId}/connections/{connectionId}/push/directIncomes | Posts a new direct income to the accounting package for a given company.

# **companies_company_id_connections_connection_id_data_direct_incomes_direct_income_id_get**
> CodatDataContractsDatasetsDirectIncome companies_company_id_connections_connection_id_data_direct_incomes_direct_income_id_get(company_id, connection_id, direct_income_id)

Gets the specified direct income for a given company and connection.

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
api_instance = codat_python_sdk.DirectIncomesApi(codat_python_sdk.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
direct_income_id = 'direct_income_id_example' # str | 

try:
    # Gets the specified direct income for a given company and connection.
    api_response = api_instance.companies_company_id_connections_connection_id_data_direct_incomes_direct_income_id_get(company_id, connection_id, direct_income_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DirectIncomesApi->companies_company_id_connections_connection_id_data_direct_incomes_direct_income_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **connection_id** | [**str**](.md)|  | 
 **direct_income_id** | **str**|  | 

### Return type

[**CodatDataContractsDatasetsDirectIncome**](CodatDataContractsDatasetsDirectIncome.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_connection_id_data_direct_incomes_get**
> CodatDataContractsDatasetsDirectIncomePagedResponseModel companies_company_id_connections_connection_id_data_direct_incomes_get(company_id, connection_id, page, page_size=page_size, query=query, order_by=order_by)

Gets the direct incomes for a given company.

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
api_instance = codat_python_sdk.DirectIncomesApi(codat_python_sdk.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
page = 1 # int |  (default to 1)
page_size = 100 # int |  (optional) (default to 100)
query = 'query_example' # str |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    # Gets the direct incomes for a given company.
    api_response = api_instance.companies_company_id_connections_connection_id_data_direct_incomes_get(company_id, connection_id, page, page_size=page_size, query=query, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DirectIncomesApi->companies_company_id_connections_connection_id_data_direct_incomes_get: %s\n" % e)
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

[**CodatDataContractsDatasetsDirectIncomePagedResponseModel**](CodatDataContractsDatasetsDirectIncomePagedResponseModel.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_connection_id_push_direct_incomes_post**
> CodatDataContractsDatasetsDirectIncomePushOperation companies_company_id_connections_connection_id_push_direct_incomes_post(company_id, connection_id, body=body, timeout_in_minutes=timeout_in_minutes)

Posts a new direct income to the accounting package for a given company.

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
api_instance = codat_python_sdk.DirectIncomesApi(codat_python_sdk.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = codat_python_sdk.CodatDataContractsDatasetsDirectIncome() # CodatDataContractsDatasetsDirectIncome |  (optional)
timeout_in_minutes = 56 # int |  (optional)

try:
    # Posts a new direct income to the accounting package for a given company.
    api_response = api_instance.companies_company_id_connections_connection_id_push_direct_incomes_post(company_id, connection_id, body=body, timeout_in_minutes=timeout_in_minutes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DirectIncomesApi->companies_company_id_connections_connection_id_push_direct_incomes_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **connection_id** | [**str**](.md)|  | 
 **body** | [**CodatDataContractsDatasetsDirectIncome**](CodatDataContractsDatasetsDirectIncome.md)|  | [optional] 
 **timeout_in_minutes** | **int**|  | [optional] 

### Return type

[**CodatDataContractsDatasetsDirectIncomePushOperation**](CodatDataContractsDatasetsDirectIncomePushOperation.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

