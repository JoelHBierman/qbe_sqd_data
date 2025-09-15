import numpy as np
import matplotlib.pyplot as plt

######### r = 1.3 Angstroms #########

nuclear_repulsion_energy_1p3 = 9.133975910779744
drmg_energy_1p3 = [-4.385327981507567]
qbe_fragment_dimension_1p3 = [4157521]

additional_sqd_dimensions = []
additional_sqd_energies = []
additional_sqd_energy_errors = []

energies_result_0 = [-13.491714050864568, -13.49627164605883, -13.501033169610743, -13.502640010720425, -13.503853174973523, -13.504038724782141]
energies_result_0 = [energy + nuclear_repulsion_energy_1p3 for energy in energies_result_0]
energies_error_result_0 = [abs(energy - drmg_energy_1p3[0]) for energy in energies_result_0]
dimensions_result_0 = [1249924, 3459600, 8898289, 13616100, 18748900, 23164969]
additional_sqd_dimensions.append(dimensions_result_0)
additional_sqd_energies.append(energies_result_0)
additional_sqd_energy_errors.append(energies_error_result_0)

energies_result_1 = [-13.488881361777954, -13.497164810720058, -13.501581313505298, -13.503189330066357, -13.503723297258757, -13.504109657546703]
energies_result_1 = [energy + nuclear_repulsion_energy_1p3 for energy in energies_result_1]
energies_errors_result_1 = [abs(energy - drmg_energy_1p3[0]) for energy in energies_result_1]
dimensions_result_1 = [1401856, 3728761, 8958049, 13608721, 18826921, 23931664]
additional_sqd_dimensions.append(dimensions_result_1)
additional_sqd_energies.append(energies_result_1)
additional_sqd_energy_errors.append(energies_errors_result_1)

energies_result_2 = [-13.492359396433745, -13.49711596495446, -13.501328577502276, -13.503143969057135, -13.503755331291227, -13.504016252350754]
energies_result_2 = [energy + nuclear_repulsion_energy_1p3 for energy in energies_result_2]
energies_errors_result_2 = [abs(energy - drmg_energy_1p3[0]) for energy in energies_result_2]
dimensions_result_2 = [1430416, 3818116, 9006001, 13793796, 19333609, 23078416]
additional_sqd_dimensions.append(dimensions_result_2)
additional_sqd_energies.append(energies_result_2)
additional_sqd_energy_errors.append(energies_errors_result_2)

energies_result_4 = [-13.492700955449227, -13.49663237834812, -13.501397066993615, -13.503020865832934, -13.503645069722326, -13.503961350305168]
energies_result_4 = [energy + nuclear_repulsion_energy_1p3 for energy in energies_result_4]
energies_errors_result_4 = [abs(energy - drmg_energy_1p3[0]) for energy in energies_result_4]
dimensions_result_4 = [1338649, 3682561, 8561476, 13801225, 18215824, 22953681]
additional_sqd_dimensions.append(dimensions_result_4)
additional_sqd_energies.append(energies_result_4)
additional_sqd_energy_errors.append(energies_errors_result_4)

energies_result_5 = [-13.491046159610544, -13.496536105238967, -13.50104525038684, -13.50278722320673, -13.503623465592348
, -13.503940776352437]
energies_result_5 = [energy + nuclear_repulsion_energy_1p3 for energy in energies_result_5]
energies_errors_result_5 = [abs(energy - drmg_energy_1p3[0]) for energy in energies_result_5]
dimensions_result_5 = [1216609, 3478225, 8625969, 13756681, 18558864, 23261329]
additional_sqd_dimensions.append(dimensions_result_5)
additional_sqd_energies.append(energies_result_5)
additional_sqd_energy_errors.append(energies_errors_result_5)

energies_result_6 = [-13.490392023040176, -13.49589620016494, -13.500675776596253, -13.502657238108124, -13.503453591522518, -13.503987610020742]
energies_result_6 = [energy + nuclear_repulsion_energy_1p3 for energy in energies_result_6]
energies_errors_result_6 = [abs(energy - drmg_energy_1p3[0]) for energy in energies_result_6]
dimensions_result_6 = [1192464, 3448449, 8288641, 13704804, 18550249, 22791076]
additional_sqd_dimensions.append(dimensions_result_6)
additional_sqd_energies.append(energies_result_6)
additional_sqd_energy_errors.append(energies_errors_result_6)

energies_result_8 = [-13.492472193762035, -13.497193157116644, -13.501751826569658, -13.503189099906155, -13.503751336441228, -13.50415067861535]
energies_result_8 = [energy + nuclear_repulsion_energy_1p3 for energy in energies_result_8]
energies_errors_result_8 = [abs(energy - drmg_energy_1p3[0]) for energy in energies_result_8]
dimensions_result_8 = [1498176, 3674889, 9066121, 14167696, 19289664, 23551609]
additional_sqd_dimensions.append(dimensions_result_8)
additional_sqd_energies.append(energies_result_8)
additional_sqd_energy_errors.append(energies_errors_result_8)

energies_result_9 = [-13.490477272541161, -13.496408005593418, -13.500347325228887, -13.502473694097493, -13.503451144484066, -13.503901974515752]
energies_result_9 = [energy + nuclear_repulsion_energy_1p3 for energy in energies_result_9]
energies_errors_result_9 = [abs(energy - drmg_energy_1p3[0]) for energy in energies_result_9]
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
sqd_energies_19o_0 = [energy + nuclear_repulsion_energy_1p3 for energy in sqd_energies_19o_0]
sqd_energy_errors_19o_0 = [abs(energy - drmg_energy_1p3[0]) for energy in sqd_energies_19o_0]
additional_sqd_energies_19o.append(sqd_energies_19o_0)
additional_sqd_energy_errors_19o.append(sqd_energy_errors_19o_0)
additional_sqd_dimensions_19o.append(sqd_dimensions_19o_0)

sqd_energies_19o_1 = [-13.461260410902804, -13.463202363759219, -13.463548505438025, -13.463650630559128, -13.46369304398062, -13.463716300504798]
sqd_dimensions_19o_1 = [966289, 1713481, 2461761, 2805625, 3334276, 3572100]
sqd_energies_19o_1 = [energy + nuclear_repulsion_energy_1p3 for energy in sqd_energies_19o_1]
sqd_energy_errors_19o_1 = [abs(energy - drmg_energy_1p3[0]) for energy in sqd_energies_19o_1]
additional_sqd_energies_19o.append(sqd_energies_19o_1)
additional_sqd_energy_errors_19o.append(sqd_energy_errors_19o_1)
additional_sqd_dimensions_19o.append(sqd_dimensions_19o_1)

