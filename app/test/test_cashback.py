from app.cashback import cashback


def test_cachback_under_limit():
    result = cashback(1_000)

    assert 50 == result
