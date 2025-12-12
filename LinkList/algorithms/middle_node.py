class ListNode:
    """ListNode for represents a single node in the singly linked list"""

    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def __init__(self):
        self.head = None

    def appendNode(self, data):
        new_node = ListNode(data)

        if self.head is None:
            self.head = new_node
            return

        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = new_node

    def middleNode(self):
        curr = self.head
        len = 0

        while curr is not None:
            curr = curr.next
            len += 1

        curr = self.head
        for i in range(len // 2):
            curr = curr.next
        return curr

    def middleNodeOptimized(self):
        fast = self.head
        slow = self.head

        while fast!=None and fast.next!=None:
            slow = slow.next
            fast = fast.next.next

        return slow


if __name__ == "__main__":
    sol = Solution()

    sol.appendNode(1)
    sol.appendNode(2)
    sol.appendNode(3)
    sol.appendNode(4)
    print("\n")
    mid = sol.middleNode()
    print("Normal solution: ", mid.data)

    mid_optm = sol.middleNodeOptimized()
    print("Through Optimized solution: ", mid.data)
