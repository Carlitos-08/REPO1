def vectores_paralelos(v1,v2):

    x1 , y1 = v1
    x2 , y2 = v2

    return x1 * y2 - y1 * x2 == 0


def main():

    v1 = (1,2)
    v2 = (2,4)

    print(vectores_paralelos(v1,v2))

main()