sqd_energies_19o_2 = [-13.4616868156378, -13.463329477361064, -13.463595066266967, -13.46365040772688, -13.463707126933189, -13.46372963659289]
sqd_dimensions_19o_2 = [990025, 1760929, 2356225, 2798929, 3258025, 3606201]
sqd_energies_19o_2 = [energy + nuclear_repulsion_energy_1p3 for energy in sqd_energies_19o_2]
sqd_energy_errors_19o_2 = [abs(energy - drmg_energy_1p3[0]) for energy in sqd_energies_19o_2]
additional_sqd_energies_19o.append(sqd_energies_19o_2)
additional_sqd_energy_errors_19o.append(sqd_energy_errors_19o_2)
additional_sqd_dimensions_19o.append(sqd_dimensions_19o_2)

sqd_energies_19o_3 = [-13.461820344163574, -13.46332673510912, -13.463639020382832, -13.463667997822649, -13.463702940059672, -13.463724810359277]
sqd_dimensions_19o_3 = [912025, 1768900, 2319529, 2808976, 3247204, 3508129]
sqd_energies_19o_3 = [energy + nuclear_repulsion_energy_1p3 for energy in sqd_energies_19o_3]
sqd_energy_errors_19o_3 = [abs(energy - drmg_energy_1p3[0]) for energy in sqd_energies_19o_3]
additional_sqd_energies_19o.append(sqd_energies_19o_3)
additional_sqd_energy_errors_19o.append(sqd_energy_errors_19o_3)
additional_sqd_dimensions_19o.append(sqd_dimensions_19o_3)

sqd_energies_19o_4 = [-13.46181321676647, -13.463380405234819, -13.463586534445199, -13.463662044944812, -13.463702215777886, -13.463737393994025]
sqd_dimensions_19o_4 = [952576, 1790244, 2353156, 2842596, 3168400, 3636649]
sqd_energies_19o_4 = [energy + nuclear_repulsion_energy_1p3 for energy in sqd_energies_19o_4]
sqd_energy_errors_19o_4 = [abs(energy - drmg_energy_1p3[0]) for energy in sqd_energies_19o_4]
additional_sqd_energies_19o.append(sqd_energies_19o_4)
additional_sqd_energy_errors_19o.append(sqd_energy_errors_19o_4)
additional_sqd_dimensions_19o.append(sqd_dimensions_19o_4)

sqd_energies_19o_5 = [-13.46212888063303, -13.46311807707955, -13.46352970695461, -13.463667207267152, -13.46367556910303, -13.46372717601834]
sqd_dimensions_19o_5 = [1030225, 1726596, 2377764, 2890000, 3348900, 3794704]
sqd_energies_19o_5 = [energy + nuclear_repulsion_energy_1p3 for energy in sqd_energies_19o_5]
sqd_energy_errors_19o_5 = [abs(energy - drmg_energy_1p3[0]) for energy in sqd_energies_19o_5]
additional_sqd_energies_19o.append(sqd_energies_19o_5)
additional_sqd_energy_errors_19o.append(sqd_energy_errors_19o_5)
additional_sqd_dimensions_19o.append(sqd_dimensions_19o_5)

sqd_energies_19o_6 = [-13.461928822412933, -13.463302330379882, -13.463563267325206, -13.463633949130159, -13.463692598613287, -13.463730144278978]
sqd_dimensions_19o_6 = [968256, 1787569, 2280100, 2782224, 3207681, 3606201]
sqd_energies_19o_6 = [energy + nuclear_repulsion_energy_1p3 for energy in sqd_energies_19o_6]
sqd_energy_errors_19o_6 = [abs(energy - drmg_energy_1p3[0]) for energy in sqd_energies_19o_6]
additional_sqd_energies_19o.append(sqd_energies_19o_6)
additional_sqd_energy_errors_19o.append(sqd_energy_errors_19o_6)
additional_sqd_dimensions_19o.append(sqd_dimensions_19o_6)

sqd_energies_19o_7 = [-13.461693765109963, -13.46319036045498, -13.463567105361246, -13.463672608240566, -13.46369493264944, -13.463729129754409]
sqd_dimensions_19o_7 = [978121, 1803649, 2298256, 2842596, 3196944, 3655744]
sqd_energies_19o_7 = [energy + nuclear_repulsion_energy_1p3 for energy in sqd_energies_19o_7]
sqd_energy_errors_19o_7 = [abs(energy - drmg_energy_1p3[0]) for energy in sqd_energies_19o_7]
additional_sqd_energies_19o.append(sqd_energies_19o_7)
additional_sqd_energy_errors_19o.append(sqd_energy_errors_19o_7)
additional_sqd_dimensions_19o.append(sqd_dimensions_19o_7)

sqd_energies_19o_8 = [-13.461644680016844, -13.463304472584431, -13.463564880198554, -13.463682361130349, -13.463713216783946, -13.463735342380932]
sqd_dimensions_19o_8 = [998001, 1806336, 2337841, 2913849, 3204100, 3629025]
sqd_energies_19o_8 = [energy + nuclear_repulsion_energy_1p3 for energy in sqd_energies_19o_8]
sqd_energy_errors_19o_8 = [abs(energy - drmg_energy_1p3[0]) for energy in sqd_energies_19o_8]
additional_sqd_energies_19o.append(sqd_energies_19o_8)
additional_sqd_energy_errors_19o.append(sqd_energy_errors_19o_8)
additional_sqd_dimensions_19o.append(sqd_dimensions_19o_8)

sqd_energies_19o_9 = [-13.462056723361842, -13.463096397402234, -13.463592863801184, -13.463656615716337, -13.463705945719482, -13.463718325238556]
sqd_dimensions_19o_9 = [929296, 1703025, 2340900, 2775556, 3157729, 3775249]
sqd_energies_19o_9 = [energy + nuclear_repulsion_energy_1p3 for energy in sqd_energies_19o_9]
sqd_energy_errors_19o_9 = [abs(energy - drmg_energy_1p3[0]) for energy in sqd_energies_19o_9]
additional_sqd_energies_19o.append(sqd_energies_19o_9)
additional_sqd_energy_errors_19o.append(sqd_energy_errors_19o_9)
additional_sqd_dimensions_19o.append(sqd_dimensions_19o_9)

