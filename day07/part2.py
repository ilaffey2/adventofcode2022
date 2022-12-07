from treelib import Node, Tree
file = open('input.txt', 'r')
lines = file.readlines()

tree = Tree()
tree.create_node("/", "/")
pwd = "/"
ls_mode = False
for line in lines[1:]:
    line = line.strip()
    argv = line.split(" ")
    if argv[0] == "$":
        ls_mode = False
        if argv[1] == "cd":
            if argv[2] == "..":
                pwd = pwd.split("/")[:-2]
                print(pwd)
                pwd = "/".join(pwd) + "/"
                print(pwd)

            else:
                pwd = pwd + argv[2] + "/"
        if argv[1] == 'ls':
            ls_mode = True
    else:
        if argv[0] == "dir":
                print(argv)
                tree.create_node(argv[1], pwd + argv[1] + "/", parent=pwd)
        else:
                tree.create_node(argv[1], pwd + argv[1] + "/", parent=pwd, data=argv[0])
            
result_list = []
def calc_size(node):
    size = 0
    children = tree.children(node)
    if len(children) > 0:
        for child in children:
            size += calc_size(child.identifier)
    else:
        if tree.get_node(node).data != None:
            size = int(tree.get_node(node).data)
        else:
            size = 0
    if (47870454 - size < (70000000 - 30000000 )) and len(children) > 0:
        result_list.append(size)
    return size 

print(tree.show())
print(calc_size(('/')))
result_list.sort()
print((result_list))
