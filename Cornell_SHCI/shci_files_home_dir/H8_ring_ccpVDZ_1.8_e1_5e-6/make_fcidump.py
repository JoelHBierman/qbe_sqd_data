from functools import reduce
import numpy
from pyscf import gto, scf, ao2mo
from pyscf import symm
from pyscf.tools import fcidump

import numpy as np

n_atoms = 8
radius = 1.8
angles_list = [2*np.pi * (n/n_atoms) for n in range(n_atoms)]
atom = "".join([f'H 0 {radius*np.cos(angles_list[n])} {radius*np.sin(angles_list[n])};' for n in range(n_atoms)])[:-1]
mol = gto.M(
    atom=atom,
    basis="cc-pVDZ",
    charge=0,
)


mf = scf.RHF(mol)
mf.conv_tol = 1e-12
mf.kernel()

c = mf.mo_coeff
h1e = reduce(numpy.dot, (c.T, mf.get_hcore(), c))
eri = ao2mo.kernel(mol, c)

fcidump.from_integrals('FCIDUMP', h1e, eri, c.shape[1],
                             mol.nelectron)
