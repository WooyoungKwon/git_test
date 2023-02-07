class TreeNode:
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None


def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else:
        return 1

# def factorial(n):
#     result = 1
#     for item in range(1, n + 1, 1):
#         result *= item  # result = result * item
#     return result


print(factorial(5))

node1 = TreeNode()
node1.data = '화사'

node2 = TreeNode()
node2.data = '솔라'
node1.left = node2