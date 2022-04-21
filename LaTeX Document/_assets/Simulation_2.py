import numpy as np 					# pip install numpy
import matplotlib.pyplot as plt 	# pip install matplotlib
import scipy as sp 					# pip install scipy
from scipy import stats 			# Used to generate gamma pdf array

# Settings for matplotlib figure size and font
plt.rcParams["figure.figsize"] = [10, 7]
plt.rcParams["font.family"] = "CMU Serif"


def histogram_beta(alpha_=2, beta_=5, lambda_=1):
    # x and y are arrays of 1000000 i.i.d. Gamma(alpha_,lambda_) r.v.
    x = np.random.gamma(alpha_, 1/lambda_, 1000000)
    y = np.random.gamma(beta_, 1/lambda_, 1000000)
    v = x/(x + y)  # r.v. of interest

    # Generating histogram using matplotlib
    plt.title(fr"X/(X+Y) where X$\sim$Gamma({alpha_}, {lambda_}) and Y$\sim$Gamma({beta_}, {lambda_})", fontsize=20)
    plt.xlabel("T", fontsize=16)
    plt.ylabel("Density", fontsize=16)
    plt.hist(v, bins=10000, density=True, color="darkblue")
    plt.annotate(r"$\dfrac{X}{X+Y}$", xy=(0.6, 2.7), size=14, ha="center", va="center", color="darkblue")
    plt.ylim([0, 3])
    plt.xlim([0, 1])
    plt.show()


def beta(alpha_=2, beta_=5):
    x = np.linspace(0, 1, 10000)
    y = sp.stats.beta.pdf(x, alpha_, beta_)

    # Generating graph using matplotlib
    plt.title("Probability Density Function of Beta Distribution", fontsize=20)
    plt.xlabel("T", fontsize=16)
    plt.ylabel("Density", fontsize=16)
    plt.plot(x, y, linewidth=3, color="firebrick")
    plt.annotate(f"Beta({alpha_}, {beta_})", xy=(0.6, 2.7), size=14, ha="center", va="center", color="firebrick")
    plt.ylim([0, 3])
    plt.xlim([0, 1])
    plt.show()


histogram_beta(2, 5, 1)
beta(2, 5)
