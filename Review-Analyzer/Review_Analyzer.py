from string import punctuation, digits
import numpy as np
import random
from math import sqrt

# Part I


#pragma: coderesponse template
def get_order(n_samples):
    try:
        with open(str(n_samples) + '.txt') as fp:
            line = fp.readline()
            return list(map(int, line.split(',')))
    except FileNotFoundError:
        random.seed(1)
        indices = list(range(n_samples))
        random.shuffle(indices)
        return indices
#pragma: coderesponse end


#pragma: coderesponse template
def hinge_loss_single(feature_vector, label, theta, theta_0):
    z = label*(np.dot(feature_vector,theta) + theta_0)
    hinge_loss_single = 0
    if z >= 1 :
        return hinge_loss_single
    elif z < 1 :
        return 1 - z
    raise NotImplementedError
#pragma: coderesponse end


#pragma: coderesponse template
def hinge_loss_full(feature_matrix, labels, theta, theta_0):
    hinge_loss_full = 0
    shape = np.shape(feature_matrix)
    for i, feature_vector in enumerate(feature_matrix):
        z = labels[i]*(np.dot(feature_vector,theta) + theta_0)
        if z < 1 :
            hinge_loss_full += (1 - z)
    return hinge_loss_full / shape[0]
    raise NotImplementedError
#pragma: coderesponse end


#pragma: coderesponse template
def perceptron_single_step_update(
        feature_vector,
        label,
        current_theta,
        current_theta_0):

    for i in range(3):
        new_theta = current_theta
        new_theta_0 = current_theta_0
        if label * (np.dot(current_theta,feature_vector) + current_theta_0) <= 0:
            new_theta = new_theta + label*feature_vector
            new_theta_0 = new_theta_0 + label
    return new_theta,new_theta_0
    raise NotImplementedError
#pragma: coderesponse end


#pragma: coderesponse template
def perceptron(feature_matrix, labels, T):

    new_theta = np.zeros((feature_matrix.shape[1],))
    new_theta_0 = 0
    for t in range(T):
        for i in get_order(feature_matrix.shape[0]):
            updated_data = perceptron_single_step_update(feature_matrix[i],labels[i],new_theta,new_theta_0)
            new_theta = updated_data[0]
            new_theta_0 = updated_data[1]
            pass
    return new_theta,new_theta_0
    raise NotImplementedError
#pragma: coderesponse end


#pragma: coderesponse template
def average_perceptron(feature_matrix, labels, T):

    new_theta = np.zeros((feature_matrix.shape[1],))
    new_theta_0 = 0
    sum_of_theta = new_theta
    sum_of_theta_0 = new_theta_0
    for t in range(T):
        for i in get_order(feature_matrix.shape[0]):
            updated_data = perceptron_single_step_update(feature_matrix[i],labels[i],new_theta,new_theta_0)
            new_theta = updated_data[0]
            new_theta_0 = updated_data[1]
            sum_of_theta += new_theta
            sum_of_theta_0 += new_theta_0
            pass
    return sum_of_theta/(feature_matrix.shape[0]*T), sum_of_theta_0/(feature_matrix.shape[0]*T)
    raise NotImplementedError
#pragma: coderesponse end


#pragma: coderesponse template
def pegasos_single_step_update(
        feature_vector,
        label,
        L,
        eta,
        current_theta,
        current_theta_0):

    for i in range(3):
        new_theta = current_theta
        new_theta_0 = current_theta_0
        if label * (np.dot(current_theta,feature_vector) + current_theta_0) <= 1:
            new_theta = new_theta*(1 - eta*L) + eta*label*feature_vector
            new_theta_0 = new_theta_0 + eta*label
        else:
            new_theta = (1 - eta*L)*new_theta
            new_theta_0 = new_theta_0
    return new_theta,new_theta_0
    raise NotImplementedError
#pragma: coderesponse end


