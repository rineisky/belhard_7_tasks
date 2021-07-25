from tasks.phone import Phone


def test_creation():
    phone = Phone("brand", "model", 2020)

    assert hasattr(phone, "brand")
    assert phone.brand == "brand"
    assert hasattr(phone, "model")
    assert phone.model == "model"
    assert hasattr(phone, "issue_year")
    assert phone.issue_year == 2020

    assert hasattr(phone, "receive_call")
    assert hasattr(phone, "get_info")


def test_get_info():
    phone = Phone("brand", "model", 2020)
    assert phone.get_info() == ("brand", "model", 2020)
