import numpy as np
import matplotlib.pyplot as plt

fontsize = 14

batch_list = [0,1,2,3,4,5,6,7,8,9]
batch_size_list = [500, 1000, 2000, 3000, 4000, 5000]

qbe_sqd_energy = -4.330382461513233
qbe_sqd_dimension = 2965284 # max value
dmrg_energy = -4.1743049472965215
nuclear_repulsion_energy = 5.397349401824396

qbe_sqd_energy_error = (qbe_sqd_energy - dmrg_energy) * 10**3

sqd_energies = [[-9.547541222266057, -9.559063821139127, -9.563471159112478, -9.564921702082646, -9.565301869629852, -9.56565355378523],
                    [-9.544155735296792, -9.555594976453516, -9.56264994565824, -9.564378859335662, -9.56501350818502, -9.565442956631763],
                    [-9.540916769581134, -9.55683700513421, -9.562848512214298, -9.56387510022844, -9.565141811041837, -9.565337310824365],
                    [-9.542352426344921, -9.556455046928553, -9.562773296382408, -9.564389499908922, -9.56509294966397, -9.565454704262514]]
sqd_dimensions = [[1371241, 3459600, 7590025, 11847364, 15547249, 19873764],
                      [1153476, 2992900, 6770404, 11082241, 15000129, 19351201],
                      [1283689, 3052009, 6859161, 10791225, 14969161, 19070689],
                      [1181569, 2866249, 6906384, 10725625, 15288100,18974736]]

sqd_energies = np.asarray(sqd_energies).flatten() + nuclear_repulsion_energy
sqd_energy_errors = (sqd_energies - dmrg_energy) * 10**3
sqd_dimensions = np.asarray(sqd_dimensions).flatten()
print(sqd_energies)

hci_dum_dets_30o_8_e_1e_4 = [231707]
hci_energies_30o_8e_1e_4 = [-4.126733909063901]
hci_energy_errors_30o_8e_1e_4 = [(hci_energy - dmrg_energy) * 10**3 for hci_energy in hci_energies_30o_8e_1e_4]

hci_dum_dets_30o_8_e_1e_5 = [1695868]
hci_energies_30o_8e_1e_5 = [-4.1281265733967984]
hci_energy_errors_30o_8e_1e_5 = [(hci_energy - dmrg_energy) * 10**3 for hci_energy in hci_energies_30o_8e_1e_5]

hci_dum_dets_30o_8_e_1e_6 = [8862493]
hci_energies_30o_8e_1e_6 = [-4.139549942858453]
hci_energy_errors_30o_8e_1e_6 = [(hci_energy - dmrg_energy) * 10**3 for hci_energy in hci_energies_30o_8e_1e_6]

hci_dum_dets_40o_8_e_1e_4 = [405184]
hci_energies_40o_8e_1e_4 = [-4.131462012566635]
hci_energy_errors_40o_8e_1e_4 = [(hci_energy - dmrg_energy) * 10**3 for hci_energy in hci_energies_40o_8e_1e_4]

hci_dum_dets_40o_8_e_1e_5 = [6111043]
hci_energies_40o_8e_1e_5 = [-4.174260556148964]
hci_energy_errors_40o_8e_1e_5 = [(hci_energy - dmrg_energy) * 10**3 for hci_energy in hci_energies_40o_8e_1e_5]

shci_var_dum_det_30o_8e_eps_5e_6 = [3383098]
shci_var_energy_error_30o_8e_eps_5e_6 = [(-9.5662899523 + nuclear_repulsion_energy - dmrg_energy) * 10**3]

shci_var_dum_det_30o_8e_eps_1e_5 = [2263228]
shci_var_energy_error_30o_8e_eps_1e_5 = [(-9.56624272 + nuclear_repulsion_energy - dmrg_energy) * 10**3]

dmrg_e1 = -4.1334632595
#shci_var_dum_det_40o_4e_eps_1e_5 = []
#shci_var_energy_error_40o_4e_eps_1e_5 = [( + nuclear_repulsion_energy - dmrg_energy) * 10**3]

alpha = 0.5
plt.rcParams.update({'font.size': 32, 'lines.markersize': 18})
plt.rcParams.update({'xtick.labelsize': 32, 'ytick.labelsize': 32, 'xtick.major.size': 8,      # Length of major x ticks
    'xtick.major.width': 2,     # Width of major x ticks
    'xtick.minor.size': 4,      # Length of minor x ticks
    'xtick.minor.width': 1,     # Width of minor x ticks
    'ytick.major.size': 8,      # Length of major y ticks
    'ytick.major.width': 2,     # Width of major y ticks
    'ytick.minor.size': 4,      # Length of minor y ticks
    'ytick.minor.width': 1  })
