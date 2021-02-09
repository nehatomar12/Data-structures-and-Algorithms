import numpy as np

def MaximumMarks(marksarr, timearr, h, n, p) :

    no_of_topics = n + 1
    total_time = h + 1

    T = np.zeros((no_of_topics, total_time))

    # Initialization

    # If we are given 0 time
    # then nothing can be done
    # So all values are 0
    for i in range(no_of_topics) :
        T[i][0] = 0

    # If we are given 0 topics
    # then the time required
    # will be 0 for sure
    for j in range(total_time) :
        T[0][j] = 0

    # Calculating the maximum marks
    # that can be achieved under
    # the given time constraints
    for i in range(1, no_of_topics) :

        for j in range(1, total_time) :

            # If time taken to read that topic
            # is more than the time left now at
            # position j then do no read that topic
            if (j < timearr[i]) :

                T[i][j] = T[i - 1][j]

            else :

                """Two cases arise:
                1) Considering current topic
                2) Ignoring current topic
                We are finding maximum of (current topic weightage
                + topics which can be done in leftover time
                - current topic time)
                and ignoring current topic weightage sum
                """
                T[i][j] = max(marksarr[i] +
                              T[i - 1][j - timearr[i]],
                              T[i - 1][j])

    # Moving upwards in table from bottom right
    # to calculate the total time taken to
    # read the topics which can be done in
    # given time and have highest weightage sum
    i = no_of_topics - 1 j = total_time - 1

    sum = 0

    while (i > 0 and j > 0) :

        # It means we have not considered
        # reading this topic for
        # max weightage sum
        if (T[i][j] == T[i - 1][j]) :

            i -= 1

        else :

            # Adding the topic time
            sum += timearr[i]

            # Evaluating the left over time after
            # considering this current topic
            j -= timearr[i]

            # One topic completed
            i -= 1

    # It contains the maximum weightage sum
    # formed by considering the topics
    marks = T[no_of_topics - 1][total_time - 1]

    # Condition when exam cannot be passed
    if (marks < p) :
        return -1

    # Return the marks that
    # can be obtained after
    # passing the exam
    return sum

# Driver code
if __name__ == "__main__" :

    # Number of topics, hours left
    # and the passing marks
    n = 4
    h = 10
    p = 10

    # n+1 is taken for simplicity in loops
    # Array will be indexed starting from 1
    marksarr = [ 0, 6, 4, 2, 8 ]
    timearr = [ 0, 4, 6, 2, 7 ]

    print(MaximumMarks(marksarr, timearr, h, n, p))
