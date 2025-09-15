import numpy as np
import matplotlib.pyplot as plt

# compare results for H8 ring with SQD and QBE at interatomic distance 1.3 angstroms
fontsize = 14
sqd_dimensions_list = [3556996, 8678916, 14379264, 19421649, 23961025]
sqd_energies_list = [-13.496413942899059, -13.501194577595221, -13.502920162670897, -13.503528279716013, -13.503921506809066]
qbe_energies_list = [-4.3642546996417915]
qbe_fragment_dimension = [4157521]
# max dim of solution state
4076361
# max dim of all batch states
4157521
drmg_energy = [-4.385327981507567]
nuclear_repulsion_energy = 9.133975910779744
sqd_energies_list = [sqd_electronic_energy + nuclear_repulsion_energy for sqd_electronic_energy in sqd_energies_list]   

dice_shci_dimensions = [4487, 6277, 6971, 15611, 16971, 18618, 21556, 23944, 24503, 24598, 24634, 24642]
dice_shci_energies = [-13.4675733448, -13.4721081349, -13.4725284175, -13.4756347197, -13.4759816114, -13.4767127711, -13.4780974268, -13.4785970319, -13.4786781889, -13.4787034976, -13.4787111487, -13.4787134509]
dice_shci_energies = [dice_energy + nuclear_repulsion_energy for dice_energy in dice_shci_energies]
dice_shci_energy_errors = [abs(dice_energy - drmg_energy[0]) for dice_energy in dice_shci_energies]

plt.plot(sqd_dimensions_list, sqd_energies_list, label='SQD', marker='o')
# plot scatter of QBE energy as function of QBE dimension
plt.scatter(qbe_fragment_dimension, qbe_energies_list, label='QBE', color='red')
plt.plot(dice_shci_dimensions, dice_shci_energies, label='SHCI (DICE)', marker='x')
#plt.axhline(y=qbe_energies_list[0], color='r', linestyle='--', label='QBE')
plt.axhline(y=drmg_energy[0], color='g', linestyle='--', label='DMRG')
plt.xlabel('Number of Slater Determinants', fontsize=fontsize)
plt.ylabel('Energy (Ha)', fontsize=fontsize)
plt.title('H8 Ring SQD vs QBE Energy Comparison')
plt.legend()
plt.show()

# plot QBE and SQD energies as a function of error against DMRG energy on a log scale
sqd_errors = [abs(sqd_energy - drmg_energy[0]) for sqd_energy in sqd_energies_list]
qbe_error = abs(qbe_energies_list[0] - drmg_energy[0])
plt.semilogy(sqd_dimensions_list, sqd_errors, label='SQD', marker='o')
plt.semilogy(dice_shci_dimensions, dice_shci_energy_errors, label='SHCI (DICE)', marker='x')
plt.scatter(qbe_fragment_dimension, [qbe_error], label='QBE-SQD', color='red')
plt.scatter([3157729], [-13.463705945719482 + nuclear_repulsion_energy - drmg_energy[0]], label="SQD (19o, 4e)")
plt.scatter([3459600], [-13.49627164605883 + nuclear_repulsion_energy - drmg_energy[0]], label="SQD (30o, 4e)")
#plt.axhline(y=qbe_error, color='r', linestyle='--', label='QBE Error')
plt.xlabel('Number of Slater Determinants', fontsize=fontsize)
plt.ylabel('Energy Error (Ha)', fontsize=fontsize)
plt.title('SQD vs QBE Energy Error Comparison', fontsize=fontsize)
plt.legend(fontsize=fontsize)
plt.show()

# plot QBE and SQD energies as a function of error against DMRG energy on a log scale
sqd_errors = [abs(sqd_energy - drmg_energy[0]) for sqd_energy in sqd_energies_list]
qbe_error = abs(qbe_energies_list[0] - drmg_energy[0])
plt.loglog(sqd_dimensions_list, sqd_errors, label='SQD', marker='o')
plt.loglog(dice_shci_dimensions, dice_shci_energy_errors, label='SHCI (DICE)', marker='x')
plt.scatter(qbe_fragment_dimension, [qbe_error], label='QBE-SQD', color='red')
plt.scatter([3157729], [-13.463705945719482 + nuclear_repulsion_energy - drmg_energy[0]], label="SQD (19o, 4e)")
plt.scatter([3459600], [-13.49627164605883 + nuclear_repulsion_energy - drmg_energy[0]], label="SQD (30o, 4e)")
#plt.axhline(y=qbe_error, color='r', linestyle='--', label='QBE Error')
plt.xlabel('Number of Slater Determinants', fontsize=fontsize)
plt.ylabel('Energy Error (Ha)', fontsize=fontsize)
plt.title('SQD vs QBE Energy Error Comparison', fontsize=fontsize)
plt.legend(fontsize=20)
plt.show()

