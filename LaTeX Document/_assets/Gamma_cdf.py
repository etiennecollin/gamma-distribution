import math
import itertools
import numpy as np 					# pip install numpy
import matplotlib.pyplot as plt 	# pip install matplotlib

# Settings for matplotlib figure size, font and dpi
plt.rcParams["figure.figsize"] = [10, 7]
plt.rcParams["font.family"] = "CMU Serif"
plt.rcParams['figure.dpi'] = 140


def gamma_cdf(alpha_=4, lambda_=3):
	x = np.linspace(0, 4, 1000000)
	# PDF of Gamma(alpha_, lambda_)
	y1 = sp.stats.gamma.cdf(x, alpha_, scale=1/lambda_)

    # Generating graph using matplotlib
	plt.title("Cumulative Distribution Function of the Gamma Distribution", fontsize=20)
	plt.xlabel("T", fontsize=16)
	plt.ylabel("Probability", fontsize=16)
	plt.plot(x, y1, label=f"Gamma({alpha_}, {lambda_})", linewidth=3, color="blue")
	plt.legend(bbox_to_anchor=(1, 1), loc="upper right", borderaxespad=1, fontsize=12)
	plt.ylim([0, 1])
	plt.xlim([0, 4])
	plt.show()

gamma_cdf()
