

#%% Exercise 1

from Excercise_1 import recalculate_quality, ham

def test_lessthan5_recalculation1():
 
    recalculate_quality(ham)
    assert ham.quality == 1
    
    

    
    

    

    
from Excercise_1 import recalculate_quality, carrot    
    
def test_zero_quality_product():
    
    recalculate_quality(carrot)
    assert carrot.quality == 0
    
#%% Excersise 1
    
from Excercise_1 import recalculate_quality, potatoe, potato, potato2, potato1, cheese, cheese1, cheese2, pasta, pasta1, pasta2

    
def test_defined_product():
    
    recalculate_quality(potatoe)
    assert potatoe.quality == 9.5
    
def test_after_one_potato_recalculations(): 
    recalculate_quality(potato)
    recalculate_quality(potato1)
    recalculate_quality(potato2)
    assert potato.quality == 9.5
    assert potato1.quality == 99.5
    assert potato2.quality == 0

def test_after_two_potato_recalculations():
    recalculate_quality(potato)
    recalculate_quality(potato1)
    assert potato.quality == 9
    assert potato1.quality == 99
    
def test_after_one_cheese_recalculations(): 
    recalculate_quality(cheese)
    recalculate_quality(cheese1)
    assert cheese.quality == 8
    assert cheese1.quality == 98

    
def test_after_two_cheese_recalculations(): 
    recalculate_quality(cheese)
    recalculate_quality(cheese1)
    assert cheese.quality == 6
    assert cheese1.quality == 96
    

def test_after_unknown_product_recalculations(): 
    recalculate_quality(pasta)
    recalculate_quality(pasta1)
    assert pasta.quality == 1
#    inmmutable cause no if statements
    assert pasta1.quality == 20
    assert pasta2.quality == 5

def test_after_unknown_product_recalculation_bellow_zero(): 
    recalculate_quality(pasta)
    assert pasta.quality == -2