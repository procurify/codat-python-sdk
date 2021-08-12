# swagger_client.ReportsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_company_id_reports_aged_creditor_available_get**](ReportsApi.md#companies_company_id_reports_aged_creditor_available_get) | **GET** /companies/{companyId}/reports/agedCreditor/available | 
[**companies_company_id_reports_aged_creditor_get**](ReportsApi.md#companies_company_id_reports_aged_creditor_get) | **GET** /companies/{companyId}/reports/agedCreditor | Gets the aged creditor report for a company.
[**companies_company_id_reports_aged_debtor_available_get**](ReportsApi.md#companies_company_id_reports_aged_debtor_available_get) | **GET** /companies/{companyId}/reports/agedDebtor/available | 
[**companies_company_id_reports_aged_debtor_get**](ReportsApi.md#companies_company_id_reports_aged_debtor_get) | **GET** /companies/{companyId}/reports/agedDebtor | Gets the aged debtor report for a company.
[**companies_company_id_reports_events_get**](ReportsApi.md#companies_company_id_reports_events_get) | **GET** /companies/{companyId}/reports/events | 

# **companies_company_id_reports_aged_creditor_available_get**
> bool companies_company_id_reports_aged_creditor_available_get(company_id)



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
api_instance = swagger_client.ReportsApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    api_response = api_instance.companies_company_id_reports_aged_creditor_available_get(company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->companies_company_id_reports_aged_creditor_available_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 

### Return type

**bool**

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_reports_aged_creditor_get**
> CodatDataContractsDatasetsAgedCreditorOutstandingICollectionReport companies_company_id_reports_aged_creditor_get(company_id, report_date=report_date, number_of_periods=number_of_periods, period_length_days=period_length_days)

Gets the aged creditor report for a company.

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
api_instance = swagger_client.ReportsApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
report_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
number_of_periods = 56 # int |  (optional)
period_length_days = 56 # int |  (optional)

try:
    # Gets the aged creditor report for a company.
    api_response = api_instance.companies_company_id_reports_aged_creditor_get(company_id, report_date=report_date, number_of_periods=number_of_periods, period_length_days=period_length_days)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->companies_company_id_reports_aged_creditor_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **report_date** | **datetime**|  | [optional] 
 **number_of_periods** | **int**|  | [optional] 
 **period_length_days** | **int**|  | [optional] 

### Return type

[**CodatDataContractsDatasetsAgedCreditorOutstandingICollectionReport**](CodatDataContractsDatasetsAgedCreditorOutstandingICollectionReport.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_reports_aged_debtor_available_get**
> bool companies_company_id_reports_aged_debtor_available_get(company_id)



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
api_instance = swagger_client.ReportsApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    api_response = api_instance.companies_company_id_reports_aged_debtor_available_get(company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->companies_company_id_reports_aged_debtor_available_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 

### Return type

**bool**

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_reports_aged_debtor_get**
> CodatDataContractsDatasetsAgedDebtorOutstandingICollectionReport companies_company_id_reports_aged_debtor_get(company_id, report_date=report_date, number_of_periods=number_of_periods, period_length_days=period_length_days)

Gets the aged debtor report for a company.

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
api_instance = swagger_client.ReportsApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
report_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
number_of_periods = 56 # int |  (optional)
period_length_days = 56 # int |  (optional)

try:
    # Gets the aged debtor report for a company.
    api_response = api_instance.companies_company_id_reports_aged_debtor_get(company_id, report_date=report_date, number_of_periods=number_of_periods, period_length_days=period_length_days)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->companies_company_id_reports_aged_debtor_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **report_date** | **datetime**|  | [optional] 
 **number_of_periods** | **int**|  | [optional] 
 **period_length_days** | **int**|  | [optional] 

### Return type

[**CodatDataContractsDatasetsAgedDebtorOutstandingICollectionReport**](CodatDataContractsDatasetsAgedDebtorOutstandingICollectionReport.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_reports_events_get**
> CodatPublicApiModelsCompanyCompanyEventStream companies_company_id_reports_events_get(company_id, from_date=from_date, to_date=to_date, page_size=page_size)



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
api_instance = swagger_client.ReportsApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
from_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
to_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
page_size = 56 # int |  (optional)

try:
    api_response = api_instance.companies_company_id_reports_events_get(company_id, from_date=from_date, to_date=to_date, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->companies_company_id_reports_events_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **from_date** | **datetime**|  | [optional] 
 **to_date** | **datetime**|  | [optional] 
 **page_size** | **int**|  | [optional] 

### Return type

[**CodatPublicApiModelsCompanyCompanyEventStream**](CodatPublicApiModelsCompanyCompanyEventStream.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

