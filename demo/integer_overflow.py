import sys

def main():
    x = (sys.maxsize)*2-4

    print("What does integer overflow look like in Python?")
    for i in range(8):
        x += 1
        b = format(x,'b')
        print("decimal:",x,"-- binary:",b,"--",len(b),"bits.")

    print("int just adds more bits! No overflow!")

if __name__ == "__main__":
    main()