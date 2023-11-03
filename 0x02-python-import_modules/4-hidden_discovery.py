#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
   hidden_names = dir(hidden_4)
    for i in hidden_names:
        if i[:2] != "__":
            print(i)
