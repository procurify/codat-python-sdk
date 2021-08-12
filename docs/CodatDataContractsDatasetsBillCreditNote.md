# CodatDataContractsDatasetsBillCreditNote

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**bill_credit_note_number** | **str** |  | [optional] 
**supplier_ref** | [**CodatDataContractsDatasetsSupplierRef**](CodatDataContractsDatasetsSupplierRef.md) |  | [optional] 
**withholding_tax** | [**list[CodatDataContractsDatasetsWithholdingTax]**](CodatDataContractsDatasetsWithholdingTax.md) |  | [optional] 
**total_amount** | **float** |  | 
**total_discount** | **float** |  | 
**sub_total** | **float** |  | 
**total_tax_amount** | **float** |  | 
**discount_percentage** | **float** |  | 
**remaining_credit** | **float** |  | 
**status** | [**CodatDataContractsDatasetsCreditNoteStatus**](CodatDataContractsDatasetsCreditNoteStatus.md) |  | 
**issue_date** | **datetime** |  | [optional] 
**allocated_on_date** | **datetime** |  | [optional] 
**currency** | **str** |  | [optional] 
**currency_rate** | **float** |  | [optional] 
**line_items** | [**list[CodatDataContractsDatasetsBillCreditNoteLineItem]**](CodatDataContractsDatasetsBillCreditNoteLineItem.md) |  | [optional] 
**payment_allocations** | [**list[CodatDataContractsDatasetsCreditNotePaymentAllocation]**](CodatDataContractsDatasetsCreditNotePaymentAllocation.md) |  | [optional] 
**modified_date** | **datetime** |  | [optional] 
**source_modified_date** | **datetime** |  | [optional] 
**note** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

