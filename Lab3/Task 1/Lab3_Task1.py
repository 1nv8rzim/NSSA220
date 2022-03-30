from sys import argv
from statistics import stdev

class Iris:
    def __init__(self, sepal_length, sepal_width, petal_length, petal_width, iris_type):
        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width
        self.iris_type = iris_type
    
    def __str__(self): return f'Iris({self.sepal_length}, {self.sepal_width}, {self.petal_length}, {self.petal_width}, {self.iris_type})'
    
    def __repr__(self): return self.__str__()

def read_data(file_name, irises):
    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip()
            if line == '':
                continue
            if line[0] in '%@':
                continue
            irises.append(Iris(*line.split(',')))

def parse_irises(irises):
    sepal_lengths, sepal_widths, petal_lengths, petal_widths = [], [], [], []
    iris_count = {}
    
    for iris in irises:
        sepal_lengths.append(float(iris.sepal_length))
        sepal_widths.append(float(iris.sepal_width))
        petal_lengths.append(float(iris.petal_length))
        petal_widths.append(float(iris.petal_width))
        if iris.iris_type in iris_count:
            iris_count[iris.iris_type] += 1
        else:
            iris_count[iris.iris_type] = 1

    return sepal_lengths, sepal_widths, petal_lengths, petal_widths, iris_count

def process_numeric_fields(data):
    return {'max':max(data), 'min':min(data), 'average':sum(data)/len(data), 'standard_deviation':stdev(data)}

def print_metrics(sepal_length_metrics, sepal_width_metrics, petal_length_metrics, petal_width_metrics, iris_count):
    for data, title in zip((sepal_length_metrics, sepal_width_metrics, petal_length_metrics, petal_width_metrics), ('Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width')):
        print(f'{title}: min={data["min"]}, max={data["max"]}, average={data["average"]}, standard_deviation={data["standard_deviation"]}\n')
    
    print('Iris Types: ', end='')
    for iris_type, count in iris_count.items():
        print(f'{iris_type}={count}, ', end='')
    print()

def main():
    try:
        file_name = argv[1]
    except:
        file_name = 'iris_full.txt'

    irises = []
    
    read_data(file_name, irises)
    sepal_lengths, sepal_widths, petal_lengths, petal_widths, iris_count = parse_irises(irises)
    sepal_length_metrics, sepal_width_metrics, petal_length_metrics, petal_width_metrics = [process_numeric_fields(data) for data in (sepal_lengths, sepal_widths, petal_lengths, petal_widths)]
    print_metrics(sepal_length_metrics, sepal_width_metrics, petal_length_metrics, petal_width_metrics, iris_count)
    

if __name__ == '__main__':
    main()