#sqd_errors = [abs(sqd_energy - drmg_energy_1p3[0]) for sqd_energy in sqd_energies_list]
qbe_energies_list = [-4.3642546996417915]
qbe_error = abs(qbe_energies_list[0] - drmg_energy_1p3[0])


hci_num_dets_40e_8e_1e_4 = [478390]
hci_energies_40e_8e_1e_4 = [-4.383110393466067]
hci_energy_errors_40e_8e_1e_4 = [abs(hci_energy - drmg_energy_1p3[0]) for hci_energy in hci_energies_40e_8e_1e_4]

hci_num_dets_40e_8e_1e_5 = [5430851]
hci_energies_40e_8e_1e_5 = [-4.385374797500871]
hci_energy_errors_40e_8e_1e_5 = [abs(hci_energy - drmg_energy_1p3[0]) for hci_energy in hci_energies_40e_8e_1e_5]


hci_num_dets_30e_8e_1e_4 = [324020]
hci_energies_30e_8e_1e_4 = [-4.369255274780247]
hci_energy_errors_30e_8e_1e_4 = [abs(hci_energy - drmg_energy_1p3[0]) for hci_energy in hci_energies_30e_8e_1e_4]


hci_num_dets_30e_8e_1e_5 = [2657952]
hci_energies_30e_8e_1e_5 = [-4.370801684350697]
hci_energy_errors_30e_8e_1e_5 = [abs(hci_energy - drmg_energy_1p3[0]) for hci_energy in hci_energies_30e_8e_1e_5]


shci_var_dum_det_30o_8e_eps_5e_6 =  [3101487]
shci_var_energy_30o_8e_eps_5e_6 = -13.50484716 + nuclear_repulsion_energy_1p3
shci_var_energy_error_30o_8e_eps_5e_6 = [(shci_var_energy_30o_8e_eps_5e_6 - drmg_energy_1p3[0]) * 10**3]


shci_var_dum_det_30o_8e_eps_1e_5 =  [1850693]
shci_var_energy_30o_8e_eps_1e_5 = -13.50478101 + nuclear_repulsion_energy_1p3
shci_var_energy_error_30o_8e_eps_1e_5 = [(shci_var_energy_30o_8e_eps_1e_5 - drmg_energy_1p3[0]) * 10**3]

shci_var_dum_det_40o_8e_eps_1e_5 =  [4006538]
shci_var_energy_40o_8e_eps_1e_5 = -13.5193144272 + nuclear_repulsion_energy_1p3
shci_var_energy_error_40o_8e_eps_1e_5 = [(shci_var_energy_40o_8e_eps_1e_5 - drmg_energy_1p3[0]) * 10**3]

#plt.loglog(sqd_dimensions_list, sqd_errors, label='SQD', marker='o')
#plt.yscale('log')
#plt.rcParams.update({'font.size': 32, 'lines.markersize': 18})
#plt.rcParams.update({'xtick.labelsize': 32, 'ytick.labelsize': 32, 'xtick.major.size': 8,      # Length of major x ticks
#    'xtick.major.width': 2,     # Width of major x ticks
#    'xtick.minor.size': 4,      # Length of minor x ticks
#    'xtick.minor.width': 1,     # Width of minor x ticks
#    'ytick.major.size': 8,      # Length of major y ticks
#    'ytick.major.width': 2,     # Width of major y ticks
#    'ytick.minor.size': 4,      # Length of minor y ticks
#    'ytick.minor.width': 1  })
#plt.figure(figsize=(12, 7))  # width=10, height=6 inches
#plt.xscale('log')
#alpha = 0.5
#plt.figure(figsize=(11, 6))  # width=10, height=6 inches
#plt.loglog(dice_shci_dimensions, dice_shci_energy_errors, label='SHCI (DICE)', marker='x', color='orange')
#for n in [0, 1, 2, 3, 4, 5, 6, 7]:
#    if n == 0:
#        plt.scatter(additional_sqd_dimensions[n], 1000*np.asarray(additional_sqd_energy_errors[n]), label=f"SQD (8e, 30o)", marker='o', color='c', alpha=alpha)
#    else:
#        plt.scatter(additional_sqd_dimensions[n], 1000*np.asarray(additional_sqd_energy_errors[n]), marker='o', color='c', alpha=alpha)


#for n in [0,1,2, 3, 4, 5 ,6 ,7 ,8 ,9]:
#    if n == 0:
#        plt.scatter(additional_sqd_dimensions_19o[n], 1000*np.asarray(additional_sqd_energy_errors_19o[n]), label=f"SQD (8e, 19o)", marker='o', color='g', alpha=alpha)
#    else:
#        plt.scatter(additional_sqd_dimensions_19o[n], 1000*np.asarray(additional_sqd_energy_errors_19o[n]), marker='o', color='g', alpha=alpha)

