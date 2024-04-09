from data_reader import *
from scipy.optimize import curve_fit

# def plot(a, b, title, x, y, log_scale=False):
#     plt.plot(a, b, marker='o', ls="")  # Plot a in function of b with markers
#     plt.xlabel(f'{x}')  # Label for the x-axis
#     plt.ylabel(f'{y}')  # Label for the y-axis
#     plt.title(title)  # Set the title of the plot
    
#     if log_scale:
#         plt.xscale('log')  # Set x-axis to log scale
#         plt.yscale('log')  # Set y-axis to log scale
        
#     plt.grid(True)  # Add a grid
#     plt.show()  # Display the plot


# Define a power-law model function for curve fitting
def power_law(x, a, b):
    return a * x**b

def linear_model(x, m, c):
    return m * x + c

def plot(x, y, title, xaxis, yaxis,y_err,x_err,xlog,ylog):
    #agregar incertezaspara cada eje 
    y = np.array(y) 
    # Perform weighted least squares regression using curve_fit
    popt, pcov = curve_fit(power_law, x, y, sigma=y_err, absolute_sigma=True)
    a, b = popt

    # Create an array for the fit curve
    x_fit = np.linspace(min(x), max(x), 400)

    # Plot the data with error bars
    plt.errorbar(x, y, xerr = x_err,yerr=y_err, fmt='.',label='Data')
    # plt.scatter(x,y,s = 5)
    # Plot the weighted power-law fit
    plt.plot(x_fit, power_law(x_fit, a, b), label=f"Fit: y={a:.2f}x^{b:.2f}")

    plt.xlabel(xaxis, fontsize = 14)
    plt.ylabel(yaxis, fontsize = 14)
    plt.legend()
    plt.title(title, fontsize = 16)
    plt.show()

    # Hacemos el logaritmo de los datos
    log_x = np.log10(x)
    log_y = np.log10(y)
    log_y_err = y_err / (y * np.log(10))

    # Para que log_y_err no tenga valores negativos, los paso como errores absolutos
    popt_linear, pcov_linear = curve_fit(linear_model, log_x, log_y, sigma=log_y_err, absolute_sigma=True)
    m, c = popt_linear
    m_err, c_err = np.sqrt(np.diag(pcov_linear))

    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 2)
    plt.errorbar(log_x, log_y, yerr=log_y_err, fmt='.', label="Log Data")
    plt.plot(log_x, linear_model(log_x, m, c), label=f"Linear Fit: y={m:.2f}±{m_err:.2f}x + {c:.2f}±{c_err:.2f}")
    plt.xlabel(xlog, fontsize = 14)
    plt.ylabel(ylog, fontsize = 14)
    plt.legend()
    plt.title("Data en Log-Log con ajuste lineal", fontsize = 16)

    plt.subplot(1, 2, 1)
    plt.errorbar(x, y, yerr=y_err, fmt='.', label="Data")
    plt.plot(x, power_law(x, a, b), label=f"Power Law Fit: y={a:.2f}x^{b:.2f}")
    plt.xlabel(xaxis, fontsize = 14)
    plt.ylabel(yaxis, fontsize = 14)
    plt.legend()
    plt.title("Data con ajuste de ley de potencias", fontsize = 16)

    plt.tight_layout()
    plt.show()
    print(f"Slope (m): {m:.2f} ± {m_err:.2f}")
    print(f"Intercept (c): {c:.2f} ± {c_err:.2f}")
    plt.savefig(yaxis +'.jpg', bbox_inches = 'tight')



def main():
    data = {'LARGO':[],'ANCHO':[],'MASA':[],'AREA':[],'incerteza':[]}
    incerteza = [2,2,2,2,2,2,2,2,1,1,1,1,1,0.3,1,1,1,1,1,1,1,1,1,1,1] 
    charge_data(data,'datos.csv')
    print("mean de la altura de las hojas C1 →", mean(data['LARGO']))
    print("mean del ancho de las hojas C1 →", mean(data['ANCHO']))
    print("varianza de la altura de las hojas C1 →", var(data['LARGO']))
    print("varianza del ancho de las hojas C1 →", var(data['ANCHO']))
    # histo_fr(data['LARGO'],10)
    # histo_densidad(data['ANCHO'],10)
    x_err = []
    for i in range(0,len(data['AREA'])):
        x_err.append(0.01)
    plot(data['MASA'],data['LARGO'],'Largo en función de la masa','masa[g]','largo[mm]',np.ones(len(data['LARGO'])),x_err,'log(masa)[g]','log(largo)[mm]')
    plot(data['MASA'],data['ANCHO'],'Ancho en función de la masa','masa[g]','ancho[mm]',np.ones(len(data['LARGO'])),x_err,'log(masa)[g]','log(ancho)[mm]')
    plot(data['MASA'],data['AREA'],'Area en función de la masa','masa[g]','area[cm^2]',incerteza,x_err,'log(masa)[g]','log(area)[cm^2]')

if __name__ == '__main__':
    main()