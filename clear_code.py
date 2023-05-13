import matplotlib.pyplot as plt 
import numpy as np 

company_names = ['MS Excel', 'MS Word', 'MS PowerPoint']
categories = ['1 кв.', '2 кв.', '3 кв.', '4 кв.']
 
values1 = [112, 231, 178, 129] 
values2 = [187, 195, 118, 149] 
values3 = [167, 129, 70, 90] 

index = np.arange(len(categories))

bw=0.15

 
plt.title('Групова горизонтальна гістограма', fontsize=20) 
plt.barh(index+bw, values1, bw, color='red') 
plt.barh(index+2*bw, values2, bw, color='purple') 
plt.barh(index+3*bw, values3, bw, color='blue') 
plt.yticks(index + (len(company_names) - 1) * bw / 2, categories)
plt.legend(company_names)
plt.savefig('D:/Python/Laba6/laba6_6.png')
plt.show()