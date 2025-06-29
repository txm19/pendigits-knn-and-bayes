# pendigits-knn-and-bayes
A two-part machine learning project using the UCI PenDigits dataset: Task 1 implements Bayesian posterior probability computation, and Task 2 applies a k-nearest neighbors (k-NN) classifier for handwritten digit recognition.

Language: Python 3.10  

TASK1:
How to run:
------------
1. Open terminal and navigate to the `task1` folder.
2. Run the script with the command:

   python compute_posterior.py CCLLLLLLCCCC

3. The result will be saved to `result.txt` in the same folder.

If no argument is given (i.e., run as `python compute_posterior.py`), the program will assume no observations and generate output accordingly.

Omega Compatibility: Yes, this runs on ACS Omega.

TASK2:
How the code is structured:
----------------------------
- knn_classifier.py:
  This file contains the full implementation of the k-nearest neighbor (k-NN) classifier.
  It reads a training dataset and test dataset from text files, performs k-NN classification,
  and writes the classification results to result.txt.

- result.txt:
  Contains prediction results for each test object, including object ID, predicted class, true class, and accuracy.

How to run:
-----------
1. Open the terminal and navigate to the 'task2' folder.
2. Make sure the datasets are in a folder named 'datasets' located at the same level as task1 and task2.
3. Run the script using the following command:

   python knn_classifier.py ../datasets/pendigits_training.txt ../datasets/pendigits_test.txt 3

   (You can change the file names and value of k as needed.)

Output:
-------
- The program prints the overall classification accuracy to standard output.
- A file named result.txt will be created in the same directory, containing detailed prediction results.

Omega Compatibility:
--------------------
Yes, this code runs on the ACS Omega system (tested with Python 3.10).
