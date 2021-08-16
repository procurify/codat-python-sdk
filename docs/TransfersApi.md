# codat_python_sdk.TransfersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_company_id_connections_connection_id_data_transfers_get**](TransfersApi.md#companies_company_id_connections_connection_id_data_transfers_get) | **GET** /companies/{companyId}/connections/{connectionId}/data/transfers | Gets the transfers for a given company.
[**companies_company_id_connections_connection_id_data_transfers_transfer_id_get**](TransfersApi.md#companies_company_id_connections_connection_id_data_transfers_transfer_id_get) | **GET** /companies/{companyId}/connections/{connectionId}/data/transfers/{transferId} | Gets the specified transfer for a given company.
[**companies_company_id_connections_connection_id_push_transfers_post**](TransfersApi.md#companies_company_id_connections_connection_id_push_transfers_post) | **POST** /companies/{companyId}/connections/{connectionId}/push/transfers | Posts a new transfer to the accounting package for a given company.


# **companies_company_id_connections_connection_id_data_transfers_get**
> CodatDataContractsDatasetsTransferPagedResponseModel companies_company_id_connections_connection_id_data_transfers_get(company_id, connection_id, )

Gets the transfers for a given company.

### Example

* Api Key Authentication (API Key Auth):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import transfers_api
from codat_python_sdk.model.codat_data_contracts_datasets_transfer_paged_response_model import CodatDataContractsDatasetsTransferPagedResponseModel
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
    api_instance = transfers_api.TransfersApi(api_client)
    company_id = "companyId_example" # str | 
    connection_id = "connectionId_example" # str | 
    page_size = 100 # int |  (optional) if omitted the server will use the default value of 100
    query = "query_example" # str |  (optional)
    order_by = "orderBy_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets the transfers for a given company.
        api_response = api_instance.companies_company_id_connections_connection_id_data_transfers_get(company_id, connection_id, )
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling TransfersApi->companies_company_id_connections_connection_id_data_transfers_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets the transfers for a given company.
        api_response = api_instance.companies_company_id_connections_connection_id_data_transfers_get(company_id, connection_id, page_size=page_size, query=query, order_by=order_by)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling TransfersApi->companies_company_id_connections_connection_id_data_transfers_get: %s\n" % e)
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

[**CodatDataContractsDatasetsTransferPagedResponseModel**](CodatDataContractsDatasetsTransferPagedResponseModel.md)

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

# **companies_company_id_connections_connection_id_data_transfers_transfer_id_get**
> CodatDataContractsDatasetsTransfer companies_company_id_connections_connection_id_data_transfers_transfer_id_get(company_id, connection_id, transfer_id)

Gets the specified transfer for a given company.

### Example

* Api Key Authentication (API Key Auth):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import transfers_api
from codat_python_sdk.model.codat_data_contracts_datasets_transfer import CodatDataContractsDatasetsTransfer
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
    api_instance = transfers_api.TransfersApi(api_client)
    company_id = "companyId_example" # str | 
    connection_id = "connectionId_example" # str | 
    transfer_id = "transferId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Gets the specified transfer for a given company.
        api_response = api_instance.companies_company_id_connections_connection_id_data_transfers_transfer_id_get(company_id, connection_id, transfer_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling TransfersApi->companies_company_id_connections_connection_id_data_transfers_transfer_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **connection_id** | **str**|  |
 **transfer_id** | **str**|  |

### Return type

[**CodatDataContractsDatasetsTransfer**](CodatDataContractsDatasetsTransfer.md)

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

# **companies_company_id_connections_connection_id_push_transfers_post**
> CodatDataContractsDatasetsTransferPushOperation companies_company_id_connections_connection_id_push_transfers_post(company_id, connection_id)

Posts a new transfer to the accounting package for a given company.

### Example

* Api Key Authentication (API Key Auth):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import transfers_api
from codat_python_sdk.model.codat_data_contracts_datasets_transfer_push_operation import CodatDataContractsDatasetsTransferPushOperation
from codat_python_sdk.model.codat_data_contracts_datasets_transfer import CodatDataContractsDatasetsTransfer
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
    api_instance = transfers_api.TransfersApi(api_client)
    company_id = "companyId_example" # str | 
    connection_id = "connectionId_example" # str | 
    timeout_in_minutes = 1 # int |  (optional)
    codat_data_contracts_datasets_transfer = CodatDataContractsDatasetsTransfer(
        id="id_example",
        description="description_example",
        contact_ref=CodatDataContractsDatasetsContactRef(
            id="id_example",
            data_type="data_type_example",
        ),
        date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        _from=CodatDataContractsDatasetsFromAccount(
            account_ref=CodatDataContractsDatasetsRecordRef(
                id="id_example",
                data_type="data_type_example",
            ),
            currency="currency_example",
            amount=3.14,
        ),
        to=CodatDataContractsDatasetsToAccount(
            account_ref=CodatDataContractsDatasetsRecordRef(
                id="id_example",
                data_type="data_type_example",
            ),
            currency="currency_example",
            amount=3.14,
        ),
        tracking_category_refs=[
            CodatDataContractsDatasetsTrackingCategoryRef(
                id="id_example",
                name="name_example",
            ),
        ],
        modified_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        source_modified_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # CodatDataContractsDatasetsTransfer |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Posts a new transfer to the accounting package for a given company.
        api_response = api_instance.companies_company_id_connections_connection_id_push_transfers_post(company_id, connection_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling TransfersApi->companies_company_id_connections_connection_id_push_transfers_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Posts a new transfer to the accounting package for a given company.
        api_response = api_instance.companies_company_id_connections_connection_id_push_transfers_post(company_id, connection_id, timeout_in_minutes=timeout_in_minutes, codat_data_contracts_datasets_transfer=codat_data_contracts_datasets_transfer)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling TransfersApi->companies_company_id_connections_connection_id_push_transfers_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **connection_id** | **str**|  |
 **timeout_in_minutes** | **int**|  | [optional]
 **codat_data_contracts_datasets_transfer** | [**CodatDataContractsDatasetsTransfer**](CodatDataContractsDatasetsTransfer.md)|  | [optional]

### Return type

[**CodatDataContractsDatasetsTransferPushOperation**](CodatDataContractsDatasetsTransferPushOperation.md)

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

