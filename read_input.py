from types import SimpleNamespace

def read_input_file ():
    # read geometries
    # the file should contain the xyz coordinates for each geometry
    # two geometries are separated by a blank line
    ifile = open("geometries.txt")
    data = ifile.read()
    ifile.close()
    geometries = data.split("\n\n")

    ifile = open("energies.txt")
    energies = ifile.readlines()
    ifile.close()

    energies = [float(energies[i]) for i in range(len(energies))]

    return geometries, energies


def read_single_geom (geomData):
    geomData = geomData.split("\n") # split the string by newlines

    geomData = [(geomData[i].strip(" ")).split(" ") for i in range(len(geomData))] # split each line by empty space

    geomData = [list(filter(None, geomData[i])) for i in range(len(geomData))] # remove empty strings from the list

    atoms = [geomData[i][0] for i in range(len(geomData))] # get the list of atoms

    atomic_number = [float(geomData[i][1]) for i in range(len(geomData))] # get the atomic numbers

    positions = [geomData[i][2:] for i in range(len(geomData))] # get the positions
    for i in range(len(positions)):
        positions[i] = [float(positions[i][k].strip('\n')) for k in range(3)]

    # return a dictionary containing the atoms, atomic numbers and atomic positions
    return {"atoms": atoms, "atomic_number": atomic_number, "positions": positions}


if __name__ == "__main__":
    geom, en = read_input_file()

    for i in range(len(geom)):
        dict_at = read_single_geom(geom[i])
        print(dict_at["positions"])
        print(dict_at["atomic_number"])