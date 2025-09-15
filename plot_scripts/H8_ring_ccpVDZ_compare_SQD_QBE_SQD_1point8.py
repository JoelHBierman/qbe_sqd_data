import numpy as np
import matplotlib.pyplot as plt

fontsize = 16

batch_size_list = [500, 1000, 2000, 3000, 4000, 5000]

qbe_sqd_energy = -4.267035427832645
qbe_sqd_dimension = 3341584 # max value
dmrg_energy = -4.302523105341811
nuclear_repulsion_energy = 6.596760380007595
qbe_sqd_energy_error = (qbe_sqd_energy - dmrg_energy) * 10**3

sqd_energies = [[-10.871446260042607, -10.881949112687806, -10.88647274051866, -10.88827320873833, -10.888942605172225, -10.889298787926233],
                [-10.871568868211941, -10.880074012246858, -10.886400266382232, -10.888213556613827, -10.88872740208054, -10.88920620473598],
                [-10.87310579124953, -10.880515678465462, -10.886857643676478, -10.888222668359585, -10.888905193040873, -10.889165762930109]]
sqd_dimensions = [[1338649, 3655744, 8614225, 13801225, 18567481, 23902321],
                  [1249924, 3370896, 8323225, 13571856, 18241441, 23319241],
                  [1240996, 3568321, 8708401, 13542400, 18601969, 23068809]]

sqd_energies = np.asarray(sqd_energies).flatten() + nuclear_repulsion_energy
sqd_energy_errors = (sqd_energies - dmrg_energy) * 10**3
sqd_dimensions = np.asarray(sqd_dimensions).flatten()
print(sqd_energies)

hci_dum_dets_30o_8_e_1e_4 = [225356]
hci_energies_30o_8e_1e_4 = [-4.247949410003903]
hci_energy_errors_30o_8e_1e_4 = [(hci_energy - dmrg_energy) * 10**3 for hci_energy in hci_energies_30o_8e_1e_4]

hci_dum_dets_30o_8_e_1e_5 = [1761714]
hci_energies_30o_8e_1e_5 = [-4.2509494094366715]
hci_energy_errors_30o_8e_1e_5 = [(hci_energy - dmrg_energy) * 10**3 for hci_energy in hci_energies_30o_8e_1e_5]

hci_dum_dets_40o_8_e_1e_4 = [333423]
hci_energies_40o_8e_1e_4 = [-4.256949398691914]
hci_energy_errors_40o_8e_1e_4 = [(hci_energy - dmrg_energy) * 10**3 for hci_energy in hci_energies_40o_8e_1e_4]

hci_dum_dets_40o_8_e_1e_5 = [3447879]
hci_energies_40o_8e_1e_5 = [-4.259069204253517]
hci_energy_errors_40o_8e_1e_5 = [(hci_energy - dmrg_energy) * 10**3 for hci_energy in hci_energies_40o_8e_1e_5]

shci_var_dum_det_30o_8e_eps_5e_6 =  [2842121]
shci_var_energy_30o_8e_eps_5e_6 = -10.84636042 + nuclear_repulsion_energy
shci_var_energy_error_30o_8e_eps_5e_6 = [(shci_var_energy_30o_8e_eps_5e_6 - dmrg_energy) * 10**3]


shci_var_dum_det_30o_8e_eps_1e_5 =  [1618025]
shci_var_energy_30o_8e_eps_1e_5 = -10.84628940 + nuclear_repulsion_energy
shci_var_energy_error_30o_8e_eps_1e_5 = [(shci_var_energy_30o_8e_eps_1e_5 - dmrg_energy) * 10**3]

shci_var_dum_det_40o_8e_eps_1e_5 =  [3509839]
shci_var_energy_40o_8e_eps_1e_5 = -10.8557952925 + nuclear_repulsion_energy
shci_var_energy_error_40o_8e_eps_1e_5 = [(shci_var_energy_40o_8e_eps_1e_5 - dmrg_energy) * 10**3]

