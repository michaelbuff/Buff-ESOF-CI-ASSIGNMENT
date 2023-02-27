def add(a, b):
    return a +b

def test_add():
    assert add(2,3) == 5
    assert add("space", "ship") == "spaceship"



def main():
    print("Hope this is good enough")

if __name__ == "__main__":
    main()