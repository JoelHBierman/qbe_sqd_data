# Illustrates a simple molecular BE calculation with BE
# density matching between edge & centers of fragments.

from pyscf import fci, gto, scf

from QBE_SQD.molbe import BE, fragmentate
import numpy as np

from QBE_SQD.molbe.chemfrag import ChemGenArgs
from QBE_SQD.shared.config import settings

# PySCF HF generated mol & mf (molecular desciption & HF object)
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

# Perform PySCF FCI to get reference energy
#mc = fci.FCI(mf)
#fci_ecorr = mc.kernel()[0] - mf.e_tot
#`print(f"*** FCI Correlation Energy: {fci_ecorr:>14.8f} Ha", flush=True)

# Perform BE calculations with different fragment schemes:
# Using chemgen, treat_H_different is False to treat the hydrogen chain correctly
add_args = ChemGenArgs(treat_H_different=False)
fobj = fragmentate(n_BE=2, mol=mol, frag_type="autogen", frozen_core=False)
mybe = BE(mf, fobj)
mybe.optimize(solver="FCI",
              use_cumulant=True,
              max_iter=10,
              conv_tol=10**-5,
              max_line_search=3
)

# Compute BE error
be_ecorr = mybe.ebe_tot - mybe.ebe_hf
#err_ = (fci_ecorr - be_ecorr) * 100.0 / fci_ecorr
print(f"*** BE2 Correlation Energy Error (%) : {err_:>8.4f} %")

# Define BE3 fragments
#fobj = fragmentate(n_BE=3, mol=mol)
#mybe = BE(mf, fobj)
#mybe.optimize(solver="FCI")

# Compute BE error
#be_ecorr = mybe.ebe_tot - mybe.ebe_hf
#err_ = (fci_ecorr - be_ecorr) * 100.0 / fci_ecorr
#print(f"*** BE3 Correlation Energy Error (%) : {err_:>8.4f} %")
