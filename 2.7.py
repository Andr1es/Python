import numpy as np

#loop
random_array = np.random.rand(50)
period = 7

for i in range(period,len(random_array)):
    array = random_array[i-period:i]
    
    
#print de formule met tekst in console
print("Gemiddelde van dag", i-period, "tot", i, "is", np.mean(array));
                     
                     
    




      
