from turtle import color
import numpy as numpy
import matplotlib.pyplot as plt

fontsize = 14
iter_list = [0,1,2,3,4,5]
fci_iter_list = [0,1,2,3,4,5,6,7,8,9,10]
#energy_results = [-4.364795560322212, -4.3648199567122035, -4.362203129697468, -4.364365089565609, -4.363925195018003, -4.364264580250294]
#density_error_results = [4.1172e-03, 3.5872e-03, 8.5497e-04, 1.8264e-04, 1.2178e-04, 6.7381e-05]

qbe_fci_energy_results = [-4.364801898025974, -4.3648263241111325, -4.3622120063485195, -4.364369360012734, -4.3639306812929455, -4.364278473647456, -4.364198570598671, -4.364209362716969
, -4.364203414401606, -4.364205782811084, -4.364204451244154]
qbe_fci_error_results = [4.1180e-03, 3.5880e-03, 8.5701e-04, 1.8239e-04, 1.2192e-04, 6.7066e-05, 5.4584e-05, 5.2202e-05, 5.2098e-05, 5.2117e-05, 5.2110e-05]

pittsburgh_2500_density_errors = [4.1161e-03, 3.5867e-03, 8.5593e-04,
                                  1.8186e-04, 1.2199e-04, 6.7138e-05]
pittsburgh_2500_energies = [-4.364779618705463, -4.364802099058355, -4.362197516671807,
                            -4.364341692690181, -4.363903826572007, -4.3642546996417915]

ccsd_energy = - 4.34438
dmrg_energy = -4.385327981507567
pittsburgh_2500_energy_errors = [(qbe_energy - dmrg_energy) * 10**3 for qbe_energy in pittsburgh_2500_energies]
qbe_fci_energy_errors = [(qbe_energy - dmrg_energy) * 10**3 for qbe_energy in qbe_fci_energy_results]

plt.plot(fci_iter_list, qbe_fci_energy_errors, marker='x', label="QBE-FCI")
#plt.plot(iter_list, energy_results, label='QBE-SQD (ibm_marrakesh, batch size 4000)')
plt.plot(iter_list, pittsburgh_2500_energy_errors, marker='o', color='g', linestyle='--', label='QBE-SQD')
#plt.semilogy(iter_list, [ccsd_energy - dmrg_energy]*len(iter_list), label='CCSD')
#plt.semilogy(iter_list, [dmrg_energy]*len(iter_list), label='DMRG')
#plt.title('QBE-SQD vs QBE-FCI Energy Error Convergernce', fontsize=fontsize)
plt.ylabel('E - E$_{\mathrm{DMRG}}$ [mHa]', fontsize=fontsize)
plt.xlabel('BE Iteration', fontsize=fontsize)
plt.legend(fontsize=fontsize)
plt.show()

plt.semilogy(fci_iter_list, qbe_fci_error_results, label='QBE-FCI', marker='x')
#plt.semilogy(iter_list, density_error_results, label='QBE-SQD')
plt.plot(iter_list, pittsburgh_2500_density_errors, label='QBE-SQD', marker='o', color='g', linestyle='--')
plt.xlabel('BE Iteration', fontsize=fontsize)
plt.ylabel('Density matching error', fontsize=fontsize)
#plt.title('QBE-SQD Density Matching Error', fontsize=fontsize)
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
ax1.plot(fci_iter_list, qbe_fci_energy_errors, marker='D')
ax1.plot(iter_list, pittsburgh_2500_energy_errors, marker='o', color='r', linestyle='--')
ax1.set_ylabel('E - E$_{\mathrm{DMRG}}$ [mHa]', labelpad=15)
ax1.grid(which='both', axis='y')

# Second subplot - Density error
ax2.semilogy(fci_iter_list, qbe_fci_error_results, label='QBE-FCI', marker='D')
ax2.semilogy(iter_list, pittsburgh_2500_density_errors, label='QBE-SQD', marker='o', color='r', linestyle='--')
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
plt.savefig('/home/joel/Desktop/numerical_results/QBE_SQD/paper_figures/QBE_SQD_convergence_H8_ring_1point3_cc-pVDZ.pdf', dpi=300, bbox_inches='tight')
plt.show()


#plt.rcParams.update({'font.size': 18})
#fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(20, 10), sharex=True)

# First subplot - Energy error
#ax1.plot(fci_iter_list, qbe_fci_energy_errors, marker='x')
#ax1.plot(iter_list, pittsburgh_2500_energy_errors, marker='o', color='g', linestyle='--')
#ax1.set_ylabel('E - E$_{\mathrm{DMRG}}$ [mHa]')
#ax1.grid(which='both', axis='y')

# Second subplot - Density error
#ax2.semilogy(fci_iter_list, qbe_fci_error_results, label='QBE-FCI', marker='x')
#ax2.semilogy(iter_list, pittsburgh_2500_density_errors, label='QBE-SQD', marker='o', color='g', linestyle='--')
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
#plt.savefig('/home/joel/Desktop/numerical_results/QBE_SQD/paper_figures/QBE_SQD_convergence_H8_ring_1point3_cc-pVDZ_elongated.pdf', dpi=300, bbox_inches='tight')
#plt.show()