plt.figure(figsize=(12, 7))  # width=10, height=7 inches
plt.xscale('log')
plt.scatter(sqd_dimensions, sqd_energy_errors, c='c', label='SQD (8e,30o)', marker='o', alpha=alpha)
plt.scatter(qbe_sqd_dimension, qbe_sqd_energy_error, c='r', label='QBE-SQD', marker='o', alpha=alpha)
plt.scatter(hci_dum_dets_40o_8_e_1e_4, hci_energy_errors_40o_8e_1e_4, c='crimson', label='HCI (8e, 40o) $ε_1=10^{-4}$', marker='s', alpha=alpha)
plt.scatter(hci_dum_dets_40o_8_e_1e_5, hci_energy_errors_40o_8e_1e_5, c='grey', label='HCI (8e, 40o) $ε_1=10^{-5}$', marker='s', alpha=alpha)
plt.scatter(hci_dum_dets_30o_8_e_1e_4, hci_energy_errors_30o_8e_1e_4, c='blue', label='HCI (8e, 30o) $ε_1=10^{-4}$', marker='s', alpha=alpha)
plt.scatter(hci_dum_dets_30o_8_e_1e_5, hci_energy_errors_30o_8e_1e_5, c='green', label='HCI (8e, 30o) $ε_1=10^{-5}$', marker='s', alpha=alpha)
plt.scatter(hci_dum_dets_30o_8_e_1e_6, hci_energy_errors_30o_8e_1e_6, c='brown', label='HCI (8e, 30o) $ε_1=10^{-6}$', marker='s', alpha=alpha)
plt.scatter(shci_var_dum_det_30o_8e_eps_5e_6, shci_var_energy_error_30o_8e_eps_5e_6, c='navy', label='SHCI (8e,30o) $ε_1=5\\times 10^{-6}$', marker='^', alpha=alpha)
plt.scatter(shci_var_dum_det_30o_8e_eps_1e_5, shci_var_energy_error_30o_8e_eps_1e_5, c='purple', label='SHCI (8e,30o) $ε_1=10^{-5}$', marker='^', alpha=alpha)
#plt.scatter(shci_var_dum_det_40o_4e_eps_1e_5, shci_var_energy_error_40o_4e_eps_1e_5, c='brown', label='SHCI (40o,4e) $ε_1=1\\times 10^{-5}$', marker='x', alpha=alpha)
plt.axhline(y=0, color='k', linestyle='-')
plt.axhline(y=(dmrg_e1 - dmrg_energy) * 10**3, color='gray', linestyle='--', label='$E_1$ DMRG, bond dim. 400')
plt.xlabel('Number of Slater determinants')
plt.ylabel('E - E$_{\mathrm{DMRG}}$ [mHa]')
#plt.title('QBE-SQD vs SQD Energy Error Convergence', fontsize=fontsize)
plt.legend(fontsize=20)
plt.grid(which='both', axis='y')
plt.tight_layout()
plt.savefig('/home/joel/Desktop/numerical_results/QBE_SQD/paper_figures/H8_ring_ccpVDZ_compare_SQD_QBE_SQD_2point2.pdf', dpi=300, bbox_inches='tight')
#plt.xscale('log')
plt.show()

#dmrg_e1 = -4.1334632595

#alpha = 0.5
#plt.figure(figsize=(20, 7))  # width=10, height=7 inches
#plt.rcParams.update({'font.size': 18, 'lines.markersize': 10})
#plt.xscale('log')
#plt.scatter(sqd_dimensions, sqd_energy_errors, c='c', label='SQD (4e, 30o)', marker='o', alpha=alpha)
#plt.scatter(qbe_sqd_dimension, qbe_sqd_energy_error, c='r', label='QBE-SQD', marker='o', alpha=alpha)
#plt.scatter(hci_dum_dets_40o_4_e_1e_4, hci_energy_errors_40o_4e_1e_4, c='darkorange', label='HCI (4e, 40o) $ε_1=10^{-4}$', marker='x', alpha=0.8)
#plt.scatter(hci_dum_dets_40o_4_e_1e_5, hci_energy_errors_40o_4e_1e_5, c='tomato', label='HCI (4e, 40o) $ε_1=10^{-5}$', marker='x', alpha=0.8)
#plt.scatter(hci_dum_dets_30o_4_e_1e_4, hci_energy_errors_30o_4e_1e_4, c='blue', label='HCI (4e, 30o) $ε_1=10^{-4}$', marker='x', alpha=0.8)
#plt.scatter(hci_dum_dets_30o_4_e_1e_5, hci_energy_errors_30o_4e_1e_5, c='green', label='HCI (4e, 30o) $ε_1=10^{-5}$', marker='x', alpha=0.8)
#plt.scatter(hci_dum_dets_30o_4_e_1e_6, hci_energy_errors_30o_4e_1e_6, c='brown', label='HCI (4e, 30o) $ε_1=10^{-6}$', marker='x', alpha=0.8)
#plt.scatter(shci_var_dum_det_30o_4e_eps_5e_6, shci_var_energy_error_30o_4e_eps_5e_6, c='navy', label='SHCI (4e, 30o) $ε_1=5\\times 10^{-6}$', marker='^', alpha=alpha)
#plt.scatter(shci_var_dum_det_30o_4e_eps_1e_5, shci_var_energy_error_30o_4e_eps_1e_5, c='purple', label='SHCI (4e, 30o) $ε_1=10^{-5}$', marker='^', alpha=alpha)
#plt.scatter(shci_var_dum_det_40o_4e_eps_1e_5, shci_var_energy_error_40o_4e_eps_1e_5, c='brown', label='SHCI (40o,4e) $ε_1=1\\times 10^{-5}$', marker='x', alpha=alpha)
#plt.axhline(y=0, color='k', linestyle='-')
#plt.axhline(y=(dmrg_e1 - dmrg_energy) * 10**3, color='gray', linestyle='--', label='$E_1$ DMRG, bond dim. 400')
#plt.xlabel('Number of Slater determinants')
#plt.ylabel('E - E$_{\mathrm{DMRG}}$ [mHa]')
#plt.title('QBE-SQD vs SQD Energy Error Convergence', fontsize=fontsize)
#plt.legend()
#plt.grid(which='both', axis='y')
#plt.tight_layout()
#plt.savefig('/home/joel/Desktop/numerical_results/QBE_SQD/paper_figures/H8_ring_ccpVDZ_compare_SQD_QBE_SQD_2point2_elongated.pdf', dpi=300, bbox_inches='tight')
#plt.xscale('log')
#plt.show()