sqd_configuration_recovery_dimensions = [16, 2250000, 1957201, 2627641, 3538161]

#qbe_sqd_configuration_recovery_dimensions_f0_iter_0 = [356409, 2992900, 3225616, 3175524, 3175524]
#qbe_sqd_configuration_recovery_dimensions_f0_iter_5 = [1416100, 3143529, 3055504, 3186225, 3200521]

#plt.semilogy(sqd_configuration_recovery_dimensions, label='SQD', marker='o')
#plt.semilogy(qbe_sqd_configuration_recovery_dimensions_f0_iter_0, label='QBE-SQD f0 iter 0', marker='x')
#plt.semilogy(qbe_sqd_configuration_recovery_dimensions_f0_iter_5, label='QBE-SQD f0 iter 5', marker='s')
#plt.xlabel('Configuration Recovery Iteration', fontsize=20)
#plt.ylabel('Number of Slater Determinants', fontsize=20)
#plt.title('QBE-SQD VS SQD Configuration Recovery Comparison', fontsize=20)
#plt.legend(fontsize=20)
#plt.show()

qbe_sqd_configuration_recovery_dimensions_f1_iter_1 = [[26569, 26569, 26569, 26569, 26569],
                                                       [3602404, 3775249, 3659569, 3636649, 3606201],
                                                       [3984016, 3751969, 3837681, 3721041, 3779136],
                                                       [3810304, 3825936, 3822025, 3873024, 3814209],
                                                       [3783025, 3798601, 3825936, 3841600, 4008004]]

qbe_sqd_configuration_recovery_dimensions_f1_iter_1_avgs = [np.mean(dimensions) for dimensions in qbe_sqd_configuration_recovery_dimensions_f1_iter_1]
qbe_sqd_configuration_recovery_dimensions_f1_iter_1_stdevs = [np.std(dimensions)/np.sqrt(5) for dimensions in qbe_sqd_configuration_recovery_dimensions_f1_iter_1]


qbe_sqd_configuration_recovery_dimensions_f2_iter_5 =[[1962801, 1962801, 1962801, 1962801, 1962801],
                                                      [3020644, 2822400, 3034564, 3027600, 2910436],
                                                      [3076516, 2968729, 2982529, 2999824, 3111696],
                                                      [3027600, 2999824, 3055504, 3052009, 2948089],
                                                      [2968729, 2883204, 2992900, 3017169, 3069504]]

qbe_sqd_configuration_recover_dimensions_f2_iter_5_avgs = [np.mean(dimensions) for dimensions in qbe_sqd_configuration_recovery_dimensions_f2_iter_5]
qbe_sqd_configuration_recovery_dimensions_f2_iter_5_stdevs = [np.std(dimensions)/np.sqrt(5) for dimensions in qbe_sqd_configuration_recovery_dimensions_f2_iter_5]

sqd_configuration_recovery_dimensions = [[64, 64, 64, 64, 64],
                                         [1830609, 1803649, 1737124, 1758276, 1819801],
                                         [2719201, 2798929, 2768896, 2785561, 2910436],
                                         [2996361, 3062500, 2972176, 2930944, 3020644],
                                         [3674889, 3678724, 3663396, 3617604, 3690241]]

sqd_configuration_recovery_dimensions_avgs = [np.mean(dimensions) for dimensions in sqd_configuration_recovery_dimensions]
sqd_configuration_recovery_dimensions_stdevs = [np.std(dimensions)/np.sqrt(5) for dimensions in sqd_configuration_recovery_dimensions_avgs]

plt.figure(figsize=(12, 7))
plt.rcParams.update({'font.size': 24, 'lines.markersize': 16})
plt.rcParams.update({'xtick.labelsize': 24, 'ytick.labelsize': 24, 'xtick.major.size': 8,      # Length of major x ticks
    'xtick.major.width': 2,     # Width of major x ticks
    'xtick.minor.size': 4,      # Length of minor x ticks
    'xtick.minor.width': 1,     # Width of minor x ticks
    'ytick.major.size': 8,      # Length of major y ticks
    'ytick.major.width': 2,     # Width of major y ticks
    'ytick.minor.size': 4,      # Length of minor y ticks
    'ytick.minor.width': 1  })
