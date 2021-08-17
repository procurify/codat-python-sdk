# CodatDataContractsDatasetsBill


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issue_date** | **datetime** |  | 
**status** | [**CodatDataContractsDatasetsBillStatus**](CodatDataContractsDatasetsBillStatus.md) |  | 
**sub_total** | **float** |  | 
**tax_amount** | **float** |  | 
**total_amount** | **float** |  | 
**id** | **str, none_type** |  | [optional] 
**reference** | **str, none_type** |  | [optional] 
**supplier_ref** | [**CodatDataContractsDatasetsSupplierRef**](CodatDataContractsDatasetsSupplierRef.md) |  | [optional] 
**purchase_order_ref** | [**CodatDataContractsDatasetsPurchaseOrderRef**](CodatDataContractsDatasetsPurchaseOrderRef.md) |  | [optional] 
**purchase_order_refs** | [**[CodatDataContractsDatasetsPurchaseOrderRef], none_type**](CodatDataContractsDatasetsPurchaseOrderRef.md) |  | [optional] 
**due_date** | **datetime, none_type** |  | [optional] 
**currency** | **str, none_type** |  | [optional] 
**currency_rate** | **float, none_type** |  | [optional] 
**line_items** | [**[CodatDataContractsDatasetsBillLineItem], none_type**](CodatDataContractsDatasetsBillLineItem.md) |  | [optional] 
**withholding_tax** | [**[CodatDataContractsDatasetsWithholdingTax], none_type**](CodatDataContractsDatasetsWithholdingTax.md) |  | [optional] 
**amount_due** | **float, none_type** |  | [optional] 
**modified_date** | **datetime, none_type** |  | [optional] 
**source_modified_date** | **datetime, none_type** |  | [optional] 
**note** | **str, none_type** |  | [optional] 
**payment_allocations** | [**[CodatDataContractsDatasetsDetailedPaymentAllocation], none_type**](CodatDataContractsDatasetsDetailedPaymentAllocation.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


