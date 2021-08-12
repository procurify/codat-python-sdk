# swagger_client.RulesApi

All URIs are relative to */*

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
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: API Key Auth
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.RulesApi(swagger_client.ApiClient(configuration))
alert_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    api_response = api_instance.rules_alerts_alert_id_get(alert_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RulesApi->rules_alerts_alert_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | [**str**](.md)|  | 

### Return type

[**CodatRulesContractsResponsesAlert**](CodatRulesContractsResponsesAlert.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rules_alerts_alert_id_resolve_post**
> CodatRulesContractsResponsesAlert rules_alerts_alert_id_resolve_post(alert_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: API Key Auth
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.RulesApi(swagger_client.ApiClient(configuration))
alert_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    api_response = api_instance.rules_alerts_alert_id_resolve_post(alert_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RulesApi->rules_alerts_alert_id_resolve_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_id** | [**str**](.md)|  | 

### Return type

[**CodatRulesContractsResponsesAlert**](CodatRulesContractsResponsesAlert.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rules_alerts_get**
> CodatRulesContractsResponsesAlertPagedResponseModel rules_alerts_get(page, company_id=company_id, page_size=page_size, query=query, order_by=order_by)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: API Key Auth
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.RulesApi(swagger_client.ApiClient(configuration))
page = 1 # int |  (default to 1)
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
page_size = 100 # int |  (optional) (default to 100)
query = 'query_example' # str |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    api_response = api_instance.rules_alerts_get(page, company_id=company_id, page_size=page_size, query=query, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RulesApi->rules_alerts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [default to 1]
 **company_id** | [**str**](.md)|  | [optional] 
 **page_size** | **int**|  | [optional] [default to 100]
 **query** | **str**|  | [optional] 
 **order_by** | **str**|  | [optional] 

### Return type

[**CodatRulesContractsResponsesAlertPagedResponseModel**](CodatRulesContractsResponsesAlertPagedResponseModel.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rules_get**
> CodatPublicApiModelsRulesRulePagedResponseModel rules_get(page, company_id=company_id, page_size=page_size, query=query, order_by=order_by)

Fetch a list of rules a company is subscribed to

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: API Key Auth
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.RulesApi(swagger_client.ApiClient(configuration))
page = 1 # int |  (default to 1)
company_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str |  (optional)
page_size = 100 # int |  (optional) (default to 100)
query = 'query_example' # str |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    # Fetch a list of rules a company is subscribed to
    api_response = api_instance.rules_get(page, company_id=company_id, page_size=page_size, query=query, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RulesApi->rules_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [default to 1]
 **company_id** | [**str**](.md)|  | [optional] 
 **page_size** | **int**|  | [optional] [default to 100]
 **query** | **str**|  | [optional] 
 **order_by** | **str**|  | [optional] 

### Return type

[**CodatPublicApiModelsRulesRulePagedResponseModel**](CodatPublicApiModelsRulesRulePagedResponseModel.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rules_post**
> CodatPublicApiModelsRulesRule rules_post(body=body)

Subscribe to a rule

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: API Key Auth
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.RulesApi(swagger_client.ApiClient(configuration))
body = swagger_client.CodatPublicApiModelsRulesAddRuleModel() # CodatPublicApiModelsRulesAddRuleModel |  (optional)

try:
    # Subscribe to a rule
    api_response = api_instance.rules_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RulesApi->rules_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CodatPublicApiModelsRulesAddRuleModel**](CodatPublicApiModelsRulesAddRuleModel.md)|  | [optional] 

### Return type

[**CodatPublicApiModelsRulesRule**](CodatPublicApiModelsRulesRule.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rules_rule_id_alerts_get**
> CodatRulesContractsResponsesAlertPagedResponseModel rules_rule_id_alerts_get(rule_id, page, page_size=page_size, query=query, order_by=order_by)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: API Key Auth
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.RulesApi(swagger_client.ApiClient(configuration))
rule_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
page = 1 # int |  (default to 1)
page_size = 100 # int |  (optional) (default to 100)
query = 'query_example' # str |  (optional)
order_by = 'order_by_example' # str |  (optional)

try:
    api_response = api_instance.rules_rule_id_alerts_get(rule_id, page, page_size=page_size, query=query, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RulesApi->rules_rule_id_alerts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | [**str**](.md)|  | 
 **page** | **int**|  | [default to 1]
 **page_size** | **int**|  | [optional] [default to 100]
 **query** | **str**|  | [optional] 
 **order_by** | **str**|  | [optional] 

### Return type

[**CodatRulesContractsResponsesAlertPagedResponseModel**](CodatRulesContractsResponsesAlertPagedResponseModel.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rules_rule_id_delete**
> rules_rule_id_delete(rule_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: API Key Auth
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.RulesApi(swagger_client.ApiClient(configuration))
rule_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    api_instance.rules_rule_id_delete(rule_id)
except ApiException as e:
    print("Exception when calling RulesApi->rules_rule_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rules_rule_id_get**
> CodatPublicApiModelsRulesRule rules_rule_id_get(rule_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: API Key Auth
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.RulesApi(swagger_client.ApiClient(configuration))
rule_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    api_response = api_instance.rules_rule_id_get(rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RulesApi->rules_rule_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | [**str**](.md)|  | 

### Return type

[**CodatPublicApiModelsRulesRule**](CodatPublicApiModelsRulesRule.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rules_rule_id_put**
> CodatPublicApiModelsRulesRule rules_rule_id_put(rule_id, body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: API Key Auth
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.RulesApi(swagger_client.ApiClient(configuration))
rule_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
body = swagger_client.CodatPublicApiModelsRulesRule() # CodatPublicApiModelsRulesRule |  (optional)

try:
    api_response = api_instance.rules_rule_id_put(rule_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RulesApi->rules_rule_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | [**str**](.md)|  | 
 **body** | [**CodatPublicApiModelsRulesRule**](CodatPublicApiModelsRulesRule.md)|  | [optional] 

### Return type

[**CodatPublicApiModelsRulesRule**](CodatPublicApiModelsRulesRule.md)

### Authorization

[API Key Auth](../README.md#API Key Auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

