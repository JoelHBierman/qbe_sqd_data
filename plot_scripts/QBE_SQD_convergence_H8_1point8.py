import numpy as np
import matplotlib.pyplot as plt
fontsize = 14
qbe_fci_iter_list = [0,1,2,3,4,5,6,7,8,9]
qbe_fci_density_error_results = [4.5618e-03, 3.4562e-03, 3.0461e-03, 1.2474e-03, 1.1034e-03, 8.6271e-04, 5.2147e-04, 5.1282e-04, 4.7661e-04, 1.8535e-04]
qbe_fci_energy_results = [-4.273129512880274, -4.265584527998431, -4.263448950067268, -4.2656007048944, -4.267231631097284, -4.269225767506505, -4.268106300278657, -4.268112873990669, -4.268140338356512, -4.268350959379263]

qbe_sqd_iter_list = [0,1,2,3,4,5]
qbe_sqd_density_error_results = [4.5578e-03, 3.4658e-03, 3.0633e-03, 1.5848e-03, 1.2712e-03, 1.2101e-03]
qbe_sqd_energy_results = [-4.273097340366544, -4.265553339931611, -4.263501064403261, -4.264486579529108, -4.2654172136983055, -4.267035427832645]

dmrg_energy = -4.302523105341811

alpha = 0.5
qbe_fci_energy_errors = [(qbe_energy - dmrg_energy) * 10**3 for qbe_energy in qbe_fci_energy_results]
plt.plot(qbe_fci_iter_list, qbe_fci_energy_errors, marker='D', label="QBE-FCI")
plt.plot(qbe_sqd_iter_list, [(qbe_energy - dmrg_energy) * 10**3 for qbe_energy in qbe_sqd_energy_results], marker='o', color='g', linestyle='--', label='QBE-SQD')
plt.title('QBE-SQD vs QBE-FCI Energy Error Convergence', fontsize=fontsize)
plt.ylabel('E - E$_{\mathrm{DMRG}}$ [mHa]', fontsize=fontsize)
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

plt.show()


plt.rcParams.update({'font.size': 32, 'lines.markersize': 16})
plt.rcParams.update({'xtick.labelsize': 32, 'ytick.labelsize': 32, 'xtick.major.size': 8,      # Length of major x ticks
    'xtick.major.width': 2,     # Width of major x ticks
    'xtick.minor.size': 4,      # Length of minor x ticks
    'xtick.minor.width': 1,     # Width of minor x ticks
    'ytick.major.size': 8,      # Length of major y ticks
    'ytick.major.width': 2,     # Width of major y ticks
    'ytick.minor.size': 4,      # Length of minor y ticks
    'ytick.minor.width': 1  }) 
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 14), sharex=True)

# First subplot - Energy error
ax1.plot(qbe_fci_iter_list, qbe_fci_energy_errors, marker='D')
ax1.plot(qbe_sqd_iter_list, [(qbe_energy - dmrg_energy) * 10**3 for qbe_energy in qbe_sqd_energy_results], marker='o', color='r', linestyle='--')
ax1.set_ylabel('E - E$_{\mathrm{DMRG}}$ [mHa]', labelpad=15)
ax1.grid(which='both', axis='y')

# Second subplot - Density error
ax2.semilogy(qbe_fci_iter_list, qbe_fci_density_error_results, label='QBE-FCI', marker='D')
ax2.semilogy(qbe_sqd_iter_list, qbe_sqd_density_error_results, label='QBE-SQD', marker='o', color='r', linestyle='--')
ax2.set_ylabel('Density matching error', labelpad=15)
ax2.grid(which='both', axis='y')

# Set shared x-axis ticks
ax2.set_xlim(0, 9)
ax2.set_xticks(range(0, 10))

# Shared x-axis label and legend
fig.text(0.55, 0.02, 'BE iteration', ha='center')
fig.legend(loc='upper right', bbox_to_anchor=(0.95, 0.85))

plt.tight_layout()
plt.subplots_adjust(bottom=0.1, top=0.88, hspace=0)
plt.savefig('/home/joel/Desktop/numerical_results/QBE_SQD/paper_figures/QBE_SQD_convergence_H8_1point8.pdf', dpi=300, bbox_inches='tight')
plt.show()



#plt.rcParams.update({'font.size': 18})
#fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(20, 10), sharex=True)

# First subplot - Energy error
#ax1.plot(qbe_fci_iter_list, qbe_fci_energy_errors, marker='x')
#ax1.plot(qbe_sqd_iter_list, [(qbe_energy - dmrg_energy) * 10**3 for qbe_energy in qbe_sqd_energy_results], marker='o', color='g', linestyle='--')
#ax1.set_ylabel('E - E$_{\mathrm{DMRG}}$ [mHa]')
#ax1.grid(which='both', axis='y')

# Second subplot - Density error
#ax2.semilogy(qbe_fci_iter_list, qbe_fci_density_error_results, label='QBE-FCI', marker='x')
#ax2.semilogy(qbe_sqd_iter_list, qbe_sqd_density_error_results, label='QBE-SQD', marker='o', color='g', linestyle='--')
#ax2.set_ylabel('Density matching error')
#ax2.grid(which='both', axis='y')

# Set shared x-axis ticks
#ax2.set_xlim(0, 9)
#ax2.set_xticks(range(0, 10))

# Shared x-axis label and legend
#fig.text(0.5, 0.04, 'BE iteration', ha='center')
#fig.legend(loc='upper right', bbox_to_anchor=(0.95, 0.85))

#plt.tight_layout()
#plt.subplots_adjust(bottom=0.1, top=0.88, hspace=0)
#plt.savefig('/home/joel/Desktop/numerical_results/QBE_SQD/paper_figures/QBE_SQD_convergence_H8_1point8_elongated.pdf', dpi=300, bbox_inches='tight')
#plt.show()