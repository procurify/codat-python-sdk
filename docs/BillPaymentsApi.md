# swagger_client.BillPaymentsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_company_id_connections_connection_id_push_bill_payments_post**](BillPaymentsApi.md#companies_company_id_connections_connection_id_push_bill_payments_post) | **POST** /companies/{companyId}/connections/{connectionId}/push/billPayments | Posts a new bill payment to the accounting package for a given company.
[**companies_company_id_data_bill_payments_bill_payment_id_get**](BillPaymentsApi.md#companies_company_id_data_bill_payments_bill_payment_id_get) | **GET** /companies/{companyId}/data/billPayments/{billPaymentId} | 
[**companies_company_id_data_bill_payments_get**](BillPaymentsApi.md#companies_company_id_data_bill_payments_get) | **GET** /companies/{companyId}/data/billPayments | Gets the latest billPayments for a company, with pagination

# **companies_company_id_connections_connection_id_push_bill_payments_post**
> CodatDataContractsDatasetsBillPaymentPushOperation companies_company_id_connections_connection_id_push_bill_payments_post(company_id, connection_id, body=body, timeout_in_minutes=timeout_in_minutes)

Posts a new bill payment to the accounting package for a given company.

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
api_instance = swagger_client.BillPaymentsApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = swagger_client.CodatDataContractsDatasetsBillPayment() # CodatDataContractsDatasetsBillPayment |  (optional)
timeout_in_minutes = 56 # int |  (optional)

try:
    # Posts a new bill payment to the accounting package for a given company.
    api_response = api_instance.companies_company_id_connections_connection_id_push_bill_payments_post(company_id, connection_id, body=body, timeout_in_minutes=timeout_in_minutes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillPaymentsApi->companies_company_id_connections_connection_id_push_bill_payments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **connection_id** | [**str**](.md)|  | 
 **body** | [**CodatDataContractsDatasetsBillPayment**](CodatDataContractsDatasetsBillPayment.md)|  | [optional] 
 **timeout_in_minutes** | **int**|  | [optional] 

### Return type

[**CodatDataContractsDatasetsBillPaymentPushOperation**](CodatDataContractsDatasetsBillPaymentPushOperation.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_data_bill_payments_bill_payment_id_get**
> CodatDataContractsDatasetsBillPayment companies_company_id_data_bill_payments_bill_payment_id_get(company_id, bill_payment_id)



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
api_instance = swagger_client.BillPaymentsApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
bill_payment_id = 'bill_payment_id_example' # str | 

try:
    api_response = api_instance.companies_company_id_data_bill_payments_bill_payment_id_get(company_id, bill_payment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillPaymentsApi->companies_company_id_data_bill_payments_bill_payment_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **bill_payment_id** | **str**|  | 

### Return type

[**CodatDataContractsDatasetsBillPayment**](CodatDataContractsDatasetsBillPayment.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_data_bill_payments_get**
> CodatDataContractsDatasetsBillPaymentPagedResponseModel companies_company_id_data_bill_payments_get(company_id, page, page_size=page_size, query=query, order_by=order_by)

Gets the latest billPayments for a company, with pagination

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
api_instance = swagger_client.BillPaymentsApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
page = 1 # int |  (default to 1)
page_size = 100 # int |  (optional) (default to 100)
query = 'query_example' # str |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    # Gets the latest billPayments for a company, with pagination
    api_response = api_instance.companies_company_id_data_bill_payments_get(company_id, page, page_size=page_size, query=query, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillPaymentsApi->companies_company_id_data_bill_payments_get: %s\n" % e)
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

[**CodatDataContractsDatasetsBillPaymentPagedResponseModel**](CodatDataContractsDatasetsBillPaymentPagedResponseModel.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