plt.errorbar([0, 1, 2, 3, 4], sqd_configuration_recovery_dimensions_avgs, yerr=sqd_configuration_recovery_dimensions_stdevs, label='SQD', marker='o', capsize=5, color='c')
plt.errorbar([0, 1, 2, 3, 4], qbe_sqd_configuration_recovery_dimensions_f1_iter_1_avgs, yerr=qbe_sqd_configuration_recovery_dimensions_f1_iter_1_stdevs, label='QBE-SQD ($f_{1}$ BE iteration 1)', marker='D', capsize=5, color='red')
plt.errorbar([0, 1, 2, 3, 4], qbe_sqd_configuration_recover_dimensions_f2_iter_5_avgs, yerr=qbe_sqd_configuration_recovery_dimensions_f2_iter_5_stdevs, label='QBE-SQD ($f_{2}$ BE iteration 5)', marker='s', capsize=5, color='mediumpurple')   
plt.grid(axis='y')
plt.xlabel('Configuration recovery iteration', labelpad=10)
plt.ylabel('Number of Slater determinants', labelpad=10)
plt.yscale('log')
plt.xticks([0, 1, 2, 3, 4])
plt.legend()
plt.tight_layout()
plt.savefig('/home/joel/Desktop/numerical_results/QBE_SQD/paper_figures/H8_ring_ccpVDZ_compare_SQD_QBE_SQD_configuration_recovery_1point3.pdf', dpi=300, bbox_inches='tight')
plt.show()

additional_sqd_dimensions = []
additional_sqd_energies = []
additional_sqd_energy_errors = []

energies_result_0 = [-13.491714050864568, -13.49627164605883, -13.501033169610743, -13.502640010720425, -13.503853174973523, -13.504038724782141]
energies_result_0 = [energy + nuclear_repulsion_energy for energy in energies_result_0]
energies_error_result_0 = [abs(energy - drmg_energy[0]) for energy in energies_result_0]
dimensions_result_0 = [1249924, 3459600, 8898289, 13616100, 18748900, 23164969]
additional_sqd_dimensions.append(dimensions_result_0)
additional_sqd_energies.append(energies_result_0)
additional_sqd_energy_errors.append(energies_error_result_0)

energies_result_1 = [-13.488881361777954, -13.497164810720058, -13.501581313505298, -13.503189330066357, -13.503723297258757, -13.504109657546703]
energies_result_1 = [energy + nuclear_repulsion_energy for energy in energies_result_1]
energies_errors_result_1 = [abs(energy - drmg_energy[0]) for energy in energies_result_1]
dimensions_result_1 = [1401856, 3728761, 8958049, 13608721, 18826921, 23931664]
additional_sqd_dimensions.append(dimensions_result_1)
additional_sqd_energies.append(energies_result_1)
additional_sqd_energy_errors.append(energies_errors_result_1)

energies_result_2 = [-13.492359396433745, -13.49711596495446, -13.501328577502276, -13.503143969057135, -13.503755331291227, -13.504016252350754]
energies_result_2 = [energy + nuclear_repulsion_energy for energy in energies_result_2]
energies_errors_result_2 = [abs(energy - drmg_energy[0]) for energy in energies_result_2]
dimensions_result_2 = [1430416, 3818116, 9006001, 13793796, 19333609, 23078416]
additional_sqd_dimensions.append(dimensions_result_2)
additional_sqd_energies.append(energies_result_2)
additional_sqd_energy_errors.append(energies_errors_result_2)

energies_result_4 = [-13.492700955449227, -13.49663237834812, -13.501397066993615, -13.503020865832934, -13.503645069722326, -13.503961350305168]
energies_result_4 = [energy + nuclear_repulsion_energy for energy in energies_result_4]
energies_errors_result_4 = [abs(energy - drmg_energy[0]) for energy in energies_result_4]
dimensions_result_4 = [1338649, 3682561, 8561476, 13801225, 18215824, 22953681]
additional_sqd_dimensions.append(dimensions_result_4)
additional_sqd_energies.append(energies_result_4)
additional_sqd_energy_errors.append(energies_errors_result_4)

