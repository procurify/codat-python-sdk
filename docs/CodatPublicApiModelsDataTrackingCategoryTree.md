# CodatPublicApiModelsDataTrackingCategoryTree

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub_categories** | [**list[CodatPublicApiModelsDataTrackingCategoryTree]**](CodatPublicApiModelsDataTrackingCategoryTree.md) |  | [optional] 
**id** | **str** | The identifier for the item, unique per tracking category | [optional] 
**parent_id** | **str** | The identifier for this item&#x27;s immediate parent | [optional] 
**modified_date** | **datetime** | The date the record was last updated in the system cache | [optional] 
**source_modified_date** | **datetime** | The date the record was last changed in the originating system | [optional] 
**name** | **str** | The name of the tracking category | [optional] 
**has_children** | **bool** | Boolean value indicating whether this category has SubCategories | [optional] 
**status** | [**CodatDataContractsDatasetsTrackingCategoryStatus**](CodatDataContractsDatasetsTrackingCategoryStatus.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

