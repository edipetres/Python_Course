import numpy as np

global_pr = np.ones(graph.number_of_nodes())

def page_rank(node):
    n = graph.number_of_nodes()
    damping = 0.85

    return pr_node