#plt.scatter(qbe_fragment_dimension_1p3, [1000*qbe_error], label='QBE-SQD', color='red', alpha=alpha)
#plt.scatter(hci_num_dets_40e_4e, [1000*error for error in hci_energy_errors_40e_4e], label='HCI (40o, 4e)', marker='x', color='orange', alpha=alpha)
#plt.scatter(hci_num_dets_30e_4e, [1000*error for error in hci_energy_errors_30e_4e], label='HCI (30o, 4e)', marker='x', color='blue', alpha=alpha)
#plt.scatter(hci_num_dets_40e_8e_1e_4, [1000*error for error in hci_energy_errors_40e_8e_1e_4], label='HCI (8e, 40o) $ε_1=10^{-4}$', marker='s', color='crimson', alpha=alpha)
#plt.scatter(hci_num_dets_40e_8e_1e_5, [1000*error for error in hci_energy_errors_40e_8e_1e_5], label='HCI (8e, 40o) $ε_1=10^{-5}$', marker='s', color='grey', alpha=alpha)
#plt.scatter(hci_num_dets_30e_8e_1e_4, [1000*error for error in hci_energy_errors_30e_8e_1e_4], label='HCI (8e, 30o) $ε_1=10^{-4}$', marker='s', color='blue', alpha=alpha)
#plt.scatter(hci_num_dets_30e_8e_1e_5, [1000*error for error in hci_energy_errors_30e_8e_1e_5], label='HCI (8e, 30o) $ε_1=10^{-5}$', marker='s', color='green', alpha=alpha)
#plt.scatter(shci_var_dum_det_30o_8e_eps_5e_6, shci_var_energy_error_30o_8e_eps_5e_6, c='navy', label='SHCI (8e, 30o) $ε_1=5\\times 10^{-6}$', marker='^', alpha=alpha)
#plt.scatter(shci_var_dum_det_30o_8e_eps_1e_5, shci_var_energy_error_30o_8e_eps_1e_5, c='purple', label='SHCI (8e, 30o) $ε_1=10^{-5}$', marker='^', alpha=alpha)
#plt.scatter(shci_var_dum_det_40o_8e_eps_1e_5, shci_var_energy_error_40o_8e_eps_1e_5, c='brown', label='SHCI (8e, 40o) $ε_1=1\\times 10^{-5}$', marker='^', alpha=alpha)
#plt.xlabel('Number of Slater determinants')
#plt.axhline(y=0, color='k', linestyle='-')
#plt.ylabel('Energy error [mHa]', fontsize=fontsize)
#plt.ylabel('E - E$_{\mathrm{DMRG}}$ [mHa]')
#plt.title('Hydrogen ring (H8, cc-pVDZ) SQD vs QBE Energy Error Comparison', fontsize=16)
#plt.legend(loc="upper right", fontsize=14)
# add grid
#plt.grid()
#plt.tight_layout()
#plt.savefig('/home/joel/Desktop/numerical_results/QBE_SQD/paper_figures/H8_ring_ccpVDZ_compare_SQD_QBE_SQD_1point3.pdf', dpi=300, bbox_inches='tight')
#plt.show()



###### r = 1.8 Angstroms ######

fontsize = 16

batch_size_list_1p8 = [500, 1000, 2000, 3000, 4000, 5000]

qbe_sqd_energy_1p8 = -4.267035427832645
qbe_sqd_dimension_1p8 = 3341584 # max value
dmrg_energy_1p8 = -4.302523105341811
nuclear_repulsion_energy_1p8 = 6.596760380007595
qbe_sqd_energy_error_1p8 = (qbe_sqd_energy_1p8 - dmrg_energy_1p8) * 10**3

sqd_energies_1p8 = [[-10.871446260042607, -10.881949112687806, -10.88647274051866, -10.88827320873833, -10.888942605172225, -10.889298787926233],
                [-10.871568868211941, -10.880074012246858, -10.886400266382232, -10.888213556613827, -10.88872740208054, -10.88920620473598],
                [-10.87310579124953, -10.880515678465462, -10.886857643676478, -10.888222668359585, -10.888905193040873, -10.889165762930109]]
sqd_dimensions_1p8 = [[1338649, 3655744, 8614225, 13801225, 18567481, 23902321],
                  [1249924, 3370896, 8323225, 13571856, 18241441, 23319241],
                  [1240996, 3568321, 8708401, 13542400, 18601969, 23068809]]

sqd_energies_1p8 = np.asarray(sqd_energies_1p8).flatten() + nuclear_repulsion_energy_1p8
sqd_energy_errors_1p8 = (sqd_energies_1p8 - dmrg_energy_1p8) * 10**3
sqd_dimensions_1p8 = np.asarray(sqd_dimensions_1p8).flatten()
print(sqd_energies_1p8)

hci_dum_dets_30o_8_e_1e_4_1p8 = [225356]
hci_energies_30o_8e_1e_4_1p8 = [-4.247949410003903]
hci_energy_errors_30o_8e_1e_4_1p8 = [(hci_energy - dmrg_energy_1p8) * 10**3 for hci_energy in hci_energies_30o_8e_1e_4_1p8]

hci_dum_dets_30o_8_e_1e_5_1p8 = [1761714]
hci_energies_30o_8e_1e_5_1p8 = [-4.2509494094366715]
hci_energy_errors_30o_8e_1e_5_1p8 = [(hci_energy - dmrg_energy_1p8) * 10**3 for hci_energy in hci_energies_30o_8e_1e_5_1p8]

hci_dum_dets_40o_8_e_1e_4_1p8 = [333423]
hci_energies_40o_8e_1e_4_1p8 = [-4.256949398691914]
hci_energy_errors_40o_8e_1e_4_1p8 = [(hci_energy - dmrg_energy_1p8) * 10**3 for hci_energy in hci_energies_40o_8e_1e_4_1p8]

hci_dum_dets_40o_8_e_1e_5_1p8 = [3447879]
hci_energies_40o_8e_1e_5_1p8 = [-4.259069204253517]
hci_energy_errors_40o_8e_1e_5_1p8 = [(hci_energy - dmrg_energy_1p8) * 10**3 for hci_energy in hci_energies_40o_8e_1e_5_1p8]

shci_var_dum_det_30o_8e_eps_5e_6_1p8 =  [2842121]
shci_var_energy_30o_8e_eps_5e_6_1p8 = -10.84636042 + nuclear_repulsion_energy_1p8
shci_var_energy_error_30o_8e_eps_5e_6_1p8 = [(shci_var_energy_30o_8e_eps_5e_6_1p8 - dmrg_energy_1p8) * 10**3]


shci_var_dum_det_30o_8e_eps_1e_5_1p8 =  [1618025]
shci_var_energy_30o_8e_eps_1e_5_1p8 = -10.84628940 + nuclear_repulsion_energy_1p8
shci_var_energy_error_30o_8e_eps_1e_5_1p8 = [(shci_var_energy_30o_8e_eps_1e_5_1p8 - dmrg_energy_1p8) * 10**3]

shci_var_dum_det_40o_8e_eps_1e_5_1p8 =  [3509839]
shci_var_energy_40o_8e_eps_1e_5_1p8 = -10.8557952925 + nuclear_repulsion_energy_1p8
shci_var_energy_error_40o_8e_eps_1e_5_1p8 = [(shci_var_energy_40o_8e_eps_1e_5_1p8 - dmrg_energy_1p8) * 10**3]

