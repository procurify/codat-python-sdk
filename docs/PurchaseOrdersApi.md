# codat_python_sdk.PurchaseOrdersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_company_id_connections_connection_id_push_purchase_orders_post**](PurchaseOrdersApi.md#companies_company_id_connections_connection_id_push_purchase_orders_post) | **POST** /companies/{companyId}/connections/{connectionId}/push/purchaseOrders | Posts a new purchase order to the accounting package for a given company.
[**companies_company_id_connections_connection_id_push_purchase_orders_purchase_order_id_put**](PurchaseOrdersApi.md#companies_company_id_connections_connection_id_push_purchase_orders_purchase_order_id_put) | **PUT** /companies/{companyId}/connections/{connectionId}/push/purchaseOrders/{purchaseOrderId} | Posts an updated purchase order to the accounting package for a given company.
[**companies_company_id_data_purchase_orders_get**](PurchaseOrdersApi.md#companies_company_id_data_purchase_orders_get) | **GET** /companies/{companyId}/data/purchaseOrders | 
[**companies_company_id_data_purchase_orders_purchase_order_id_get**](PurchaseOrdersApi.md#companies_company_id_data_purchase_orders_purchase_order_id_get) | **GET** /companies/{companyId}/data/purchaseOrders/{purchaseOrderId} | 


# **companies_company_id_connections_connection_id_push_purchase_orders_post**
> CodatDataContractsDatasetsPurchaseOrderPushOperation companies_company_id_connections_connection_id_push_purchase_orders_post(company_id, connection_id)

Posts a new purchase order to the accounting package for a given company.

### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import purchase_orders_api
from codat_python_sdk.model.codat_data_contracts_datasets_purchase_order import CodatDataContractsDatasetsPurchaseOrder
from codat_python_sdk.model.codat_data_contracts_datasets_purchase_order_push_operation import CodatDataContractsDatasetsPurchaseOrderPushOperation
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
    api_instance = purchase_orders_api.PurchaseOrdersApi(api_client)
    company_id = "companyId_example" # str | 
    connection_id = "connectionId_example" # str | 
    timeout_in_minutes = 1 # int |  (optional)
    codat_data_contracts_datasets_purchase_order = CodatDataContractsDatasetsPurchaseOrder(
        id="id_example",
        purchase_order_number="purchase_order_number_example",
        issue_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        payment_due_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        expected_delivery_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        delivery_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        note="note_example",
        ship_to=CodatDataContractsDatasetsShipTo(
            contact=CodatDataContractsDatasetsShipToContact(
                name="name_example",
                email="email_example",
                phone="phone_example",
            ),
            address=CodatDataContractsDatasetsAddress(
                type=CodatDataContractsDatasetsAddressType("Unknown"),
                line1="line1_example",
                line2="line2_example",
                city="city_example",
                region="region_example",
                country="country_example",
                postal_code="postal_code_example",
            ),
        ),
        supplier_ref=CodatDataContractsDatasetsSupplierRef(
            id="id_example",
            supplier_name="supplier_name_example",
        ),
        bill_ref=CodatDataContractsDatasetsBillRef(
            id="id_example",
            reference="reference_example",
        ),
        status=CodatDataContractsDatasetsPurchaseOrderStatus("Unknown"),
        currency="currency_example",
        currency_rate=3.14,
        line_items=[
            CodatDataContractsDatasetsPurchaseOrderLineItem(
                description="description_example",
                account_ref=CodatDataContractsDatasetsAccountRef(
                    id="id_example",
                    name="name_example",
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
                unit_amount=3.14,
                quantity=3.14,
                discount_amount=3.14,
                discount_percentage=3.14,
                sub_total=3.14,
                tax_amount=3.14,
                tax_rate_ref=CodatDataContractsDatasetsTaxRateRef(
                    id="id_example",
                    name="name_example",
                    effective_tax_rate=3.14,
                ),
                total_amount=3.14,
            ),
        ],
        total_discount=3.14,
        sub_total=3.14,
        total_tax_amount=3.14,
        total_amount=3.14,
        modified_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        source_modified_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # CodatDataContractsDatasetsPurchaseOrder |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Posts a new purchase order to the accounting package for a given company.
        api_response = api_instance.companies_company_id_connections_connection_id_push_purchase_orders_post(company_id, connection_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling PurchaseOrdersApi->companies_company_id_connections_connection_id_push_purchase_orders_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Posts a new purchase order to the accounting package for a given company.
        api_response = api_instance.companies_company_id_connections_connection_id_push_purchase_orders_post(company_id, connection_id, timeout_in_minutes=timeout_in_minutes, codat_data_contracts_datasets_purchase_order=codat_data_contracts_datasets_purchase_order)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling PurchaseOrdersApi->companies_company_id_connections_connection_id_push_purchase_orders_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **connection_id** | **str**|  |
 **timeout_in_minutes** | **int**|  | [optional]
 **codat_data_contracts_datasets_purchase_order** | [**CodatDataContractsDatasetsPurchaseOrder**](CodatDataContractsDatasetsPurchaseOrder.md)|  | [optional]

### Return type

[**CodatDataContractsDatasetsPurchaseOrderPushOperation**](CodatDataContractsDatasetsPurchaseOrderPushOperation.md)

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

# **companies_company_id_connections_connection_id_push_purchase_orders_purchase_order_id_put**
> CodatDataContractsDatasetsPurchaseOrderPushOperation companies_company_id_connections_connection_id_push_purchase_orders_purchase_order_id_put(company_id, connection_id, purchase_order_id)

Posts an updated purchase order to the accounting package for a given company.

### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import purchase_orders_api
from codat_python_sdk.model.codat_data_contracts_datasets_purchase_order import CodatDataContractsDatasetsPurchaseOrder
from codat_python_sdk.model.codat_data_contracts_datasets_purchase_order_push_operation import CodatDataContractsDatasetsPurchaseOrderPushOperation
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
    api_instance = purchase_orders_api.PurchaseOrdersApi(api_client)
    company_id = "companyId_example" # str | 
    connection_id = "connectionId_example" # str | 
    purchase_order_id = "purchaseOrderId_example" # str | 
    timeout_in_minutes = 1 # int |  (optional)
    force_update = False # bool |  (optional) if omitted the server will use the default value of False
    codat_data_contracts_datasets_purchase_order = CodatDataContractsDatasetsPurchaseOrder(
        id="id_example",
        purchase_order_number="purchase_order_number_example",
        issue_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        payment_due_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        expected_delivery_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        delivery_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        note="note_example",
        ship_to=CodatDataContractsDatasetsShipTo(
            contact=CodatDataContractsDatasetsShipToContact(
                name="name_example",
                email="email_example",
                phone="phone_example",
            ),
            address=CodatDataContractsDatasetsAddress(
                type=CodatDataContractsDatasetsAddressType("Unknown"),
                line1="line1_example",
                line2="line2_example",
                city="city_example",
                region="region_example",
                country="country_example",
                postal_code="postal_code_example",
            ),
        ),
        supplier_ref=CodatDataContractsDatasetsSupplierRef(
            id="id_example",
            supplier_name="supplier_name_example",
        ),
        bill_ref=CodatDataContractsDatasetsBillRef(
            id="id_example",
            reference="reference_example",
        ),
        status=CodatDataContractsDatasetsPurchaseOrderStatus("Unknown"),
        currency="currency_example",
        currency_rate=3.14,
        line_items=[
            CodatDataContractsDatasetsPurchaseOrderLineItem(
                description="description_example",
                account_ref=CodatDataContractsDatasetsAccountRef(
                    id="id_example",
                    name="name_example",
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
                unit_amount=3.14,
                quantity=3.14,
                discount_amount=3.14,
                discount_percentage=3.14,
                sub_total=3.14,
                tax_amount=3.14,
                tax_rate_ref=CodatDataContractsDatasetsTaxRateRef(
                    id="id_example",
                    name="name_example",
                    effective_tax_rate=3.14,
                ),
                total_amount=3.14,
            ),
        ],
        total_discount=3.14,
        sub_total=3.14,
        total_tax_amount=3.14,
        total_amount=3.14,
        modified_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        source_modified_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # CodatDataContractsDatasetsPurchaseOrder |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Posts an updated purchase order to the accounting package for a given company.
        api_response = api_instance.companies_company_id_connections_connection_id_push_purchase_orders_purchase_order_id_put(company_id, connection_id, purchase_order_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling PurchaseOrdersApi->companies_company_id_connections_connection_id_push_purchase_orders_purchase_order_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Posts an updated purchase order to the accounting package for a given company.
        api_response = api_instance.companies_company_id_connections_connection_id_push_purchase_orders_purchase_order_id_put(company_id, connection_id, purchase_order_id, timeout_in_minutes=timeout_in_minutes, force_update=force_update, codat_data_contracts_datasets_purchase_order=codat_data_contracts_datasets_purchase_order)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling PurchaseOrdersApi->companies_company_id_connections_connection_id_push_purchase_orders_purchase_order_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **connection_id** | **str**|  |
 **purchase_order_id** | **str**|  |
 **timeout_in_minutes** | **int**|  | [optional]
 **force_update** | **bool**|  | [optional] if omitted the server will use the default value of False
 **codat_data_contracts_datasets_purchase_order** | [**CodatDataContractsDatasetsPurchaseOrder**](CodatDataContractsDatasetsPurchaseOrder.md)|  | [optional]

### Return type

[**CodatDataContractsDatasetsPurchaseOrderPushOperation**](CodatDataContractsDatasetsPurchaseOrderPushOperation.md)

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

# **companies_company_id_data_purchase_orders_get**
> CodatDataContractsDatasetsPurchaseOrderPagedResponseModel companies_company_id_data_purchase_orders_get(company_id, )



### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import purchase_orders_api
from codat_python_sdk.model.codat_data_contracts_datasets_purchase_order_paged_response_model import CodatDataContractsDatasetsPurchaseOrderPagedResponseModel
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
    api_instance = purchase_orders_api.PurchaseOrdersApi(api_client)
    company_id = "companyId_example" # str | 
    page_size = 100 # int |  (optional) if omitted the server will use the default value of 100
    query = "query_example" # str |  (optional)
    order_by = "orderBy_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.companies_company_id_data_purchase_orders_get(company_id, )
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling PurchaseOrdersApi->companies_company_id_data_purchase_orders_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.companies_company_id_data_purchase_orders_get(company_id, page_size=page_size, query=query, order_by=order_by)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling PurchaseOrdersApi->companies_company_id_data_purchase_orders_get: %s\n" % e)
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

[**CodatDataContractsDatasetsPurchaseOrderPagedResponseModel**](CodatDataContractsDatasetsPurchaseOrderPagedResponseModel.md)

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

# **companies_company_id_data_purchase_orders_purchase_order_id_get**
> CodatDataContractsDatasetsPurchaseOrder companies_company_id_data_purchase_orders_purchase_order_id_get(company_id, purchase_order_id)



### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import purchase_orders_api
from codat_python_sdk.model.codat_data_contracts_datasets_purchase_order import CodatDataContractsDatasetsPurchaseOrder
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
    api_instance = purchase_orders_api.PurchaseOrdersApi(api_client)
    company_id = "companyId_example" # str | 
    purchase_order_id = "purchaseOrderId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.companies_company_id_data_purchase_orders_purchase_order_id_get(company_id, purchase_order_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling PurchaseOrdersApi->companies_company_id_data_purchase_orders_purchase_order_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **purchase_order_id** | **str**|  |

### Return type

[**CodatDataContractsDatasetsPurchaseOrder**](CodatDataContractsDatasetsPurchaseOrder.md)

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

