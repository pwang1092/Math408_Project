
import random
import matplotlib.pyplot as plt
import random
import numpy

seed = 1000
a = pow(7, 5)
c = 0
m = pow(2, 31) - 1

def randomNum(num):
    # constants and list to store the random numbers
    list = []

    global seed
    global a
    global c
    global m

    # generate the random numbers
    curr_x = (a * seed + c) % m
    list.append(curr_x / m)
    for i in range(0, num):
        curr_x = (a * curr_x + c) % m
        list.append(curr_x / m )

    # update seed
    seed = list[len(list)-1]
    return list


# plot probabilities against x
def plotList(intervals, randList, title=""):
    plt.xlabel("Random Values")
    plt.ylabel("Probability")

    n, bins, rects = plt.hist(randList, bins=intervals, edgecolor="black", rwidth=0.9)

    for r in rects:
        r.set_height(r.get_height() / 10000)
    plt.ylim(0, 1/intervals * 2)
    plt.title(title)
    plt.show()


def plotPairs(randList, title="Pair Plot"):
    # Prepare x and y values for the pairs
    x_vals = randList[0:9998]  # u1, u2, ..., u(n-1)
    y_vals = randList[1:9999]  # u2, u3, ..., un

    # Plot the pairs
    plt.figure(figsize=(8, 8))
    plt.scatter(x_vals, y_vals, s=1, alpha=0.5)
    plt.title(title)
    plt.xlabel("u_i")
    plt.ylabel("u_(i+1)")
    plt.grid(True)
    plt.show()


def main():
    # generate 10000 random using our own generator
    randList = randomNum(10000)

    # plot the list made with our random generator
    plotList(20, randList, "Uniform random generator made from scratch")

    # use library to get 10000 random numbers and plot them
    print()
    libraryList = []
    for i in range(0, 10000):
        libraryList.append(random.uniform(0, 1))
    plotList(20, libraryList, "Python library uniform distribution")

    # now we compare the lists
    print("Average of our list: ", numpy.average(randList))
    print("Average of library list: ", numpy.average(libraryList))
    print("Variance of our list: ", numpy.var(randList))
    print("Variance of library list: ", numpy.var(libraryList))

    plotPairs(randList, "Pair Plot of Custom Random Generator")
    plotPairs(libraryList, "Pair Plot of Custom Random Generator")

if __name__ == "__main__":
    main()


