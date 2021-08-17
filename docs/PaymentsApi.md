# codat_python_sdk.PaymentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_company_id_connections_connection_id_push_payments_post**](PaymentsApi.md#companies_company_id_connections_connection_id_push_payments_post) | **POST** /companies/{companyId}/connections/{connectionId}/push/payments | Posts a new payment to the accounting package for a given company.
[**companies_company_id_data_payments_get**](PaymentsApi.md#companies_company_id_data_payments_get) | **GET** /companies/{companyId}/data/payments | Gets the latest payments for a company, with pagination
[**companies_company_id_data_payments_payment_id_get**](PaymentsApi.md#companies_company_id_data_payments_payment_id_get) | **GET** /companies/{companyId}/data/payments/{paymentId} | 


# **companies_company_id_connections_connection_id_push_payments_post**
> CodatDataContractsDatasetsPaymentPushOperation companies_company_id_connections_connection_id_push_payments_post(company_id, connection_id)

Posts a new payment to the accounting package for a given company.

### Example

* Api Key Authentication (API Key Auth):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import payments_api
from codat_python_sdk.model.codat_data_contracts_datasets_payment_push_operation import CodatDataContractsDatasetsPaymentPushOperation
from codat_python_sdk.model.codat_data_contracts_datasets_payment import CodatDataContractsDatasetsPayment
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
    api_instance = payments_api.PaymentsApi(api_client)
    company_id = "companyId_example" # str | 
    connection_id = "connectionId_example" # str | 
    timeout_in_minutes = 1 # int |  (optional)
    codat_data_contracts_datasets_payment = CodatDataContractsDatasetsPayment(
        id="id_example",
        customer_ref=CodatDataContractsDatasetsCustomerRef(
            id="id_example",
            company_name="company_name_example",
        ),
        account_ref=CodatDataContractsDatasetsAccountRef(
            id="id_example",
            name="name_example",
        ),
        total_amount=3.14,
        currency="currency_example",
        currency_rate=3.14,
        date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        note="note_example",
        lines=[
            CodatDataContractsDatasetsPaymentLine(
                amount=3.14,
                links=[
                    CodatDataContractsDatasetsPaymentLineLink(
                        type=CodatDataContractsDatasetsPaymentLinkType("Unknown"),
                        id="id_example",
                        amount=3.14,
                        currency_rate=3.14,
                    ),
                ],
                allocated_on_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
            ),
        ],
        modified_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        source_modified_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        reference="reference_example",
    ) # CodatDataContractsDatasetsPayment |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Posts a new payment to the accounting package for a given company.
        api_response = api_instance.companies_company_id_connections_connection_id_push_payments_post(company_id, connection_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling PaymentsApi->companies_company_id_connections_connection_id_push_payments_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Posts a new payment to the accounting package for a given company.
        api_response = api_instance.companies_company_id_connections_connection_id_push_payments_post(company_id, connection_id, timeout_in_minutes=timeout_in_minutes, codat_data_contracts_datasets_payment=codat_data_contracts_datasets_payment)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling PaymentsApi->companies_company_id_connections_connection_id_push_payments_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **connection_id** | **str**|  |
 **timeout_in_minutes** | **int**|  | [optional]
 **codat_data_contracts_datasets_payment** | [**CodatDataContractsDatasetsPayment**](CodatDataContractsDatasetsPayment.md)|  | [optional]

### Return type

[**CodatDataContractsDatasetsPaymentPushOperation**](CodatDataContractsDatasetsPaymentPushOperation.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_data_payments_get**
> CodatDataContractsDatasetsPaymentPagedResponseModel companies_company_id_data_payments_get(company_id, )

Gets the latest payments for a company, with pagination

### Example

* Api Key Authentication (API Key Auth):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import payments_api
from codat_python_sdk.model.codat_data_contracts_datasets_payment_paged_response_model import CodatDataContractsDatasetsPaymentPagedResponseModel
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
    api_instance = payments_api.PaymentsApi(api_client)
    company_id = "companyId_example" # str | 
    page_size = 100 # int |  (optional) if omitted the server will use the default value of 100
    query = "query_example" # str |  (optional)
    order_by = "orderBy_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets the latest payments for a company, with pagination
        api_response = api_instance.companies_company_id_data_payments_get(company_id, )
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling PaymentsApi->companies_company_id_data_payments_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets the latest payments for a company, with pagination
        api_response = api_instance.companies_company_id_data_payments_get(company_id, page_size=page_size, query=query, order_by=order_by)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling PaymentsApi->companies_company_id_data_payments_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **page** | **int**|  | defaults to 1
 **page_size** | **int**|  | [optional] if omitted the server will use the default value of 100
 **query** | **str**|  | [optional]
 **order_by** | **str**|  | [optional]

### Return type

[**CodatDataContractsDatasetsPaymentPagedResponseModel**](CodatDataContractsDatasetsPaymentPagedResponseModel.md)

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

# **companies_company_id_data_payments_payment_id_get**
> CodatDataContractsDatasetsPayment companies_company_id_data_payments_payment_id_get(company_id, payment_id)



### Example

* Api Key Authentication (API Key Auth):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import payments_api
from codat_python_sdk.model.codat_data_contracts_datasets_payment import CodatDataContractsDatasetsPayment
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
    api_instance = payments_api.PaymentsApi(api_client)
    company_id = "companyId_example" # str | 
    payment_id = "paymentId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.companies_company_id_data_payments_payment_id_get(company_id, payment_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling PaymentsApi->companies_company_id_data_payments_payment_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **payment_id** | **str**|  |

### Return type

[**CodatDataContractsDatasetsPayment**](CodatDataContractsDatasetsPayment.md)

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

