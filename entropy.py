import math

def calculate_entropy(positive, negative):
    total = positive + negative

    # Check if positive or negative are 0 to handle log(0) which is undefined.
    if positive == 0:
        p_positive = 0
    else:
        p_positive = -positive/total * math.log2(positive/total)

    if negative == 0:
        p_negative = 0
    else:
        p_negative = -negative/total * math.log2(negative/total)

    return p_positive + p_negative

def main():
    # Get inputs from the user.
    positive = int(input("Enter the number of positive examples (+): "))
    negative = int(input("Enter the number of negative examples (-): "))

    entropy = calculate_entropy(positive, negative)
    print(f"Entropy for {positive}+ and {negative}- is: {entropy:.4f}")

if __name__ == "__main__":
    main()
