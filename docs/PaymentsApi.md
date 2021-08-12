# swagger_client.PaymentsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_company_id_connections_connection_id_push_payments_post**](PaymentsApi.md#companies_company_id_connections_connection_id_push_payments_post) | **POST** /companies/{companyId}/connections/{connectionId}/push/payments | Posts a new payment to the accounting package for a given company.
[**companies_company_id_data_payments_get**](PaymentsApi.md#companies_company_id_data_payments_get) | **GET** /companies/{companyId}/data/payments | Gets the latest payments for a company, with pagination
[**companies_company_id_data_payments_payment_id_get**](PaymentsApi.md#companies_company_id_data_payments_payment_id_get) | **GET** /companies/{companyId}/data/payments/{paymentId} | 

# **companies_company_id_connections_connection_id_push_payments_post**
> CodatDataContractsDatasetsPaymentPushOperation companies_company_id_connections_connection_id_push_payments_post(company_id, connection_id, body=body, timeout_in_minutes=timeout_in_minutes)

Posts a new payment to the accounting package for a given company.

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
api_instance = swagger_client.PaymentsApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
connection_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = swagger_client.CodatDataContractsDatasetsPayment() # CodatDataContractsDatasetsPayment |  (optional)
timeout_in_minutes = 56 # int |  (optional)

try:
    # Posts a new payment to the accounting package for a given company.
    api_response = api_instance.companies_company_id_connections_connection_id_push_payments_post(company_id, connection_id, body=body, timeout_in_minutes=timeout_in_minutes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->companies_company_id_connections_connection_id_push_payments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **connection_id** | [**str**](.md)|  | 
 **body** | [**CodatDataContractsDatasetsPayment**](CodatDataContractsDatasetsPayment.md)|  | [optional] 
 **timeout_in_minutes** | **int**|  | [optional] 

### Return type

[**CodatDataContractsDatasetsPaymentPushOperation**](CodatDataContractsDatasetsPaymentPushOperation.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_data_payments_get**
> CodatDataContractsDatasetsPaymentPagedResponseModel companies_company_id_data_payments_get(company_id, page, page_size=page_size, query=query, order_by=order_by)

Gets the latest payments for a company, with pagination

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
api_instance = swagger_client.PaymentsApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
page = 1 # int |  (default to 1)
page_size = 100 # int |  (optional) (default to 100)
query = 'query_example' # str |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    # Gets the latest payments for a company, with pagination
    api_response = api_instance.companies_company_id_data_payments_get(company_id, page, page_size=page_size, query=query, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->companies_company_id_data_payments_get: %s\n" % e)
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

[**CodatDataContractsDatasetsPaymentPagedResponseModel**](CodatDataContractsDatasetsPaymentPagedResponseModel.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_data_payments_payment_id_get**
> CodatDataContractsDatasetsPayment companies_company_id_data_payments_payment_id_get(company_id, payment_id)



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
api_instance = swagger_client.PaymentsApi(swagger_client.ApiClient(configuration))
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
payment_id = 'payment_id_example' # str | 

try:
    api_response = api_instance.companies_company_id_data_payments_payment_id_get(company_id, payment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->companies_company_id_data_payments_payment_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | [**str**](.md)|  | 
 **payment_id** | **str**|  | 

### Return type

[**CodatDataContractsDatasetsPayment**](CodatDataContractsDatasetsPayment.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

