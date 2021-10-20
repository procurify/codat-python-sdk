# codat_python_sdk.BillPaymentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_company_id_connections_connection_id_push_bill_payments_post**](BillPaymentsApi.md#companies_company_id_connections_connection_id_push_bill_payments_post) | **POST** /companies/{companyId}/connections/{connectionId}/push/billPayments | Posts a new bill payment to the accounting package for a given company.
[**companies_company_id_data_bill_payments_bill_payment_id_get**](BillPaymentsApi.md#companies_company_id_data_bill_payments_bill_payment_id_get) | **GET** /companies/{companyId}/data/billPayments/{billPaymentId} | 
[**companies_company_id_data_bill_payments_get**](BillPaymentsApi.md#companies_company_id_data_bill_payments_get) | **GET** /companies/{companyId}/data/billPayments | Gets the latest billPayments for a company, with pagination


# **companies_company_id_connections_connection_id_push_bill_payments_post**
> CodatDataContractsDatasetsBillPaymentPushOperation companies_company_id_connections_connection_id_push_bill_payments_post(company_id, connection_id)

Posts a new bill payment to the accounting package for a given company.

### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import bill_payments_api
from codat_python_sdk.model.codat_data_contracts_datasets_bill_payment import CodatDataContractsDatasetsBillPayment
from codat_python_sdk.model.codat_data_contracts_datasets_bill_payment_push_operation import CodatDataContractsDatasetsBillPaymentPushOperation
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
    api_instance = bill_payments_api.BillPaymentsApi(api_client)
    company_id = "companyId_example" # str | 
    connection_id = "connectionId_example" # str | 
    timeout_in_minutes = 1 # int |  (optional)
    codat_data_contracts_datasets_bill_payment = CodatDataContractsDatasetsBillPayment(
        id="id_example",
        supplier_ref=CodatDataContractsDatasetsSupplierRef(
            id="id_example",
            supplier_name="supplier_name_example",
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
        payment_method_ref=CodatDataContractsDatasetsPaymentMethodRef(
            id="id_example",
            name="name_example",
        ),
        lines=[
            CodatDataContractsDatasetsBillPaymentLine(
                amount=3.14,
                links=[
                    CodatDataContractsDatasetsBillPaymentLineLink(
                        type=CodatDataContractsDatasetsBillPaymentLinkType("Unknown"),
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
    ) # CodatDataContractsDatasetsBillPayment |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Posts a new bill payment to the accounting package for a given company.
        api_response = api_instance.companies_company_id_connections_connection_id_push_bill_payments_post(company_id, connection_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling BillPaymentsApi->companies_company_id_connections_connection_id_push_bill_payments_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Posts a new bill payment to the accounting package for a given company.
        api_response = api_instance.companies_company_id_connections_connection_id_push_bill_payments_post(company_id, connection_id, timeout_in_minutes=timeout_in_minutes, codat_data_contracts_datasets_bill_payment=codat_data_contracts_datasets_bill_payment)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling BillPaymentsApi->companies_company_id_connections_connection_id_push_bill_payments_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **connection_id** | **str**|  |
 **timeout_in_minutes** | **int**|  | [optional]
 **codat_data_contracts_datasets_bill_payment** | [**CodatDataContractsDatasetsBillPayment**](CodatDataContractsDatasetsBillPayment.md)|  | [optional]

### Return type

[**CodatDataContractsDatasetsBillPaymentPushOperation**](CodatDataContractsDatasetsBillPaymentPushOperation.md)

### Authorization

[API Key Auth](../README.md#API Key Auth), [Codat Login](../README.md#Codat Login)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_data_bill_payments_bill_payment_id_get**
> CodatDataContractsDatasetsBillPayment companies_company_id_data_bill_payments_bill_payment_id_get(company_id, bill_payment_id)



### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import bill_payments_api
from codat_python_sdk.model.codat_data_contracts_datasets_bill_payment import CodatDataContractsDatasetsBillPayment
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
    api_instance = bill_payments_api.BillPaymentsApi(api_client)
    company_id = "companyId_example" # str | 
    bill_payment_id = "billPaymentId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.companies_company_id_data_bill_payments_bill_payment_id_get(company_id, bill_payment_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling BillPaymentsApi->companies_company_id_data_bill_payments_bill_payment_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **bill_payment_id** | **str**|  |

### Return type

[**CodatDataContractsDatasetsBillPayment**](CodatDataContractsDatasetsBillPayment.md)

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

# **companies_company_id_data_bill_payments_get**
> CodatDataContractsDatasetsBillPaymentPagedResponseModel companies_company_id_data_bill_payments_get(company_id, )

Gets the latest billPayments for a company, with pagination

### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import bill_payments_api
from codat_python_sdk.model.codat_data_contracts_datasets_bill_payment_paged_response_model import CodatDataContractsDatasetsBillPaymentPagedResponseModel
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
    api_instance = bill_payments_api.BillPaymentsApi(api_client)
    company_id = "companyId_example" # str | 
    page_size = 100 # int |  (optional) if omitted the server will use the default value of 100
    query = "query_example" # str |  (optional)
    order_by = "orderBy_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets the latest billPayments for a company, with pagination
        api_response = api_instance.companies_company_id_data_bill_payments_get(company_id, )
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling BillPaymentsApi->companies_company_id_data_bill_payments_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets the latest billPayments for a company, with pagination
        api_response = api_instance.companies_company_id_data_bill_payments_get(company_id, page_size=page_size, query=query, order_by=order_by)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling BillPaymentsApi->companies_company_id_data_bill_payments_get: %s\n" % e)
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

[**CodatDataContractsDatasetsBillPaymentPagedResponseModel**](CodatDataContractsDatasetsBillPaymentPagedResponseModel.md)

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

