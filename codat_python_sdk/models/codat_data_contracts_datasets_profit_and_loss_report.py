# coding: utf-8

"""
    Codat API

    [What's changed in our Swagger](https://docs.codat.io/docs/new-swagger-ui)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class CodatDataContractsDatasetsProfitAndLossReport(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'from_date': 'datetime',
        'to_date': 'datetime',
        'income': 'CodatDataContractsDatasetsReportLine',
        'cost_of_sales': 'CodatDataContractsDatasetsReportLine',
        'gross_profit': 'float',
        'expenses': 'CodatDataContractsDatasetsReportLine',
        'net_operating_profit': 'float',
        'other_expenses': 'CodatDataContractsDatasetsReportLine',
        'other_income': 'CodatDataContractsDatasetsReportLine',
        'net_other_income': 'float',
        'net_profit': 'float'
    }

    attribute_map = {
        'from_date': 'fromDate',
        'to_date': 'toDate',
        'income': 'income',
        'cost_of_sales': 'costOfSales',
        'gross_profit': 'grossProfit',
        'expenses': 'expenses',
        'net_operating_profit': 'netOperatingProfit',
        'other_expenses': 'otherExpenses',
        'other_income': 'otherIncome',
        'net_other_income': 'netOtherIncome',
        'net_profit': 'netProfit'
    }

    def __init__(self, from_date=None, to_date=None, income=None, cost_of_sales=None, gross_profit=None, expenses=None, net_operating_profit=None, other_expenses=None, other_income=None, net_other_income=None, net_profit=None):  # noqa: E501
        """CodatDataContractsDatasetsProfitAndLossReport - a model defined in Swagger"""  # noqa: E501
        self._from_date = None
        self._to_date = None
        self._income = None
        self._cost_of_sales = None
        self._gross_profit = None
        self._expenses = None
        self._net_operating_profit = None
        self._other_expenses = None
        self._other_income = None
        self._net_other_income = None
        self._net_profit = None
        self.discriminator = None
        if from_date is not None:
            self.from_date = from_date
        if to_date is not None:
            self.to_date = to_date
        if income is not None:
            self.income = income
        if cost_of_sales is not None:
            self.cost_of_sales = cost_of_sales
        self.gross_profit = gross_profit
        if expenses is not None:
            self.expenses = expenses
        self.net_operating_profit = net_operating_profit
        if other_expenses is not None:
            self.other_expenses = other_expenses
        if other_income is not None:
            self.other_income = other_income
        self.net_other_income = net_other_income
        self.net_profit = net_profit

    @property
    def from_date(self):
        """Gets the from_date of this CodatDataContractsDatasetsProfitAndLossReport.  # noqa: E501


        :return: The from_date of this CodatDataContractsDatasetsProfitAndLossReport.  # noqa: E501
        :rtype: datetime
        """
        return self._from_date

    @from_date.setter
    def from_date(self, from_date):
        """Sets the from_date of this CodatDataContractsDatasetsProfitAndLossReport.


        :param from_date: The from_date of this CodatDataContractsDatasetsProfitAndLossReport.  # noqa: E501
        :type: datetime
        """

        self._from_date = from_date

    @property
    def to_date(self):
        """Gets the to_date of this CodatDataContractsDatasetsProfitAndLossReport.  # noqa: E501


        :return: The to_date of this CodatDataContractsDatasetsProfitAndLossReport.  # noqa: E501
        :rtype: datetime
        """
        return self._to_date

    @to_date.setter
    def to_date(self, to_date):
        """Sets the to_date of this CodatDataContractsDatasetsProfitAndLossReport.


        :param to_date: The to_date of this CodatDataContractsDatasetsProfitAndLossReport.  # noqa: E501
        :type: datetime
        """

        self._to_date = to_date

    @property
    def income(self):
        """Gets the income of this CodatDataContractsDatasetsProfitAndLossReport.  # noqa: E501


        :return: The income of this CodatDataContractsDatasetsProfitAndLossReport.  # noqa: E501
        :rtype: CodatDataContractsDatasetsReportLine
        """
        return self._income

    @income.setter
    def income(self, income):
        """Sets the income of this CodatDataContractsDatasetsProfitAndLossReport.


        :param income: The income of this CodatDataContractsDatasetsProfitAndLossReport.  # noqa: E501
        :type: CodatDataContractsDatasetsReportLine
        """

        self._income = income

    @property
    def cost_of_sales(self):
        """Gets the cost_of_sales of this CodatDataContractsDatasetsProfitAndLossReport.  # noqa: E501


        :return: The cost_of_sales of this CodatDataContractsDatasetsProfitAndLossReport.  # noqa: E501
        :rtype: CodatDataContractsDatasetsReportLine
        """
        return self._cost_of_sales

    @cost_of_sales.setter
    def cost_of_sales(self, cost_of_sales):
        """Sets the cost_of_sales of this CodatDataContractsDatasetsProfitAndLossReport.


        :param cost_of_sales: The cost_of_sales of this CodatDataContractsDatasetsProfitAndLossReport.  # noqa: E501
        :type: CodatDataContractsDatasetsReportLine
        """

        self._cost_of_sales = cost_of_sales

    @property
    def gross_profit(self):
        """Gets the gross_profit of this CodatDataContractsDatasetsProfitAndLossReport.  # noqa: E501


        :return: The gross_profit of this CodatDataContractsDatasetsProfitAndLossReport.  # noqa: E501
        :rtype: float
        """
        return self._gross_profit

    @gross_profit.setter
    def gross_profit(self, gross_profit):
        """Sets the gross_profit of this CodatDataContractsDatasetsProfitAndLossReport.


        :param gross_profit: The gross_profit of this CodatDataContractsDatasetsProfitAndLossReport.  # noqa: E501
        :type: float
        """
        if gross_profit is None:
            raise ValueError("Invalid value for `gross_profit`, must not be `None`")  # noqa: E501

        self._gross_profit = gross_profit

    @property
    def expenses(self):
        """Gets the expenses of this CodatDataContractsDatasetsProfitAndLossReport.  # noqa: E501


        :return: The expenses of this CodatDataContractsDatasetsProfitAndLossReport.  # noqa: E501
        :rtype: CodatDataContractsDatasetsReportLine
        """
        return self._expenses

    @expenses.setter
    def expenses(self, expenses):
        """Sets the expenses of this CodatDataContractsDatasetsProfitAndLossReport.


        :param expenses: The expenses of this CodatDataContractsDatasetsProfitAndLossReport.  # noqa: E501
        :type: CodatDataContractsDatasetsReportLine
        """

        self._expenses = expenses

    @property
    def net_operating_profit(self):
        """Gets the net_operating_profit of this CodatDataContractsDatasetsProfitAndLossReport.  # noqa: E501


        :return: The net_operating_profit of this CodatDataContractsDatasetsProfitAndLossReport.  # noqa: E501
        :rtype: float
        """
        return self._net_operating_profit

    @net_operating_profit.setter
    def net_operating_profit(self, net_operating_profit):
        """Sets the net_operating_profit of this CodatDataContractsDatasetsProfitAndLossReport.


        :param net_operating_profit: The net_operating_profit of this CodatDataContractsDatasetsProfitAndLossReport.  # noqa: E501
        :type: float
        """
        if net_operating_profit is None:
            raise ValueError("Invalid value for `net_operating_profit`, must not be `None`")  # noqa: E501

        self._net_operating_profit = net_operating_profit

    @property
    def other_expenses(self):
        """Gets the other_expenses of this CodatDataContractsDatasetsProfitAndLossReport.  # noqa: E501


        :return: The other_expenses of this CodatDataContractsDatasetsProfitAndLossReport.  # noqa: E501
        :rtype: CodatDataContractsDatasetsReportLine
        """
        return self._other_expenses

    @other_expenses.setter
    def other_expenses(self, other_expenses):
        """Sets the other_expenses of this CodatDataContractsDatasetsProfitAndLossReport.


        :param other_expenses: The other_expenses of this CodatDataContractsDatasetsProfitAndLossReport.  # noqa: E501
        :type: CodatDataContractsDatasetsReportLine
        """

        self._other_expenses = other_expenses

    @property
    def other_income(self):
        """Gets the other_income of this CodatDataContractsDatasetsProfitAndLossReport.  # noqa: E501


        :return: The other_income of this CodatDataContractsDatasetsProfitAndLossReport.  # noqa: E501
        :rtype: CodatDataContractsDatasetsReportLine
        """
        return self._other_income

    @other_income.setter
    def other_income(self, other_income):
        """Sets the other_income of this CodatDataContractsDatasetsProfitAndLossReport.


        :param other_income: The other_income of this CodatDataContractsDatasetsProfitAndLossReport.  # noqa: E501
        :type: CodatDataContractsDatasetsReportLine
        """

        self._other_income = other_income

    @property
    def net_other_income(self):
        """Gets the net_other_income of this CodatDataContractsDatasetsProfitAndLossReport.  # noqa: E501


        :return: The net_other_income of this CodatDataContractsDatasetsProfitAndLossReport.  # noqa: E501
        :rtype: float
        """
        return self._net_other_income

    @net_other_income.setter
    def net_other_income(self, net_other_income):
        """Sets the net_other_income of this CodatDataContractsDatasetsProfitAndLossReport.


        :param net_other_income: The net_other_income of this CodatDataContractsDatasetsProfitAndLossReport.  # noqa: E501
        :type: float
        """
        if net_other_income is None:
            raise ValueError("Invalid value for `net_other_income`, must not be `None`")  # noqa: E501

        self._net_other_income = net_other_income

    @property
    def net_profit(self):
        """Gets the net_profit of this CodatDataContractsDatasetsProfitAndLossReport.  # noqa: E501


        :return: The net_profit of this CodatDataContractsDatasetsProfitAndLossReport.  # noqa: E501
        :rtype: float
        """
        return self._net_profit

    @net_profit.setter
    def net_profit(self, net_profit):
        """Sets the net_profit of this CodatDataContractsDatasetsProfitAndLossReport.


        :param net_profit: The net_profit of this CodatDataContractsDatasetsProfitAndLossReport.  # noqa: E501
        :type: float
        """
        if net_profit is None:
            raise ValueError("Invalid value for `net_profit`, must not be `None`")  # noqa: E501

        self._net_profit = net_profit

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(CodatDataContractsDatasetsProfitAndLossReport, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CodatDataContractsDatasetsProfitAndLossReport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other