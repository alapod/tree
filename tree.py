from itertools import groupby


class TreeStore:
    def __init__(self, nodes):
        self.nodes = {x["id"]: x for x in nodes}
        self.children_data = self.get_children_data()

    def get_children_data(self):
        parent_data = {}
        for key, group in groupby(self.nodes.values(), lambda x: x["parent"]):
            parent_data[key] = list(group)
        return parent_data

    def get_all(self):
        return list(self.nodes.values())

    def get_item(self, node_id):
        return self.nodes[node_id]

    def get_children(self, node_id):
        try:
            return self.children_data[node_id]
        except KeyError:
            return []

    def get_all_parents(self, node_id):
        parent = self.get_item(node_id)["parent"]
        parents = []
        while parent != "root":
            parents.append(self.get_item(parent))
            parent = self.get_item(parent)["parent"]
        return parents
