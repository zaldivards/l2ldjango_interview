"""Custom Django filters for the l2l app"""

from datetime import datetime
from typing import Union

from django import template

register = template.Library()


def l2l_dt(value: Union[datetime, str]) -> str:
    """Custom Django filter for transforming a datetime/date string into the %Y-%m-%d %H:%M:%S format

    Parameters
    ----------
    value : Union[datetime, str]
        Either a datetime object or a date string in the %Y-%m-%dT%H:%M:%S format

    Returns
    -------
    str
        A string representation of the given value, following the `%Y-%m-%d %H:%M:%S` format
    """
    expected_format = "%Y-%m-%d %H:%M:%S"
    if isinstance(value, datetime):
        return value.strftime(expected_format)
    return datetime.strptime(value, "%Y-%m-%dT%H:%M:%S").strftime(expected_format)


register.filter("l2l_dt", l2l_dt)