energies_result_5 = [-13.491046159610544, -13.496536105238967, -13.50104525038684, -13.50278722320673, -13.503623465592348
, -13.503940776352437]
energies_result_5 = [energy + nuclear_repulsion_energy for energy in energies_result_5]
energies_errors_result_5 = [abs(energy - drmg_energy[0]) for energy in energies_result_5]
dimensions_result_5 = [1216609, 3478225, 8625969, 13756681, 18558864, 23261329]
additional_sqd_dimensions.append(dimensions_result_5)
additional_sqd_energies.append(energies_result_5)
additional_sqd_energy_errors.append(energies_errors_result_5)

energies_result_6 = [-13.490392023040176, -13.49589620016494, -13.500675776596253, -13.502657238108124, -13.503453591522518, -13.503987610020742]
energies_result_6 = [energy + nuclear_repulsion_energy for energy in energies_result_6]
energies_errors_result_6 = [abs(energy - drmg_energy[0]) for energy in energies_result_6]
dimensions_result_6 = [1192464, 3448449, 8288641, 13704804, 18550249, 22791076]
additional_sqd_dimensions.append(dimensions_result_6)
additional_sqd_energies.append(energies_result_6)
additional_sqd_energy_errors.append(energies_errors_result_6)

energies_result_8 = [-13.492472193762035, -13.497193157116644, -13.501751826569658, -13.503189099906155, -13.503751336441228, -13.50415067861535]
energies_result_8 = [energy + nuclear_repulsion_energy for energy in energies_result_8]
energies_errors_result_8 = [abs(energy - drmg_energy[0]) for energy in energies_result_8]
dimensions_result_8 = [1498176, 3674889, 9066121, 14167696, 19289664, 23551609]
additional_sqd_dimensions.append(dimensions_result_8)
additional_sqd_energies.append(energies_result_8)
additional_sqd_energy_errors.append(energies_errors_result_8)

energies_result_9 = [-13.490477272541161, -13.496408005593418, -13.500347325228887, -13.502473694097493, -13.503451144484066, -13.503901974515752]
energies_result_9 = [energy + nuclear_repulsion_energy for energy in energies_result_9]
energies_errors_result_9 = [abs(energy - drmg_energy[0]) for energy in energies_result_9]
dimensions_result_9 = [1125721, 3426201, 8065600, 13322500, 18173169, 22877089]
additional_sqd_dimensions.append(dimensions_result_9)
additional_sqd_energies.append(energies_result_9)
additional_sqd_energy_errors.append(energies_errors_result_9)

additional_sqd_dimensions_19o = []
additional_sqd_energies_19o = []
additional_sqd_energy_errors_19o = []

################# 19o 4e results #####################
sqd_energies_19o_0 = [-13.461457426291359, -13.463382516679944, -13.463599950271604, -13.46365817988923, -13.463706883773241, -13.463732922376531]
sqd_dimensions_19o_0 = [1000000, 1792921, 2322576, 2752281, 3243601, 3678724]
sqd_energies_19o_0 = [energy + nuclear_repulsion_energy for energy in sqd_energies_19o_0]
sqd_energy_errors_19o_0 = [abs(energy - drmg_energy[0]) for energy in sqd_energies_19o_0]
additional_sqd_energies_19o.append(sqd_energies_19o_0)
additional_sqd_energy_errors_19o.append(sqd_energy_errors_19o_0)
additional_sqd_dimensions_19o.append(sqd_dimensions_19o_0)

sqd_energies_19o_1 = [-13.461260410902804, -13.463202363759219, -13.463548505438025, -13.463650630559128, -13.46369304398062, -13.463716300504798]
sqd_dimensions_19o_1 = [966289, 1713481, 2461761, 2805625, 3334276, 3572100]
sqd_energies_19o_1 = [energy + nuclear_repulsion_energy for energy in sqd_energies_19o_1]
sqd_energy_errors_19o_1 = [abs(energy - drmg_energy[0]) for energy in sqd_energies_19o_1]
additional_sqd_energies_19o.append(sqd_energies_19o_1)
additional_sqd_energy_errors_19o.append(sqd_energy_errors_19o_1)
additional_sqd_dimensions_19o.append(sqd_dimensions_19o_1)

