from scipy.stats import expon,norm,poisson,chi2
from pylab import *

def charge_data(data, filename):
    with open(filename, 'r') as f:
        lineas = f.readlines()
        for l in lineas:
            l = l.strip().split('\t')  # Split using tab as the separator
            data['LARGO'].append(float(l[0].replace(',', '.')))
            data['ANCHO'].append(float(l[1].replace(',', '.')))
            data['MASA'].append(float(l[2].replace(',', '.')))
            data['AREA'].append(float(l[3].replace(',', '.')))
          
def  dist_poisson(lamb,size):
    return poisson.rvs(mu = lamb, size = size)

def dist_exp(lamb, size):
    return expon.rvs(scale = 1/lamb, size = size)

def dist_uni (min,max,size):
    return np.random.uniform(low=min, high=max, size=size)

def dist_norm(n,p,size):
    return norm.rvs(loc=n, scale= p, size = size)

def histo_fr(muestra,bins):
    plt.xlabel(r'$Y$',fontsize = 15)
    plt.ylabel(r'Frecuencia relativa',fontsize = 15)
    plt.title("Histograma de frecuencias relativas para ancho = "+str(bins)+" con "+str(len(muestra))+" elementos")
    plt.hist(muestra, bins = np.arange(min(muestra),max(muestra)+bins, bins), weights = np.zeros(len(muestra))+1/len(muestra))
    plt.show()

def histo_densidad (muestra,bins):
    plt.xlabel(r'$Y$',fontsize = 15)
    plt.ylabel(r'Frecuencia relativa',fontsize = 15)
    plt.title("Histograma de densidad para ancho = "+str(bins)+" con "+str(len(muestra))+" elementos")
    plt.hist(muestra, bins = np.arange(min(muestra),max(muestra)+bins, bins), weights = np.zeros(len(muestra))+1/len(muestra),density = True)
    plt.show()

def mean(data):
    return sum(data)/len(data)

def var(data):
    med = mean(data)
    values = [(v - med)**2 for v in data]
    return sum(values)/(len(data)-1)
   