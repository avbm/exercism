from json import dumps


class Tree(object):
    def __init__(self, label, children=None):
        self.label = label
        if children is None:
            self.children = list()
        else:
            self.children = children

    def __dict__(self):
        return {self.label: [c.__dict__() for c in sorted(self.children)]}

    def __str__(self, indent=None):
        return dumps(self.__dict__(), indent=indent)

    def __lt__(self, other):
        return self.label < other.label

    def __eq__(self, other):
        return self.__dict__() == other.__dict__()

    def from_pov(self, from_node):
        if self.label == from_node:
            return self

        path_to_node = []
        if not self.path_from_root(to_node=from_node, current_path=path_to_node):
            raise ValueError('from_node: {} not found in tree: {}'.format(from_node, self))
        index = 1
        node = self
        while index < len(path_to_node):
            child = node.get_child_with_label(path_to_node[index])
            node = node.rotate(child)
            index += 1
        return node

    def path_to(self, from_node, to_node):
        temp = self.from_pov(from_node)
        current_path = []
        if not temp.path_from_root(to_node, current_path):
            raise ValueError('to_node: {} not found in tree: {}'.format(to_node, self))
        return current_path

    def get_child_with_label(self, label):
        for child in self.children:
            if child.label == label:
                return child

    def rotate(self, child):
        if child not in self.children:
            raise ValueError("Cant rotate if child: {} not in children for node:{}".format(child.label, self))
        self.children.remove(child)
        parent = self
        child.children.append(parent)
        return child

    def path_from_root(self, to_node, current_path=[]):
        '''Depth first traversal to get path from root node to target node'''
        if self.label == to_node:
            current_path.append(self.label)
            return True
        if len(self.children) == 0:
            return False
        current_path.append(self.label)
        for child in self.children:
            if child.path_from_root(to_node, current_path):
                return True
        current_path.pop(-1)
        return False
