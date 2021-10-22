# codat_python_sdk.PaymentMethodsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**companies_company_id_data_payment_methods_get**](PaymentMethodsApi.md#companies_company_id_data_payment_methods_get) | **GET** /companies/{companyId}/data/paymentMethods | Gets the payment methods for a given company.
[**companies_company_id_data_payment_methods_payment_method_id_get**](PaymentMethodsApi.md#companies_company_id_data_payment_methods_payment_method_id_get) | **GET** /companies/{companyId}/data/paymentMethods/{paymentMethodId} | Gets the specified payment method for a given company.


# **companies_company_id_data_payment_methods_get**
> CodatDataContractsDatasetsPaymentMethodPagedResponseModel companies_company_id_data_payment_methods_get(company_id, )

Gets the payment methods for a given company.

### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import payment_methods_api
from codat_python_sdk.model.codat_data_contracts_datasets_payment_method_paged_response_model import CodatDataContractsDatasetsPaymentMethodPagedResponseModel
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
    api_instance = payment_methods_api.PaymentMethodsApi(api_client)
    company_id = "companyId_example" # str | 
    page_size = 100 # int |  (optional) if omitted the server will use the default value of 100
    query = "query_example" # str |  (optional)
    order_by = "orderBy_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets the payment methods for a given company.
        api_response = api_instance.companies_company_id_data_payment_methods_get(company_id, )
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling PaymentMethodsApi->companies_company_id_data_payment_methods_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets the payment methods for a given company.
        api_response = api_instance.companies_company_id_data_payment_methods_get(company_id, page_size=page_size, query=query, order_by=order_by)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling PaymentMethodsApi->companies_company_id_data_payment_methods_get: %s\n" % e)
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

[**CodatDataContractsDatasetsPaymentMethodPagedResponseModel**](CodatDataContractsDatasetsPaymentMethodPagedResponseModel.md)

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

# **companies_company_id_data_payment_methods_payment_method_id_get**
> CodatDataContractsDatasetsPaymentMethod companies_company_id_data_payment_methods_payment_method_id_get(company_id, payment_method_id)

Gets the specified payment method for a given company.

### Example

* Api Key Authentication (API Key Auth):
* OAuth Authentication (Codat Login):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import payment_methods_api
from codat_python_sdk.model.codat_data_contracts_datasets_payment_method import CodatDataContractsDatasetsPaymentMethod
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
    api_instance = payment_methods_api.PaymentMethodsApi(api_client)
    company_id = "companyId_example" # str | 
    payment_method_id = "paymentMethodId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Gets the specified payment method for a given company.
        api_response = api_instance.companies_company_id_data_payment_methods_payment_method_id_get(company_id, payment_method_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling PaymentMethodsApi->companies_company_id_data_payment_methods_payment_method_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **payment_method_id** | **str**|  |

### Return type

[**CodatDataContractsDatasetsPaymentMethod**](CodatDataContractsDatasetsPaymentMethod.md)

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

