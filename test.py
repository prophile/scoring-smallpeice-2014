from colours import calculate_scores

def test_empty():
    assert calculate_scores({}) == {}

def test_movement():
    assert calculate_scores({'aaa': {'moved': True}}) == {'aaa':1}

def test_golds():
    assert calculate_scores({'aaa': {'gold': 2}}) == {'aaa':4}

def test_silver():
    assert calculate_scores({'aaa': {'silver': 2}}) == {'aaa':4}

def test_combination():
    assert calculate_scores({'aaa': {'gold': 2,
                                     'silver': 2}}) == {'aaa':4}

