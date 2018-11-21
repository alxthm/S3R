from numpy import int32
from numpy.ma import array, masked_array

results = {'mean_fit_time': array([211.60588193, 215.59488042, 188.31423402, 184.80423307,
                                   244.09419195, 184.58076668, 181.69795291, 189.89488395,
                                   192.48143522, 216.42579246]),
           'std_fit_time': array([5.85185124, 4.67121916, 3.21217949, 1.36224715, 5.98574791,
                                  12.58655982, 4.36248341, 4.01766763, 2.16219025, 17.29793794]),
           'mean_score_time': array([0.27007699, 0.21061222, 0.22768005, 0.22479558, 0.21906694,
                                     0.25305041, 0.20462584, 0.22775698, 0.20316021, 0.21594071]),
           'std_score_time': array([0.03418748, 0.01318435, 0.03707464, 0.00549991, 0.00251312,
                                    0.04268225, 0.00282426, 0.00422646, 0.00403452, 0.0020014]),
           'param_module__activation_fct': masked_array(data=['swish', 'relu', 'prelu', 'prelu', 'relu', 'prelu',
                                                              'prelu', 'prelu', 'relu', 'swish'],
                                                        mask=[False, False, False, False, False, False, False, False,
                                                              False, False],
                                                        fill_value='?',
                                                        dtype=object),
           'param_max_epochs': masked_array(data=[200, 200, 200, 200, 200, 200, 200,
                                                  200, 200, 200],
                                            mask=[False, False, False,
                                                  False, False, False,
                                                  False, False,
                                                  False, False],
                                            fill_value='?',
                                            dtype=object),
           'param_lr': masked_array(data=[0.0001, 0.01, 0.01, 0.0001, 0.001, 0.001, 0.001, 0.01,
                                          0.001, 0.01],
                                    mask=[False, False, False, False, False, False, False, False,
                                          False, False],
                                    fill_value='?',
                                    dtype=object),
           'param_batch_size': masked_array(data=[32, 64, 64, 32, 32, 32, 64, 32, 64, 64],
                                            mask=[False, False, False, False, False,
                                                  False, False, False,
                                                  False, False],
                                            fill_value='?',
                                            dtype=object),
           'params': [{'module__activation_fct': 'swish', 'max_epochs': 200, 'lr': 0.0001, 'batch_size': 32},
                      {'module__activation_fct': 'relu', 'max_epochs': 200, 'lr': 0.01, 'batch_size': 64},
                      {'module__activation_fct': 'prelu', 'max_epochs': 200, 'lr': 0.01, 'batch_size': 64},
                      {'module__activation_fct': 'prelu', 'max_epochs': 200, 'lr': 0.0001, 'batch_size': 32},
                      {'module__activation_fct': 'relu', 'max_epochs': 200, 'lr': 0.001, 'batch_size': 32},
                      {'module__activation_fct': 'prelu', 'max_epochs': 200, 'lr': 0.001, 'batch_size': 32},
                      {'module__activation_fct': 'prelu', 'max_epochs': 200, 'lr': 0.001, 'batch_size': 64},
                      {'module__activation_fct': 'prelu', 'max_epochs': 200, 'lr': 0.01, 'batch_size': 32},
                      {'module__activation_fct': 'relu', 'max_epochs': 200, 'lr': 0.001, 'batch_size': 64},
                      {'module__activation_fct': 'swish', 'max_epochs': 200, 'lr': 0.01, 'batch_size': 64}],
           'split0_test_score': array([0.75688073, 0.80275229, 0.87003058, 0.8470948, 0.84556575,
                                       0.87461774, 0.86697248, 0.77675841, 0.84862385, 0.882263]),
           'split1_test_score': array([0.81470138, 0.83001531, 0.88667688, 0.81163859, 0.87442573,
                                       0.88973966, 0.88820827, 0.77488515, 0.85451761, 0.90199081]),
           'split2_test_score': array([0.80091884, 0.77947933, 0.84839204, 0.85145482, 0.83154671,
                                       0.87595712, 0.8805513, 0.81929556, 0.82082695, 0.86370597]),
           'mean_test_score': array([0.79081633, 0.80408163, 0.86836735, 0.83673469, 0.8505102,
                                     0.88010204, 0.87857143, 0.79030612, 0.84132653, 0.88265306]),
           'std_test_score': array([0.0246645, 0.02064741, 0.01567, 0.01782794, 0.01784716,
                                    0.00683414, 0.00878279, 0.02050505, 0.01468831, 0.01562817]),
           'rank_test_score': array([9, 8, 4, 7, 5, 2, 3, 10, 6, 1], dtype=int32),
           'split0_train_score': array([0.82695253, 0.9042879, 0.97779479, 0.91883614, 0.97090352,
                                        0.97932619, 0.98545176, 0.79862175, 0.97320061, 0.97856049]),
           'split1_train_score': array([0.86381025, 0.88446825, 0.97245601, 0.86993114, 0.97016067,
                                        0.97092578, 0.97092578, 0.90283091, 0.96557001, 0.979342]),
           'split2_train_score': array([0.8599847, 0.84468248, 0.97016067, 0.91277735, 0.93955624,
                                        0.96863045, 0.97092578, 0.94261668, 0.93496557, 0.9716909]),
           'mean_train_score': array([0.85024916, 0.87781288, 0.97347049, 0.90051488, 0.96020681,
                                      0.97296081, 0.97576778, 0.88135645, 0.95791206, 0.97653113]),
           'std_train_score': array([0.01654707, 0.0247847, 0.00319811, 0.02176696, 0.01460531,
                                     0.00459751, 0.00684761, 0.06071518, 0.01652196,
                                     0.0034374])
           }