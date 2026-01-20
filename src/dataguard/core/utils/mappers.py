import polars as pl

from dataguard.core.utils.enums import (
    CheckCases,
    ValidationType,
)

validation_type_mapper = {
    ValidationType.DATE: pl.Date,
    ValidationType.DATETIME: pl.Datetime,
    ValidationType.BOOL: pl.Boolean,
    ValidationType.FLOAT: pl.Float64,
    ValidationType.INT: pl.Int64,
    ValidationType.STR: pl.Utf8,
    # Cannot cast numerical to categorical, so reling on String
    ValidationType.CAT: pl.Utf8,
    ValidationType.DECIMAL: pl.Decimal,
}

check_cases_mapper = {
    CheckCases.CONDITION: 'when_then',
    CheckCases.CONJUNCTION: 'and_',
    CheckCases.DISJUNCTION: 'or_',
}

expression_mapper = {
    'is_equal_to': 'eq',
    'is_equal_to_or_both_missing': 'eq_missing',
    'is_greater_than_or_equal_to': 'ge',
    'is_greater_than': 'gt',
    'is_less_than_or_equal_to': 'le',
    'is_less_than': 'lt',
    'is_not_equal_to': 'ne',
    'is_not_equal_to_and_not_both_missing': 'ne_missing',
    'is_unique': 'is_unique',
    'is_duplicated': 'is_duplicated',
    'is_in': 'is_in',
    'is_null': 'is_null',
    'is_not_null': 'is_not_null',
}

# maps for errors

title_mapper = {
    'is_equal_to': 'equal to',
    'is_equal_to_or_both_missing': 'equal to or both are missing',
    'is_greater_than_or_equal_to': 'greater than or equal to',
    'is_greater_than': 'greater than',
    'is_less_than_or_equal_to': 'less than or equal to',
    'is_less_than': 'less than',
    'is_not_equal_to': 'not equal to',
    'is_not_equal_to_and_not_both_missing': 'not equal to and not both are missing',  # noqa: E501
    'is_unique': 'unique',
    'is_duplicated': 'duplicated',
    'is_in': 'in',
    'is_null': 'missing',
    'is_not_null': 'not missing',
}

msg_mapper = {
    'is_equal_to': 'be equal to',
    'is_equal_to_or_both_missing': 'either not contain any values or must be equal to',  # noqa: E501
    'is_greater_than_or_equal_to': 'be greater than or equal to',
    'is_greater_than': 'be greater than',
    'is_less_than_or_equal_to': 'be less than or equal to',
    'is_less_than': 'be less than',
    'is_not_equal_to': 'not be equal to',
    'is_not_equal_to_and_not_both_missing': 'contain values and must be different from',  # noqa: E501
    'is_unique': 'be unique',
    'is_duplicated': 'be duplicated',
    'is_in': 'be in',
    'is_null': 'not contain any values',
    'is_not_null': 'contain values',
}
