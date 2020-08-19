#!/usr/bin/env python3
from complex import Complex
from math import sqrt

# List of different input data for tests
z1_values = [(-6, 3), (-3, -6), (0, 2), (3, -3), 7]
z2_values = [(1, 0), (2, 12), (11, -11), (3, -3), (1, -2)]

val_len = len(z1_values)

def test_add_complex():
	"""Tests that the add function in complex.py works
	
	Loops through the lists of z values and appends
	the result of their sum to a new list, then compares that
	list of computed values to a list of correct answers.
	"""
	
	# Hand-calculated values to test against
	z_real_list = [(-5, 3), (-1, 6), (11, -9), (6, -6), (8, -2)]
	# Program-calculated values, starts empty
	z_computed_list = []
	
	# Converts zx_values and adds test-answers to z_computed_list
	for i in range(val_len):
		if isinstance(z1_values[i], (float, int)):
			z1 = Complex(z1_values[i])
		else:
			z1 = Complex(z1_values[i][0], z1_values[i][1])
			
		if isinstance(z2_values[i], (float, int)):
			z2 = Complex(z2_values[i])
		else:
			z2 = Complex(z2_values[i][0], z2_values[i][1])	
			
		z_computed = z1+z2
		z_computed_list.append(z_computed())
	
	# Asserts for all values in lists
	# Could have asserted lists directly against each other,
	# Decided to iterate to easily display message for correct assertion error
	for i in range(val_len):
		msg = "\nError in value number %d\n\
				z1 = %s \n\
				z2 = %s \n\
				z_real = %s \n\
				z_computed = %s"\
			   % (i, z1_values[i], z2_values[i], z_real_list[i], z_computed_list[i])
		# Remove tab-spacings for prettier format
		msg = msg.replace('	', '')
		assert z_real_list[i] == z_computed_list[i], msg
	
	
def test_sub_complex():
	"""Tests that the sub function in complex.py works
	
	Loops through the lists of z values and appends
	the result of their difference to a new list, then compares
	that list of computed values to a list of correct answers.
	"""
	
	# Hand-calculated values to test against
	z_real_list = [(-7, 3), (-5, -18), (-11, 13), (0, 0), (6, 2)]
	
	z_computed_list = []
	for i in range(val_len):
		if isinstance(z1_values[i], (float, int)):
			z1 = Complex(z1_values[i])
		else:
			z1 = Complex(z1_values[i][0], z1_values[i][1])
			
		if isinstance(z2_values[i], (float, int)):
			z2 = Complex(z2_values[i])
		else:
			z2 = Complex(z2_values[i][0], z2_values[i][1])
			
		z_computed = z1-z2
		z_computed_list.append(z_computed())
	
	# Asserts for all values in lists
	# Could have asserted lists directly against each other,
	# Decided to iterate to easily display message for correct assertion error
	for i in range(val_len):
		msg = "\nError in value number %d\n\
				z1 = %s \n\
				z2 = %s \n\
				z_real = %s \n\
				z_computed = %s"\
			   % (i, z1_values[i], z2_values[i], z_real_list[i], z_computed_list[i])
		# Remove tab-spacings for prettier format
		msg = msg.replace('	', '')
		
		assert z_real_list[i] == z_computed_list[i], msg


def test_conjugate_complex():
	"""Tests that the conjugate function in complex.py works
	
	Loops through the first list of z values and appends
	the result of the conjugation to a new list, then compares
	that list of computed values to a list of correct answers.
	"""
	
	# Hand-calculated values to test against
	z_real_list = [(-6, -3), (-3, 6), (0, -2), (3, 3), (7, 0)]
	
	z_computed_list = []
	for i in range(val_len):
		if isinstance(z1_values[i], (float, int)):
			z = Complex(z1_values[i])
		else:
			z = Complex(z1_values[i][0], z1_values[i][1])
		
		z_computed = z.conjugate()
		z_computed_list.append(z_computed())
		
	for i in range(val_len):
		msg = "\nError in value number %d\n\
				z1 = %s \n\
				z_real = %s \n\
				z_computed = %s"\
			   % (i, z1_values[i], z_real_list[i], z_computed_list[i])
		msg = msg.replace('	', '')
		
		assert z_real_list[i] == z_computed_list[i], msg
	

