
import matplotlib.pyplot as plt
import UniformDistr

def main():
    randList = UniformDistr.randomNum(10000)

    stocksList = []
    # 0 for increase, 1 for decrease, 2 for stays the same
    for i in randList:
        if i < 0.1:
            stocksList.append(15)
        elif i < 0.3:
            stocksList.append(100)
        elif i < 0.6:
            stocksList.append(-100)
        elif i < 1:
            stocksList.append(200)

        # Plot the distribution
    plt.title("Frequencies of Stock Performance")
    plt.ylabel("Frequency")
    plt.xlabel("Stock Value (k)")
    labels = [15, 100, -100, 200]
    plt.hist(stocksList, bins=len(labels), align="mid", rwidth=0.9, edgecolor="black",
             range=(min(labels) - 10, max(labels) + 10))
    plt.xticks(labels)
    plt.show()

    # Print the frequencies
    print("Frequencies of Stock Performance:")
    for label in labels:
        print(f"{label}: {stocksList.count(label)}")

if __name__ == "__main__":
    main()