from types import SimpleNamespace

def read_single_geom ():
    ifile = open("acac.dat")
    lns = ifile.readlines()
    ifile.close()

    atoms = [lns[i].split(' ')[0] for i in range(len(lns))]
    atomic_number = [float(lns[i].split(' ')[1]) for i in range(len(lns))]
    positions = [lns[i].split(' ')[2:] for i in range(len(lns))]
    for i in range(len(positions)):
        positions[i] = [float(positions[i][k].strip('\n')) for k in range(3)]

    return {"atoms": atoms, "atomic_number": atomic_number, "positions": positions}

#d = {'key1': 'value1', 'key2': 'value2'}
#n = SimpleNamespace(**d)
#n.key2

if __name__ == "__main__":
    dict_at = read_single_geom()
    print(dict_at["positions"])
    print(dict_at["atomic_number"])