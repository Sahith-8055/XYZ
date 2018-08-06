"""Exercise: eval quadratic. This function takes in four numbers and returns a single number."""
def eval_quadratic(a_in, b_in, c_in, x_in):
    """square"""
    return a_in*(x_in**2) + b_in*x_in + c_in
def main():
    """Writing inside this function"""
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    for x_i in range(len((data))):
        temp = str(data[x_i]).split('.')
        if temp[1] == '0':
            data[x_i] = int(float(str(data[x_i])))
        else:
            data[x_i] = data[x_i]
    print(eval_quadratic(data[0], data[1], data[2], data[3]))
if __name__ == "__main__":
    main()
