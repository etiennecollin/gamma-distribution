import math
import numpy as np 					# pip install numpy
import matplotlib.pyplot as plt 	# pip install matplotlib

# Settings for matplotlib figure size, font and dpi
plt.rcParams["figure.figsize"] = [10, 7]
plt.rcParams["font.family"] = "CMU Serif"
plt.rcParams['figure.dpi'] = 140


def gamma_pdf(alpha_=4, lambda_=3):
	x = np.linspace(0, 5, 100000)
	# PDF of Gamma(alpha_, lambda_)
	y1 = sp.stats.gamma.pdf(x, alpha_, scale=1/lambda_)

    # Generating graph using matplotlib
	plt.title("Probability Density Function of the Gamma Distribution", fontsize=20)
	plt.xlabel("T", fontsize=16)
	plt.ylabel("Density", fontsize=16)
	plt.plot(x, y1, label=f"Gamma({alpha_}, {lambda_})", linewidth=3, color="blue")
	plt.legend(bbox_to_anchor=(1, 1), loc="upper right", borderaxespad=1, fontsize=12)
	plt.ylim([0, 0.7])
	plt.xlim([0, 5])
	plt.show()

gamma_pdf(4, 3)