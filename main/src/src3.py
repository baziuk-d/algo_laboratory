class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right


def post_order(root: BinaryTree) -> list:
    if root is None:
        return []

    result = []
    result += post_order(root.left)
    result += post_order(root.right)
    result.append(root.value)

    return result