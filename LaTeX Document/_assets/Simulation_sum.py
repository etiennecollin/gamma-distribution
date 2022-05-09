import numpy as np 					# pip install numpy
import matplotlib.pyplot as plt 	# pip install matplotlib
import scipy as sp 					# pip install scipy
from scipy import stats 			# Used to generate gamma pdf array

# Settings for matplotlib figure size, font and dpi
plt.rcParams["figure.figsize"] = [10, 7]
plt.rcParams["font.family"] = "CMU Serif"
plt.rcParams['figure.dpi'] = 140


def simulation_sum(alpha_=1, beta_=3, lambda_=3):
	# x and y are vectors of 1000000 i.i.d. Gamma(alpha_,lambda_) r.v.
	x1 = np.random.gamma(alpha_, 1/lambda_, 1000000)
	y1 = np.random.gamma(beta_, 1/lambda_, 1000000)
	n = np.linspace(0, 5, 1000000)
	# PDF of Gamma(alpha_+ beta_, lambda_)
	y2 = sp.stats.gamma.pdf(n, (alpha_+beta_), scale=1/lambda_)

	# r.v. of interest
	u = x1 + y1

	plt.title("PDF of Gamma Distribution vs Histogram of Gamma Distributions", fontsize=20)
	plt.xlabel("T", fontsize=16)
	plt.ylabel("Density", fontsize=16)
	plt.plot(n, y2, label=f"PDF of Gamma({alpha_}+{beta_}, {lambda_})", linewidth=3, color="turquoise")
	plt.hist(u, label="Histogram of (X+Y)", bins=10000, density=True, color="darkblue")
	plt.legend(bbox_to_anchor=(1, 1), loc="upper right", borderaxespad=1, fontsize=12)
	plt.ylim([0, 0.8])
	plt.xlim([0, 5])
	plt.show()

simulation_sum(1, 3, 3)
