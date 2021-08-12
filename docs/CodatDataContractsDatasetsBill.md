# CodatDataContractsDatasetsBill

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**reference** | **str** |  | [optional] 
**supplier_ref** | [**CodatDataContractsDatasetsSupplierRef**](CodatDataContractsDatasetsSupplierRef.md) |  | [optional] 
**purchase_order_ref** | [**CodatDataContractsDatasetsPurchaseOrderRef**](CodatDataContractsDatasetsPurchaseOrderRef.md) |  | [optional] 
**purchase_order_refs** | [**list[CodatDataContractsDatasetsPurchaseOrderRef]**](CodatDataContractsDatasetsPurchaseOrderRef.md) |  | [optional] 
**issue_date** | **datetime** |  | 
**due_date** | **datetime** |  | [optional] 
**currency** | **str** |  | [optional] 
**currency_rate** | **float** |  | [optional] 
**line_items** | [**list[CodatDataContractsDatasetsBillLineItem]**](CodatDataContractsDatasetsBillLineItem.md) |  | [optional] 
**withholding_tax** | [**list[CodatDataContractsDatasetsWithholdingTax]**](CodatDataContractsDatasetsWithholdingTax.md) |  | [optional] 
**status** | [**CodatDataContractsDatasetsBillStatus**](CodatDataContractsDatasetsBillStatus.md) |  | 
**sub_total** | **float** |  | 
**tax_amount** | **float** |  | 
**total_amount** | **float** |  | 
**amount_due** | **float** |  | [optional] 
**modified_date** | **datetime** |  | [optional] 
**source_modified_date** | **datetime** |  | [optional] 
**note** | **str** |  | [optional] 
**payment_allocations** | [**list[CodatDataContractsDatasetsDetailedPaymentAllocation]**](CodatDataContractsDatasetsDetailedPaymentAllocation.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

