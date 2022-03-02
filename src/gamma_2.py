import matplotlib.pyplot as plt
import numpy as np

########################
# f(x) = exp(-x) graph #
########################
def gamma_1():
	# Create x and y
	x = np.linspace(-2, 20, 100)
	y = np.exp(-x)

	# Create the plot
	fig, ax = plt.subplots()
	plt.plot(x, y, label='f(x) = exp(-x)', linewidth=3, color='palegreen')

	# Make the x=0, y=0 thicker
	ax.set_aspect('equal')
	ax.grid(True, which='both')
	ax.axhline(y=0, color='k')
	ax.axvline(x=0, color='k')

	# Add a title
	plt.title('f(x) = exp(-x)', fontsize=20)

	# Add X and y Label
	plt.xlabel('x', fontsize=16)
	plt.ylabel('f(x)', fontsize=16)

	# Add a grid
	plt.grid(alpha=.4, linestyle='--')

	# Show the plot
	plt.show()


####################
# f(x) = x^z graph #
####################
def gamma_2():
	# Create x and y
	x = np.linspace(0, 2, 100)
	y1 = x ** 1.3
	y2 = x ** 2.5
	y3 = x ** 3.8

	# Create the plot
	fig, ax = plt.subplots()
	plt.plot(x, y1, label='f(x) = x^1.3', linewidth=3, color='palegreen')
	plt.plot(x, y2, label='f(x) = x^2.5', linewidth=3, color='yellowgreen')
	plt.plot(x, y3, label='f(x) = x^3.8', linewidth=3, color='olivedrab')

	# Make the x=0, y=0 thicker
	ax.set_aspect('equal')
	ax.grid(True, which='both')
	ax.axhline(y=0, color='k')
	ax.axvline(x=0, color='k')

	# Add a title
	plt.title('f(x) = x^z', fontsize=20)

	# Add X and y Label
	plt.xlabel('x', fontsize=16)
	plt.ylabel('f(x)', fontsize=16)

	# Add a grid
	plt.grid(alpha=.4, linestyle='--')

	# Add a Legend
	plt.legend(bbox_to_anchor=(1, 1), loc='best', borderaxespad=1, fontsize=12)

	# Show the plot
	plt.show()


###############################
# f(x) = x^(3.8)*e^(-x) graph #
###############################
def gamma_3():
	# Create x and y
	x = np.linspace(0, 20, 100)
	y = x ** 3.8 * np.exp(-x)

	# Create the plot
	fig, ax = plt.subplots()
	plt.plot(x, y, label='f(x) = x^(3.8) * np.exp(-x)', linewidth=3, color='palegreen')
	ax.fill_between(x, 0, y, color='yellowgreen')

	# Make the x=0, y=0 thicker
	ax.set_aspect('equal')
	ax.grid(True, which='both')
	ax.axhline(y=0, color='k')
	ax.axvline(x=0, color='k')

	# Add a title
	plt.title('f(x) =  x^(3.8)*e^(-x) ', fontsize=20)

	# Add X and y Label
	plt.xlabel('x', fontsize=16)
	plt.ylabel('f(x)', fontsize=16)

	# Add a grid
	plt.grid(alpha=.4, linestyle='--')

	# Add a Legend
	plt.legend(bbox_to_anchor=(1, 1), loc='upper right', borderaxespad=1, fontsize=12)

	# Show the plot
	plt.show()