#pragma: coderesponse template
def pegasos(feature_matrix, labels, T, L):

    new_theta = np.zeros((feature_matrix.shape[1],))
    new_theta_0 = 0
    update_count = 1
    for t in range(T):
        for i, feature_vector in enumerate(feature_matrix):
            eta = 1/sqrt(update_count)
            if labels[i] * (np.dot(new_theta,feature_vector) + new_theta_0) <= 1:
                new_theta = new_theta*(1 - eta*L) + eta*labels[i]*feature_vector
                new_theta_0 = new_theta_0 + eta*labels[i]
                update_count += 1
            else:
                new_theta = (1 - eta*L)*new_theta
                new_theta_0 = new_theta_0
                update_count += 1
    return new_theta, new_theta_0
    raise NotImplementedError
#pragma: coderesponse end

# Part II


#pragma: coderesponse template
def classify(feature_matrix, theta, theta_0):
    """
    A classification function that uses theta and theta_0 to classify a set of
    data points.

    Args:
        feature_matrix - A numpy matrix describing the given data. Each row
            represents a single data point.
                theta - A numpy array describing the linear classifier.
        theta - A numpy array describing the linear classifier.
        theta_0 - A real valued number representing the offset parameter.

    Returns: A numpy array of 1s and -1s where the kth element of the array is
    the predicted classification of the kth row of the feature matrix using the
    given theta and theta_0. If a prediction is GREATER THAN zero, it should
    be considered a positive classification.
    """
    # Your code here
    raise NotImplementedError
#pragma: coderesponse end


#pragma: coderesponse template
def classifier_accuracy(
        classifier,
        train_feature_matrix,
        val_feature_matrix,
        train_labels,
        val_labels,
        **kwargs):
    """
    Trains a linear classifier using the perceptron algorithm with a given T
    value. The classifier is trained on the train data. The classifier's
    accuracy on the train and validation data is then returned.

    Args:
        classifier - A classifier function that takes arguments
            (feature matrix, labels, **kwargs)
        train_feature_matrix - A numpy matrix describing the training
            data. Each row represents a single data point.
        val_feature_matrix - A numpy matrix describing the training
            data. Each row represents a single data point.
        train_labels - A numpy array where the kth element of the array
            is the correct classification of the kth row of the training
            feature matrix.
        val_labels - A numpy array where the kth element of the array
            is the correct classification of the kth row of the validation
            feature matrix.
        **kwargs - Additional named arguments to pass to the classifier
            (e.g. T or L)

    Returns: A tuple in which the first element is the (scalar) accuracy of the
    trained classifier on the training data and the second element is the
    accuracy of the trained classifier on the validation data.
    """
    # Your code here
    raise NotImplementedError
#pragma: coderesponse end


#pragma: coderesponse template
def extract_words(input_string):
    """
    Helper function for bag_of_words()
    Inputs a text string
    Returns a list of lowercase words in the string.
    Punctuation and digits are separated out into their own words.
    """
    for c in punctuation + digits:
        input_string = input_string.replace(c, ' ' + c + ' ')

    return input_string.lower().split()
#pragma: coderesponse end


#pragma: coderesponse template
def bag_of_words(texts):
    """
    Inputs a list of string reviews
    Returns a dictionary of unique unigrams occurring over the input

    Feel free to change this code as guided by Problem 9
    """
    # Your code here
    dictionary = {} # maps word to unique index
    for text in texts:
        word_list = extract_words(text)
        for word in word_list:
            if word not in dictionary:
                dictionary[word] = len(dictionary)
    return dictionary
#pragma: coderesponse end


#pragma: coderesponse template
def extract_bow_feature_vectors(reviews, dictionary):
    """
    Inputs a list of string reviews
    Inputs the dictionary of words as given by bag_of_words
    Returns the bag-of-words feature matrix representation of the data.
    The returned matrix is of shape (n, m), where n is the number of reviews
    and m the total number of entries in the dictionary.

    Feel free to change this code as guided by Problem 9
    """
    # Your code here

    num_reviews = len(reviews)
    feature_matrix = np.zeros([num_reviews, len(dictionary)])

    for i, text in enumerate(reviews):
        word_list = extract_words(text)
        for word in word_list:
            if word in dictionary:
                feature_matrix[i, dictionary[word]] = 1
    return feature_matrix
#pragma: coderesponse end


#pragma: coderesponse template
def accuracy(preds, targets):
    """
    Given length-N vectors containing predicted and target labels,
    returns the percentage and number of correct predictions.
    """
    return (preds == targets).mean()
#pragma: coderesponse end