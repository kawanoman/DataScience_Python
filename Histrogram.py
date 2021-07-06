# library
import matplotlib.pyplot as plt
# create random data
names = 'groupA', 'groupB', 'groupC', 'groupD',
values = [12, 11, 3, 30]
# Label distance: gives the space between labels and the center of the pie
plt.pie(values, labels=names, labeldistance=1.15);
plt.show();
