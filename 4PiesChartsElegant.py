import matplotlib.pyplot as plt
plt.style.use('ggplot')

fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2, figsize=(11,10))

labels1 = ('new', 'closed', 'developing', 'testing', 'tbd')
labels2 = ('Intern', 'Kunde')
labels3 = ('HW', 'SW')
labels4 = ('Closed', 'Open')

sizes1 = [1, 2, 3, 4, 5]
sizes2 = [1,2]
sizes3 = [1,2]
sizes4 = [1,2]

colors1 = ['#F5FC34', '#52FC34', '#FAAB23', '#237DFA', '#C863FA', ]
colors2 = ['#FAF063', '#63BBFA']
colors3 = ['#6A0D7D', '#503C3C']
colors4 = ['#58FB4C', '#F8183A']

explode1 = (0, 0, 0, 0, 0)
explode2 = (0, 0)
explode3 = (0, 0)
explode4 = (0, 0)

ax1.pie(sizes1, explode=explode1, colors=colors1, autopct='%1.1f%%',shadow=True, startangle=90)
ax2.pie(sizes2, explode=explode2, colors=colors2, autopct='%1.1f%%',shadow=True, startangle=90)
ax3.pie(sizes3, explode=explode3, colors=colors3, autopct='%1.1f%%',shadow=True, startangle=90)
ax4.pie(sizes4, explode=explode4, colors=colors4, autopct='%1.1f%%',shadow=True, startangle=90)

ax1.set_title("Status")
ax2.set_title("Department")
ax3.set_title("Origin")
ax4.set_title("Closed-Status")

ax1.legend(labels1, bbox_to_anchor=(0.05, 0.8))
ax2.legend(labels2, bbox_to_anchor=(1.25, 0.65))
ax3.legend(labels3, bbox_to_anchor=(0, 0.6))
ax4.legend(labels4, bbox_to_anchor=(1.25, 0.65))

plt.show()

fig.savefig('/Users/kawanoman/Desktop/test.png', bbox_inches="tight")
