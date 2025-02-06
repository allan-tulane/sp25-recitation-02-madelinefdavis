from main import *

def test_simple_work():
	""" done. """
	assert simple_work_calc(10, 2, 2) == 40
	assert simple_work_calc(20, 3, 2) == 270
	assert simple_work_calc(30, 4, 2) == 630

def test_work():
	assert work_calc(10, 2, 2, lambda n: 1) == 40
	assert work_calc(20, 1, 2, lambda n: n*n) == 530
	assert work_calc(30, 3, 2, lambda n: n) == 2110

def test_compare_work():
	# curry work_calc to create multiple work
	# functions taht can be passed to compare_work

	# create work_fn1
	# create work_fn2

  res = compare_work(work_fn1, work_fn2)
	print(res)


def test_compare_span():
	# TODO