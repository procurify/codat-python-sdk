# CodatDataContractsDatasetsInvoice

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**invoice_number** | **str** |  | [optional] 
**customer_ref** | [**CodatDataContractsDatasetsCustomerRef**](CodatDataContractsDatasetsCustomerRef.md) |  | [optional] 
**issue_date** | **datetime** |  | 
**due_date** | **datetime** |  | [optional] 
**modified_date** | **datetime** |  | [optional] 
**source_modified_date** | **datetime** |  | [optional] 
**paid_on_date** | **datetime** |  | [optional] 
**currency** | **str** |  | [optional] 
**currency_rate** | **float** |  | [optional] 
**line_items** | [**list[CodatDataContractsDatasetsInvoiceLineItem]**](CodatDataContractsDatasetsInvoiceLineItem.md) |  | [optional] 
**payment_allocations** | [**list[CodatDataContractsDatasetsInvoicePaymentAllocation]**](CodatDataContractsDatasetsInvoicePaymentAllocation.md) |  | [optional] 
**withholding_tax** | [**list[CodatDataContractsDatasetsWithholdingTax]**](CodatDataContractsDatasetsWithholdingTax.md) |  | [optional] 
**total_discount** | **float** |  | [optional] 
**sub_total** | **float** |  | [optional] 
**total_tax_amount** | **float** |  | 
**total_amount** | **float** |  | 
**amount_due** | **float** |  | 
**discount_percentage** | **float** |  | [optional] 
**status** | [**CodatDataContractsDatasetsInvoiceStatus**](CodatDataContractsDatasetsInvoiceStatus.md) |  | 
**note** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