E_1_dmrg_1p8 = -4.2588094076


alpha = 0.5
#plt.rcParams.update({'font.size': 32, 'lines.markersize': 18})
#plt.rcParams.update({'xtick.labelsize': 32, 'ytick.labelsize': 32, 'xtick.major.size': 8,      # Length of major x ticks
#    'xtick.major.width': 2,     # Width of major x ticks
#    'xtick.minor.size': 4,      # Length of minor x ticks
#    'xtick.minor.width': 1,     # Width of minor x ticks
#    'ytick.major.size': 8,      # Length of major y ticks
#    'ytick.major.width': 2,     # Width of major y ticks
#    'ytick.minor.size': 4,      # Length of minor y ticks
#    'ytick.minor.width': 1  })
#plt.figure(figsize=(12, 8))  # width=10, height=6 inches
#plt.xscale('log')
#plt.scatter(sqd_dimensions_1p8, sqd_energy_errors_1p8, c='cyan', label='SQD (8e,30o)', marker='o', alpha=alpha)
#plt.scatter(qbe_sqd_dimension_1p8, qbe_sqd_energy_error_1p8, c='red', label='QBE-SQD', marker='o', alpha=alpha)
#plt.scatter(hci_dum_dets_40o_8_e_1e_4_1p8, hci_energy_errors_40o_8e_1e_4_1p8, c='crimson', label='HCI (8e,40o) $ε_1=10^{-4}$', marker='s', alpha=alpha)
#plt.scatter(hci_dum_dets_40o_8_e_1e_5_1p8, hci_energy_errors_40o_8e_1e_5_1p8, c='grey', label='HCI (8e,40o) $ε_1=10^{-5}$', marker='s', alpha=alpha)
#plt.scatter(hci_dum_dets_30o_8_e_1e_4_1p8, hci_energy_errors_30o_8e_1e_4_1p8, c='blue', label='HCI (8e,30o) $ε_1=10^{-4}$', marker='s', alpha=alpha)
#plt.scatter(hci_dum_dets_30o_8_e_1e_5_1p8, hci_energy_errors_30o_8e_1e_5_1p8, c='green', label='HCI (8e,30o) $ε_1=10^{-5}$', marker='s', alpha=alpha)
#plt.scatter(shci_var_dum_det_30o_8e_eps_5e_6_1p8, shci_var_energy_error_30o_8e_eps_5e_6_1p8, c='navy', label='SHCI (8e,30o) $ε_1=5\\times 10^{-6}$', marker='^', alpha=alpha)
#plt.scatter(shci_var_dum_det_30o_8e_eps_1e_5_1p8, shci_var_energy_error_30o_8e_eps_1e_5_1p8, c='purple', label='SHCI (8e,30o) $ε_1=10^{-5}$', marker='^', alpha=alpha)
#plt.scatter(shci_var_dum_det_40o_8e_eps_1e_5_1p8, shci_var_energy_error_40o_8e_eps_1e_5_1p8, c='brown', label='SHCI (8e,40o) $ε_1=10^{-5}$', marker='^', alpha=alpha)
#plt.xlabel('Number of Slater determinants')
#plt.ylabel('E - E$_{\mathrm{DMRG}}$ [mHa]', labelpad=15)
#plt.axhline(y=0, color='k', linestyle='-')
#plt.axhline(y=(E_1_dmrg_1p8 - dmrg_energy_1p8) * 10**3, color='gray', linestyle='--', label='$E_1$ DMRG, bond dim. 400')
#plt.title('QBE-SQD vs SQD Energy Error Convergence', fontsize=fontsize)
#plt.legend(fontsize=20)
#plt.grid(which='both', axis='y')
#plt.tight_layout()
#plt.savefig('/home/joel/Desktop/numerical_results/QBE_SQD/paper_figures/H8_ring_ccpVDZ_compare_SQD_QBE_SQD_1point8.pdf', dpi=300, bbox_inches='tight')
#plt.xscale('log')
#plt.show()


####### r = 2.2 Angstroms ########

fontsize = 14

batch_list_2p2 = [0,1,2,3,4,5,6,7,8,9]
batch_size_list_2p2 = [500, 1000, 2000, 3000, 4000, 5000]

qbe_sqd_energy_2p2 = -4.330382461513233
qbe_sqd_dimension_2p2 = 2965284 # max value
dmrg_energy_2p2 = -4.1743049472965215
nuclear_repulsion_energy_2p2 = 5.397349401824396

qbe_sqd_energy_error_2p2 = (qbe_sqd_energy_2p2 - dmrg_energy_2p2) * 10**3

sqd_energies_2p2 = [[-9.547541222266057, -9.559063821139127, -9.563471159112478, -9.564921702082646, -9.565301869629852, -9.56565355378523],
                    [-9.544155735296792, -9.555594976453516, -9.56264994565824, -9.564378859335662, -9.56501350818502, -9.565442956631763],
                    [-9.540916769581134, -9.55683700513421, -9.562848512214298, -9.56387510022844, -9.565141811041837, -9.565337310824365],
                    [-9.542352426344921, -9.556455046928553, -9.562773296382408, -9.564389499908922, -9.56509294966397, -9.565454704262514]]
sqd_dimensions_2p2 = [[1371241, 3459600, 7590025, 11847364, 15547249, 19873764],
                      [1153476, 2992900, 6770404, 11082241, 15000129, 19351201],
                      [1283689, 3052009, 6859161, 10791225, 14969161, 19070689],
                      [1181569, 2866249, 6906384, 10725625, 15288100,18974736]]

sqd_energies_2p2 = np.asarray(sqd_energies_2p2).flatten() + nuclear_repulsion_energy_2p2
sqd_energy_errors_2p2 = (sqd_energies_2p2 - dmrg_energy_2p2) * 10**3
sqd_dimensions_2p2 = np.asarray(sqd_dimensions_2p2).flatten()
print(sqd_energies_2p2)

hci_dum_dets_30o_8_e_1e_4_2p2 = [231707]
hci_energies_30o_8e_1e_4_2p2 = [-4.126733909063901]
hci_energy_errors_30o_8e_1e_4_2p2 = [(hci_energy - dmrg_energy_2p2) * 10**3 for hci_energy in hci_energies_30o_8e_1e_4_2p2]

