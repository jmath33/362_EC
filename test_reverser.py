import pytest
import reverser

def test_rev():
	assert (rev("Will this reverse")) == ("reverse this Will")

def test_rev_1():
	assert (rev("sense. make doesn't This")) == ("This doesn't make sense.")

#designed to fail
def test_rev_2():
	assert (rev("Reverse this.")) == ("this Reverse.")

