# codat_python_sdk.CommercePaymentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_company_id_connections_connection_id_data_commerce_payments_get**](CommercePaymentsApi.md#companies_company_id_connections_connection_id_data_commerce_payments_get) | **GET** /companies/{companyId}/connections/{connectionId}/data/commerce-payments | Gets the latest commerce payments for a company, with pagination
[**companies_company_id_connections_connection_id_data_commerce_payments_payment_id_get**](CommercePaymentsApi.md#companies_company_id_connections_connection_id_data_commerce_payments_payment_id_get) | **GET** /companies/{companyId}/connections/{connectionId}/data/commerce-payments/{paymentId} | Gets the specified commerce payment for a given company


# **companies_company_id_connections_connection_id_data_commerce_payments_get**
> CodatDataContractsDatasetsCommercePaymentPagedResponseModel companies_company_id_connections_connection_id_data_commerce_payments_get(company_id, connection_id, )

Gets the latest commerce payments for a company, with pagination

### Example

* Api Key Authentication (API Key Auth):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import commerce_payments_api
from codat_python_sdk.model.codat_data_contracts_datasets_commerce_payment_paged_response_model import CodatDataContractsDatasetsCommercePaymentPagedResponseModel
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
    api_instance = commerce_payments_api.CommercePaymentsApi(api_client)
    company_id = "companyId_example" # str | 
    connection_id = "connectionId_example" # str | 
    page_size = 100 # int |  (optional) if omitted the server will use the default value of 100
    query = "query_example" # str |  (optional)
    order_by = "orderBy_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets the latest commerce payments for a company, with pagination
        api_response = api_instance.companies_company_id_connections_connection_id_data_commerce_payments_get(company_id, connection_id, )
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling CommercePaymentsApi->companies_company_id_connections_connection_id_data_commerce_payments_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets the latest commerce payments for a company, with pagination
        api_response = api_instance.companies_company_id_connections_connection_id_data_commerce_payments_get(company_id, connection_id, page_size=page_size, query=query, order_by=order_by)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling CommercePaymentsApi->companies_company_id_connections_connection_id_data_commerce_payments_get: %s\n" % e)
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

[**CodatDataContractsDatasetsCommercePaymentPagedResponseModel**](CodatDataContractsDatasetsCommercePaymentPagedResponseModel.md)

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

# **companies_company_id_connections_connection_id_data_commerce_payments_payment_id_get**
> CodatDataContractsDatasetsCommercePayment companies_company_id_connections_connection_id_data_commerce_payments_payment_id_get(company_id, connection_id, payment_id)

Gets the specified commerce payment for a given company

### Example

* Api Key Authentication (API Key Auth):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import commerce_payments_api
from codat_python_sdk.model.codat_data_contracts_datasets_commerce_payment import CodatDataContractsDatasetsCommercePayment
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
    api_instance = commerce_payments_api.CommercePaymentsApi(api_client)
    company_id = "companyId_example" # str | 
    connection_id = "connectionId_example" # str | 
    payment_id = "paymentId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Gets the specified commerce payment for a given company
        api_response = api_instance.companies_company_id_connections_connection_id_data_commerce_payments_payment_id_get(company_id, connection_id, payment_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling CommercePaymentsApi->companies_company_id_connections_connection_id_data_commerce_payments_payment_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **connection_id** | **str**|  |
 **payment_id** | **str**|  |

### Return type

[**CodatDataContractsDatasetsCommercePayment**](CodatDataContractsDatasetsCommercePayment.md)

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

