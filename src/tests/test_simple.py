from json.tool import main
import random
from text_classification import main as m


def test_main():
    rand1 = random.seed(1)
    rand2 = random.seed(2)
    
    eval1 = m(rand1)
    eval2 = m(rand2)
    
    if(abs(eval1 - eval2) > 0.1):
        print("test failed")
    else:
        print("test succeeded")
      
    

if __name__ == "__main__":
    main()