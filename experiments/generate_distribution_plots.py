import matplotlib.pyplot as plt
import numpy as np

idxs = []
with open('../parse_out/parsed_queries.txt', 'r') as f:
    for line in f.readlines():
        if line and len(line.split(':')) > 1:
            idxs.append(int(line.split(':')[0]))

plt.hist(idxs, bins=np.arange(1, 370000, 5000))
# plt.show()
plt.savefig('../parse_out/parsed_queries_dist.png')
plt.clf()

idxs = []
with open('../parse_out/failed_queries.txt', 'r') as f:
    for line in f.readlines():
        idxs.append(int(line.split(' ')[-2]))

plt.hist(idxs, bins=np.arange(1, 370000, 5000))
# plt.show()
plt.savefig('../parse_out/failed_queries_dist.png')
plt.clf()

idxs = []
with open('../parse_out/timeout.txt', 'r') as f:
    for line in f.readlines():
        idxs.append(int(line.split(' ')[-2]))

plt.hist(idxs, bins=np.arange(1, 370000, 5000))
# plt.show()
plt.savefig('../parse_out/timeout_dist.png')
plt.clf()

idxs = []
with open('../parse_out/exceptions.txt', 'r') as f:
    for line in f.readlines():
        idxs.append(int(line.split(' ')[-2]))

plt.hist(idxs, bins=np.arange(1, 370000, 5000))
# plt.show()
plt.savefig('../parse_out/exceptions_dist.png')
plt.clf()
