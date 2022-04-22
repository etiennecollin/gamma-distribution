import numpy as np 					# pip install numpy
import matplotlib.pyplot as plt 	# pip install matplotlib
import scipy as sp 					# pip install scipy
from scipy import stats 			# Used to generate gamma pdf array

# Settings for matplotlib figure size, font and dpi
plt.rcParams["figure.figsize"] = [10, 7]
plt.rcParams["font.family"] = "CMU Serif"
plt.rcParams['figure.dpi'] = 140


def histogram_gamma_sum(alpha_=1, beta_=3, lambda_=3):
	# x and y are arrays of 1000000 i.i.d. Gamma(alpha_,lambda_) r.v.
	x = np.random.gamma(alpha_, 1/lambda_, 1000000)
	y = np.random.gamma(beta_, 1/lambda_, 1000000)
	u = x + y  # r.v. of interest

	# Generating histogram using matplotlib
	plt.title(fr"(X+Y) where X$\sim$Gamma({alpha_}, {lambda_}) and Y$\sim$Gamma({beta_}, {lambda_})", fontsize=20)
	plt.xlabel("T", fontsize=16)
	plt.ylabel("Density", fontsize=16)
	plt.hist(u, bins=10000, density=True, color="darkblue")
	plt.annotate("(X+Y)", xy=(3, 0.6), size=14, ha="center", va="center", color="darkblue")
	plt.ylim([0, 0.8])
	plt.xlim([0, 5])
	plt.show()


def gamma(alpha_=1, beta_=3, lambda_=3):
	x = np.linspace(0, 60, 1000000)
	y = sp.stats.gamma.pdf(x, (alpha_+beta_), scale=1/lambda_)

	# Generating graph using matplotlib
	plt.title("Probability Density Function of Gamma Distribution", fontsize=20)
	plt.xlabel("T", fontsize=16)
	plt.ylabel("Density", fontsize=16)
	plt.plot(x, y, linewidth=3, color="firebrick")
	plt.annotate(f"Gamma({alpha_}+{beta_}, {lambda_})", xy=(3, 0.6), size=14, ha="center", va="center", color="firebrick")
	plt.ylim([0, 0.8])
	plt.xlim([0, 5])
	plt.show()


histogram_gamma_sum(1, 3, 3)
gamma(1, 3, 3)