sqd_energies_19o_2 = [-13.4616868156378, -13.463329477361064, -13.463595066266967, -13.46365040772688, -13.463707126933189, -13.46372963659289]
sqd_dimensions_19o_2 = [990025, 1760929, 2356225, 2798929, 3258025, 3606201]
sqd_energies_19o_2 = [energy + nuclear_repulsion_energy for energy in sqd_energies_19o_2]
sqd_energy_errors_19o_2 = [abs(energy - drmg_energy[0]) for energy in sqd_energies_19o_2]
additional_sqd_energies_19o.append(sqd_energies_19o_2)
additional_sqd_energy_errors_19o.append(sqd_energy_errors_19o_2)
additional_sqd_dimensions_19o.append(sqd_dimensions_19o_2)

sqd_energies_19o_3 = [-13.461820344163574, -13.46332673510912, -13.463639020382832, -13.463667997822649, -13.463702940059672, -13.463724810359277]
sqd_dimensions_19o_3 = [912025, 1768900, 2319529, 2808976, 3247204, 3508129]
sqd_energies_19o_3 = [energy + nuclear_repulsion_energy for energy in sqd_energies_19o_3]
sqd_energy_errors_19o_3 = [abs(energy - drmg_energy[0]) for energy in sqd_energies_19o_3]
additional_sqd_energies_19o.append(sqd_energies_19o_3)
additional_sqd_energy_errors_19o.append(sqd_energy_errors_19o_3)
additional_sqd_dimensions_19o.append(sqd_dimensions_19o_3)

sqd_energies_19o_4 = [-13.46181321676647, -13.463380405234819, -13.463586534445199, -13.463662044944812, -13.463702215777886, -13.463737393994025]
sqd_dimensions_19o_4 = [952576, 1790244, 2353156, 2842596, 3168400, 3636649]
sqd_energies_19o_4 = [energy + nuclear_repulsion_energy for energy in sqd_energies_19o_4]
sqd_energy_errors_19o_4 = [abs(energy - drmg_energy[0]) for energy in sqd_energies_19o_4]
additional_sqd_energies_19o.append(sqd_energies_19o_4)
additional_sqd_energy_errors_19o.append(sqd_energy_errors_19o_4)
additional_sqd_dimensions_19o.append(sqd_dimensions_19o_4)

sqd_energies_19o_5 = [-13.46212888063303, -13.46311807707955, -13.46352970695461, -13.463667207267152, -13.46367556910303, -13.46372717601834]
sqd_dimensions_19o_5 = [1030225, 1726596, 2377764, 2890000, 3348900, 3794704]
sqd_energies_19o_5 = [energy + nuclear_repulsion_energy for energy in sqd_energies_19o_5]
sqd_energy_errors_19o_5 = [abs(energy - drmg_energy[0]) for energy in sqd_energies_19o_5]
additional_sqd_energies_19o.append(sqd_energies_19o_5)
additional_sqd_energy_errors_19o.append(sqd_energy_errors_19o_5)
additional_sqd_dimensions_19o.append(sqd_dimensions_19o_5)

sqd_energies_19o_6 = [-13.461928822412933, -13.463302330379882, -13.463563267325206, -13.463633949130159, -13.463692598613287, -13.463730144278978]
sqd_dimensions_19o_6 = [968256, 1787569, 2280100, 2782224, 3207681, 3606201]
sqd_energies_19o_6 = [energy + nuclear_repulsion_energy for energy in sqd_energies_19o_6]
sqd_energy_errors_19o_6 = [abs(energy - drmg_energy[0]) for energy in sqd_energies_19o_6]
additional_sqd_energies_19o.append(sqd_energies_19o_6)
additional_sqd_energy_errors_19o.append(sqd_energy_errors_19o_6)
additional_sqd_dimensions_19o.append(sqd_dimensions_19o_6)

sqd_energies_19o_7 = [-13.461693765109963, -13.46319036045498, -13.463567105361246, -13.463672608240566, -13.46369493264944, -13.463729129754409]
sqd_dimensions_19o_7 = [978121, 1803649, 2298256, 2842596, 3196944, 3655744]
sqd_energies_19o_7 = [energy + nuclear_repulsion_energy for energy in sqd_energies_19o_7]
sqd_energy_errors_19o_7 = [abs(energy - drmg_energy[0]) for energy in sqd_energies_19o_7]
additional_sqd_energies_19o.append(sqd_energies_19o_7)
additional_sqd_energy_errors_19o.append(sqd_energy_errors_19o_7)
additional_sqd_dimensions_19o.append(sqd_dimensions_19o_7)

