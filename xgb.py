# implement xgb from scratch

class Node:

    def __init__(self):
        self.leaf_flag: bool = False
        self.left_child_node: Node = None
        self.right_child_node: Node = None
        self.split_threshold: float = None
        self.split_feature_idx: int = None
        self.prediction: float = None