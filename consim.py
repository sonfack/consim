from rdflib import Graph
from rdflib.namespace import RDFS

SEPERATOR = "/"

def getConcepts(ontoFile):
    """
    This function uses a taxonomy to create two lists with a one to one correspondance
    between child and parent
    """
    pko_onto = Graph()
    pko_onto.parse(ontoFile)
    children = []
    parent = []
    for sub, obj in pko_onto.subject_objects(predicate=RDFS.subClassOf):
        children.append(sub.rsplit(SEPERATOR)[-1])
        parent.append(obj.rsplit(SEPERATOR)[-1])
    return parent, children


def createChains(parent, children):
    """
    This function uses the two list on children and parents to create
    list of all lineages of the corresponding taxonomy
    """
    chains = []
    i = 0
    while i < len(children):
        chain = []
        chain.append(children[i])
        chain.append(parent[i])
        j = i
        while parent[j] in children:
            pos = children.index(parent[j])
            chain.append(parent[pos])
            j = pos
        # print(i+1, "---", chain)
        # print("###", chains)
        if chains:
            for element in chains:
                flag = 0
                if len(element) > len(chain):
                    # print(element, "++", chain)
                    for idx in range(len(element) - len(chain) + 1):
                        if element[idx: idx + len(chain)] == chain:
                            flag = 1
                            break
                elif len(element) < len(chain):
                    # print(element, "--", chain)
                    for idx in range(len(chain) - len(element) + 1):
                        if chain[idx: idx + len(element)] == element:
                            flag = 2
                            break
                if flag != 0:
                    break
            if flag == 2:
                pos = chains.index(element)
                chains[pos] = chain
            elif flag == 0:
                chains.append(chain)
        else:
            chains.append(chain)
        i += 1
    return chains


def consim(filettl, concept1, concept2):
    """
    This function select lineage for each concept, find their common ancestor
    and calculate their similarity
    """
    parent, children = getConcepts(filettl)
    # print("parent", parent)
    # print("\n\n")
    # print("children", children)
    # print("\n\n")
    chains = createChains(parent, children)
    # print("\n\n")
    # print("chains", chains)
    # print("\n\n")
    if concept1 and concept2:
        pos1 = -1
        pos2 = -1
        i = 0
        while i < len(chains):
            if any(concept1 in concept for concept in chains[i]):
                pos1 = i
                break
            i += 1
        if i < len(chains):
            print(concept1, "--", chains[pos1])
        c = chains[pos1]
        print("#", c)
        chain1 = c[c.index(concept1):]
        # print(concept1, "--", chain1)
        i = 0
        while i < len(chains):
            if any(concept2 in concept for concept in chains[i]):
                pos2 = i
                break
            i += 1
        if i < len(chains):
            print(concept2, "--", chains[pos2])
        c = chains[pos2]
        chain2 = c[c.index(concept2):]
        # print(concept2, "--", chain2)
        intersect = list(set(chain1).intersection(set(chain2)))
        # print("intersect", intersect)
        nr2 = len(intersect)*2
        n = len(chain1)-len(intersect)+len(chain2)-len(intersect)+len(intersect)*2
        print("concept similarity between:", concept1, "--", concept2, "= ", nr2/n)
        return nr2/n

if __name__ == "__main__":
    consim("taxonomy.ttl", "Activity", "Activity")