sqd_energies_19o_8 = [-13.461644680016844, -13.463304472584431, -13.463564880198554, -13.463682361130349, -13.463713216783946, -13.463735342380932]
sqd_dimensions_19o_8 = [998001, 1806336, 2337841, 2913849, 3204100, 3629025]
sqd_energies_19o_8 = [energy + nuclear_repulsion_energy for energy in sqd_energies_19o_8]
sqd_energy_errors_19o_8 = [abs(energy - drmg_energy[0]) for energy in sqd_energies_19o_8]
additional_sqd_energies_19o.append(sqd_energies_19o_8)
additional_sqd_energy_errors_19o.append(sqd_energy_errors_19o_8)
additional_sqd_dimensions_19o.append(sqd_dimensions_19o_8)

sqd_energies_19o_9 = [-13.462056723361842, -13.463096397402234, -13.463592863801184, -13.463656615716337, -13.463705945719482, -13.463718325238556]
sqd_dimensions_19o_9 = [929296, 1703025, 2340900, 2775556, 3157729, 3775249]
sqd_energies_19o_9 = [energy + nuclear_repulsion_energy for energy in sqd_energies_19o_9]
sqd_energy_errors_19o_9 = [abs(energy - drmg_energy[0]) for energy in sqd_energies_19o_9]
additional_sqd_energies_19o.append(sqd_energies_19o_9)
additional_sqd_energy_errors_19o.append(sqd_energy_errors_19o_9)
additional_sqd_dimensions_19o.append(sqd_dimensions_19o_9)

sqd_errors = [abs(sqd_energy - drmg_energy[0]) for sqd_energy in sqd_energies_list]
qbe_error = abs(qbe_energies_list[0] - drmg_energy[0])


hci_num_dets_40e_8e_1e_4 = [478390]
hci_energies_40e_8e_1e_4 = [-4.383110393466067]
hci_energy_errors_40e_8e_1e_4 = [abs(hci_energy - drmg_energy[0]) for hci_energy in hci_energies_40e_8e_1e_4]

hci_num_dets_40e_8e_1e_5 = [5430851]
hci_energies_40e_8e_1e_5 = [-4.385374797500871]
hci_energy_errors_40e_8e_1e_5 = [abs(hci_energy - drmg_energy[0]) for hci_energy in hci_energies_40e_8e_1e_5]


hci_num_dets_30e_8e_1e_4 = [324020]
hci_energies_30e_8e_1e_4 = [-4.369255274780247]
hci_energy_errors_30e_8e_1e_4 = [abs(hci_energy - drmg_energy[0]) for hci_energy in hci_energies_30e_8e_1e_4]


hci_num_dets_30e_8e_1e_5 = [2657952]
hci_energies_30e_8e_1e_5 = [-4.370801684350697]
hci_energy_errors_30e_8e_1e_5 = [abs(hci_energy - drmg_energy[0]) for hci_energy in hci_energies_30e_8e_1e_5]


shci_var_dum_det_30o_8e_eps_5e_6 =  [3101487]
shci_var_energy_30o_8e_eps_5e_6 = -13.50484716 + nuclear_repulsion_energy
shci_var_energy_error_30o_8e_eps_5e_6 = [(shci_var_energy_30o_8e_eps_5e_6 - drmg_energy[0]) * 10**3]


shci_var_dum_det_30o_8e_eps_1e_5 =  [1850693]
shci_var_energy_30o_8e_eps_1e_5 = -13.50478101 + nuclear_repulsion_energy
shci_var_energy_error_30o_8e_eps_1e_5 = [(shci_var_energy_30o_8e_eps_1e_5 - drmg_energy[0]) * 10**3]

shci_var_dum_det_40o_8e_eps_1e_5 =  [4006538]
shci_var_energy_40o_8e_eps_1e_5 = -13.5193144272 + nuclear_repulsion_energy
shci_var_energy_error_40o_8e_eps_1e_5 = [(shci_var_energy_40o_8e_eps_1e_5 - drmg_energy[0]) * 10**3]

#plt.loglog(sqd_dimensions_list, sqd_errors, label='SQD', marker='o')
#plt.yscale('log')
plt.rcParams.update({'font.size': 32, 'lines.markersize': 18})
plt.rcParams.update({'xtick.labelsize': 32, 'ytick.labelsize': 32, 'xtick.major.size': 8,      # Length of major x ticks
    'xtick.major.width': 2,     # Width of major x ticks
    'xtick.minor.size': 4,      # Length of minor x ticks
    'xtick.minor.width': 1,     # Width of minor x ticks
    'ytick.major.size': 8,      # Length of major y ticks
    'ytick.major.width': 2,     # Width of major y ticks
    'ytick.minor.size': 4,      # Length of minor y ticks
    'ytick.minor.width': 1  })
