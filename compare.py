def minimum(value_a, value_b):
    if value_a < value_b:
        return value_a 
    else:
        return value_b 

def main():
    print("minimum of 1 and 2 is", minimum(1,2))
    print(minimum(1,2) == 1)
    print(minimum(1,1) == 1)

#if __name__ == "__main__":
 #   main()

main()