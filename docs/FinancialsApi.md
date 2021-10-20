# codat_python_sdk.FinancialsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_company_id_data_financials_balance_sheet_get**](FinancialsApi.md#companies_company_id_data_financials_balance_sheet_get) | **GET** /companies/{companyId}/data/financials/balanceSheet | Gets the latest balance sheet for a company.
[**companies_company_id_data_financials_cash_flow_statement_get**](FinancialsApi.md#companies_company_id_data_financials_cash_flow_statement_get) | **GET** /companies/{companyId}/data/financials/cashFlowStatement | Gets the latest cash flow statement for a company.
[**companies_company_id_data_financials_profit_and_loss_get**](FinancialsApi.md#companies_company_id_data_financials_profit_and_loss_get) | **GET** /companies/{companyId}/data/financials/profitAndLoss | Gets the latest profit and loss for a company.


# **companies_company_id_data_financials_balance_sheet_get**
> CodatPublicApiModelsDataBalanceSheetResponse companies_company_id_data_financials_balance_sheet_get(company_id, period_length, periods_to_compare)

Gets the latest balance sheet for a company.

### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import financials_api
from codat_python_sdk.model.codat_public_api_models_data_balance_sheet_response import CodatPublicApiModelsDataBalanceSheetResponse
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
    api_instance = financials_api.FinancialsApi(api_client)
    company_id = "companyId_example" # str | 
    period_length = 1 # int | 
    periods_to_compare = 1 # int | 
    start_month = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets the latest balance sheet for a company.
        api_response = api_instance.companies_company_id_data_financials_balance_sheet_get(company_id, period_length, periods_to_compare)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling FinancialsApi->companies_company_id_data_financials_balance_sheet_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets the latest balance sheet for a company.
        api_response = api_instance.companies_company_id_data_financials_balance_sheet_get(company_id, period_length, periods_to_compare, start_month=start_month)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling FinancialsApi->companies_company_id_data_financials_balance_sheet_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **period_length** | **int**|  |
 **periods_to_compare** | **int**|  |
 **start_month** | **datetime**|  | [optional]

### Return type

[**CodatPublicApiModelsDataBalanceSheetResponse**](CodatPublicApiModelsDataBalanceSheetResponse.md)

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

# **companies_company_id_data_financials_cash_flow_statement_get**
> CodatPublicApiModelsDataCashFlowStatementResponse companies_company_id_data_financials_cash_flow_statement_get(company_id, period_length, periods_to_compare)

Gets the latest cash flow statement for a company.

### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import financials_api
from codat_python_sdk.model.codat_public_api_models_data_cash_flow_statement_response import CodatPublicApiModelsDataCashFlowStatementResponse
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
    api_instance = financials_api.FinancialsApi(api_client)
    company_id = "companyId_example" # str | 
    period_length = 1 # int | 
    periods_to_compare = 1 # int | 
    start_month = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets the latest cash flow statement for a company.
        api_response = api_instance.companies_company_id_data_financials_cash_flow_statement_get(company_id, period_length, periods_to_compare)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling FinancialsApi->companies_company_id_data_financials_cash_flow_statement_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets the latest cash flow statement for a company.
        api_response = api_instance.companies_company_id_data_financials_cash_flow_statement_get(company_id, period_length, periods_to_compare, start_month=start_month)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling FinancialsApi->companies_company_id_data_financials_cash_flow_statement_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **period_length** | **int**|  |
 **periods_to_compare** | **int**|  |
 **start_month** | **datetime**|  | [optional]

### Return type

[**CodatPublicApiModelsDataCashFlowStatementResponse**](CodatPublicApiModelsDataCashFlowStatementResponse.md)

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

# **companies_company_id_data_financials_profit_and_loss_get**
> CodatPublicApiModelsDataProfitAndLossResponse companies_company_id_data_financials_profit_and_loss_get(company_id, period_length, periods_to_compare)

Gets the latest profit and loss for a company.

### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import financials_api
from codat_python_sdk.model.codat_public_api_models_data_profit_and_loss_response import CodatPublicApiModelsDataProfitAndLossResponse
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
    api_instance = financials_api.FinancialsApi(api_client)
    company_id = "companyId_example" # str | 
    period_length = 1 # int | 
    periods_to_compare = 1 # int | 
    start_month = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets the latest profit and loss for a company.
        api_response = api_instance.companies_company_id_data_financials_profit_and_loss_get(company_id, period_length, periods_to_compare)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling FinancialsApi->companies_company_id_data_financials_profit_and_loss_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets the latest profit and loss for a company.
        api_response = api_instance.companies_company_id_data_financials_profit_and_loss_get(company_id, period_length, periods_to_compare, start_month=start_month)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling FinancialsApi->companies_company_id_data_financials_profit_and_loss_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **period_length** | **int**|  |
 **periods_to_compare** | **int**|  |
 **start_month** | **datetime**|  | [optional]

### Return type

[**CodatPublicApiModelsDataProfitAndLossResponse**](CodatPublicApiModelsDataProfitAndLossResponse.md)

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