plt.figure(figsize=(12, 7))  # width=10, height=6 inches
plt.xscale('log')
alpha = 0.5
#plt.figure(figsize=(11, 6))  # width=10, height=6 inches
#plt.loglog(dice_shci_dimensions, dice_shci_energy_errors, label='SHCI (DICE)', marker='x', color='orange')
for n in [0, 1, 2, 3, 4, 5, 6, 7]:
    if n == 0:
        plt.scatter(additional_sqd_dimensions[n], 1000*np.asarray(additional_sqd_energy_errors[n]), label=f"SQD (8e, 30o)", marker='o', color='c', alpha=alpha)
    else:
        plt.scatter(additional_sqd_dimensions[n], 1000*np.asarray(additional_sqd_energy_errors[n]), marker='o', color='c', alpha=alpha)


for n in [0,1,2, 3, 4, 5 ,6 ,7 ,8 ,9]:
    if n == 0:
        plt.scatter(additional_sqd_dimensions_19o[n], 1000*np.asarray(additional_sqd_energy_errors_19o[n]), label=f"SQD (8e, 19o)", marker='o', color='g', alpha=alpha)
    else:
        plt.scatter(additional_sqd_dimensions_19o[n], 1000*np.asarray(additional_sqd_energy_errors_19o[n]), marker='o', color='g', alpha=alpha)

plt.scatter(qbe_fragment_dimension, [1000*qbe_error], label='QBE-SQD', color='red', alpha=alpha)
#plt.scatter(hci_num_dets_40e_4e, [1000*error for error in hci_energy_errors_40e_4e], label='HCI (40o, 4e)', marker='x', color='orange', alpha=alpha)
#plt.scatter(hci_num_dets_30e_4e, [1000*error for error in hci_energy_errors_30e_4e], label='HCI (30o, 4e)', marker='x', color='blue', alpha=alpha)
plt.scatter(hci_num_dets_40e_8e_1e_4, [1000*error for error in hci_energy_errors_40e_8e_1e_4], label='HCI (8e, 40o) $ε_1=10^{-4}$', marker='s', color='crimson', alpha=alpha)
plt.scatter(hci_num_dets_40e_8e_1e_5, [1000*error for error in hci_energy_errors_40e_8e_1e_5], label='HCI (8e, 40o) $ε_1=10^{-5}$', marker='s', color='grey', alpha=alpha)
plt.scatter(hci_num_dets_30e_8e_1e_4, [1000*error for error in hci_energy_errors_30e_8e_1e_4], label='HCI (8e, 30o) $ε_1=10^{-4}$', marker='s', color='blue', alpha=alpha)
plt.scatter(hci_num_dets_30e_8e_1e_5, [1000*error for error in hci_energy_errors_30e_8e_1e_5], label='HCI (8e, 30o) $ε_1=10^{-5}$', marker='s', color='green', alpha=alpha)
plt.scatter(shci_var_dum_det_30o_8e_eps_5e_6, shci_var_energy_error_30o_8e_eps_5e_6, c='navy', label='SHCI (8e, 30o) $ε_1=5\\times 10^{-6}$', marker='^', alpha=alpha)
plt.scatter(shci_var_dum_det_30o_8e_eps_1e_5, shci_var_energy_error_30o_8e_eps_1e_5, c='purple', label='SHCI (8e, 30o) $ε_1=10^{-5}$', marker='^', alpha=alpha)
plt.scatter(shci_var_dum_det_40o_8e_eps_1e_5, shci_var_energy_error_40o_8e_eps_1e_5, c='brown', label='SHCI (8e, 40o) $ε_1=1\\times 10^{-5}$', marker='^', alpha=alpha)
plt.xlabel('Number of Slater determinants')
plt.axhline(y=0, color='k', linestyle='-')
#plt.ylabel('Energy error [mHa]', fontsize=fontsize)
plt.ylabel('E - E$_{\mathrm{DMRG}}$ [mHa]')
#plt.title('Hydrogen ring (H8, cc-pVDZ) SQD vs QBE Energy Error Comparison', fontsize=16)
plt.legend(loc="upper right", fontsize=14)
# add grid
plt.grid()
plt.tight_layout()
plt.savefig('/home/joel/Desktop/numerical_results/QBE_SQD/paper_figures/H8_ring_ccpVDZ_compare_SQD_QBE_SQD_1point3.pdf', dpi=300, bbox_inches='tight')
plt.show()



