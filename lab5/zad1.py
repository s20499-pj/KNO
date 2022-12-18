# a
print("#a")
from treelib import Tree, Node

# tworzenie drzewa
tree = Tree()
tree.create_node("Harry", "h")  # korzen
tree.create_node("Jane", "j", parent="h")
tree.create_node("Bill", "b", parent="h")
tree.create_node("Diane", "d", parent="j")
tree.create_node("Mary", "m", parent="d")
tree.create_node("Harry", "h2", parent="j")

# wyswietlenie drzewa
tree.show()

# wyswietlenie info o niektorych wierzcholkach
x = tree.get_node("m")
print(x.tag)
print(x.identifier)
y = tree.parent("m")
print(y.tag)
print(y.identifier)
z = tree.get_node("h")
print(z.tag)
print(z.is_root())


# b
def dupilcate_node_path_check(tree, node):  # FIFO
    queue = [tree.get_node(tree.root)]
    while queue:
        current_node = queue.pop(0)
        if current_node.tag == node.tag and current_node.identifier != node.identifier:
            return True
        queue.extend(tree.children(current_node.identifier))
    return False


print("#b")
x = tree.get_node("h2")
print(dupilcate_node_path_check(tree, x))
x = tree.get_node("m")
print(dupilcate_node_path_check(tree, x))
