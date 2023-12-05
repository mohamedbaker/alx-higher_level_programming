#!/usr/bin/python3
"""Module My Int that inherits from int."""


class MyInt(int):
    """Invert int operators == and !=."""

    def __eq__(self, value):
        """Override == opeartor to !=."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator to ==."""
        return self.real == value
