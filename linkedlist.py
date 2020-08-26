"""
This module is for implementation of linked list
"""
from typing import List, Optional


class _Node:
    """
    This is a private class that is used in linked list
    """

    def __init__(self, item: 'object') -> None:
        """initialize the attribute of this node"""
        self.item = item
        self.next = None


class LinkedList:
    """This class is for the singly linked list that uses regular loops for implementation of its methods"""

    def __init__(self, items: List[Optional['object']]) -> None:
        """initialize the content of this list by converting <items> into linked list"""
        if not items:
            self._first = None
        else:
            self._first = _Node(items[0])
            current_node = self._first
            for item in items[1:]:
                current_node.next = _Node(item)
                current_node = current_node.next

    def __str__(self) -> str:
        """
        Return the string representation of this linked list

        >>> lnk = LinkedList(["mango", 23, "^^", "file_path", "fruits"])
        >>> str(lnk)
        'mango -> 23 -> ^^ -> file_path -> fruits'
        """
        current_node, container = self._first, []
        while current_node:
            container.append(str(current_node.item))
            current_node = current_node.next
        return " -> ".join(container)

    def __len__(self) -> int:
        """
        Return the length of this linked list

        >>> link = LinkedList(["mango", 23, "^^", "file_path", "fruits"])
        >>> len(link)
        5
        """
        current_node, counter = self._first, 0
        while current_node:
            counter += 1
            current_node = current_node.next
        return counter

    def __getitem__(self, index: int) -> Optional['object']:
        """"
        Return the item at position <index> in this linked list. Index is invalid
        raise IndexError

         >>> link = LinkedList(["mango", 23, "^^", "file_path", "fruits"])
        >>> link[1]
        23
        >>> link[-2]
        'file_path'
        >>> link[7]
        Traceback (most recent call last):
        IndexError
        """
        if (index < 0 and abs(index) > len(self)) or (index >= len(self)):
            raise IndexError
        else:
            index1 = index
            if index < 0:
                index1 = len(self) + index
            current_index, current_node = 0, self._first
            while current_index < index1:
                current_node = current_node.next
                current_index += 1
            return current_node.item

    def __contains__(self, item) -> 'bool':
        """
        Return True if and only if <item> in this linked list. Otherwise, return False

        >>> link = LinkedList(["mango", 23, "^^", "file_path", "fruits"])
        >>> 23 in link
        True
        >>> 'blue' in link
        False
        """
        current_node = self._first
        while current_node:
            if current_node.item == item:
                return True
            current_node = current_node.next
        return False

    def __setitem__(self, index, value) -> None:
        """
        Replace the item at position <index> with <value>. Raise IndexError if <index> is invalid

        >>> link = LinkedList(["mango", 23, "^^", "file_path", "fruits"])
        >>> link[3] = "paths"
        >>> str(link)
        'mango -> 23 -> ^^ -> paths -> fruits'
        >>> link[-1] = "banana"
        >>> str(link)
        'mango -> 23 -> ^^ -> paths -> banana'
        """
        if (index < 0 and abs(index) > len(self)) or (index >= len(self)):
            raise IndexError
        else:
            index1 = index
            if index < 0:
                index1 = len(self) + index
            current_index, current_node = 0, self._first
            while current_index < index1:
                current_node = current_node.next
                current_index += 1
            current_node.item = value

    def append(self, item) -> None:
        """
        Append <item> to this linked list

        >>> link = LinkedList(["mango", 23, "^^", "file_path", "fruits"])
        >>> link.append("colors")
        >>> str(link)
        'mango -> 23 -> ^^ -> file_path -> fruits -> colors'
        """
        if not self._first:
            self._first = _Node(item)
        else:
            current_node = self._first
            while current_node.next:
                current_node = current_node.next
            current_node.next = _Node(item)

    def count(self, item) -> int:
        """
        Return the number of times <item> occurs in this linked list

        >>> link = LinkedList(["mango", 23, "^^", "file_path", "fruits", 23, "blue", "mango", 23, "mango"])
        >>> link.count(23)
        3
        >>> link.count("banana")
        0
        >>> link.count("mango")
        3
        """
        current_node, count = self._first, 0
        while current_node:
            if current_node.item == item:
                count += 1
            current_node = current_node.next
        return count

    def pop(self) -> Optional['object']:
        """
        Remove and return the last item of this linked list. Raise IndexError if this linked list is empty

        >>> link = LinkedList(["mango", 23, "^^", "file_path", "fruits"])
        >>> link.pop()
        'fruits'
        >>> str(link)
        'mango -> 23 -> ^^ -> file_path'
        >>> link = LinkedList([])
        >>> link.pop()
        Traceback (most recent call last):
        IndexError
        """
        if not self._first:
            raise IndexError
        else:
            hold = self._first.item
            if len(self) == 1:
                self._first = None
            else:
                prev_node, current_node, next_node = self._first, self._first, self._first.next
                while next_node:
                    prev_node = current_node
                    current_node, next_node = next_node, next_node.next
                hold = current_node.item
                prev_node.next = None
            return hold

    def extend(self, link_list: 'LinkedList') -> None:
        """
        Extend <link_list> to this linked list

        >>> other = LinkedList(['maths', 'gcd', 'fibonacci', 'pascal coefficient'])
        >>> link = LinkedList(["mango", 23, "^^", "file_path", "fruits"])
        >>> link.extend(other)
        >>> str(link)
        'mango -> 23 -> ^^ -> file_path -> fruits -> maths -> gcd -> fibonacci -> pascal coefficient'
        """
        if not self._first:
            self._first = link_list._first
        else:
            current_node = self._first
            while current_node.next:
                current_node = current_node.next
            current_node.next = link_list._first

    def remove(self, item: 'object') -> None:
        """
        Remove the first occurance of <item> from this linked list. Raise ValueError if <item> is not
        in this linked list
        >>> link = LinkedList(["mango", 23, "^^", "file_path", "fruits"])
        >>> link.remove(23)
        >>> str(link)
        'mango -> ^^ -> file_path -> fruits'
        >>> link.remove('brown')
        Traceback (most recent call last):
        ValueError
        >>> link.remove('fruits')
        >>> str(link)
        'mango -> ^^ -> file_path'
        """
        if item not in self:
            raise ValueError
        elif self._first.item == item:
            self._first = self._first.next
        else:
            prev_node, current_node = self._first, self._first,
            while current_node.item != item:
                prev_node, current_node = current_node, current_node.next
            prev_node.next = current_node.next

    def clear(self) -> None:
        """clear this linked list by removing every thing"""
        self._first = None


if __name__ == "__main__":
    import doctest
    doctest.testmod()
