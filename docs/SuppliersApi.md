# codat_python_sdk.SuppliersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_attachment_id_download_get**](SuppliersApi.md#companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_attachment_id_download_get) | **GET** /companies/{companyId}/connections/{connectionId}/data/suppliers/{supplierId}/attachments/{attachmentId}/download | 
[**companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_attachment_id_get**](SuppliersApi.md#companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_attachment_id_get) | **GET** /companies/{companyId}/connections/{connectionId}/data/suppliers/{supplierId}/attachments/{attachmentId} | 
[**companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_get**](SuppliersApi.md#companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_get) | **GET** /companies/{companyId}/connections/{connectionId}/data/suppliers/{supplierId}/attachments | 
[**companies_company_id_connections_connection_id_push_suppliers_post**](SuppliersApi.md#companies_company_id_connections_connection_id_push_suppliers_post) | **POST** /companies/{companyId}/connections/{connectionId}/push/suppliers | 
[**companies_company_id_data_suppliers_get**](SuppliersApi.md#companies_company_id_data_suppliers_get) | **GET** /companies/{companyId}/data/suppliers | Gets the latest suppliers for a company, with pagination
[**companies_company_id_data_suppliers_supplier_id_get**](SuppliersApi.md#companies_company_id_data_suppliers_supplier_id_get) | **GET** /companies/{companyId}/data/suppliers/{supplierId} | Gets a single supplier corresponding to the supplied Id


# **companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_attachment_id_download_get**
> companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_attachment_id_download_get(company_id, connection_id, supplier_id, attachment_id)



### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import suppliers_api
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
    api_instance = suppliers_api.SuppliersApi(api_client)
    company_id = "companyId_example" # str | 
    connection_id = "connectionId_example" # str | 
    supplier_id = "supplierId_example" # str | 
    attachment_id = "attachmentId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_attachment_id_download_get(company_id, connection_id, supplier_id, attachment_id)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling SuppliersApi->companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_attachment_id_download_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **connection_id** | **str**|  |
 **supplier_id** | **str**|  |
 **attachment_id** | **str**|  |

### Return type

void (empty response body)

### Authorization

[API Key Auth](../README.md#API Key Auth), [Codat Login](../README.md#Codat Login)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_attachment_id_get**
> CodatDataContractsDatasetsAttachmentsDatasetAttachment companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_attachment_id_get(company_id, connection_id, supplier_id, attachment_id)



### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import suppliers_api
from codat_python_sdk.model.codat_data_contracts_datasets_attachments_dataset_attachment import CodatDataContractsDatasetsAttachmentsDatasetAttachment
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
    api_instance = suppliers_api.SuppliersApi(api_client)
    company_id = "companyId_example" # str | 
    connection_id = "connectionId_example" # str | 
    supplier_id = "supplierId_example" # str | 
    attachment_id = "attachmentId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_attachment_id_get(company_id, connection_id, supplier_id, attachment_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling SuppliersApi->companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_attachment_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **connection_id** | **str**|  |
 **supplier_id** | **str**|  |
 **attachment_id** | **str**|  |

### Return type

[**CodatDataContractsDatasetsAttachmentsDatasetAttachment**](CodatDataContractsDatasetsAttachmentsDatasetAttachment.md)

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

# **companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_get**
> CodatDataContractsDatasetsAttachmentsDataset companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_get(company_id, connection_id, supplier_id)



### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import suppliers_api
from codat_python_sdk.model.codat_data_contracts_datasets_attachments_dataset import CodatDataContractsDatasetsAttachmentsDataset
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
    api_instance = suppliers_api.SuppliersApi(api_client)
    company_id = "companyId_example" # str | 
    connection_id = "connectionId_example" # str | 
    supplier_id = "supplierId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_get(company_id, connection_id, supplier_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling SuppliersApi->companies_company_id_connections_connection_id_data_suppliers_supplier_id_attachments_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **connection_id** | **str**|  |
 **supplier_id** | **str**|  |

### Return type

[**CodatDataContractsDatasetsAttachmentsDataset**](CodatDataContractsDatasetsAttachmentsDataset.md)

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

# **companies_company_id_connections_connection_id_push_suppliers_post**
> CodatDataContractsDatasetsSupplierPushOperation companies_company_id_connections_connection_id_push_suppliers_post(company_id, connection_id)



### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import suppliers_api
from codat_python_sdk.model.codat_data_contracts_datasets_supplier import CodatDataContractsDatasetsSupplier
from codat_python_sdk.model.codat_data_contracts_datasets_supplier_push_operation import CodatDataContractsDatasetsSupplierPushOperation
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
    api_instance = suppliers_api.SuppliersApi(api_client)
    company_id = "companyId_example" # str | 
    connection_id = "connectionId_example" # str | 
    timeout_in_minutes = 1 # int |  (optional)
    codat_data_contracts_datasets_supplier = CodatDataContractsDatasetsSupplier(
        id="id_example",
        supplier_name="supplier_name_example",
        contact_name="contact_name_example",
        email_address="email_address_example",
        phone="phone_example",
        addresses=[
            CodatDataContractsDatasetsAddress(
                type=CodatDataContractsDatasetsAddressType("Unknown"),
                line1="line1_example",
                line2="line2_example",
                city="city_example",
                region="region_example",
                country="country_example",
                postal_code="postal_code_example",
            ),
        ],
        registration_number="registration_number_example",
        tax_number="tax_number_example",
        status=CodatDataContractsDatasetsSupplierStatus("Unknown"),
        modified_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        source_modified_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        default_currency="default_currency_example",
    ) # CodatDataContractsDatasetsSupplier |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.companies_company_id_connections_connection_id_push_suppliers_post(company_id, connection_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling SuppliersApi->companies_company_id_connections_connection_id_push_suppliers_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.companies_company_id_connections_connection_id_push_suppliers_post(company_id, connection_id, timeout_in_minutes=timeout_in_minutes, codat_data_contracts_datasets_supplier=codat_data_contracts_datasets_supplier)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling SuppliersApi->companies_company_id_connections_connection_id_push_suppliers_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **connection_id** | **str**|  |
 **timeout_in_minutes** | **int**|  | [optional]
 **codat_data_contracts_datasets_supplier** | [**CodatDataContractsDatasetsSupplier**](CodatDataContractsDatasetsSupplier.md)|  | [optional]

### Return type

[**CodatDataContractsDatasetsSupplierPushOperation**](CodatDataContractsDatasetsSupplierPushOperation.md)

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

# **companies_company_id_data_suppliers_get**
> CodatDataContractsDatasetsSupplierPagedResponseModel companies_company_id_data_suppliers_get(company_id, )

Gets the latest suppliers for a company, with pagination

### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import suppliers_api
from codat_python_sdk.model.codat_data_contracts_datasets_supplier_paged_response_model import CodatDataContractsDatasetsSupplierPagedResponseModel
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
    api_instance = suppliers_api.SuppliersApi(api_client)
    company_id = "companyId_example" # str | 
    page_size = 100 # int |  (optional) if omitted the server will use the default value of 100
    query = "query_example" # str |  (optional)
    order_by = "orderBy_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets the latest suppliers for a company, with pagination
        api_response = api_instance.companies_company_id_data_suppliers_get(company_id, )
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling SuppliersApi->companies_company_id_data_suppliers_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets the latest suppliers for a company, with pagination
        api_response = api_instance.companies_company_id_data_suppliers_get(company_id, page_size=page_size, query=query, order_by=order_by)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling SuppliersApi->companies_company_id_data_suppliers_get: %s\n" % e)
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

[**CodatDataContractsDatasetsSupplierPagedResponseModel**](CodatDataContractsDatasetsSupplierPagedResponseModel.md)

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

# **companies_company_id_data_suppliers_supplier_id_get**
> CodatDataContractsDatasetsSupplier companies_company_id_data_suppliers_supplier_id_get(company_id, supplier_id)

Gets a single supplier corresponding to the supplied Id

### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import suppliers_api
from codat_python_sdk.model.codat_data_contracts_datasets_supplier import CodatDataContractsDatasetsSupplier
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
    api_instance = suppliers_api.SuppliersApi(api_client)
    company_id = "companyId_example" # str | 
    supplier_id = "supplierId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Gets a single supplier corresponding to the supplied Id
        api_response = api_instance.companies_company_id_data_suppliers_supplier_id_get(company_id, supplier_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling SuppliersApi->companies_company_id_data_suppliers_supplier_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **supplier_id** | **str**|  |

### Return type

[**CodatDataContractsDatasetsSupplier**](CodatDataContractsDatasetsSupplier.md)

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

