import sys
import math
import random
from collections import Counter

# Function to compute Euclidean distance between two feature vectors
def euclidean_distance(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))

# Main classifier function
def nn_classify(train_file, test_file, k=1):
    # Load training data
    with open(train_file) as f:
        training_data = [list(map(float, line.strip().split())) for line in f if line.strip()]

    # Load test data
    with open(test_file) as f:
        test_data = [list(map(float, line.strip().split())) for line in f if line.strip()]

    result_lines = []
    total_accuracy = 0

    for obj_id, test_obj in enumerate(test_data):
        test_features = test_obj[:-1]
        true_class = int(test_obj[-1])

        # Calculate distance to each training point
        distances = []
        for train_obj in training_data:
            train_features = train_obj[:-1]
            train_class = int(train_obj[-1])
            dist = euclidean_distance(test_features, train_features)
            distances.append((dist, train_class))

        # Find k-nearest neighbors
        distances.sort()
        nearest = [label for _, label in distances[:k]]
        class_votes = Counter(nearest)
        max_votes = max(class_votes.values())
        candidates = [cls for cls, count in class_votes.items() if count == max_votes]
        predicted_class = random.choice(candidates)

        # Determine accuracy
        if len(candidates) == 1:
            accuracy = 1.0 if predicted_class == true_class else 0.0
        else:
            accuracy = 1.0 / len(candidates) if true_class in candidates else 0.0

        total_accuracy += accuracy
        result_lines.append(f"objID = {obj_id} predicted class = {predicted_class} true class = {true_class} accuracy = {accuracy:.1f}")

    # Write results to result.txt
    with open("result.txt", "w") as f:
        f.write("\n".join(result_lines))

    # Print overall accuracy to stdout
    avg_accuracy = total_accuracy / len(test_data)
    print(f"Overall classification accuracy = {avg_accuracy:.5f}")

# Run from command line
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python knn_classifier.py <training-file> <test-file> [<k>]")
        sys.exit(1)

    train_file = sys.argv[1]
    test_file = sys.argv[2]
    k = int(sys.argv[3]) if len(sys.argv) >= 4 else 1
    nn_classify(train_file, test_file, k)
