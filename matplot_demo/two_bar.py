import matplotlib.pyplot as plt
import numpy as np

data_2 = [93, 92, 93, 91, 92, 93]

data_3 = [57, 56, 57, 56, 56., 54]

labels = ['HL', 'ED', 'HD_2', 'HD_all', 'Voting', 'ME']

fig, ax = plt.subplots(figsize=(9, 6), dpi=300)
width_1 = 0.4

ax.bar(np.arange(len(data_2)), data_2, width=width_1, tick_label=labels, color='b', label="UCI")

ax.bar(np.arange(len(data_3)) + width_1, data_3, width=width_1, tick_label=labels, color='r', label="Opportunity")

ax.set_ylim([55, 94])

plt.ylabel('%')

ax.legend()

plt.tight_layout()
plt.show()
