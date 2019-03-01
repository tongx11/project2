import matplotlib.pyplot as plt

b1 = [1.4220562499999998, 1.23943689, 0.8937811600000001, 0.85988529, 0.84842521, 0.8328387599999999, 0.8366760899999999, 0.8723560000000001, 0.9785166399999999]
b2 = [1.44072009, 1.2719328399999998, 0.94031809, 0.90725625, 0.89038096, 0.8866105599999999, 0.898704, 0.9649132899999999, 2.19662041]
a = [0.001, 0.01, 0.06, 0.08, 0.1, 0.12, 0.14, 0.2, 1]
b1 = [x/2.0 for x in b1]
b2 = [x/2.0 for x in b2]
one, = plt.plot(a,b1,'r-',label='biased')
two, = plt.plot(a,b2,'b-',label='unbiased')
plt.legend([one, two], ['biased', 'unbiased'])
plt.xlabel('lambda')
plt.ylabel('Eout')
plt.legend()
plt.savefig('off-shelf-error', dpi = 600)
plt.show()
