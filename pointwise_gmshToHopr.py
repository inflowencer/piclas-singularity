#!/usr/bin/python3
import sys

def Pointwise_Gmsh_To_Hopr(fname):
    with open(fname, "r") as f:
        mesh = f.readlines()

    # mesh = mesh[5:]
    del_indices = []

    # Comments
    for i, j in enumerate(mesh):
        if "Comment" in j and not "End" in j:
            comment_start = i
        if "EndComment" in j:
            comment_end = i
            tmp_list = list(range(comment_start, comment_end + 1))
            del_indices.extend(tmp_list)

    # Delete Comments
    for index in sorted(del_indices, reverse=True):
        del mesh[index]

    # Physical names
    for i, j in enumerate(mesh):
        if "Physical" in j and not "End" in j:
            names_start = i
        if "EndPhysical" in j:
            names_end = i
            tmp_list = list(range(names_start, names_end + 1))
            names = mesh[names_start:names_end + 1]
            del mesh[names_start:names_end + 1]

    for i, j in enumerate(mesh):
        if "EndMeshFormat" in j:
            for name in names:
                mesh.insert(i + 1, name)
                i += 1
            

    fname = f"{fname[:-4]}_clean.msh"
    with open(fname, "w") as f:
        f.writelines(mesh)


if __name__ == "__main__":
    fname = sys.argv[1]
    Pointwise_Gmsh_To_Hopr(fname)