E_1_dmrg = -4.2588094076


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
plt.figure(figsize=(12, 8))  # width=10, height=6 inches
plt.xscale('log')
plt.scatter(sqd_dimensions, sqd_energy_errors, c='cyan', label='SQD (8e,30o)', marker='o', alpha=alpha)
plt.scatter(qbe_sqd_dimension, qbe_sqd_energy_error, c='red', label='QBE-SQD', marker='o', alpha=alpha)
plt.scatter(hci_dum_dets_40o_8_e_1e_4, hci_energy_errors_40o_8e_1e_4, c='crimson', label='HCI (8e,40o) $ε_1=10^{-4}$', marker='s', alpha=alpha)
plt.scatter(hci_dum_dets_40o_8_e_1e_5, hci_energy_errors_40o_8e_1e_5, c='grey', label='HCI (8e,40o) $ε_1=10^{-5}$', marker='s', alpha=alpha)
plt.scatter(hci_dum_dets_30o_8_e_1e_4, hci_energy_errors_30o_8e_1e_4, c='blue', label='HCI (8e,30o) $ε_1=10^{-4}$', marker='s', alpha=alpha)
plt.scatter(hci_dum_dets_30o_8_e_1e_5, hci_energy_errors_30o_8e_1e_5, c='green', label='HCI (8e,30o) $ε_1=10^{-5}$', marker='s', alpha=alpha)
plt.scatter(shci_var_dum_det_30o_8e_eps_5e_6, shci_var_energy_error_30o_8e_eps_5e_6, c='navy', label='SHCI (8e,30o) $ε_1=5\\times 10^{-6}$', marker='^', alpha=alpha)
plt.scatter(shci_var_dum_det_30o_8e_eps_1e_5, shci_var_energy_error_30o_8e_eps_1e_5, c='purple', label='SHCI (8e,30o) $ε_1=10^{-5}$', marker='^', alpha=alpha)
plt.scatter(shci_var_dum_det_40o_8e_eps_1e_5, shci_var_energy_error_40o_8e_eps_1e_5, c='brown', label='SHCI (8e,40o) $ε_1=10^{-5}$', marker='^', alpha=alpha)
plt.xlabel('Number of Slater determinants')
plt.ylabel('E - E$_{\mathrm{DMRG}}$ [mHa]', labelpad=15)
plt.axhline(y=0, color='k', linestyle='-')
plt.axhline(y=(E_1_dmrg - dmrg_energy) * 10**3, color='gray', linestyle='--', label='$E_1$ DMRG, bond dim. 400')
#plt.title('QBE-SQD vs SQD Energy Error Convergence', fontsize=fontsize)
plt.legend(fontsize=20)
plt.grid(which='both', axis='y')
plt.tight_layout()
plt.savefig('/home/joel/Desktop/numerical_results/QBE_SQD/paper_figures/H8_ring_ccpVDZ_compare_SQD_QBE_SQD_1point8.pdf', dpi=300, bbox_inches='tight')
#plt.xscale('log')
plt.show()


#alpha = 0.5
#plt.figure(figsize=(20, 7))  # width=10, height=6 inches
#plt.rcParams.update({'font.size': 18, 'lines.markersize': 10})
#plt.xscale('log')
#plt.scatter(sqd_dimensions, sqd_energy_errors, c='cyan', label='SQD (4e, 30o)', marker='o', alpha=alpha)
#plt.scatter(qbe_sqd_dimension, qbe_sqd_energy_error, c='red', label='QBE-SQD', marker='o', alpha=alpha)
#plt.scatter(hci_dum_dets_40o_4_e_1e_4, hci_energy_errors_40o_4e_1e_4, c='darkorange', label='HCI (4e, 40o) $ε_1=10^{-4}$', marker='x', alpha=0.8)
#plt.scatter(hci_dum_dets_40o_4_e_1e_5, hci_energy_errors_40o_4e_1e_5, c='tomato', label='HCI (4e, 40o) $ε_1=10^{-5}$', marker='x', alpha=0.8)
#plt.scatter(hci_dum_dets_30o_4_e_1e_4, hci_energy_errors_30o_4e_1e_4, c='blue', label='HCI (4e, 30o) $ε_1=10^{-4}$', marker='x', alpha=0.8)
#plt.scatter(hci_dum_dets_30o_4_e_1e_5, hci_energy_errors_30o_4e_1e_5, c='green', label='HCI (4e, 30o) $ε_1=10^{-5}$', marker='x', alpha=0.8)
#plt.scatter(shci_var_dum_det_30o_4e_eps_5e_6, shci_var_energy_error_30o_4e_eps_5e_6, c='navy', label='SHCI (4e, 30o) $ε_1=5\\times 10^{-6}$', marker='^', alpha=alpha)
#plt.scatter(shci_var_dum_det_30o_4e_eps_1e_5, shci_var_energy_error_30o_4e_eps_1e_5, c='purple', label='SHCI (4e, 30o) $ε_1=10^{-5}$', marker='^', alpha=alpha)
#plt.scatter(shci_var_dum_det_40o_4e_eps_1e_5, shci_var_energy_error_40o_4e_eps_1e_5, c='brown', label='SHCI (4e, 40o) $ε_1=10^{-5}$', marker='^', alpha=alpha)
#plt.xlabel('Number of Slater determinants')
#plt.ylabel('E - E$_{\mathrm{DMRG}}$ [mHa]')
#plt.axhline(y=0, color='k', linestyle='-')
#plt.axhline(y=(E_1_dmrg - dmrg_energy) * 10**3, color='gray', linestyle='--', label='$E_1$ DMRG, bond dim. 400')
#plt.title('QBE-SQD vs SQD Energy Error Convergence', fontsize=fontsize)
#plt.legend(fontsize=fontsize)
#plt.grid(which='both', axis='y')
#plt.tight_layout()
#plt.savefig('/home/joel/Desktop/numerical_results/QBE_SQD/paper_figures/H8_ring_ccpVDZ_compare_SQD_QBE_SQD_1point8_elongated.pdf', dpi=300, bbox_inches='tight')
#plt.xscale('log')
#plt.show()

