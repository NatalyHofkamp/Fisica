from data_reader import *
def count_if(data,condition):
    result = 0
    media = mean(data)
    for d in data:
        if condition == '<' and d<media:
            result+=1
        if condition == '>' and d>media:
            result+=1
    return result 

def plot(a,b,title,x,y):
    plt.plot(a,b, marker='o')  # Plot a in function of b with markers
    plt.xlabel(f'{x}')  # Label for the x-axis
    plt.ylabel(f'{y}')  # Label for the y-axis
    plt.title(title)  # Set the title of the plot
    plt.grid(True)  # Add a grid
    plt.show()  # Display the plot


   

def main():
    data = {'LARGO':[],'ANCHO':[],'MASA':[],'AREA':[]} 
    charge_data(data,'datos.csv')
    print("mean de la altura de las hojas C1 →", mean(data['LARGO']))
    print("mean del ancho de las hojas C1 →", mean(data['ANCHO']))
    print("varianza de la altura de las hojas C1 →", var(data['LARGO']))
    print("varianza del ancho de las hojas C1 →", var(data['ANCHO']))
    print(f"En C1 hay {count_if(data['LARGO'], '<')} hojas que miden menos que la media")
    print(f"En C1 hay {count_if(data['LARGO'], '>')} hojas que miden mas que la media")
    histo_fr(data['LARGO'],10)
    histo_densidad(data['ANCHO'],10)
    data['MASA']= sort( data['MASA'])
    plot(data['MASA'],data['LARGO'],'Largo en función de la masa','masa','largo')
    plot(data['MASA'],data['ANCHO'],'Ancho en función de la masa','masa','ancho')
    plot(data['MASA'],data['AREA'],'Area en función de la masa','masa','area')


if __name__ == '__main__':
    main()