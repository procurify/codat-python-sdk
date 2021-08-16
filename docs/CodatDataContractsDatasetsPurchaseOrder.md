# CodatDataContractsDatasetsPurchaseOrder


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str, none_type** |  | [optional] 
**purchase_order_number** | **str, none_type** |  | [optional] 
**issue_date** | **datetime** |  | [optional] 
**payment_due_date** | **datetime, none_type** |  | [optional] 
**expected_delivery_date** | **datetime, none_type** |  | [optional] 
**delivery_date** | **datetime, none_type** |  | [optional] 
**note** | **str, none_type** |  | [optional] 
**ship_to** | [**CodatDataContractsDatasetsShipTo**](CodatDataContractsDatasetsShipTo.md) |  | [optional] 
**supplier_ref** | [**CodatDataContractsDatasetsSupplierRef**](CodatDataContractsDatasetsSupplierRef.md) |  | [optional] 
**bill_ref** | [**CodatDataContractsDatasetsBillRef**](CodatDataContractsDatasetsBillRef.md) |  | [optional] 
**status** | [**CodatDataContractsDatasetsPurchaseOrderStatus**](CodatDataContractsDatasetsPurchaseOrderStatus.md) |  | [optional] 
**currency** | **str, none_type** |  | [optional] 
**currency_rate** | **float, none_type** |  | [optional] 
**line_items** | [**[CodatDataContractsDatasetsPurchaseOrderLineItem], none_type**](CodatDataContractsDatasetsPurchaseOrderLineItem.md) |  | [optional] 
**total_discount** | **float** |  | [optional] 
**sub_total** | **float** |  | [optional] 
**total_tax_amount** | **float** |  | [optional] 
**total_amount** | **float** |  | [optional] 
**modified_date** | **datetime, none_type** |  | [optional] 
**source_modified_date** | **datetime, none_type** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


