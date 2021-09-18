import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


def setup_plot(ax, title, xlabel, ylabel):
    ax.minorticks_on()
    ax.grid(which='major', linewidth=0.5, linestyle='dashed', color='black')

    # устанавливаем подпись
    ax.set_title(title)

    # делаем штрихи внутрь
    ax.tick_params(which='major', direction='in', width=1.5, length=8)
    ax.tick_params(which='minor', direction='in', width=1.5, length=4)

    # устанавливаем подписи к осям
    ax.set_xlabel(xlabel, fontsize='large')
    ax.set_ylabel(ylabel, fontsize='large')

    # ax.axhline(linewidth=3)
    # ax.axvline(linewidth=3)


if __name__ == "__main__":

    # ---------------------------/ Graphics /--------------------------

    fig, ax = plt.subplots()

    # Погрешности

    ax.errorbar(x_arr, y_arr, xerr=x_err, yerr=y_err, fmt='s')


    # ---------------------------/ МНК /--------------------------------

    def f(x, a):
        return a * x

    popt, perr = curve_fit(f, np.array(x_arr), np.array(y_arr))
    print(popt)
    ax.errorbar(x_arr, f(np.array(x_arr), *popt), linewidth=2)

    # ---------------------------//-----------------------------------

    plt.show()
