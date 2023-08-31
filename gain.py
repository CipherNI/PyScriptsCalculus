import math

def calculate_entropy(positive, negative):
    total = positive + negative
    if positive == 0:
        p_positive = 0
    else:
        p_positive = -positive/total * math.log2(positive/total)

    if negative == 0:
        p_negative = 0
    else:
        p_negative = -negative/total * math.log2(negative/total)

    return p_positive + p_negative

def information_gain(original_entropy, subsets):
    total_samples = sum([pos + neg for pos, neg in subsets])
    weighted_entropy = sum([(pos + neg) / total_samples * calculate_entropy(pos, neg) for pos, neg in subsets])
    return original_entropy - weighted_entropy

def main():
    # Get inputs for the original dataset.
    original_positive = int(input("Enter the number of positive examples (+) for the original dataset: "))
    original_negative = int(input("Enter the number of negative examples (-) for the original dataset: "))
    original_entropy = calculate_entropy(original_positive, original_negative)

    # Get inputs for subsets.
    num_subsets = int(input("Enter the number of values (subsets) for the attribute you're considering: "))
    subsets = []
    for i in range(num_subsets):
        print(f"For subset {i + 1}:")
        positive = int(input("Enter the number of positive examples (+): "))
        negative = int(input("Enter the number of negative examples (-): "))
        subsets.append((positive, negative))

    ig = information_gain(original_entropy, subsets)
    print(f"Information Gain is: {ig:.3f}")

if __name__ == "__main__":
    main()
