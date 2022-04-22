import math
import numpy as np 				# pip install numpy
import matplotlib.pyplot as plt # pip install matplotlib
import scipy as sp 				# pip install scipy
from scipy import stats 		# Used to generate gamma pdf array

# Settings for matplotlib figure size, font and dpi
plt.rcParams["figure.figsize"] = [10, 7]
plt.rcParams["font.family"] = "CMU Serif"
plt.rcParams['figure.dpi'] = 140

def central_limit_theorem(alpha_=60, lambda_=1, expected_=60, variance_=60):
	x = np.linspace(30, 90, 100000)
	y1 = sp.stats.gamma.pdf(x, alpha_, scale=1/lambda_) 		# PDF of Gamma(alpha_, lambda_)
	y2 = sp.stats.norm.pdf(x, expected_, math.sqrt(variance_)) 	# PDF of N(expected_, variance_)

	# Generating graph using matplotlib
	plt.title("Central Limit Theorem", fontsize=20)
	plt.xlabel("T", fontsize=16)
	plt.ylabel("Density", fontsize=16)
	plt.plot(x, y1, label=f"Gamma({alpha_}, {lambda_})", linewidth=3, color="firebrick")
	plt.plot(x, y2, label=f"N{expected_, variance_}", linewidth=3, color="orange")
	plt.legend(bbox_to_anchor=(1, 1), loc="upper right", borderaxespad=1, fontsize=12)
	plt.xlim([30, 90])
	plt.show()

central_limit_theorem(60, 1, 60, 60)