hci_dum_dets_30o_8_e_1e_5_2p2 = [1695868]
hci_energies_30o_8e_1e_5_2p2 = [-4.1281265733967984]
hci_energy_errors_30o_8e_1e_5_2p2 = [(hci_energy - dmrg_energy_2p2) * 10**3 for hci_energy in hci_energies_30o_8e_1e_5_2p2]

hci_dum_dets_30o_8_e_1e_6_2p2 = [8862493]
hci_energies_30o_8e_1e_6_2p2 = [-4.139549942858453]
hci_energy_errors_30o_8e_1e_6_2p2 = [(hci_energy - dmrg_energy_2p2) * 10**3 for hci_energy in hci_energies_30o_8e_1e_6_2p2]

hci_dum_dets_40o_8_e_1e_4_2p2 = [405184]
hci_energies_40o_8e_1e_4_2p2 = [-4.131462012566635]
hci_energy_errors_40o_8e_1e_4_2p2 = [(hci_energy - dmrg_energy_2p2) * 10**3 for hci_energy in hci_energies_40o_8e_1e_4_2p2]

hci_dum_dets_40o_8_e_1e_5_2p2 = [6111043]
hci_energies_40o_8e_1e_5_2p2 = [-4.174260556148964]
hci_energy_errors_40o_8e_1e_5_2p2 = [(hci_energy - dmrg_energy_2p2) * 10**3 for hci_energy in hci_energies_40o_8e_1e_5_2p2]

shci_var_dum_det_30o_8e_eps_5e_6_2p2 = [3383098]
shci_var_energy_error_30o_8e_eps_5e_6_2p2 = [(-9.5662899523 + nuclear_repulsion_energy_2p2 - dmrg_energy_2p2) * 10**3]

shci_var_dum_det_30o_8e_eps_1e_5_2p2 = [2263228]
shci_var_energy_error_30o_8e_eps_1e_5_2p2 = [(-9.56624272 + nuclear_repulsion_energy_2p2 - dmrg_energy_2p2) * 10**3]

dmrg_e1_2p2 = -4.1334632595
#shci_var_dum_det_40o_4e_eps_1e_5 = []
#shci_var_energy_error_40o_4e_eps_1e_5 = [( + nuclear_repulsion_energy - dmrg_energy) * 10**3]

#alpha = 0.5
#plt.rcParams.update({'font.size': 32, 'lines.markersize': 18})
#plt.rcParams.update({'xtick.labelsize': 32, 'ytick.labelsize': 32, 'xtick.major.size': 8,      # Length of major x ticks
#    'xtick.major.width': 2,     # Width of major x ticks
#    'xtick.minor.size': 4,      # Length of minor x ticks
#    'xtick.minor.width': 1,     # Width of minor x ticks
#    'ytick.major.size': 8,      # Length of major y ticks
#    'ytick.major.width': 2,     # Width of major y ticks
#    'ytick.minor.size': 4,      # Length of minor y ticks
#    'ytick.minor.width': 1  })
#plt.figure(figsize=(12, 7))  # width=10, height=7 inches
#plt.xscale('log')
#plt.scatter(sqd_dimensions_2p2, sqd_energy_errors_2p2, c='c', label='SQD (8e,30o)', marker='o', alpha=alpha)
#plt.scatter(qbe_sqd_dimension_2p2, qbe_sqd_energy_error_2p2, c='r', label='QBE-SQD', marker='o', alpha=alpha)
#plt.scatter(hci_dum_dets_40o_8_e_1e_4_2p2, hci_energy_errors_40o_8e_1e_4_2p2, c='crimson', label='HCI (8e, 40o) $ε_1=10^{-4}$', marker='s', alpha=alpha)
#plt.scatter(hci_dum_dets_40o_8_e_1e_5_2p2, hci_energy_errors_40o_8e_1e_5_2p2, c='grey', label='HCI (8e, 40o) $ε_1=10^{-5}$', marker='s', alpha=alpha)
#plt.scatter(hci_dum_dets_30o_8_e_1e_4_2p2, hci_energy_errors_30o_8e_1e_4_2p2, c='blue', label='HCI (8e, 30o) $ε_1=10^{-4}$', marker='s', alpha=alpha)
#plt.scatter(hci_dum_dets_30o_8_e_1e_5_2p2, hci_energy_errors_30o_8e_1e_5_2p2, c='green', label='HCI (8e, 30o) $ε_1=10^{-5}$', marker='s', alpha=alpha)
#plt.scatter(hci_dum_dets_30o_8_e_1e_6_2p2, hci_energy_errors_30o_8e_1e_6_2p2, c='brown', label='HCI (8e, 30o) $ε_1=10^{-6}$', marker='s', alpha=alpha)
#plt.scatter(shci_var_dum_det_30o_8e_eps_5e_6_2p2, shci_var_energy_error_30o_8e_eps_5e_6_2p2, c='navy', label='SHCI (8e,30o) $ε_1=5\\times 10^{-6}$', marker='^', alpha=alpha)
#plt.scatter(shci_var_dum_det_30o_8e_eps_1e_5_2p2, shci_var_energy_error_30o_8e_eps_1e_5_2p2, c='purple', label='SHCI (8e,30o) $ε_1=10^{-5}$', marker='^', alpha=alpha)
#plt.scatter(shci_var_dum_det_40o_4e_eps_1e_5, shci_var_energy_error_40o_4e_eps_1e_5, c='brown', label='SHCI (40o,4e) $ε_1=1\\times 10^{-5}$', marker='x', alpha=alpha)
#plt.axhline(y=0, color='k', linestyle='-')
#plt.axhline(y=(dmrg_e1_2p2 - dmrg_energy_2p2) * 10**3, color='gray', linestyle='--', label='$E_1$ DMRG, bond dim. 400')
#plt.xlabel('Number of Slater determinants')
#plt.ylabel('E - E$_{\mathrm{DMRG}}$ [mHa]')
#plt.title('QBE-SQD vs SQD Energy Error Convergence', fontsize=fontsize)
#plt.legend(fontsize=20)
#plt.grid(which='both', axis='y')
#plt.tight_layout()
#plt.savefig('/home/joel/Desktop/numerical_results/QBE_SQD/paper_figures/H8_ring_ccpVDZ_compare_SQD_QBE_SQD_2point2.pdf', dpi=300, bbox_inches='tight')
#plt.xscale('log')
#plt.show()


