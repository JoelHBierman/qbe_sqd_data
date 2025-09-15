import numpy as np
import matplotlib.pyplot as plt
fontsize = 14
qbe_fci_iter_list = [0,1,2,3,4,5,6,7,8,9]
qbe_fci_density_error_results = [3.3310e-02, 2.5936e-02, 6.5859e-02, 2.7305e-02, 1.8947e-02, 1.6666e-02, 1.6493e-02, 1.1384e-02, 3.2480e-02, 5.8840e-02]
qbe_fci_energy_results = [-4.285768352756245, -4.233210277179956, -3.997706229094792, -4.129627413582012, -4.150465505660455, -4.324342527739505, -4.3244317107400345, -4.283294203158642, -4.27234064560105, -4.247725801583474]

qbe_sqd_iter_list = [0,1,2,3,4,5]
qbe_sqd_density_error_results = [3.3307e-02, 1.9066e-02, 4.5394e-02, 1.4337e-02, 1.8632e-02, 1.8489e-02]
qbe_sqd_energy_results = [-4.285742774397161, -4.146637856180334, -4.06190664209049, -4.285829976093274, -4.33084139485889, -4.330382461513233]

dmrg_energy = -4.1743049472965215

qbe_fci_energy_errors = [(qbe_energy - dmrg_energy) * 10**3 for qbe_energy in qbe_fci_energy_results]
plt.plot(qbe_fci_iter_list, qbe_fci_energy_errors, marker='x', label="QBE-FCI")
plt.plot(qbe_sqd_iter_list, [(qbe_energy - dmrg_energy) * 10**3 for qbe_energy in qbe_sqd_energy_results], marker='o', color='g', linestyle='--', label='QBE-SQD')
plt.title('QBE-SQD vs QBE-FCI Energy Error Convergernce', fontsize=fontsize)
plt.ylabel('Energy error (mHa)', fontsize=fontsize)
plt.xlabel('BE iteration', fontsize=fontsize)
plt.legend(fontsize=fontsize)
plt.grid(which='both', axis='y')
plt.show()

plt.semilogy(qbe_fci_iter_list, qbe_fci_density_error_results, label='QBE-FCI', marker='x')
plt.semilogy(qbe_sqd_iter_list, qbe_sqd_density_error_results, label='QBE-SQD', marker='o', color='g', linestyle='--')
plt.title('QBE-SQD density matching error', fontsize=fontsize)
plt.xlabel('BE iteration', fontsize=fontsize)
plt.ylabel('Density matching error', fontsize=fontsize)
plt.grid(which='both', axis='y')
plt.legend(fontsize=fontsize)
plt.savefig('/home/joel/Desktop/numerical_results/QBE_SQD/paper_figures/QBE_SQD_convergence_H8_2point2.pdf', dpi=300, bbox_inches='tight')
plt.show()


plt.rcParams.update({'font.size': 32, 'lines.markersize': 16})
plt.rcParams.update({'xtick.labelsize': 28, 'ytick.labelsize': 28, 'xtick.major.size': 8,      # Length of major x ticks
    'xtick.major.width': 2,     # Width of major x ticks
    'xtick.minor.size': 4,      # Length of minor x ticks
    'xtick.minor.width': 1,     # Width of minor x ticks
    'ytick.major.size': 8,      # Length of major y ticks
    'ytick.major.width': 2,     # Width of major y ticks
    'ytick.minor.size': 8,      # Length of minor y ticks
    'ytick.minor.width': 2  }) 
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 14), sharex=True)
# First subplot - Energy error
ax1.plot(qbe_fci_iter_list, qbe_fci_energy_errors, marker='D')
ax1.plot(qbe_sqd_iter_list, [(qbe_energy - dmrg_energy) * 10**3 for qbe_energy in qbe_sqd_energy_results], marker='o', color='r', linestyle='--')
ax1.set_ylabel('E - E$_{\mathrm{DMRG}}$ [mHa]', labelpad=15)
ax1.grid(which='both', axis='y')
#ax1.tick_params(axis='y', pad=10)

# Second subplot - Density error
ax2.semilogy(qbe_fci_iter_list, qbe_fci_density_error_results, label='QBE-FCI', marker='D')
ax2.semilogy(qbe_sqd_iter_list, qbe_sqd_density_error_results, label='QBE-SQD', marker='o', color='r', linestyle='--')
ax2.set_ylabel('Density matching error', labelpad=15)
ax2.grid(which='both', axis='y')
#ax2.tick_params(axis='both', pad=10)

# Set shared x-axis ticks
ax2.set_xlim(0, 9)
ax2.set_xticks(range(0, 10))

# Shared x-axis label and legend
fig.text(0.6, 0.02, 'BE iteration', ha='center')
fig.legend(loc='upper right', bbox_to_anchor=(0.95, 0.85))
#plt.rcParams.update({'font.size': 18})
plt.tight_layout()
plt.subplots_adjust(bottom=0.1, top=0.88, hspace=0)
plt.savefig('/home/joel/Desktop/numerical_results/QBE_SQD/paper_figures/QBE_SQD_convergence_H8_2point2.pdf', dpi=300, bbox_inches='tight')
plt.show()


#plt.rcParams.update({'font.size': 18})
#fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(20, 10), sharex=True)
# First subplot - Energy error
#ax1.plot(qbe_fci_iter_list, qbe_fci_energy_errors, marker='x')
#ax1.plot(qbe_sqd_iter_list, [(qbe_energy - dmrg_energy) * 10**3 for qbe_energy in qbe_sqd_energy_results], marker='o', color='g', linestyle='--')
#ax1.set_ylabel('E - E$_{\mathrm{DMRG}}$ [mHa]', labelpad=15)
#ax1.grid(which='both', axis='y')

# Second subplot - Density error
#ax2.semilogy(qbe_fci_iter_list, qbe_fci_density_error_results, label='QBE-FCI', marker='x')
#ax2.semilogy(qbe_sqd_iter_list, qbe_sqd_density_error_results, label='QBE-SQD', marker='o', color='g', linestyle='--')
#ax2.set_ylabel('Density matching error', labelpad=15)
#ax2.grid(which='both', axis='y')

# Set shared x-axis ticks
#ax2.set_xlim(0, 9)
#ax2.set_xticks(range(0, 10))

# Shared x-axis label and legend
#fig.text(0.5, 0.04, 'BE iteration', ha='center')
#fig.legend(loc='upper right', bbox_to_anchor=(0.95, 0.85))
#plt.rcParams.update({'font.size': 18})
#plt.tight_layout()
#plt.subplots_adjust(bottom=0.1, top=0.88, hspace=0)
#plt.savefig('/home/joel/Desktop/numerical_results/QBE_SQD/paper_figures/QBE_SQD_convergence_H8_2point2_elongated.pdf', dpi=300, bbox_inches='tight')
#plt.show()