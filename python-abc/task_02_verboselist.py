#!/usr/bin/python3

from abc import ABC


class VerboseList(list):
    """A subclass of the built-in 'list'.
    Adds verbose output for list operations."""

    def append(self, item):
        """Appends an item to the end of the list
        and print a message.

        Args:
            item: The item to append to the list.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iter):
        """Extends the list by appending from the iterable
        and prints a message.

        Args:
            iter: An iterable whose elements will be added to the list.
        """
        super().extend(iter)
        print(f"Extended the list with [{len(iter)}] items.")

    def remove(self, item):
        """Removes the first occurrence of a value
        and prints a message.

        Args:
            item: The item to remove from the list.

        Raises:
            ValueError: If the item is not in the list.
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, item=-1):
        """Removes and return item at index (default last).
        Prints a message if index is valid.

        Args:
            item (int, optional): The index of the item to remove.
                Defaults to -1.

        Returns:
            The item that was removed.

        Raises:
            IndexError: If the list is empty or index is out of range.
        """
        if abs(item) in range(0, len(self)):
            print(f"Popped [{self[item]}] from the list.")
        super().pop(item)
