import os
import params

seed = params.seed
odir = params.odir
methods = params.methods

for method in methods:
    for dkey in params.datasets.keys():
        for train_size in params.datasets[dkey]['train_sizes']:
            for key in params.parameters:
                print("Processing method %s with data set %s, train_size %s, and key %s ..." % (str(method), str(dkey), str(train_size), str(key)))
                cmd = "python " + method + ".py --dkey %s --train_size %i --key %s" % (dkey, train_size, key)
                print(cmd)
                os.system(cmd)