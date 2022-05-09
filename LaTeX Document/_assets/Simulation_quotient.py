import numpy as np 					# pip install numpy
import matplotlib.pyplot as plt 	# pip install matplotlib
import scipy as sp 					# pip install scipy
from scipy import stats 			# Used to generate gamma pdf array

# Settings for matplotlib figure size, font and dpi
plt.rcParams["figure.figsize"] = [10, 7]
plt.rcParams["font.family"] = "CMU Serif"
plt.rcParams['figure.dpi'] = 140


def simulation_quotient(alpha_=2, beta_=5, lambda_=1):
	# x and y are vectors of 1000000 i.i.d. Gamma(alpha_,lambda_) r.v.
	x1 = np.random.gamma(alpha_, 1/lambda_, 1000000)
	y1 = np.random.gamma(beta_, 1/lambda_, 1000000)
	n = np.linspace(0, 1, 10000)
	# PDF of Beta(alpha_, beta_)
	y2 = sp.stats.beta.pdf(n, alpha_, beta_)

	# r.v. of interest
	v = x1/(x1 + y1)

    # Generating graph using matplotlib
	plt.title("PDF of Beta Distribution vs Histogram of Gamma Distributions", fontsize=20)
	plt.xlabel("T", fontsize=16)
	plt.ylabel("Density", fontsize=16)
	plt.plot(n, y2, label=f"PDF of Beta({alpha_}, {beta_})", linewidth=3, color="turquoise")
	plt.hist(v, label=r"Histogram of $\dfrac{X}{X+Y}$", bins=10000, density=True, color="darkblue")
	plt.legend(bbox_to_anchor=(1, 1), loc="upper right", borderaxespad=1, fontsize=12)
	plt.ylim([0, 3])
	plt.xlim([0, 1])
	plt.show()

simulation_quotient(2, 5, 1)