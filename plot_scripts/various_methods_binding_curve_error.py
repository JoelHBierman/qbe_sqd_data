import numpy as np
import matplotlib.pyplot as plt

fontsize = 14
radius_list = [1.3, 1.8, 2.2]
nuclear_repulsions = [9.133975910779744, 6.596760380007595, 5.397349401824396]

dmrg_energies = [-4.385327981507567, -4.302523105341811, -4.1743049472965215]
qbe_sqd_energies = [-4.3642546996417915, -4.267035427832645, -4.330382461513233]
sqd_energies_30o_batch_500 = [[-13.491714050864568, -13.488881361777954, -13.492359396433745, -13.492700955449227, -13.491046159610544, -13.490392023040176, -13.492472193762035, -13.490477272541161],
                               [-10.871446260042607, -10.871568868211941, -10.87310579124953],
                               [-9.547541222266057, -9.544155735296792, -9.540916769581134, -9.542352426344921]]
sqd_energies_30o_batch_1000 = [[-13.49627164605883, -13.497164810720058, -13.49711596495446, -13.49663237834812, -13.496536105238967, -13.49589620016494, -13.497193157116644, -13.496408005593418],
                               [-10.881949112687806, -10.880074012246858, -10.880515678465462],
                               [-9.559063821139127, -9.555594976453516, -9.55683700513421, -9.556455046928553]]
sqd_energies_30o_batch_2000 = [[-13.501033169610743, -13.501581313505298, -13.501328577502276, -13.501397066993615, -13.50104525038684, -13.500675776596253, -13.501751826569658, -13.500347325228887],
                               [-10.88647274051866, -10.886400266382232, -10.886857643676478],
                               [-9.563471159112478, -9.56264994565824, -9.562848512214298, -9.562773296382408]]
sqd_energies_30o_batch_3000 = [[-13.502640010720425, -13.503189330066357, -13.503143969057135, -13.503020865832934, -13.50278722320673, -13.502657238108124, -13.503189099906155, -13.502473694097493],
                               [-10.88827320873833, -10.888213556613827, -10.888222668359585],
                               [-9.564921702082646, -9.564378859335662, -9.56387510022844, -9.564389499908922]]
sqd_energies_30o_batch_4000 = [[-13.503853174973523, -13.503723297258757, -13.503755331291227, -13.503645069722326, -13.503623465592348, -13.503453591522518, -13.503751336441228, -13.503451144484066],
                               [-10.888942605172225, -10.88872740208054, -10.888905193040873],
                               [-9.565301869629852, -9.56501350818502, -9.565141811041837, -9.56509294966397]]
sqd_energies_30o_batch_5000 = [[-13.504038724782141, -13.504109657546703, -13.504016252350754, -13.503961350305168, -13.503940776352437, -13.503987610020742, -13.50415067861535, -13.503901974515752],
                               [-10.889298787926233, -10.88920620473598, -10.889165762930109],
                               [-9.56565355378523, -9.565442956631763, -9.565337310824365, -9.565454704262514]]

sqd_energies_30o_batch_500_errors = [(np.asarray(energies) + nuclear_repulsions[i] - dmrg_energies[i])*1000 for i, energies in enumerate(sqd_energies_30o_batch_500)]
sqd_energies_30o_batch_1000_errors = [(np.asarray(energies) + nuclear_repulsions[i] - dmrg_energies[i])*1000 for i, energies in enumerate(sqd_energies_30o_batch_1000)]
sqd_energies_30o_batch_2000_errors = [(np.asarray(energies) + nuclear_repulsions[i] - dmrg_energies[i])*1000 for i, energies in enumerate(sqd_energies_30o_batch_2000)]
sqd_energies_30o_batch_3000_errors = [(np.asarray(energies) + nuclear_repulsions[i] - dmrg_energies[i])*1000 for i, energies in enumerate(sqd_energies_30o_batch_3000)]
sqd_energies_30o_batch_4000_errors = [(np.asarray(energies) + nuclear_repulsions[i] - dmrg_energies[i])*1000 for i, energies in enumerate(sqd_energies_30o_batch_4000)]
sqd_energies_30o_batch_5000_errors = [(np.asarray(energies) + nuclear_repulsions[i] - dmrg_energies[i])*1000 for i, energies in enumerate(sqd_energies_30o_batch_5000)]

sqd_energies_30o_batch_500_mean_errors = [np.mean(errors) for errors in sqd_energies_30o_batch_500_errors]
sqd_energies_30o_batch_1000_mean_errors = [np.mean(errors) for errors in sqd_energies_30o_batch_1000_errors]
sqd_energies_30o_batch_2000_mean_errors = [np.mean(errors) for errors in sqd_energies_30o_batch_2000_errors]
sqd_energies_30o_batch_3000_mean_errors = [np.mean(errors) for errors in sqd_energies_30o_batch_3000_errors]
sqd_energies_30o_batch_4000_mean_errors = [np.mean(errors) for errors in sqd_energies_30o_batch_4000_errors]
sqd_energies_30o_batch_5000_mean_errors = [np.mean(errors) for errors in sqd_energies_30o_batch_5000_errors]