def test_modulus_complex():
	"""Tests that the modulus function in complex.py works
	
	Loops through the first list of z values and appends
	the result of the modulus to a new list, then compares
	that list of computed values to a list of correct answers.
	"""
	
	# Hand-calculated values to test against
	z_real_list = [sqrt(6**2 + 3**2),
				   sqrt(3**2 + 6**2),
				   sqrt(0**2 + 2**2),
				   sqrt(3**2 + 3**2),
				   sqrt(7**2 + 0**2)]
	
	z_computed_list = []
	for i in range(val_len):
		if isinstance(z1_values[i], (float, int)):
			z = Complex(z1_values[i])
		else:
			z = Complex(z1_values[i][0], z1_values[i][1])		
		
		z_computed = z.modulus()
		z_computed_list.append(z_computed)
	
	eps = 10**(-12)
	for i in range(val_len):
		msg = "\nError in value number %d\n\
				z1 = %s \n\
				z_real = %s \n\
				z_computed = %s"\
			   % (i, z1_values[i], z_real_list[i], z_computed_list[i])
		msg = msg.replace('	', '')
		
		assert abs(z_real_list[i] - z_computed_list[i]) < eps, msg
	
	
def test_eq_complex():
	"""Tests that the eq function in complex.py works
	
	Loops through the lists of z values and appends
	the result of the comparison to a new list, then compares
	that list of computed values to a list of correct answers.
	"""
	
	# Hand-calculated values to test against
	z_real_list = [False, False, False, True, False]
	
	z_computed_list = []
	for i in range(val_len):
		if isinstance(z1_values[i], (float, int)):
			z1 = Complex(z1_values[i])
		else:
			z1 = Complex(z1_values[i][0], z1_values[i][1])
			
		if isinstance(z2_values[i], (float, int)):
			z2 = Complex(z2_values[i])
		else:
			z2 = Complex(z2_values[i][0], z2_values[i][1])
		
		z_computed = z1 == z2
		z_computed_list.append(z_computed)
		
	for i in range(val_len):
		msg = "\nError in value number %d\n\
				z1 = %s \n\
				z2 = %s \n\
				z_real = %s \n\
				z_computed = %s"\
			   % (i, z1_values[i], z2_values[i], z_real_list[i], z_computed_list[i])
		msg = msg.replace('	', '')
		
		assert z_real_list[i] == z_computed_list[i], msg


def test_radd_complex():
	"""Tests that the radd function in complex.py works
	
	Checks that the calculated values for when we add our
	complex number to a float or a complex number from
	pythons own library are correct.
	"""
	
	z_1_1 = complex(1, 4)
	z_1_2 = 2.5
	z_2 = Complex(2, 5)
	
	# Hand-calculated values to test against
	z_real_1 = (3, 9)
	z_real_2 = (4.5, 5)
	
	# Computed values
	z_computed_1 = (z_1_1 + z_2)()
	z_computed_2 = (z_1_2 + z_2)()
	
	assert z_real_1 == z_computed_1, ("Excpeted %s, got %s" % (z_real_1, z_computed_1))
	assert z_real_2 == z_computed_2, ("Excpeted %s, got %s" % (z_real_2, z_computed_2))


def test_rsub_complex():
	"""Tests that the rsub function in complex.py works
	
	Checks that the calculated values for when we subtract
	our	complex number to a float or a complex number from
	pythons own library are correct.
	"""
	
	z_1_1 = complex(1, 4)
	z_1_2 = 2.5
	z_2 = Complex(2, 5)
	
	# Hand-calculated values to test against
	z_real_1 = (-1, -1)
	z_real_2 = (0.5, -5)
	
	# Computed values
	z_computed_1 = (z_1_1 - z_2)()
	z_computed_2 = (z_1_2 - z_2)()
	
	assert z_real_1 == z_computed_1, ("Excpeted %s, got %s" % (z_real_1, z_computed_1))
	assert z_real_2 == z_computed_2, ("Excpeted %s, got %s" % (z_real_2, z_computed_2))
	
	
def test_rmul_complex():
	"""Tests that the rmul function in complex.py works
	
	Checks that the calculated values for when we multiply
	our complex number to a float or a complex number from
	pythons own library are correct.
	"""
	
	z_1_1 = complex(1, 4)
	z_1_2 = 2.5
	z_2 = Complex(2, 5)
	z_real_1 = (-18, 13)
	z_real_2 = (5, 12.5)
	z_computed_1 = (z_1_1 * z_2)()
	z_computed_2 = (z_1_2 * z_2)()
	
	assert z_real_1 == z_computed_1, ("Excpeted %s, got %s" % (z_real_1, z_computed_1))
	assert z_real_2 == z_computed_2, ("Excpeted %s, got %s" % (z_real_2, z_computed_2))

	
# Runs all test when test_complex.py is run directly
if __name__=="__main__":
	test_add_complex()	
	test_sub_complex()
	test_conjugate_complex()
	test_modulus_complex()
	test_eq_complex()
	test_radd_complex()
	test_rsub_complex()
	test_rmul_complex()