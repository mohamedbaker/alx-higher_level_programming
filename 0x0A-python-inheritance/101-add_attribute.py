#!/usr/bin/python3
"""func that  adds attrs to objects."""


def add_attribute(obj, att, value):
    """Adds new attr to an object.
    Args:
        obj : The object reciving the attr.
        att: The name of the attribute.
        valu: value.
    Raises:
        TypeError: If the attr cannt be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
