import numpy as np
import matplotlib.pyplot as plt

values = [1000000, 1525097, 2050194, 1095638, 1620736, 2145833, 1191277, 1716375, 1286916, 1382555]
strategy = [1,2,3,4,5,6,7,8,9,10]
value = np.array(values)
strategies = np.array(strategy)
plt.bar(strategy, values, .8)
plt.ylabel("Values")
plt.xlabel("Bin Number")
plt.title("Histogram")
plt.axis([1,11,0,2200000])
plt.show()