#plt.figure(figsize=(20, 7))  # width=10, height=6 inches
#plt.rcParams.update({'font.size': 18, 'lines.markersize': 10})
#plt.xscale('log')
#alpha = 0.5
#plt.figure(figsize=(11, 6))  # width=10, height=6 inches
#plt.loglog(dice_shci_dimensions, dice_shci_energy_errors, label='SHCI (DICE)', marker='x', color='orange')
#for n in [0, 1, 2, 3, 4, 5, 6, 7]:
#    if n == 0:
#        plt.scatter(additional_sqd_dimensions[n], 1000*np.asarray(additional_sqd_energy_errors[n]), label=f"SQD (4e, 30o)", marker='o', color='c', alpha=alpha)
#    else:
#        plt.scatter(additional_sqd_dimensions[n], 1000*np.asarray(additional_sqd_energy_errors[n]), marker='o', color='c', alpha=alpha)


#for n in [0,1,2, 3, 4, 5 ,6 ,7 ,8 ,9]:
#    if n == 0:
#        plt.scatter(additional_sqd_dimensions_19o[n], 1000*np.asarray(additional_sqd_energy_errors_19o[n]), label=f"SQD (4e, 19o)", marker='o', color='g', alpha=alpha)
#    else:
#        plt.scatter(additional_sqd_dimensions_19o[n], 1000*np.asarray(additional_sqd_energy_errors_19o[n]), marker='o', color='g', alpha=alpha)

#plt.scatter(qbe_fragment_dimension, [1000*qbe_error], label='QBE-SQD', color='red', alpha=alpha)
#plt.scatter(hci_num_dets_40e_4e, [1000*error for error in hci_energy_errors_40e_4e], label='HCI (40o, 4e)', marker='x', color='orange', alpha=alpha)
#plt.scatter(hci_num_dets_30e_4e, [1000*error for error in hci_energy_errors_30e_4e], label='HCI (30o, 4e)', marker='x', color='blue', alpha=alpha)
#plt.scatter(hci_num_dets_40e_4e_1e_4, [1000*error for error in hci_energy_errors_40e_4e_1e_4], label='HCI (4e, 40o) $ε_1=10^{-4}$', marker='x', color='darkorange', alpha=0.8)
#plt.scatter(hci_num_dets_40e_4e_1e_5, [1000*error for error in hci_energy_errors_40e_4e_1e_5], label='HCI (4e, 40o) $ε_1=10^{-5}$', marker='x', color='tomato', alpha=0.8)
#plt.scatter(shci_var_dum_det_30o_4e_eps_5e_6, shci_var_energy_error_30o_4e_eps_5e_6, c='navy', label='SHCI (4e, 30o) $ε_1=5\\times 10^{-6}$', marker='^', alpha=alpha)
#plt.scatter(shci_var_dum_det_30o_4e_eps_1e_5, shci_var_energy_error_30o_4e_eps_1e_5, c='purple', label='SHCI (4e, 30o) $ε_1=10^{-5}$', marker='^', alpha=alpha)
#plt.scatter(shci_var_dum_det_40o_4e_eps_1e_5, shci_var_energy_error_40o_4e_eps_1e_5, c='brown', label='SHCI (4e, 40o) $ε_1=10^{-5}$', marker='^', alpha=alpha)
#plt.xlabel('Number of Slater determinants')
#plt.axhline(y=0, color='k', linestyle='-')
#plt.ylabel('Energy error [mHa]', fontsize=fontsize)
#plt.ylabel('E - E$_{\mathrm{DMRG}}$ [mHa]')
#plt.title('Hydrogen ring (H8, cc-pVDZ) SQD vs QBE Energy Error Comparison', fontsize=16)
#plt.legend()
# add grid
#plt.grid(axis='y')
#plt.tight_layout()
#plt.savefig('/home/joel/Desktop/numerical_results/QBE_SQD/paper_figures/H8_ring_ccpVDZ_compare_SQD_QBE_SQD_1point3_elongated.pdf', dpi=300, bbox_inches='tight')
#plt.show()