import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gamma
import itertools


def standard_normal_distribution():
	# Standard Normal Distribution
	# vector of values for x: x=(-3.00,-2.99,-2.98, ... ,3.00)
	x = np.linspace(-3, 3, 601)
	# vector of values for f(x)
	fx = (1 / np.sqrt(2 * np.pi)) * np.exp(-(x ** 2) / 2)
	# graph
	plt.plot(x, fx)
	plt.show()


def gamma_distribution():
	# vector of values for x: x=(0.00,0.01,0.02,0.03, ... ,5.00)
	x = np.linspace(0, 5, 501)
	# vector of the corresponding values of f(x) if X ~ Gamma(4,3)
	fx = ((3 ** 4) / math.gamma(4)) * (x ** 3) * np.exp(-3 * x)
	# value of Delta x: same as gap between values in vector x
	dx = 0.01
	# vector of values of [f(x) Delta(x)]
	fxdx = fx * dx
	# vector of cumulative values of [f(x) Delta(x)]
	Fx = np.array(list(itertools.accumulate(fxdx)))
	# graph of F(x) as a function of x
	plt.plot(x, Fx)
	plt.show()


def histogram():
	# x and y are vectors of 1000000 i.i.d. U(0,1) r.v.
	x = np.random.uniform(0, 1, 1000000)
	y = np.random.uniform(0, 1, 1000000)
	# r.v. of interest
	w = x + y
	# produces histogram
	plt.hist(w, bins=100, density=True)
	# prints histogram
	plt.show()


def plot_gamma_k():
	"""
	k : the number of events for which you are waiting to occur.
	λ : the rate of events happening following Poisson dist.
	"""
	x = np.linspace(0, 50, 1000)
	a = 1  # k = 1
	mean, var, skew, kurt = gamma.stats(a, moments='mvsk')
	y1 = gamma.pdf(x, a)
	a = 5  # k = 5
	mean, var, skew, kurt = gamma.stats(a, moments='mvsk')
	y2 = gamma.pdf(x, a)
	a = 10  # k = 15
	mean, var, skew, kurt = gamma.stats(a, moments='mvsk')
	y3 = gamma.pdf(x, a)
	plt.title("PDF of Gamma Distribution")
	plt.xlabel("T")
	plt.ylabel("Probability Density")
	plt.plot(x, y1, label="k = 1", color='palegreen')
	plt.plot(x, y2, label="k = 5", color='yellowgreen')
	plt.plot(x, y3, label="k = 10", color='olivedrab')
	plt.legend(bbox_to_anchor=(1, 1), loc='upper right', borderaxespad=1, fontsize=12)
	plt.ylim([0, 0.40])
	plt.xlim([0, 20])
	plt.show()
	# plt.savefig('gamma_k.png')


def plot_gamma_lambda():
	"""
	k : the number of events for which you are waiting to occur.
	λ : the rate of events happening following Poisson dist.
	"""
	a = 10  # k = 10
	x = np.linspace(0, 50, 1000)
	lambda_ = 1
	mean, var, skew, kurt = gamma.stats(a, scale=1 / lambda_, moments='mvsk')
	y1 = gamma.pdf(x, a, scale=1 / lambda_)
	lambda_ = 2
	mean, var, skew, kurt = gamma.stats(a, scale=1 / lambda_, moments='mvsk')
	y2 = gamma.pdf(x, a, scale=1 / lambda_)
	lambda_ = 3
	mean, var, skew, kurt = gamma.stats(a, scale=1 / lambda_, moments='mvsk')
	y3 = gamma.pdf(x, a, scale=1 / lambda_)
	plt.title("PDF of Gamma Distribution (k = 10)")
	plt.xlabel("T")
	plt.ylabel("Probability Density")
	plt.plot(x, y1, label="λ = 1", color='gold')
	plt.plot(x, y2, label="λ = 2", color='burlywood')
	plt.plot(x, y3, label="λ = 3", color='darkorange')
	plt.legend(bbox_to_anchor=(1, 1), loc='upper right', borderaxespad=1, fontsize=12)
	plt.ylim([0, 0.40])
	plt.xlim([0, 20])
	plt.show()
	# plt.savefig('gamma_lambda.png')

standard_normal_distribution()
gamma_distribution()
histogram()
plot_gamma_lambda()
plot_gamma_k()