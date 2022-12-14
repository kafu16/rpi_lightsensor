import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd


def plot_sensor_data(dir_csv):
    # read in sensor data as dataframe from .csv
    df = pd.read_csv(dir_csv)

    # two subplots with lines
    plt.subplot(211)
    plt.plot(df["time"].to_numpy(),df["total_light"].to_numpy(), marker='o', color='b', label='Total light [lux]')
    plt.plot(df["time"].to_numpy(),df["IR"].to_numpy(), marker='*', color='m', label='IR')
    plt.ylabel("different observables")
    # hiding x-axis
    frame1 = plt.gca()
    frame1.axes.xaxis.set_ticklabels([])

    plt.grid(True)
    plt.title("")
    plt.legend(loc="upper left", bbox_to_anchor=[0.65, 1.4], ncol=1, shadow=True, fancybox=True)

    plt.subplot(212)
    plt.plot(df["time"].to_numpy(),df["visible_light"].to_numpy(), marker='o', color='y', label='Visible light')
    plt.plot(df["time"].to_numpy(),df["full_spectrum"].to_numpy(), marker='^', color='g', label='Full spectrum (visible + IR)')
    plt.xlabel("time [s]")
    plt.ylabel("different observables")
    plt.axis('tight')
    #plt.yscale("log")
    plt.grid(True)
    plt.legend(loc="upper left", bbox_to_anchor=[0.45, 1.4], ncol=1, shadow=True, fancybox=True)

    plt.savefig("plot_sensor_data.pdf",bbox_inches='tight')
    plt.clf()
    return

dir_csv = 'sensor_data.csv'
plot_sensor_data(dir_csv)
