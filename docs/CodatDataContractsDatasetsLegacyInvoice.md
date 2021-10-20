# CodatDataContractsDatasetsLegacyInvoice


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issue_date** | **datetime** |  | 
**total_tax_amount** | **float** |  | 
**total_amount** | **float** |  | 
**amount_due** | **float** |  | 
**status** | [**CodatDataContractsDatasetsInvoiceStatus**](CodatDataContractsDatasetsInvoiceStatus.md) |  | 
**id** | **str, none_type** |  | [optional] 
**invoice_number** | **str, none_type** |  | [optional] 
**customer_ref** | [**CodatDataContractsDatasetsCustomerRef**](CodatDataContractsDatasetsCustomerRef.md) |  | [optional] 
**due_date** | **datetime, none_type** |  | [optional] 
**modified_date** | **datetime, none_type** |  | [optional] 
**source_modified_date** | **datetime, none_type** |  | [optional] 
**paid_on_date** | **datetime, none_type** |  | [optional] 
**currency** | **str, none_type** |  | [optional] 
**currency_rate** | **float, none_type** |  | [optional] 
**line_items** | [**[CodatDataContractsDatasetsInvoiceLineItem], none_type**](CodatDataContractsDatasetsInvoiceLineItem.md) |  | [optional] 
**payment_allocations** | [**[CodatDataContractsDatasetsLegacyInvoicePaymentAllocation], none_type**](CodatDataContractsDatasetsLegacyInvoicePaymentAllocation.md) |  | [optional] 
**withholding_tax** | [**[CodatDataContractsDatasetsWithholdingTax], none_type**](CodatDataContractsDatasetsWithholdingTax.md) |  | [optional] 
**total_discount** | **float, none_type** |  | [optional] 
**sub_total** | **float, none_type** |  | [optional] 
**additional_tax_amount** | **float** |  | [optional] 
**additional_tax_percentage** | **float** |  | [optional] 
**discount_percentage** | **float, none_type** |  | [optional] 
**note** | **str, none_type** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


