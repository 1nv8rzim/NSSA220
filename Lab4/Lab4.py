import matplotlib.pyplot as plt


colors = {'APM1':'blue',
          'APM2':'black',
          'APM3':'red',
          'APM4':'green',
          'APM5':'yellow',
          'APM6':'cyan'}

process_metrics = {}
system_metrics = {}

def get_process_metrics():
    for APM in [f'APM{i}' for i in range(1,7)]:
        file = f'Lab4/metrics/{APM}_metrics.csv'
        with open(file, 'r') as metrics:
            for line in metrics:
                time, cpu, memory = line.strip().split(',')
                time, cpu, memory = int(time), float(cpu), float(memory)
                if time not in process_metrics:
                    process_metrics[time] = {}
                process_metrics[time][APM] = {'cpu':cpu, 'memory':memory}

def get_system_metrics():
    with open('Lab4/metrics/system_metrics.csv') as metrics:
        for line in metrics:
            time, rx, tx, disk_writes, available_disk = line.strip().split(',')
            time, rx, tx, disk_writes, available_disk = int(time), int(rx), int(tx), float(disk_writes), int(available_disk)
            system_metrics[time] = {'rx':rx, 'tx':tx, 'disk_writes':disk_writes, 'available_disk':available_disk}

def make_process_plot(metric):
    APM_metrics, times = {}, []
    for time, values in process_metrics.items():
        times.append(time)
        for APM, metrics in values.items():
            if APM not in APM_metrics:
                APM_metrics[APM] = []
            APM_metrics[APM].append(metrics[metric])
    for APM, cpu in APM_metrics.items():
        plt.plot(times, cpu, label=APM)
    plt.xlabel('time')
    plt.ylabel(metric)
    plt.title(f'{metric} metrics')
    plt.legend(loc='upper right')
    plt.show()

def make_bandwith_plots():
    rx, tx, times = [], [], []
    for time, values in system_metrics.items():
        rx.append(values['rx'])
        tx.append(values['tx'])
        times.append(time)
    plt.plot(times, rx, label='rx')
    plt.plot(times, tx, label='tx')
    plt.xlabel('time')
    plt.ylabel('bandwidth utilization')
    plt.title('bandwidth metrics')
    plt.legend(loc='upper right')
    plt.show()

def make_system_plots(metric):
    metrics, times = [], []
    for time, values in system_metrics.items():
        metrics.append(values[metric])
        times.append(time)
    plt.plot(times, metrics, label=metric)
    plt.xlabel('time')
    plt.ylabel(metric)
    plt.title(f'{metric} metrics')
    plt.legend(loc='upper right')
    plt.show()


        

def main():
    get_process_metrics()
    get_system_metrics()
    make_process_plot('cpu')
    make_process_plot('memory')
    make_bandwith_plots()
    make_system_plots('disk_writes')
    make_system_plots('available_disk')
    

    
if __name__ == '__main__':
    main()