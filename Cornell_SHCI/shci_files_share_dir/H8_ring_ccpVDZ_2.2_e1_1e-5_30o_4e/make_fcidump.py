from functools import reduce
import numpy
from pyscf import gto, scf, fci, mcscf, ao2mo, cc, symm
from pyscf.tools import fcidump

import numpy as np

n_atoms = 8
radius = 2.2
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

n_frozen = 0
num_virtual = 10
active_space = range(n_frozen, mol.nao_nr() - num_virtual)

# Get molecular integrals
scf = scf.RHF(mol).run()
num_orbitals = len(active_space)
n_electrons = int(sum(scf.mo_occ[active_space]))
num_elec_a = (n_electrons + mol.spin) // 2
num_elec_b = (n_electrons - mol.spin) // 2
cas = mcscf.CASCI(scf, num_orbitals, (num_elec_a, num_elec_b))
mo = cas.sort_mo(active_space, base=0)
hcore, nuclear_repulsion_energy = cas.get_h1cas(mo)
eri = ao2mo.restore(1, cas.get_h2cas(mo), num_orbitals)

fcidump.from_integrals('FCIDUMP', hcore, eri, num_orbitals,
                             mol.nelectron)
