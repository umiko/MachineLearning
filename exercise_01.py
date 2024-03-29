import numpy as np

traind, testd, trainl, testl = np.load(open("mnist.npz", "rb")).values()
# a)
print("Number of samples: " + str(traind.shape[0]))
print("Numbers per sample: " + str(traind.shape[1] * traind.shape[2]))
print("One hot indexing")
# b)
print("Sample 1000 is a " + str(np.argmax(trainl[1000])))
# c)
print(
    "Lowest: "
    + str(np.min(np.argmin(trainl, axis=1)))
    + " Highest: "
    + str(np.max(np.argmax(trainl, axis=1)))
)
# d)
mask = trainl[:, 5] == 1
print("Number of 5s: " + str(np.sum(mask)))
# e)
print("Smallest pixel value: " + str(np.min(traind[10])))
print("Greatest pixel value: " + str(np.max(traind[10])))
# f)
print("Every second row:")
print(traind[10, ::2, :])
print("Every second column:")
print(traind[10, :, ::2])
print("Reversed:")
print(traind[10, ::-1, ::-1])
print("Top 10 Columns All zeros:")
traind[10, 0:10, :] = 0
print(traind[10, 0:10, :])
print("Bottom 10 Columns All zeros:")
traind[10, 0:-10, :] = 0
print(traind[10, 0:-10, :])
print("Weird invert:")
print(traind[10, ::-2, ::-2])
# g)
print("All samples of class 4:")
mask = trainl[:, 4] == 1
print(traind[mask])
print("Samples: " + str(traind[mask].shape[0]))
print("Labels classed 4: " + str(np.sum(mask)))
# h)
print("All samples of class 4 or 9:")
mask = (trainl[:, 4] == 1) + (trainl[:, 9] == 1)
print(traind[mask])
print("Samples: " + str(traind[mask].shape[0]))
print("Labels classed 4 or 9: " + str(np.sum(mask)))
# i)
print("Copy out the first 10k samples:")
first10kd = traind[0:10000]
first10kl = trainl[0:10000]
# j)
print("Apply 1-x to all samples:")
inverse = np.ones(traind.shape) - traind
print(inverse)
# k)
print("copy out 1000 random samples:")
copyout = traind[np.random.randint(0, traind.shape[0], 1000)]
print(copyout)
