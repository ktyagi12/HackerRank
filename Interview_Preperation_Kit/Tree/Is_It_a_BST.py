#Problem available at: https://www.hackerrank.com/challenges/ctci-is-binary-search-tree/problem?filter=India&filter_on=country&h_l=interview&h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_v%5B%5D=zen&h_v%5B%5D=zen&page=1&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=trees&isFullScreen=true

bst_dict = {}
def checkBST(root):

    def is_bst(node, min, max):
        if node.data <= min:
            return False

        if node.data >= max:
            return False

        left_ok = True
        right_ok = True

        if node.left is not None:
            left_ok = is_bst(node.left, min, node.data)
        if node.right is not None:
            right_ok = is_bst(node.right, node.data, max)

        return left_ok and right_ok

    if root is None:
        return True

    return is_bst(root, float('-inf'), float('inf'))
