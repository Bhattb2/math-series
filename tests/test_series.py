from math_series.series_module import fibonacci,  fibonacci2, lucas, lucas2, sum_series, sum_series2

def test_import():
    assert fibonacci
    assert fibonacci2
    assert lucas
    assert lucas2
    assert sum_series
    assert sum_series2

def test_fibonacci_0():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_fibonacci_1():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_fibonacci_2():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected

def test_fibonacci_3():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected

def test_fibonacci_10():
    actual = fibonacci(10)
    expected = 55
    assert actual == expected

def test_fibonacci2_0():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_fibonacci2_1():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_fibonacci2_2():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected

def test_fibonacci2_3():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected

def test_fibonacci2_10():
    actual = fibonacci(10)
    expected = 55
    assert actual == expected

def test_lucas_0():
    actual = lucas(0)
    expected = 2
    assert actual == expected  

def test_lucas_1():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_lucas_2():
    actual = lucas(2)
    expected = 3
    assert actual == expected

def test_lucas_10():
    actual = lucas(10)
    expected = 123
    assert actual == expected 

def test_lucas2_0():
    actual = lucas(0)
    expected = 2
    assert actual == expected 

def test_lucas2_1():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_lucas2_2():
    actual = lucas(2)
    expected = 3
    assert actual == expected

def test_lucas2_3():
    actual = lucas(3)
    expected = 4
    assert actual == expected

def test_lucas2_10():
    actual = lucas(10)
    expected = 123
    assert actual == expected

def test_sum_series_0():
    actual = sum_series(0)
    expected = 0
    assert actual == expected

def test_sum_series_1():
    actual = sum_series(1)
    expected = 1
    assert actual == expected  

def test_sum_series_2():
    actual = sum_series(2)
    expected = 1
    assert actual == expected  

def test_sum_series_3():
    actual = sum_series(3)
    expected = 2
    assert actual == expected

def test_sum_series_10():
    actual = sum_series(10)
    expected = 55
    assert actual == expected

def test_sum_series_0():
    actual = sum_series(0, 2, 1)
    expected = 2
    assert actual == expected

def test_sum_series_1():
    actual = sum_series(1, 2, 1)
    expected = 1
    assert actual == expected

def test_sum_series_2():
    actual = sum_series(2, 2, 1)
    expected = 3
    assert actual == expected

def test_sum_series_3():
    actual = sum_series(3, 2, 1)
    expected = 4
    assert actual == expected

def test_sum_series_10():
    actual = sum_series(10, 2, 1)
    expected = 123
    assert actual == expected

def test_sum_series2_0():
    actual = sum_series(0)
    expected =0
    assert actual == expected

def test_sum_series2_1():
    actual = sum_series(1)
    expected =1
    assert actual == expected

def test_sum_series2_2():
    actual = sum_series(2)
    expected =1
    assert actual == expected

def test_sum_series2_3():
    actual = sum_series(3)
    expected =2
    assert actual == expected

def test_sum_series2_10():
    actual = sum_series(10)
    expected =55
    assert actual == expected

def test_sum_series2_0():
    actual = sum_series(0, 2, 1)
    expected =2
    assert actual == expected

def test_sum_series2_0():
    actual = sum_series(1, 2, 1)
    expected =1
    assert actual == expected

def test_sum_series2_0():
    actual = sum_series(2, 2 ,1)
    expected =3
    assert actual == expected

def test_sum_series2_0():
    actual = sum_series(3, 2, 1)
    expected =4
    assert actual == expected

def test_sum_series2_0():
    actual = sum_series(10, 2, 1)
    expected =123
    assert actual == expected