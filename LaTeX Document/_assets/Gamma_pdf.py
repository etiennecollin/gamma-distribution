import math
import numpy as np 					# pip install numpy
import matplotlib.pyplot as plt 	# pip install matplotlib

# Settings for matplotlib figure size and font
plt.rcParams["figure.figsize"] = [10, 7]
plt.rcParams["font.family"] = "CMU Serif"


def gamma_distribution_pdf(alpha_=4, lambda_=3):
    # Array with values from 0 to 25 with 10000 equal increments
    x = np.linspace(0, 25, 10000)

    # f(x) for X ~ Gamma(alpha_,lambda_)
    fx = (((1/lambda_)**alpha_)/math.gamma(alpha_)) * (x**(1/lambda_)) * np.exp(-(1/lambda_)*x)

    # Generating graph using matplotlib
    plt.title("Probability Density Function of Gamma Distribution", fontsize=20)
    plt.annotate(f"Gamma({alpha_}, {lambda_})", xy=(15, 0.0012), size=14, ha="center", va="center", color="firebrick")
    plt.xlabel("T", fontsize=16)
    plt.ylabel("Density", fontsize=16)
    plt.plot(x, fx, color="firebrick")
    plt.show()


gamma_distribution_pdf(4, 3)
