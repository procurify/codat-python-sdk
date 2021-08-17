# codat_python_sdk.DirectIncomesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_company_id_connections_connection_id_data_direct_incomes_direct_income_id_get**](DirectIncomesApi.md#companies_company_id_connections_connection_id_data_direct_incomes_direct_income_id_get) | **GET** /companies/{companyId}/connections/{connectionId}/data/directIncomes/{directIncomeId} | Gets the specified direct income for a given company and connection.
[**companies_company_id_connections_connection_id_data_direct_incomes_get**](DirectIncomesApi.md#companies_company_id_connections_connection_id_data_direct_incomes_get) | **GET** /companies/{companyId}/connections/{connectionId}/data/directIncomes | Gets the direct incomes for a given company.
[**companies_company_id_connections_connection_id_push_direct_incomes_post**](DirectIncomesApi.md#companies_company_id_connections_connection_id_push_direct_incomes_post) | **POST** /companies/{companyId}/connections/{connectionId}/push/directIncomes | Posts a new direct income to the accounting package for a given company.


# **companies_company_id_connections_connection_id_data_direct_incomes_direct_income_id_get**
> CodatDataContractsDatasetsDirectIncome companies_company_id_connections_connection_id_data_direct_incomes_direct_income_id_get(company_id, connection_id, direct_income_id)

Gets the specified direct income for a given company and connection.

### Example

* Api Key Authentication (API Key Auth):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import direct_incomes_api
from codat_python_sdk.model.codat_data_contracts_datasets_direct_income import CodatDataContractsDatasetsDirectIncome
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
    api_instance = direct_incomes_api.DirectIncomesApi(api_client)
    company_id = "companyId_example" # str | 
    connection_id = "connectionId_example" # str | 
    direct_income_id = "directIncomeId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Gets the specified direct income for a given company and connection.
        api_response = api_instance.companies_company_id_connections_connection_id_data_direct_incomes_direct_income_id_get(company_id, connection_id, direct_income_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling DirectIncomesApi->companies_company_id_connections_connection_id_data_direct_incomes_direct_income_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **connection_id** | **str**|  |
 **direct_income_id** | **str**|  |

### Return type

[**CodatDataContractsDatasetsDirectIncome**](CodatDataContractsDatasetsDirectIncome.md)

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

# **companies_company_id_connections_connection_id_data_direct_incomes_get**
> CodatDataContractsDatasetsDirectIncomePagedResponseModel companies_company_id_connections_connection_id_data_direct_incomes_get(company_id, connection_id, )

Gets the direct incomes for a given company.

### Example

* Api Key Authentication (API Key Auth):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import direct_incomes_api
from codat_python_sdk.model.codat_data_contracts_datasets_direct_income_paged_response_model import CodatDataContractsDatasetsDirectIncomePagedResponseModel
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
    api_instance = direct_incomes_api.DirectIncomesApi(api_client)
    company_id = "companyId_example" # str | 
    connection_id = "connectionId_example" # str | 
    page_size = 100 # int |  (optional) if omitted the server will use the default value of 100
    query = "query_example" # str |  (optional)
    order_by = "orderBy_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets the direct incomes for a given company.
        api_response = api_instance.companies_company_id_connections_connection_id_data_direct_incomes_get(company_id, connection_id, )
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling DirectIncomesApi->companies_company_id_connections_connection_id_data_direct_incomes_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets the direct incomes for a given company.
        api_response = api_instance.companies_company_id_connections_connection_id_data_direct_incomes_get(company_id, connection_id, page_size=page_size, query=query, order_by=order_by)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling DirectIncomesApi->companies_company_id_connections_connection_id_data_direct_incomes_get: %s\n" % e)
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

[**CodatDataContractsDatasetsDirectIncomePagedResponseModel**](CodatDataContractsDatasetsDirectIncomePagedResponseModel.md)

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

# **companies_company_id_connections_connection_id_push_direct_incomes_post**
> CodatDataContractsDatasetsDirectIncomePushOperation companies_company_id_connections_connection_id_push_direct_incomes_post(company_id, connection_id)

Posts a new direct income to the accounting package for a given company.

### Example

* Api Key Authentication (API Key Auth):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import direct_incomes_api
from codat_python_sdk.model.codat_data_contracts_datasets_direct_income_push_operation import CodatDataContractsDatasetsDirectIncomePushOperation
from codat_python_sdk.model.codat_data_contracts_datasets_direct_income import CodatDataContractsDatasetsDirectIncome
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
    api_instance = direct_incomes_api.DirectIncomesApi(api_client)
    company_id = "companyId_example" # str | 
    connection_id = "connectionId_example" # str | 
    timeout_in_minutes = 1 # int |  (optional)
    codat_data_contracts_datasets_direct_income = CodatDataContractsDatasetsDirectIncome(
        id="id_example",
        reference="reference_example",
        note="note_example",
        contact_ref=CodatDataContractsDatasetsContactRef(
            id="id_example",
            data_type="data_type_example",
        ),
        issue_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        currency="currency_example",
        currency_rate=3.14,
        line_items=[
            CodatDataContractsDatasetsDirectAccountTransactionLineItem(
                description="description_example",
                unit_amount=3.14,
                quantity=3.14,
                sub_total=3.14,
                tax_amount=3.14,
                total_amount=3.14,
                account_ref=CodatDataContractsDatasetsAccountRef(
                    id="id_example",
                    name="name_example",
                ),
                tax_rate_ref=CodatDataContractsDatasetsTaxRateRef(
                    id="id_example",
                    name="name_example",
                    effective_tax_rate=3.14,
                ),
                item_ref=CodatDataContractsDatasetsItemRef(
                    id="id_example",
                    name="name_example",
                ),
                tracking_category_refs=[
                    CodatDataContractsDatasetsTrackingCategoryRef(
                        id="id_example",
                        name="name_example",
                    ),
                ],
            ),
        ],
        payment_allocations=[
            CodatDataContractsDatasetsDetailedPaymentAllocation(
                payment=CodatDataContractsDatasetsPaymentAllocationPayment(
                    id="id_example",
                    note="note_example",
                    reference="reference_example",
                    account_ref=CodatDataContractsDatasetsAccountRef(
                        id="id_example",
                        name="name_example",
                    ),
                    currency="currency_example",
                    currency_rate=3.14,
                    paid_on_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    total_amount=3.14,
                ),
                allocation=CodatDataContractsDatasetsAllocation(
                    currency="currency_example",
                    currency_rate=3.14,
                    allocated_on_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    total_amount=3.14,
                ),
            ),
        ],
        sub_total=3.14,
        tax_amount=3.14,
        total_amount=3.14,
        modified_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        source_modified_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # CodatDataContractsDatasetsDirectIncome |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Posts a new direct income to the accounting package for a given company.
        api_response = api_instance.companies_company_id_connections_connection_id_push_direct_incomes_post(company_id, connection_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling DirectIncomesApi->companies_company_id_connections_connection_id_push_direct_incomes_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Posts a new direct income to the accounting package for a given company.
        api_response = api_instance.companies_company_id_connections_connection_id_push_direct_incomes_post(company_id, connection_id, timeout_in_minutes=timeout_in_minutes, codat_data_contracts_datasets_direct_income=codat_data_contracts_datasets_direct_income)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling DirectIncomesApi->companies_company_id_connections_connection_id_push_direct_incomes_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **connection_id** | **str**|  |
 **timeout_in_minutes** | **int**|  | [optional]
 **codat_data_contracts_datasets_direct_income** | [**CodatDataContractsDatasetsDirectIncome**](CodatDataContractsDatasetsDirectIncome.md)|  | [optional]

### Return type

[**CodatDataContractsDatasetsDirectIncomePushOperation**](CodatDataContractsDatasetsDirectIncomePushOperation.md)

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

