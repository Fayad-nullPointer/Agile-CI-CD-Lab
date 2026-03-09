class String_Sum_of_Digits:
    """Utilities for summing digits embedded in text."""

    @staticmethod
    def String_Sum_of_Digits(s: str) -> int:
        """Return the sum of all digit characters found in ``s``.

        Raises:
            TypeError: If ``s`` is not a string.
        """
        if not isinstance(s, str):
            raise TypeError("Input must be a string")

        total = 0
        for char in s:
            if char.isdigit():
                total += int(char)
        return total
