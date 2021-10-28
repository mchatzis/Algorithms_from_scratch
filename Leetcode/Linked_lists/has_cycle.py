from typing import Type, Optional


class ListNode:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next
    
    def __repr__(self) -> str:
        return repr(self.data)

class LList:
    def __init__(self, head = None) -> None:
        assert isinstance(head, ListNode), "LList head must be a ListNode"
        self.head = head
    
    def has_cycle(self):
        current = self.head
        traversed = []
        while current is not None:
            for node in traversed:
                if current is node:
                    return False
            traversed.append(current)
            current = current.next
        return True

    def _to_str(self) -> str:
        current = self.head
        s = ""
        while current is not None:
            s += repr(current) + " --> "
            current = current.next
        # Remove last arrow
        return s[:-4]

    def __repr__(self) -> str:
        return self._to_str()