from lenormju.meteo import should_i_bring_a_jacket

def test_should_i_bring_a_jacket() -> None:
    should_i = should_i_bring_a_jacket()
    assert should_i == "Definitely!"