sqd_energies_30o_batch_500_std_errors = [np.std(errors)/np.sqrt(len(errors)) for errors in sqd_energies_30o_batch_500_errors]
sqd_energies_30o_batch_1000_std_errors = [np.std(errors)/np.sqrt(len(errors)) for errors in sqd_energies_30o_batch_1000_errors]
sqd_energies_30o_batch_2000_std_errors = [np.std(errors)/np.sqrt(len(errors)) for errors in sqd_energies_30o_batch_2000_errors]
sqd_energies_30o_batch_3000_std_errors = [np.std(errors)/np.sqrt(len(errors)) for errors in sqd_energies_30o_batch_3000_errors]
sqd_energies_30o_batch_4000_std_errors = [np.std(errors)/np.sqrt(len(errors)) for errors in sqd_energies_30o_batch_4000_errors]
sqd_energies_30o_batch_5000_std_errors = [np.std(errors)/np.sqrt(len(errors)) for errors in sqd_energies_30o_batch_5000_errors]

hci_30o_epsilon_1e_4 = [-4.369255274780247, -4.247949410003903, -4.126733909063901]
hci_30o_epsilon_1e_5 = [-4.370801684350697, -4.2509494094366715, -4.1281265733967984]
#hci_30o_epsilon_1e_6 = []

hci_40o_epsilon_1e_4 = [-4.383110393466067, -4.256949398691914, -4.131462012566635]
hci_40o_epsilon_1e_5 = [-4.385374797500871, -4.259069204253517, -4.174260556148964]
#hci_40o_epsilon_1e_6 = []

hci_30o_epsilon_1e_4_errors = [abs(energy - dmrg_energies[i])*1000 for i, energy in enumerate(hci_30o_epsilon_1e_4)]
hci_30o_epsilon_1e_5_errors = [abs(energy - dmrg_energies[i])*1000 for i, energy in enumerate(hci_30o_epsilon_1e_5)]
#hci_30o_epsilon_1e_6_errors = [abs(energy - dmrg_energies[i])*1000 for i, energy in enumerate(hci_30o_epsilon_1e_6)]

qbe_fci_energies = [-4.364278473647456, -4.269225767506505, -4.324342527739505]

# plot averages with error bars
plt.figure(figsize=(11, 6))  # width=10, height=6 inches
plt.yscale('log')
alpha = 1
linestyle = '--'
plt.errorbar(radius_list, sqd_energies_30o_batch_500_mean_errors, yerr=sqd_energies_30o_batch_500_std_errors, label='SQD (30o,4e) batch size 500', marker='o', color='cyan', alpha=alpha, linestyle=linestyle)
plt.errorbar(radius_list, sqd_energies_30o_batch_1000_mean_errors, yerr=sqd_energies_30o_batch_1000_std_errors, label='SQD (30o,4e) batch size 1000', marker='o', color='blue', alpha=alpha, linestyle=linestyle)
plt.errorbar(radius_list, sqd_energies_30o_batch_2000_mean_errors, yerr=sqd_energies_30o_batch_2000_std_errors, label='SQD (30o,4e) batch size 2000', marker='o', color='green', alpha=alpha, linestyle=linestyle)
plt.errorbar(radius_list, sqd_energies_30o_batch_3000_mean_errors, yerr=sqd_energies_30o_batch_3000_std_errors, label='SQD (30o,4e) batch size 3000', marker='o', color='orange', alpha=alpha, linestyle=linestyle)
plt.errorbar(radius_list, sqd_energies_30o_batch_4000_mean_errors, yerr=sqd_energies_30o_batch_4000_std_errors, label='SQD (30o,4e) batch size 4000', marker='o', color='red', alpha=alpha, linestyle=linestyle)
plt.errorbar(radius_list, sqd_energies_30o_batch_5000_mean_errors, yerr=sqd_energies_30o_batch_5000_std_errors, label='SQD (30o,4e) batch size 5000', marker='o', color='purple', alpha=alpha, linestyle=linestyle)
plt.plot(radius_list, np.abs((np.asarray(qbe_sqd_energies) - np.asarray(dmrg_energies))*1000), label='QBE-SQD', marker='o', color='black', alpha=alpha, linestyle=linestyle)
plt.plot(radius_list, np.abs((np.asarray(qbe_fci_energies) - np.asarray(dmrg_energies))*1000), label='QBE-FCI', marker='x', color='gray', alpha=alpha, linestyle=linestyle)
plt.plot(radius_list, hci_30o_epsilon_1e_4_errors, label='HCI (30o,4e) $ε=10^{-4}$', marker='x', color='brown', alpha=alpha, linestyle=linestyle)
plt.plot(radius_list, hci_30o_epsilon_1e_5_errors, label='HCI (30o,4e) $ε=10^{-5}$', marker='x', color='magenta', alpha=alpha, linestyle=linestyle)
#plt.plot(radius_list, hci_
plt.axhline(y=0, color='k', linestyle='-')
plt.xlabel('Ring radius [Angstrom]', fontsize=fontsize)
plt.ylabel('|E - E$_{\mathrm{DMRG}}|$ [mHa]', fontsize=fontsize)
#plt.title('H8 ring (cc-pVDZ) SQD vs QBE-SQD Energy Error Comparison', fontsize=fontsize)
plt.legend(fontsize=12, ncol=3)
plt.grid(which='both', axis='y')
plt.xticks(radius_list)
plt.tight_layout()
plt.show()