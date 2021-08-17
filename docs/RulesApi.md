# codat_python_sdk.RulesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rules_alerts_alert_id_get**](RulesApi.md#rules_alerts_alert_id_get) | **GET** /rules/alerts/{alertId} | 
[**rules_alerts_alert_id_resolve_post**](RulesApi.md#rules_alerts_alert_id_resolve_post) | **POST** /rules/alerts/{alertId}/resolve | 
[**rules_alerts_get**](RulesApi.md#rules_alerts_get) | **GET** /rules/alerts | 
[**rules_get**](RulesApi.md#rules_get) | **GET** /rules | Fetch a list of rules a company is subscribed to
[**rules_post**](RulesApi.md#rules_post) | **POST** /rules | Subscribe to a rule
[**rules_rule_id_alerts_get**](RulesApi.md#rules_rule_id_alerts_get) | **GET** /rules/{ruleId}/alerts | 
[**rules_rule_id_delete**](RulesApi.md#rules_rule_id_delete) | **DELETE** /rules/{ruleId} | 
[**rules_rule_id_get**](RulesApi.md#rules_rule_id_get) | **GET** /rules/{ruleId} | 
[**rules_rule_id_put**](RulesApi.md#rules_rule_id_put) | **PUT** /rules/{ruleId} | 


# **rules_alerts_alert_id_get**
> CodatRulesContractsResponsesAlert rules_alerts_alert_id_get(alert_id)



### Example

* Api Key Authentication (API Key Auth):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import rules_api
from codat_python_sdk.model.codat_rules_contracts_responses_alert import CodatRulesContractsResponsesAlert
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
    api_instance = rules_api.RulesApi(api_client)
    alert_id = "alertId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.rules_alerts_alert_id_get(alert_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling RulesApi->rules_alerts_alert_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | **str**|  |

### Return type

[**CodatRulesContractsResponsesAlert**](CodatRulesContractsResponsesAlert.md)

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

# **rules_alerts_alert_id_resolve_post**
> CodatRulesContractsResponsesAlert rules_alerts_alert_id_resolve_post(alert_id)



### Example

* Api Key Authentication (API Key Auth):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import rules_api
from codat_python_sdk.model.codat_rules_contracts_responses_alert import CodatRulesContractsResponsesAlert
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
    api_instance = rules_api.RulesApi(api_client)
    alert_id = "alertId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.rules_alerts_alert_id_resolve_post(alert_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling RulesApi->rules_alerts_alert_id_resolve_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | **str**|  |

### Return type

[**CodatRulesContractsResponsesAlert**](CodatRulesContractsResponsesAlert.md)

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

# **rules_alerts_get**
> CodatRulesContractsResponsesAlertPagedResponseModel rules_alerts_get()



### Example

* Api Key Authentication (API Key Auth):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import rules_api
from codat_python_sdk.model.codat_rules_contracts_responses_alert_paged_response_model import CodatRulesContractsResponsesAlertPagedResponseModel
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
    api_instance = rules_api.RulesApi(api_client)
    company_id = "companyId_example" # str |  (optional)
    page_size = 100 # int |  (optional) if omitted the server will use the default value of 100
    query = "query_example" # str |  (optional)
    order_by = "orderBy_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.rules_alerts_get()
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling RulesApi->rules_alerts_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.rules_alerts_get(company_id=company_id, page_size=page_size, query=query, order_by=order_by)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling RulesApi->rules_alerts_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | defaults to 1
 **company_id** | **str**|  | [optional]
 **page_size** | **int**|  | [optional] if omitted the server will use the default value of 100
 **query** | **str**|  | [optional]
 **order_by** | **str**|  | [optional]

### Return type

[**CodatRulesContractsResponsesAlertPagedResponseModel**](CodatRulesContractsResponsesAlertPagedResponseModel.md)

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

# **rules_get**
> CodatPublicApiModelsRulesRulePagedResponseModel rules_get()

Fetch a list of rules a company is subscribed to

### Example

* Api Key Authentication (API Key Auth):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import rules_api
from codat_python_sdk.model.codat_public_api_models_rules_rule_paged_response_model import CodatPublicApiModelsRulesRulePagedResponseModel
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
    api_instance = rules_api.RulesApi(api_client)
    company_id = "companyId_example" # str |  (optional)
    page_size = 100 # int |  (optional) if omitted the server will use the default value of 100
    query = "query_example" # str |  (optional)
    order_by = "orderBy_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Fetch a list of rules a company is subscribed to
        api_response = api_instance.rules_get()
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling RulesApi->rules_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Fetch a list of rules a company is subscribed to
        api_response = api_instance.rules_get(company_id=company_id, page_size=page_size, query=query, order_by=order_by)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling RulesApi->rules_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | defaults to 1
 **company_id** | **str**|  | [optional]
 **page_size** | **int**|  | [optional] if omitted the server will use the default value of 100
 **query** | **str**|  | [optional]
 **order_by** | **str**|  | [optional]

### Return type

[**CodatPublicApiModelsRulesRulePagedResponseModel**](CodatPublicApiModelsRulesRulePagedResponseModel.md)

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

# **rules_post**
> CodatPublicApiModelsRulesRule rules_post()

Subscribe to a rule

### Example

* Api Key Authentication (API Key Auth):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import rules_api
from codat_python_sdk.model.codat_public_api_models_rules_rule import CodatPublicApiModelsRulesRule
from codat_python_sdk.model.codat_public_api_models_rules_add_rule_model import CodatPublicApiModelsRulesAddRuleModel
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
    api_instance = rules_api.RulesApi(api_client)
    codat_public_api_models_rules_add_rule_model = CodatPublicApiModelsRulesAddRuleModel(
        company_id="company_id_example",
        type="type_example",
        notifiers=CodatPublicApiModelsRulesNotifiers(
            emails=[
                "emails_example",
            ],
            webhook="webhook_example",
        ),
    ) # CodatPublicApiModelsRulesAddRuleModel |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Subscribe to a rule
        api_response = api_instance.rules_post(codat_public_api_models_rules_add_rule_model=codat_public_api_models_rules_add_rule_model)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling RulesApi->rules_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **codat_public_api_models_rules_add_rule_model** | [**CodatPublicApiModelsRulesAddRuleModel**](CodatPublicApiModelsRulesAddRuleModel.md)|  | [optional]

### Return type

[**CodatPublicApiModelsRulesRule**](CodatPublicApiModelsRulesRule.md)

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

# **rules_rule_id_alerts_get**
> CodatRulesContractsResponsesAlertPagedResponseModel rules_rule_id_alerts_get(rule_id, )



### Example

* Api Key Authentication (API Key Auth):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import rules_api
from codat_python_sdk.model.codat_rules_contracts_responses_alert_paged_response_model import CodatRulesContractsResponsesAlertPagedResponseModel
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
    api_instance = rules_api.RulesApi(api_client)
    rule_id = "ruleId_example" # str | 
    page_size = 100 # int |  (optional) if omitted the server will use the default value of 100
    query = "query_example" # str |  (optional)
    order_by = "orderBy_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.rules_rule_id_alerts_get(rule_id, )
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling RulesApi->rules_rule_id_alerts_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.rules_rule_id_alerts_get(rule_id, page_size=page_size, query=query, order_by=order_by)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling RulesApi->rules_rule_id_alerts_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**|  |
 **page** | **int**|  | defaults to 1
 **page_size** | **int**|  | [optional] if omitted the server will use the default value of 100
 **query** | **str**|  | [optional]
 **order_by** | **str**|  | [optional]

### Return type

[**CodatRulesContractsResponsesAlertPagedResponseModel**](CodatRulesContractsResponsesAlertPagedResponseModel.md)

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

# **rules_rule_id_delete**
> rules_rule_id_delete(rule_id)



### Example

* Api Key Authentication (API Key Auth):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import rules_api
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
    api_instance = rules_api.RulesApi(api_client)
    rule_id = "ruleId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.rules_rule_id_delete(rule_id)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling RulesApi->rules_rule_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**|  |

### Return type

void (empty response body)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rules_rule_id_get**
> CodatPublicApiModelsRulesRule rules_rule_id_get(rule_id)



### Example

* Api Key Authentication (API Key Auth):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import rules_api
from codat_python_sdk.model.codat_public_api_models_rules_rule import CodatPublicApiModelsRulesRule
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
    api_instance = rules_api.RulesApi(api_client)
    rule_id = "ruleId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.rules_rule_id_get(rule_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling RulesApi->rules_rule_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**|  |

### Return type

[**CodatPublicApiModelsRulesRule**](CodatPublicApiModelsRulesRule.md)

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

# **rules_rule_id_put**
> CodatPublicApiModelsRulesRule rules_rule_id_put(rule_id)



### Example

* Api Key Authentication (API Key Auth):
```python
import time
import codat_python_sdk
from codat_python_sdk.api import rules_api
from codat_python_sdk.model.codat_public_api_models_rules_rule import CodatPublicApiModelsRulesRule
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
    api_instance = rules_api.RulesApi(api_client)
    rule_id = "ruleId_example" # str | 
    codat_public_api_models_rules_rule = CodatPublicApiModelsRulesRule(
        id="id_example",
        type="type_example",
        company_id="company_id_example",
        notifiers=CodatPublicApiModelsRulesNotifiers(
            emails=[
                "emails_example",
            ],
            webhook="webhook_example",
        ),
    ) # CodatPublicApiModelsRulesRule |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.rules_rule_id_put(rule_id)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling RulesApi->rules_rule_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.rules_rule_id_put(rule_id, codat_public_api_models_rules_rule=codat_public_api_models_rules_rule)
        pprint(api_response)
    except codat_python_sdk.ApiException as e:
        print("Exception when calling RulesApi->rules_rule_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**|  |
 **codat_public_api_models_rules_rule** | [**CodatPublicApiModelsRulesRule**](CodatPublicApiModelsRulesRule.md)|  | [optional]

### Return type

[**CodatPublicApiModelsRulesRule**](CodatPublicApiModelsRulesRule.md)

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

