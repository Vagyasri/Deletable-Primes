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

def test_list_of_list():
    assert index.list_of_list([467, 457]) == [[67, 47], [47]]
    assert index.list_of_list([415673, 412567]) == [[45673], [41257]]
    assert index.list_of_list([4673, 4567]) == [[673, 463, 467], [467, 457]]
    assert index.list_of_list([673, 463, 467, 467, 457]) == [[73, 67], [43], [67, 47], [67, 47], [47]]
    assert index.list_of_list([73, 67, 43, 67, 47, 67, 47, 47]) == [[3, 7], [7], [3], [7], [7], [7], [7], [7]]

def xtest_get_ways_count():
    assert index.get_ways_count(467) == 2
    assert index.get_ways_count(457) == 1
    assert index.get_ways_count(45673) == 9
    assert index.get_ways_count(41257) == 1
    assert index.get_ways_count(4567) == 3