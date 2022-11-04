import index

def test_is_prime():
    assert index.is_prime(1) == False
    assert index.is_prime(2) == True
    assert index.is_prime(3) == True
    assert index.is_prime(4) == False
    assert index.is_prime(5) == True
    assert index.is_prime(6) == False
    assert index.is_prime(7) == True
    assert index.is_prime(8) == False
    assert index.is_prime(9) == False
    assert index.is_prime(10) == False
    assert index.is_prime(11) == True

def test_get_prime_list():
    assert index.get_prime_list(4567) == [467, 457]
    assert index.get_prime_list(4125673) == [415673, 412567]
    assert index.get_prime_list(45673) == [4673, 4567]
    assert index.get_prime_list(41257) == [4157, 4127]

def test_flatten_list():
    assert index.flatten_list([[67, 47], [47]]) == [67, 47, 47]
    assert index.flatten_list([[7], [7]]) == [7, 7]
    assert index.flatten_list([[673, 463, 467], [467, 457]]) == [673, 463, 467, 467, 457]
    assert index.flatten_list([[73, 67], [43], [67, 47], [67, 47], [47]]) == [73, 67, 43, 67, 47, 67, 47, 47]
    assert index.flatten_list([[3, 7], [7], [3], [7], [7], [7], [7], [7]]) == [3, 7, 7, 3, 7, 7, 7, 7, 7]
    assert index.flatten_list([[[7], [7]], [[7]]]) == [7, 7, 7]
    assert index.flatten_list([[[[7]], [[7]]], [[[7]]]]) == [7, 7, 7]
    assert index.flatten_list([[[[3, 7], [7]], [[3]], [[7], [7]]], [[[7], [7]], [[7]]]]) == [3, 7, 7, 3, 7, 7, 7, 7, 7]

def test_get_prime_digit_list():
    assert index.get_prime_digit_list(467) == [7, 7]
    assert index.get_prime_digit_list(457) == [7]
    assert index.get_prime_digit_list(45673) == [3, 7, 7, 3, 7, 7, 7, 7, 7]
    assert index.get_prime_digit_list(41257) == [7, 7, 7]
    assert index.get_prime_digit_list(4567) == [7, 7, 7]

def test_get_count():
    assert index.get_count(467) == 2
    assert index.get_count(457) == 1
    assert index.get_count(45673) == 9
    assert index.get_count(41257) == 3
    assert index.get_count(4567) == 3
    assert index.get_count(4125673) == 12
    assert index.get_count(41256793) == 21
    assert index.get_count(337424981) == 14
    assert index.get_count(537430451) == 3
    assert index.get_count(200899998) == 0
    assert index.get_count(537499093) == 8
    assert index.get_count(2147483059) == 8
    assert index.get_count(410256793) == 29
    assert index.get_count(567629137) == 84
    assert index.get_count(46216567629137) == 121
