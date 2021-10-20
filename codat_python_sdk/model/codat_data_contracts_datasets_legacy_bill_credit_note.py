"""
    Codat API

    [What's changed in our Swagger](https://docs.codat.io/docs/new-swagger-ui)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from codat_python_sdk.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)
from ..model_utils import OpenApiModel
from codat_python_sdk.exceptions import ApiAttributeError


def lazy_import():
    from codat_python_sdk.model.codat_data_contracts_datasets_bill_credit_note_line_item import CodatDataContractsDatasetsBillCreditNoteLineItem
    from codat_python_sdk.model.codat_data_contracts_datasets_credit_note_status import CodatDataContractsDatasetsCreditNoteStatus
    from codat_python_sdk.model.codat_data_contracts_datasets_legacy_credit_note_payment_allocation import CodatDataContractsDatasetsLegacyCreditNotePaymentAllocation
    from codat_python_sdk.model.codat_data_contracts_datasets_supplier_ref import CodatDataContractsDatasetsSupplierRef
    from codat_python_sdk.model.codat_data_contracts_datasets_withholding_tax import CodatDataContractsDatasetsWithholdingTax
    globals()['CodatDataContractsDatasetsBillCreditNoteLineItem'] = CodatDataContractsDatasetsBillCreditNoteLineItem
    globals()['CodatDataContractsDatasetsCreditNoteStatus'] = CodatDataContractsDatasetsCreditNoteStatus
    globals()['CodatDataContractsDatasetsLegacyCreditNotePaymentAllocation'] = CodatDataContractsDatasetsLegacyCreditNotePaymentAllocation
    globals()['CodatDataContractsDatasetsSupplierRef'] = CodatDataContractsDatasetsSupplierRef
    globals()['CodatDataContractsDatasetsWithholdingTax'] = CodatDataContractsDatasetsWithholdingTax


class CodatDataContractsDatasetsLegacyBillCreditNote(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'total_amount': (float,),  # noqa: E501
            'total_discount': (float,),  # noqa: E501
            'sub_total': (float,),  # noqa: E501
            'total_tax_amount': (float,),  # noqa: E501
            'discount_percentage': (float,),  # noqa: E501
            'remaining_credit': (float,),  # noqa: E501
            'status': (CodatDataContractsDatasetsCreditNoteStatus,),  # noqa: E501
            'id': (str, none_type,),  # noqa: E501
            'bill_credit_note_number': (str, none_type,),  # noqa: E501
            'supplier_ref': (CodatDataContractsDatasetsSupplierRef,),  # noqa: E501
            'withholding_tax': ([CodatDataContractsDatasetsWithholdingTax], none_type,),  # noqa: E501
            'issue_date': (datetime,),  # noqa: E501
            'allocated_on_date': (datetime, none_type,),  # noqa: E501
            'currency': (str, none_type,),  # noqa: E501
            'currency_rate': (float, none_type,),  # noqa: E501
            'line_items': ([CodatDataContractsDatasetsBillCreditNoteLineItem], none_type,),  # noqa: E501
            'payment_allocations': ([CodatDataContractsDatasetsLegacyCreditNotePaymentAllocation], none_type,),  # noqa: E501
            'modified_date': (datetime, none_type,),  # noqa: E501
            'source_modified_date': (datetime, none_type,),  # noqa: E501
            'note': (str, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'total_amount': 'totalAmount',  # noqa: E501
        'total_discount': 'totalDiscount',  # noqa: E501
        'sub_total': 'subTotal',  # noqa: E501
        'total_tax_amount': 'totalTaxAmount',  # noqa: E501
        'discount_percentage': 'discountPercentage',  # noqa: E501
        'remaining_credit': 'remainingCredit',  # noqa: E501
        'status': 'status',  # noqa: E501
        'id': 'id',  # noqa: E501
        'bill_credit_note_number': 'billCreditNoteNumber',  # noqa: E501
        'supplier_ref': 'supplierRef',  # noqa: E501
        'withholding_tax': 'withholdingTax',  # noqa: E501
        'issue_date': 'issueDate',  # noqa: E501
        'allocated_on_date': 'allocatedOnDate',  # noqa: E501
        'currency': 'currency',  # noqa: E501
        'currency_rate': 'currencyRate',  # noqa: E501
        'line_items': 'lineItems',  # noqa: E501
        'payment_allocations': 'paymentAllocations',  # noqa: E501
        'modified_date': 'modifiedDate',  # noqa: E501
        'source_modified_date': 'sourceModifiedDate',  # noqa: E501
        'note': 'note',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, total_amount, total_discount, sub_total, total_tax_amount, discount_percentage, remaining_credit, status, *args, **kwargs):  # noqa: E501
        """CodatDataContractsDatasetsLegacyBillCreditNote - a model defined in OpenAPI

        Args:
            total_amount (float):
            total_discount (float):
            sub_total (float):
            total_tax_amount (float):
            discount_percentage (float):
            remaining_credit (float):
            status (CodatDataContractsDatasetsCreditNoteStatus):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            id (str, none_type): [optional]  # noqa: E501
            bill_credit_note_number (str, none_type): [optional]  # noqa: E501
            supplier_ref (CodatDataContractsDatasetsSupplierRef): [optional]  # noqa: E501
            withholding_tax ([CodatDataContractsDatasetsWithholdingTax], none_type): [optional]  # noqa: E501
            issue_date (datetime): [optional]  # noqa: E501
            allocated_on_date (datetime, none_type): [optional]  # noqa: E501
            currency (str, none_type): [optional]  # noqa: E501
            currency_rate (float, none_type): [optional]  # noqa: E501
            line_items ([CodatDataContractsDatasetsBillCreditNoteLineItem], none_type): [optional]  # noqa: E501
            payment_allocations ([CodatDataContractsDatasetsLegacyCreditNotePaymentAllocation], none_type): [optional]  # noqa: E501
            modified_date (datetime, none_type): [optional]  # noqa: E501
            source_modified_date (datetime, none_type): [optional]  # noqa: E501
            note (str, none_type): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.total_amount = total_amount
        self.total_discount = total_discount
        self.sub_total = sub_total
        self.total_tax_amount = total_tax_amount
        self.discount_percentage = discount_percentage
        self.remaining_credit = remaining_credit
        self.status = status
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, total_amount, total_discount, sub_total, total_tax_amount, discount_percentage, remaining_credit, status, *args, **kwargs):  # noqa: E501
        """CodatDataContractsDatasetsLegacyBillCreditNote - a model defined in OpenAPI

        Args:
            total_amount (float):
            total_discount (float):
            sub_total (float):
            total_tax_amount (float):
            discount_percentage (float):
            remaining_credit (float):
            status (CodatDataContractsDatasetsCreditNoteStatus):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            id (str, none_type): [optional]  # noqa: E501
            bill_credit_note_number (str, none_type): [optional]  # noqa: E501
            supplier_ref (CodatDataContractsDatasetsSupplierRef): [optional]  # noqa: E501
            withholding_tax ([CodatDataContractsDatasetsWithholdingTax], none_type): [optional]  # noqa: E501
            issue_date (datetime): [optional]  # noqa: E501
            allocated_on_date (datetime, none_type): [optional]  # noqa: E501
            currency (str, none_type): [optional]  # noqa: E501
            currency_rate (float, none_type): [optional]  # noqa: E501
            line_items ([CodatDataContractsDatasetsBillCreditNoteLineItem], none_type): [optional]  # noqa: E501
            payment_allocations ([CodatDataContractsDatasetsLegacyCreditNotePaymentAllocation], none_type): [optional]  # noqa: E501
            modified_date (datetime, none_type): [optional]  # noqa: E501
            source_modified_date (datetime, none_type): [optional]  # noqa: E501
            note (str, none_type): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.total_amount = total_amount
        self.total_discount = total_discount
        self.sub_total = sub_total
        self.total_tax_amount = total_tax_amount
        self.discount_percentage = discount_percentage
        self.remaining_credit = remaining_credit
        self.status = status
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
