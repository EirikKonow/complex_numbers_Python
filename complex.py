#!/usr/bin/env python3
from math import sqrt

class Complex:
	"""
	A class used to represent complex numbers
	
	Attributes
	----------
	re : float, int
		The real part of the complex number
	im=0 : float, int
		The imaginary part of the complex number
	
	Methods
	-------
	conjugate()
		Conjugates the complex number
	modulus()
		Gives the "length" of the complex number
	__add__()
		Adds complex numbers together
	__sub__()
		Subtracts complex numbers
	__mul__()
		Multiplies complex numbers, or a real number with a complex
	__eq__()
		Checks if two complex numbers are equal
	__radd__()
		Handels right-side addition
	__rsub__()
		Handles right-side subtraction
	__rmul__()
		Handles right-side multiplication
	__neg__()
		Gives a negative version of the complex number
	__complex__()
		Makes the python 'complex' function able
		to convert from our version of complex
	__str__()
		Handles string representation
	__call__()
		Handles calls for the complex number
	"""
	

	def __init__(self, re, im=0):
		"""
		Parameters
		----------
		re : float, int
			The real part of the complex number
		im : float, int, optional
			The imaginary part of the complex number (default is 0)
		"""
		
		self.re = re
		self.im = im


	def conjugate(self) -> 'Complex':
		"""Conjugates the complex number."""
		
		ac = self.re
		bc = self.im * (-1)
		return Complex(ac, bc)


	def modulus(self) -> float:
		"""Gives the "length" of the complex number."""
		
		ac = self.re**2
		bc = self.im**2
		c = sqrt(ac + bc)
		return c


	def __add__(self, other) -> 'Complex':
		"""Adds complex numbers together."""
		
		if isinstance(other, (float, int)):
			other = Complex(other)
		if isinstance(other, complex):
			other = Complex(other.real, other.imag)
			
		ac = self.re + other.re
		bc = self.im + other.im
		return Complex(ac, bc)


	def __sub__(self, other) -> 'Complex':
		"""Subtracts complex numbers."""
		
		if isinstance(other, (float, int)):
			other = Complex(other)
		if isinstance(other, complex):
			other = Complex(other.real, other.imag)
			
		ac = self.re - other.re
		bc = self.im - other.im
		return Complex(ac, bc)


	def __mul__(self, other) -> 'Complex':
		"""Multiplies complex numbers, or a real number with a complex."""
		
		if isinstance(other, (float, int)):
			# Direct answer since z*re != z*(re +0i)
			return(Complex(other*self.re, other*self.im))
		if isinstance(other, complex):
			other = Complex(other.real, other.imag)
			
		ac = self.re * other.re - self.im * other.im
		bc = self.re * other.im + self.im * other.re
		return Complex(ac, bc)


	def __eq__(self, other) -> bool:
		"""Checks if two complex numbers are equal."""
		
		if isinstance(other, (float, int)):
			other = Complex(other)
		if isinstance(other, complex):
			other = Complex(other.real, other.imag)
			
		if (self.re == other.re and self.im == other.im):
			return True
		else:
			return False


	def __radd__(self, other) -> 'Complex':
		"""Handels right-side addition."""
		
		return(self+other)
	
	
	def __rsub__(self, other) -> 'Complex':
		"""Handles right-side subtraction."""
		
		return(-self+other)

	
	def __rmul__(self, other) -> 'Complex':
		"""Handles right-side multiplication."""
		
		return(self*other)


	# Optional, possibly useful methods

	# Allows you to write `-a`
	def __neg__(self) -> 'Complex':
		"""Gives a negative version of the complex number."""
		
		return(Complex((-1)*self.re, (-1*(self.im))))


	# Make the `complex` function turn this into Python's version of a complex number
	def __complex__(self) -> complex:
		"""Makes the python 'complex' function able
		to convert from our version of complex"""
		
		return complex(self.re, self.im)


	def __str__(self) -> str:
		"""Handles string representation."""
		
		if self.im < 0:
			sign = "-"
		else:
			sign = "+"
			
		string = "(%d %s %di)" % (self.re, sign, abs(self.im))
		return string
	
	
	def __call__(self) -> tuple:
		"""Handles calls for the complex number."""
		return (self.re, self.im)