# codat_python_sdk.CustomersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_company_id_connections_connection_id_data_customers_customer_id_attachments_attachment_id_download_get**](CustomersApi.md#companies_company_id_connections_connection_id_data_customers_customer_id_attachments_attachment_id_download_get) | **GET** /companies/{companyId}/connections/{connectionId}/data/customers/{customerId}/attachments/{attachmentId}/download | 
[**companies_company_id_connections_connection_id_data_customers_customer_id_attachments_attachment_id_get**](CustomersApi.md#companies_company_id_connections_connection_id_data_customers_customer_id_attachments_attachment_id_get) | **GET** /companies/{companyId}/connections/{connectionId}/data/customers/{customerId}/attachments/{attachmentId} | 
[**companies_company_id_connections_connection_id_data_customers_customer_id_attachments_get**](CustomersApi.md#companies_company_id_connections_connection_id_data_customers_customer_id_attachments_get) | **GET** /companies/{companyId}/connections/{connectionId}/data/customers/{customerId}/attachments | 
[**companies_company_id_connections_connection_id_push_customers_customer_id_put**](CustomersApi.md#companies_company_id_connections_connection_id_push_customers_customer_id_put) | **PUT** /companies/{companyId}/connections/{connectionId}/push/customers/{customerId} | Posts an updated customer for a given company.
[**companies_company_id_connections_connection_id_push_customers_post**](CustomersApi.md#companies_company_id_connections_connection_id_push_customers_post) | **POST** /companies/{companyId}/connections/{connectionId}/push/customers | Posts an individual customer for a given company.
[**companies_company_id_data_customers_customer_id_get**](CustomersApi.md#companies_company_id_data_customers_customer_id_get) | **GET** /companies/{companyId}/data/customers/{customerId} | Gets a single customer corresponding to the supplied Id
[**companies_company_id_data_customers_get**](CustomersApi.md#companies_company_id_data_customers_get) | **GET** /companies/{companyId}/data/customers | Gets the latest customers for a company, with pagination


# **companies_company_id_connections_connection_id_data_customers_customer_id_attachments_attachment_id_download_get**
> companies_company_id_connections_connection_id_data_customers_customer_id_attachments_attachment_id_download_get(company_id, connection_id, customer_id, attachment_id)



### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import customers_api
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
    api_instance = customers_api.CustomersApi(api_client)
    company_id = "companyId_example" # str | 
    connection_id = "connectionId_example" # str | 
    customer_id = "customerId_example" # str | 
    attachment_id = "attachmentId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.companies_company_id_connections_connection_id_data_customers_customer_id_attachments_attachment_id_download_get(company_id, connection_id, customer_id, attachment_id)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling CustomersApi->companies_company_id_connections_connection_id_data_customers_customer_id_attachments_attachment_id_download_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **connection_id** | **str**|  |
 **customer_id** | **str**|  |
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

# **companies_company_id_connections_connection_id_data_customers_customer_id_attachments_attachment_id_get**
> CodatDataContractsDatasetsAttachmentsDatasetAttachment companies_company_id_connections_connection_id_data_customers_customer_id_attachments_attachment_id_get(company_id, connection_id, customer_id, attachment_id)



### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import customers_api
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
    api_instance = customers_api.CustomersApi(api_client)
    company_id = "companyId_example" # str | 
    connection_id = "connectionId_example" # str | 
    customer_id = "customerId_example" # str | 
    attachment_id = "attachmentId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.companies_company_id_connections_connection_id_data_customers_customer_id_attachments_attachment_id_get(company_id, connection_id, customer_id, attachment_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling CustomersApi->companies_company_id_connections_connection_id_data_customers_customer_id_attachments_attachment_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **connection_id** | **str**|  |
 **customer_id** | **str**|  |
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

# **companies_company_id_connections_connection_id_data_customers_customer_id_attachments_get**
> CodatDataContractsDatasetsAttachmentsDataset companies_company_id_connections_connection_id_data_customers_customer_id_attachments_get(company_id, connection_id, customer_id)



### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import customers_api
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
    api_instance = customers_api.CustomersApi(api_client)
    company_id = "companyId_example" # str | 
    connection_id = "connectionId_example" # str | 
    customer_id = "customerId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.companies_company_id_connections_connection_id_data_customers_customer_id_attachments_get(company_id, connection_id, customer_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling CustomersApi->companies_company_id_connections_connection_id_data_customers_customer_id_attachments_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **connection_id** | **str**|  |
 **customer_id** | **str**|  |

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

# **companies_company_id_connections_connection_id_push_customers_customer_id_put**
> CodatDataContractsDatasetsCustomerPushOperation companies_company_id_connections_connection_id_push_customers_customer_id_put(company_id, connection_id, customer_id)

Posts an updated customer for a given company.

### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import customers_api
from codat_python_sdk.model.codat_data_contracts_datasets_customer import CodatDataContractsDatasetsCustomer
from codat_python_sdk.model.codat_data_contracts_datasets_customer_push_operation import CodatDataContractsDatasetsCustomerPushOperation
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
    api_instance = customers_api.CustomersApi(api_client)
    company_id = "companyId_example" # str | 
    connection_id = "connectionId_example" # str | 
    customer_id = "customerId_example" # str | 
    timeout_in_minutes = 1 # int |  (optional)
    force_update = False # bool |  (optional) if omitted the server will use the default value of False
    codat_data_contracts_datasets_customer = CodatDataContractsDatasetsCustomer(
        id="id_example",
        customer_name="customer_name_example",
        contact_name="contact_name_example",
        email_address="email_address_example",
        default_currency="default_currency_example",
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
        contacts=[
            CodatDataContractsDatasetsContact(
                name="name_example",
                email="email_example",
                phone=[
                    CodatDataContractsDatasetsPhone(
                        number="number_example",
                        type=CodatDataContractsDatasetsPhoneType("Unknown"),
                    ),
                ],
                address=CodatDataContractsDatasetsAddress(
                    type=CodatDataContractsDatasetsAddressType("Unknown"),
                    line1="line1_example",
                    line2="line2_example",
                    city="city_example",
                    region="region_example",
                    country="country_example",
                    postal_code="postal_code_example",
                ),
                status=CodatDataContractsDatasetsCustomerStatus("Unknown"),
                modified_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
            ),
        ],
        registration_number="registration_number_example",
        tax_number="tax_number_example",
        status=CodatDataContractsDatasetsCustomerStatus("Unknown"),
        modified_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        source_modified_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # CodatDataContractsDatasetsCustomer |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Posts an updated customer for a given company.
        api_response = api_instance.companies_company_id_connections_connection_id_push_customers_customer_id_put(company_id, connection_id, customer_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling CustomersApi->companies_company_id_connections_connection_id_push_customers_customer_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Posts an updated customer for a given company.
        api_response = api_instance.companies_company_id_connections_connection_id_push_customers_customer_id_put(company_id, connection_id, customer_id, timeout_in_minutes=timeout_in_minutes, force_update=force_update, codat_data_contracts_datasets_customer=codat_data_contracts_datasets_customer)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling CustomersApi->companies_company_id_connections_connection_id_push_customers_customer_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **connection_id** | **str**|  |
 **customer_id** | **str**|  |
 **timeout_in_minutes** | **int**|  | [optional]
 **force_update** | **bool**|  | [optional] if omitted the server will use the default value of False
 **codat_data_contracts_datasets_customer** | [**CodatDataContractsDatasetsCustomer**](CodatDataContractsDatasetsCustomer.md)|  | [optional]

### Return type

[**CodatDataContractsDatasetsCustomerPushOperation**](CodatDataContractsDatasetsCustomerPushOperation.md)

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

# **companies_company_id_connections_connection_id_push_customers_post**
> CodatDataContractsDatasetsCustomerPushOperation companies_company_id_connections_connection_id_push_customers_post(company_id, connection_id)

Posts an individual customer for a given company.

### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import customers_api
from codat_python_sdk.model.codat_data_contracts_datasets_customer import CodatDataContractsDatasetsCustomer
from codat_python_sdk.model.codat_data_contracts_datasets_customer_push_operation import CodatDataContractsDatasetsCustomerPushOperation
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
    api_instance = customers_api.CustomersApi(api_client)
    company_id = "companyId_example" # str | 
    connection_id = "connectionId_example" # str | 
    timeout_in_minutes = 1 # int |  (optional)
    codat_data_contracts_datasets_customer = CodatDataContractsDatasetsCustomer(
        id="id_example",
        customer_name="customer_name_example",
        contact_name="contact_name_example",
        email_address="email_address_example",
        default_currency="default_currency_example",
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
        contacts=[
            CodatDataContractsDatasetsContact(
                name="name_example",
                email="email_example",
                phone=[
                    CodatDataContractsDatasetsPhone(
                        number="number_example",
                        type=CodatDataContractsDatasetsPhoneType("Unknown"),
                    ),
                ],
                address=CodatDataContractsDatasetsAddress(
                    type=CodatDataContractsDatasetsAddressType("Unknown"),
                    line1="line1_example",
                    line2="line2_example",
                    city="city_example",
                    region="region_example",
                    country="country_example",
                    postal_code="postal_code_example",
                ),
                status=CodatDataContractsDatasetsCustomerStatus("Unknown"),
                modified_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
            ),
        ],
        registration_number="registration_number_example",
        tax_number="tax_number_example",
        status=CodatDataContractsDatasetsCustomerStatus("Unknown"),
        modified_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        source_modified_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
    ) # CodatDataContractsDatasetsCustomer |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Posts an individual customer for a given company.
        api_response = api_instance.companies_company_id_connections_connection_id_push_customers_post(company_id, connection_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling CustomersApi->companies_company_id_connections_connection_id_push_customers_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Posts an individual customer for a given company.
        api_response = api_instance.companies_company_id_connections_connection_id_push_customers_post(company_id, connection_id, timeout_in_minutes=timeout_in_minutes, codat_data_contracts_datasets_customer=codat_data_contracts_datasets_customer)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling CustomersApi->companies_company_id_connections_connection_id_push_customers_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **connection_id** | **str**|  |
 **timeout_in_minutes** | **int**|  | [optional]
 **codat_data_contracts_datasets_customer** | [**CodatDataContractsDatasetsCustomer**](CodatDataContractsDatasetsCustomer.md)|  | [optional]

### Return type

[**CodatDataContractsDatasetsCustomerPushOperation**](CodatDataContractsDatasetsCustomerPushOperation.md)

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

# **companies_company_id_data_customers_customer_id_get**
> CodatDataContractsDatasetsCustomer companies_company_id_data_customers_customer_id_get(company_id, customer_id)

Gets a single customer corresponding to the supplied Id

### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import customers_api
from codat_python_sdk.model.codat_data_contracts_datasets_customer import CodatDataContractsDatasetsCustomer
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
    api_instance = customers_api.CustomersApi(api_client)
    company_id = "companyId_example" # str | 
    customer_id = "customerId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Gets a single customer corresponding to the supplied Id
        api_response = api_instance.companies_company_id_data_customers_customer_id_get(company_id, customer_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling CustomersApi->companies_company_id_data_customers_customer_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **customer_id** | **str**|  |

### Return type

[**CodatDataContractsDatasetsCustomer**](CodatDataContractsDatasetsCustomer.md)

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

# **companies_company_id_data_customers_get**
> CodatDataContractsDatasetsCustomerPagedResponseModel companies_company_id_data_customers_get(company_id, )

Gets the latest customers for a company, with pagination

### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import customers_api
from codat_python_sdk.model.codat_data_contracts_datasets_customer_paged_response_model import CodatDataContractsDatasetsCustomerPagedResponseModel
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
    api_instance = customers_api.CustomersApi(api_client)
    company_id = "companyId_example" # str | 
    page_size = 100 # int |  (optional) if omitted the server will use the default value of 100
    query = "query_example" # str |  (optional)
    order_by = "orderBy_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets the latest customers for a company, with pagination
        api_response = api_instance.companies_company_id_data_customers_get(company_id, )
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling CustomersApi->companies_company_id_data_customers_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets the latest customers for a company, with pagination
        api_response = api_instance.companies_company_id_data_customers_get(company_id, page_size=page_size, query=query, order_by=order_by)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling CustomersApi->companies_company_id_data_customers_get: %s\n" % e)
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

[**CodatDataContractsDatasetsCustomerPagedResponseModel**](CodatDataContractsDatasetsCustomerPagedResponseModel.md)

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