###### 3 stacked plots ######

plt.rcParams.update({'font.size': 24, 'lines.markersize': 14})
plt.rcParams.update({'xtick.labelsize': 24, 'ytick.labelsize': 24, 'xtick.major.size': 8,      # Length of major x ticks
    'xtick.major.width': 2,     # Width of major x ticks
    'xtick.minor.size': 4,      # Length of minor x ticks
    'xtick.minor.width': 1,     # Width of minor x ticks
    'ytick.major.size': 8,      # Length of major y ticks
    'ytick.major.width': 2,     # Width of major y ticks
    'ytick.minor.size': 4,      # Length of minor y ticks
    'ytick.minor.width': 1  })

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 20), sharex=True)

plt.xscale('log')
alpha = 0.5
#plt.figure(figsize=(11, 6))  # width=10, height=6 inches
#plt.loglog(dice_shci_dimensions, dice_shci_energy_errors, label='SHCI (DICE)', marker='x', color='orange')


### ax1
for n in [0, 1, 2, 3, 4, 5, 6, 7]:
    if n == 0:
        ax1.scatter(additional_sqd_dimensions[n], 1000*np.asarray(additional_sqd_energy_errors[n]), label=f"SQD (8e, 30o)", marker='o', color='c', alpha=alpha)
    else:
        ax1.scatter(additional_sqd_dimensions[n], 1000*np.asarray(additional_sqd_energy_errors[n]), marker='o', color='c', alpha=alpha)


for n in [0,1,2, 3, 4, 5 ,6 ,7 ,8 ,9]:
    if n == 0:
        ax1.scatter(additional_sqd_dimensions_19o[n], 1000*np.asarray(additional_sqd_energy_errors_19o[n]), label=f"SQD (8e, 19o)", marker='o', color='mediumpurple', alpha=alpha)
    else:
        ax1.scatter(additional_sqd_dimensions_19o[n], 1000*np.asarray(additional_sqd_energy_errors_19o[n]), marker='o', color='mediumpurple', alpha=alpha)

plt.rcParams.update({'lines.markersize': 24})
ax1.scatter(qbe_fragment_dimension_1p3, [1000*qbe_error], label='QBE-SQD', color='red', alpha=alpha, marker='*')
plt.rcParams.update({'lines.markersize': 14})
#plt.scatter(hci_num_dets_40e_4e, [1000*error for error in hci_energy_errors_40e_4e], label='HCI (40o, 4e)', marker='x', color='orange', alpha=alpha)
#plt.scatter(hci_num_dets_30e_4e, [1000*error for error in hci_energy_errors_30e_4e], label='HCI (30o, 4e)', marker='x', color='blue', alpha=alpha)
ax1.scatter(hci_num_dets_40e_8e_1e_4, [1000*error for error in hci_energy_errors_40e_8e_1e_4], label='HCI (8e, 40o) $ε_1=10^{-4}$', marker='s', color='crimson', alpha=alpha)
ax1.scatter(hci_num_dets_40e_8e_1e_5, [1000*error for error in hci_energy_errors_40e_8e_1e_5], label='HCI (8e, 40o) $ε_1=10^{-5}$', marker='s', color='grey', alpha=alpha)
ax1.scatter(hci_num_dets_30e_8e_1e_4, [1000*error for error in hci_energy_errors_30e_8e_1e_4], label='HCI (8e, 30o) $ε_1=10^{-4}$', marker='s', color='blue', alpha=alpha)
ax1.scatter(hci_num_dets_30e_8e_1e_5, [1000*error for error in hci_energy_errors_30e_8e_1e_5], label='HCI (8e, 30o) $ε_1=10^{-5}$', marker='s', color='darkviolet', alpha=alpha)
ax1.plot([], [], c='brown', label='HCI (8e, 30o) $ε_1=10^{-6}$', marker='s', linestyle='None', alpha=alpha)
ax1.scatter(shci_var_dum_det_30o_8e_eps_5e_6, shci_var_energy_error_30o_8e_eps_5e_6, c='navy', label='SHCI (8e, 30o) $ε_1=5\\times 10^{-6}$', marker='^', alpha=alpha)
ax1.scatter(shci_var_dum_det_30o_8e_eps_1e_5, shci_var_energy_error_30o_8e_eps_1e_5, c='purple', label='SHCI (8e, 30o) $ε_1=10^{-5}$', marker='^', alpha=alpha)
ax1.scatter(shci_var_dum_det_40o_8e_eps_1e_5, shci_var_energy_error_40o_8e_eps_1e_5, c='brown', label='SHCI (8e, 40o) $ε_1=1\\times 10^{-5}$', marker='^', alpha=alpha)
ax1.plot([], [], label='$E_1$ DMRG, bond dim. 400', color='gray', linestyle='--')
#ax1.set_xlabel('Number of Slater determinants')
ax1.axhline(y=0, color='k', linestyle='-')
#ax1.set_ylabel('Energy error [mHa]', fontsize=fontsize)
ax1.set_ylabel('E - E$_{\mathrm{DMRG}}$ [mHa]')
#ax1.set_title('Hydrogen ring (H8, cc-pVDZ) SQD vs QBE Energy Error Comparison', fontsize=16)
#ax1.legend(loc="upper right", fontsize=14)
ax1.grid(which='both', axis='y')
ax1.set_title('r = 1.3 Å', fontsize=20, pad=10)


### ax2

