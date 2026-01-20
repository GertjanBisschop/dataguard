import pytest
from pydantic import ValidationError
from dataguard.core.check.schemas import SimpleCheckExpression, CaseCheckExpression
from dataguard.core.utils.enums import CheckCases
from dataguard.core.utils.mappers import expression_mapper

@pytest.fixture
def fake_callable():
    def callable_function(*args, **kwargs):
        return "fake_result"
    return callable_function


def test_case_check_expression_valid():
    expression_mapper['test_command'] = 'mapped_command'
    simple_expr = SimpleCheckExpression(command='test_command')
    case_expr = CaseCheckExpression(
        check_case=CheckCases.CONJUNCTION,
        expressions=[simple_expr, simple_expr]
    )
    assert case_expr.check_case == CheckCases.CONJUNCTION
    assert len(case_expr.expressions) == 2


def test_case_check_expression_invalid_length():
    expression_mapper['test_command'] = 'mapped_command'
    simple_expr = SimpleCheckExpression(command='test_command')
    with pytest.raises(ValidationError) as exc_info:
        CaseCheckExpression(
            check_case=CheckCases.CONJUNCTION,
            expressions=[simple_expr]
        )
    
def test_simple_check_expression_get_check_name():
    instance = SimpleCheckExpression(command='is_equal_to')
    assert instance.get_check_title() == 'equal to'


def test_simple_check_expression_get_message_with_subject():
    instance = SimpleCheckExpression(command='is_equal_to', subject=['column1', 'column2'])
    assert instance.get_check_message() == "The column(s) under validation must be equal to"


def test_simple_check_expression_get_message_with_arg_values():
    instance = SimpleCheckExpression(command='is_equal_to', arg_values=[1, 2, 3])
    assert instance.get_check_message() == 'The column(s) under validation must be equal to [1, 2, 3]'


def test_simple_check_expression_get_message_with_arg_columns():
    instance = SimpleCheckExpression(command='is_equal_to', arg_columns=['col1', 'col2'])
    assert instance.get_check_message() == "The column(s) under validation must be equal to ['col1', 'col2']"


def test_simple_check_expression_map_command():
    expression_mapper['is_equal_to'] = 'mapped_command'
    instance = SimpleCheckExpression(command='is_equal_to')
    instance.map_command()
    assert instance.command == 'mapped_command'


def test_simple_check_expression_get_args():
    instance = SimpleCheckExpression(
        command='is_equal_to',
        subject=['column1'],
        arg_values=[1, 2],
        arg_columns=['col1']
    )
    args = instance.get_args()
    assert args == {
        'subject': ['column1'],
        'arg_values': [1, 2],
        'arg_columns': ['col1']
    }


def test_case_check_expression_get_check_name():
    expression_mapper['is_equal_to'] = 'mapped_command'
    simple_expr = SimpleCheckExpression(command='is_equal_to')
    case_expr = CaseCheckExpression(
        check_case=CheckCases.CONJUNCTION,
        expressions=[simple_expr, simple_expr]
    )
    assert case_expr.get_check_title() == 'equal to and equal to'


def test_case_check_expression_get_message():
    expression_mapper['is_equal_to'] = 'mapped_command'
    simple_expr = SimpleCheckExpression(command='is_equal_to', subject=['column1'])
    case_expr = CaseCheckExpression(
        check_case=CheckCases.CONJUNCTION,
        expressions=[simple_expr, simple_expr]
    )
    assert case_expr.get_check_message() == (
        'The column(s) under validation must be equal to and The column(s) under validation must be equal to'
    )


def test_case_check_expression_get_args():
    expression_mapper['is_equal_to'] = 'mapped_command'
    simple_expr = SimpleCheckExpression(
        command='is_equal_to',
        subject=['column1'],
        arg_values=[1, 2]
    )
    case_expr = CaseCheckExpression(
        check_case=CheckCases.CONJUNCTION,
        expressions=[simple_expr, simple_expr]
    )
    args = case_expr.get_args()
    assert args == [
        {'subject': ['column1'], 'arg_values': [1, 2]},
        {'subject': ['column1'], 'arg_values': [1, 2]}
    ]


def test_case_check_expression_invalid_case():
    expression_mapper['is_equal_to'] = 'mapped_command'
    simple_expr = SimpleCheckExpression(command='is_equal_to')
    with pytest.raises(ValidationError) as exc_info:
        CaseCheckExpression(
            check_case='invalid_case',  # Invalid case
            expressions=[simple_expr, simple_expr]
        )