# codat_python_sdk.ReportsApi

All URIs are relative to *http://localhost*

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

* Api Key Authentication (API Key Auth):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import reports_api
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
    api_instance = reports_api.ReportsApi(api_client)
    company_id = "companyId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.companies_company_id_reports_aged_creditor_available_get(company_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling ReportsApi->companies_company_id_reports_aged_creditor_available_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |

### Return type

**bool**

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

# **companies_company_id_reports_aged_creditor_get**
> CodatDataContractsDatasetsAgedCreditorOutstandingICollectionReport companies_company_id_reports_aged_creditor_get(company_id)

Gets the aged creditor report for a company.

### Example

* Api Key Authentication (API Key Auth):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import reports_api
from codat_python_sdk.model.codat_data_contracts_datasets_aged_creditor_outstanding_i_collection_report import CodatDataContractsDatasetsAgedCreditorOutstandingICollectionReport
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
    api_instance = reports_api.ReportsApi(api_client)
    company_id = "companyId_example" # str | 
    report_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)
    number_of_periods = 1 # int |  (optional)
    period_length_days = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets the aged creditor report for a company.
        api_response = api_instance.companies_company_id_reports_aged_creditor_get(company_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling ReportsApi->companies_company_id_reports_aged_creditor_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets the aged creditor report for a company.
        api_response = api_instance.companies_company_id_reports_aged_creditor_get(company_id, report_date=report_date, number_of_periods=number_of_periods, period_length_days=period_length_days)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling ReportsApi->companies_company_id_reports_aged_creditor_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
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


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_reports_aged_debtor_available_get**
> bool companies_company_id_reports_aged_debtor_available_get(company_id)



### Example

* Api Key Authentication (API Key Auth):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import reports_api
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
    api_instance = reports_api.ReportsApi(api_client)
    company_id = "companyId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.companies_company_id_reports_aged_debtor_available_get(company_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling ReportsApi->companies_company_id_reports_aged_debtor_available_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |

### Return type

**bool**

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

# **companies_company_id_reports_aged_debtor_get**
> CodatDataContractsDatasetsAgedDebtorOutstandingICollectionReport companies_company_id_reports_aged_debtor_get(company_id)

Gets the aged debtor report for a company.

### Example

* Api Key Authentication (API Key Auth):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import reports_api
from codat_python_sdk.model.codat_data_contracts_datasets_aged_debtor_outstanding_i_collection_report import CodatDataContractsDatasetsAgedDebtorOutstandingICollectionReport
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
    api_instance = reports_api.ReportsApi(api_client)
    company_id = "companyId_example" # str | 
    report_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)
    number_of_periods = 1 # int |  (optional)
    period_length_days = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets the aged debtor report for a company.
        api_response = api_instance.companies_company_id_reports_aged_debtor_get(company_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling ReportsApi->companies_company_id_reports_aged_debtor_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets the aged debtor report for a company.
        api_response = api_instance.companies_company_id_reports_aged_debtor_get(company_id, report_date=report_date, number_of_periods=number_of_periods, period_length_days=period_length_days)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling ReportsApi->companies_company_id_reports_aged_debtor_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
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


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_reports_events_get**
> CodatPublicApiModelsCompanyCompanyEventStream companies_company_id_reports_events_get(company_id)



### Example

* Api Key Authentication (API Key Auth):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import reports_api
from codat_python_sdk.model.codat_public_api_models_company_company_event_stream import CodatPublicApiModelsCompanyCompanyEventStream
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
    api_instance = reports_api.ReportsApi(api_client)
    company_id = "companyId_example" # str | 
    from_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)
    to_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)
    page_size = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.companies_company_id_reports_events_get(company_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling ReportsApi->companies_company_id_reports_events_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.companies_company_id_reports_events_get(company_id, from_date=from_date, to_date=to_date, page_size=page_size)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling ReportsApi->companies_company_id_reports_events_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
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


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

