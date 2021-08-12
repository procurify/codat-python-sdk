# swagger_client.FinancialsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_company_id_data_financials_balance_sheet_get**](FinancialsApi.md#companies_company_id_data_financials_balance_sheet_get) | **GET** /companies/{companyId}/data/financials/balanceSheet | Gets the latest balance sheet for a company.
[**companies_company_id_data_financials_cash_flow_statement_get**](FinancialsApi.md#companies_company_id_data_financials_cash_flow_statement_get) | **GET** /companies/{companyId}/data/financials/cashFlowStatement | Gets the latest balance sheet for a company.
[**companies_company_id_data_financials_profit_and_loss_get**](FinancialsApi.md#companies_company_id_data_financials_profit_and_loss_get) | **GET** /companies/{companyId}/data/financials/profitAndLoss | Gets the latest profit and loss for a company.

# **companies_company_id_data_financials_balance_sheet_get**
> CodatPublicApiModelsDataBalanceSheetResponse companies_company_id_data_financials_balance_sheet_get(company_id, period_length, periods_to_compare, start_month=start_month)

Gets the latest balance sheet for a company.

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
api_instance = swagger_client.FinancialsApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
period_length = 56 # int | 
periods_to_compare = 56 # int | 
start_month = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

try:
    # Gets the latest balance sheet for a company.
    api_response = api_instance.companies_company_id_data_financials_balance_sheet_get(company_id, period_length, periods_to_compare, start_month=start_month)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FinancialsApi->companies_company_id_data_financials_balance_sheet_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **period_length** | **int**|  | 
 **periods_to_compare** | **int**|  | 
 **start_month** | **datetime**|  | [optional] 

### Return type

[**CodatPublicApiModelsDataBalanceSheetResponse**](CodatPublicApiModelsDataBalanceSheetResponse.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_data_financials_cash_flow_statement_get**
> CodatPublicApiModelsDataCashFlowStatementResponse companies_company_id_data_financials_cash_flow_statement_get(company_id, period_length, periods_to_compare, start_month=start_month)

Gets the latest balance sheet for a company.

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
api_instance = swagger_client.FinancialsApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
period_length = 56 # int | 
periods_to_compare = 56 # int | 
start_month = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

try:
    # Gets the latest balance sheet for a company.
    api_response = api_instance.companies_company_id_data_financials_cash_flow_statement_get(company_id, period_length, periods_to_compare, start_month=start_month)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FinancialsApi->companies_company_id_data_financials_cash_flow_statement_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **period_length** | **int**|  | 
 **periods_to_compare** | **int**|  | 
 **start_month** | **datetime**|  | [optional] 

### Return type

[**CodatPublicApiModelsDataCashFlowStatementResponse**](CodatPublicApiModelsDataCashFlowStatementResponse.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_data_financials_profit_and_loss_get**
> CodatPublicApiModelsDataProfitAndLossResponse companies_company_id_data_financials_profit_and_loss_get(company_id, period_length, periods_to_compare, start_month=start_month)

Gets the latest profit and loss for a company.

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
api_instance = swagger_client.FinancialsApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
period_length = 56 # int | 
periods_to_compare = 56 # int | 
start_month = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

try:
    # Gets the latest profit and loss for a company.
    api_response = api_instance.companies_company_id_data_financials_profit_and_loss_get(company_id, period_length, periods_to_compare, start_month=start_month)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FinancialsApi->companies_company_id_data_financials_profit_and_loss_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **period_length** | **int**|  | 
 **periods_to_compare** | **int**|  | 
 **start_month** | **datetime**|  | [optional] 

### Return type

[**CodatPublicApiModelsDataProfitAndLossResponse**](CodatPublicApiModelsDataProfitAndLossResponse.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

