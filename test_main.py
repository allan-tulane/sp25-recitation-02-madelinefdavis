from main import *

def test_simple_work():
	""" done. """
	assert simple_work_calc(10, 2, 2) == 36
	assert simple_work_calc(20, 3, 2) == 230
	assert simple_work_calc(30, 4, 2) == 650
	#additional tests
	assert simple_work_calc(100, 2, 2) == 652
	assert simple_work_calc(20,2,4) == 34
	assert simple_work_calc(20,4,2) == 524

def test_work():
	assert work_calc(10, 2, 2, lambda n: 1) == 15
	assert work_calc(20, 1, 2, lambda n: n*n) == 530
	assert work_calc(30, 3, 2, lambda n: n) == 300
	#additional tests
	assert work_calc(100, 2, 2, lambda n: 1) == 127
	assert work_calc(100, 2, 2, lambda n: n) == 652
	assert work_calc(100, 2, 2, lambda n: n*n) == 19580

def test_compare_work():
	# Test different work functions with smaller sizes for quick testing
	work_fn1 = lambda n: work_calc(n, 2, 2, lambda x: 1)
	work_fn2 = lambda n: work_calc(n, 2, 2, lambda x: x*x)
	
	sizes = [10, 20, 50, 100]  # Using smaller sizes for quick testing
	res = compare_work(work_fn1, work_fn2, sizes)
	print("\nComparison of work functions:")
	print_results(res)
	
	assert len(res) > 0, "Results should not be empty"
#compare_work(lambda n:n, lambda n: math.log(n))
#compare_work(lambda n: n ** 2, lambda n: n ** 1.5)
#compare_work(lambda n: n ** 0.5, lambda n: n ** 3.5)
	


def test_compare_span():
	span_fn1 = lambda n: span_calc(n, 2, 2, lambda x: x)
	span_fn2 = lambda n: span_calc(n, 2, 2, lambda x: 1)

	res = compare_span(span_fn1, span_fn2)
	print_results(res)

	for n, s1, s2 in res:
		assert s1 >= s2, f"Failed at n={n}: S1={s1}, S2={s2}"
	
		
