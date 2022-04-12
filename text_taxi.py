from SearchAlgorithms import AEstrela
from Taxi import Taxi
from datetime import date, datetime


def test_1():
    passanger = [0,0]
    destiny = [4,0]
    blocks = []
    size = 5
    state = Taxi([0,2],passanger,destiny,blocks,size, False,'')
    algorithm = AEstrela()
    result = algorithm.search(state)
    r = result.show_path()
    assert r == " ; left ; left ; pegou ; down ; down ; down ; down"

def test_2():
    passanger = [0,0]
    destiny = [4,0]
    blocks = [[0,1]]
    size = 5
    state = Taxi([0,2],passanger,destiny,blocks,size, False,'')
    algorithm = AEstrela()
    result = algorithm.search(state)
    r = result.show_path()
    assert r == " ; down ; left ; left ; up ; pegou ; down ; down ; down ; down"

def test_3():
    passanger = [0,0]
    destiny = [4,0]
    blocks = [[0,1],[1,1]]
    size = 5
    state = Taxi([0,2],passanger,destiny,blocks,size, False,'')
    algorithm = AEstrela()
    result = algorithm.search(state)
    r = result.show_path()
    assert r == " ; down ; down ; left ; left ; up ; up ; pegou ; down ; down ; down ; down"
