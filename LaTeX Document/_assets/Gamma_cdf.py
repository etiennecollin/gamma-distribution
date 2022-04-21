import math
import itertools
import numpy as np 					# pip install numpy
import matplotlib.pyplot as plt 	# pip install matplotlib

# Settings for matplotlib figure size and font
plt.rcParams["figure.figsize"] = [10, 7]
plt.rcParams["font.family"] = "CMU Serif"


def gamma_distribution_cdf(alpha_=4, lambda_=3):
    # Array with values from 0 to 25 with 10000 equal increments
    x = np.linspace(0, 25, 10000)

    # f(x) for X ~ Gamma(alpha_,lambda_)
    fx = (((1/lambda_)**alpha_)/math.gamma(alpha_)) * (x**(1/lambda_)) * np.exp(-(1/lambda_)*x)

    dx = 0.0025  # Same as gap between values in array x
    fxdx = fx * dx
    Fx = np.array(list(itertools.accumulate(fxdx)))

    # Generating graph using matplotlib
    plt.title("Distribution Function of Gamma Distribution", fontsize=20)
    plt.annotate(f"Gamma({alpha_}, {lambda_})", xy=(2.5, 0.028), size=14, ha="center", va="center", color="firebrick")
    plt.xlabel("T", fontsize=16)
    plt.ylabel("Probability", fontsize=16)
    plt.plot(x, Fx, color="firebrick")
    plt.show()


gamma_distribution_cdf(4, 3)