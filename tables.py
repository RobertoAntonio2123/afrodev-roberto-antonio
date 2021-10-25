import pandas as pd
import matplotlib.pyplot as plt
dt = pd.read_excel('data/popularsports.xlsx')
y  = dt['Male']
x1 = dt['initials']
x  = dt['Male']

#plt.plot(x1, x, label='feminino')

plt.title("Quantidade De Atletas Em Cada Modalidade  ")
plt.plot(x1, y,  label='(a) Athletics\n''(b) Basketball\n''(c) Football\n''(d) Judo\n'
         '(e) Rowing\n''(f)  Rugby Sevens\n''(g) Sailing\n''(h) Shooting\n''(i)  Swimming\n')
plt.legend()
plt.show()
