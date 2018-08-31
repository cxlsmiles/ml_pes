import numpy as np
from numpy import linalg as LA

def get_coulombmatrix(molecule, largest_mol_size=None):
    """
    This function generates a coulomb matrix for the given molecule
    if largest_mol size is provided matrix will have dimension lm x lm.
    Padding is provided for the bottom and right _|
    """
    #numberAtoms = len(molecule.atoms)
    numberAtoms = len(molecule['atoms'])

    if largest_mol_size == None or largest_mol_size == 0: largest_mol_size = numberAtoms

    cij = np.zeros((largest_mol_size, largest_mol_size))

    xyzmatrix = molecule['positions']
    chargearray = molecule['atomic_number']

    for i in range(numberAtoms):
        for j in range(numberAtoms):
            if i == j:
                cij[i][j] = 0.5 * chargearray[i] ** 2.4  # Diagonal term described by Potential energy of isolated atom
            else:
                dist = np.linalg.norm(np.array(xyzmatrix[i]) - np.array(xyzmatrix[j]))
                cij[i][j] = chargearray[i] * chargearray[j] / dist  # Pair-wise repulsion
    return cij

def diag_cmat (coul_matrix):
    eigval, eigvec = LA.eig(coul_matrix)
    return eigval, eigvec


if __name__ == "__main__":
    from read_input import read_single_geom

    molecule = read_single_geom()

    cmat = get_coulombmatrix(molecule)
    for i in range(len(cmat)):
        print(cmat[i][i])

    eigv, eigvec = diag_cmat(cmat)

    print(eigv)