ax2.scatter(sqd_dimensions_1p8, sqd_energy_errors_1p8, c='cyan', marker='o', alpha=alpha) # label='SQD (8e,30o)'
plt.rcParams.update({'lines.markersize': 24})
ax2.scatter(qbe_sqd_dimension_1p8, qbe_sqd_energy_error_1p8, c='red', marker='*', alpha=alpha) # label='QBE-SQD'
plt.rcParams.update({'lines.markersize': 14})
ax2.scatter(hci_dum_dets_40o_8_e_1e_4_1p8, hci_energy_errors_40o_8e_1e_4_1p8, c='crimson', marker='s', alpha=alpha) # label='HCI (8e,40o) $ε_1=10^{-4}$'
ax2.scatter(hci_dum_dets_40o_8_e_1e_5_1p8, hci_energy_errors_40o_8e_1e_5_1p8, c='grey', marker='s', alpha=alpha) # label='HCI (8e,40o) $ε_1=10^{-5}$'
ax2.scatter(hci_dum_dets_30o_8_e_1e_4_1p8, hci_energy_errors_30o_8e_1e_4_1p8, c='blue', marker='s', alpha=alpha) # label='HCI (8e,30o) $ε_1=10^{-4}$'
ax2.scatter(hci_dum_dets_30o_8_e_1e_5_1p8, hci_energy_errors_30o_8e_1e_5_1p8, c='darkviolet', marker='s', alpha=alpha) # label='HCI (8e,30o) $ε_1=10^{-5}$'
ax2.scatter(shci_var_dum_det_30o_8e_eps_5e_6_1p8, shci_var_energy_error_30o_8e_eps_5e_6_1p8, c='navy', marker='^', alpha=alpha) # label='SHCI (8e,30o) $ε_1=5\\times 10^{-6}$'
ax2.scatter(shci_var_dum_det_30o_8e_eps_1e_5_1p8, shci_var_energy_error_30o_8e_eps_1e_5_1p8, c='purple', marker='^', alpha=alpha) # label='SHCI (8e,30o) $ε_1=10^{-5}$'
ax2.scatter(shci_var_dum_det_40o_8e_eps_1e_5_1p8, shci_var_energy_error_40o_8e_eps_1e_5_1p8, c='brown', marker='^', alpha=alpha) # label='SHCI (8e,40o) $ε_1=10^{-5}$'
#ax2.xlabel('Number of Slater determinants')
ax2.set_ylabel('E - E$_{\mathrm{DMRG}}$ [mHa]', labelpad=15)
ax2.axhline(y=0, color='k', linestyle='-')
ax2.axhline(y=(E_1_dmrg_1p8 - dmrg_energy_1p8) * 10**3, color='gray', linestyle='--') # label='$E_1$ DMRG, bond dim. 400'
#ax2.set_title('QBE-SQD vs SQD Energy Error Convergence', fontsize=fontsize)
#ax2.legend(fontsize=20)
ax2.grid(which='both', axis='y')
ax2.set_title('r = 1.8 Å', fontsize = 20, pad=10)
#ax2.tight_layout()
#x2.savefig('/home/joel/Desktop/numerical_results/QBE_SQD/paper_figures/H8_ring_ccpVDZ_compare_SQD_QBE_SQD_1point8.pdf', dpi=300, bbox_inches='tight')
#ax2.xscale('log')
#.show()

### ax3

ax3.scatter(sqd_dimensions_2p2, sqd_energy_errors_2p2, c='c', marker='o', alpha=alpha) # label='SQD (8e,30o)'
plt.rcParams.update({'lines.markersize': 24})
ax3.scatter(qbe_sqd_dimension_2p2, qbe_sqd_energy_error_2p2, c='r', marker='*', alpha=alpha) # label='QBE-SQD'
plt.rcParams.update({'lines.markersize': 14})
ax3.scatter(hci_dum_dets_40o_8_e_1e_4_2p2, hci_energy_errors_40o_8e_1e_4_2p2, c='crimson', marker='s', alpha=alpha) # label='HCI (8e, 40o) $ε_1=10^{-4}$'
ax3.scatter(hci_dum_dets_40o_8_e_1e_5_2p2, hci_energy_errors_40o_8e_1e_5_2p2, c='grey', marker='s', alpha=alpha) # label='HCI (8e, 40o) $ε_1=10^{-5}$'
ax3.scatter(hci_dum_dets_30o_8_e_1e_4_2p2, hci_energy_errors_30o_8e_1e_4_2p2, c='blue', marker='s', alpha=alpha) # label='HCI (8e, 30o) $ε_1=10^{-4}$'
ax3.scatter(hci_dum_dets_30o_8_e_1e_5_2p2, hci_energy_errors_30o_8e_1e_5_2p2, c='darkviolet', marker='s', alpha=alpha) # label='HCI (8e, 30o) $ε_1=10^{-5}$'
ax3.scatter(hci_dum_dets_30o_8_e_1e_6_2p2, hci_energy_errors_30o_8e_1e_6_2p2, c='brown', marker='s', alpha=alpha) # label='HCI (8e, 30o) $ε_1=10^{-6}$'
ax3.scatter(shci_var_dum_det_30o_8e_eps_5e_6_2p2, shci_var_energy_error_30o_8e_eps_5e_6_2p2, c='navy', marker='^', alpha=alpha) # label='SHCI (8e,30o) $ε_1=5\\times 10^{-6}$'
ax3.scatter(shci_var_dum_det_30o_8e_eps_1e_5_2p2, shci_var_energy_error_30o_8e_eps_1e_5_2p2, c='purple', marker='^', alpha=alpha) # label='SHCI (8e,30o) $ε_1=10^{-5}$'
#plt.scatter(shci_var_dum_det_40o_4e_eps_1e_5, shci_var_energy_error_40o_4e_eps_1e_5, c='brown', label='SHCI (40o,4e) $ε_1=1\\times 10^{-5}$', marker='x', alpha=alpha)
ax3.axhline(y=0, color='k', linestyle='-')
ax3.axhline(y=(dmrg_e1_2p2 - dmrg_energy_2p2) * 10**3, color='gray', linestyle='--', label='$E_1$ DMRG, bond dim. 400')
ax3.set_xlabel('Number of Slater determinants')
ax3.set_ylabel('E - E$_{\mathrm{DMRG}}$ [mHa]')
ax3.grid(which='both', axis='y')
ax3.set_title('r = 2.2 Å', fontsize=20, pad=10)

handles, labels = ax1.get_legend_handles_labels()
fig.legend(handles, labels, loc='center', bbox_to_anchor=(0.55, 0.95), 
           ncol=2, fontsize=20, frameon=True)

# Adjust spacing more aggressively
#plt.tight_layout()
#plt.subplots_adjust(top=0.88, bottom=0.08) 

#plt.grid()
#plt.tight_layout()
plt.tight_layout()
plt.subplots_adjust(top=0.85)  # Make room for legend
plt.savefig('/home/joel/Desktop/numerical_results/QBE_SQD/paper_figures/H8_ring_ccpVDZ_compare_SQD_QBE_SQD_3in1.pdf', dpi=300, bbox_inches='tight')
plt.show()