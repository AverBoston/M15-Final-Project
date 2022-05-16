# Author: E. Avery Boston
# Date: 05/15/22
# Summary: function to allow customers to share feedback via input
#          and writes it to a file
# Variables:
#	review: holds the input so it can be written to file (str)


def feedback():
    # opens file for holding reviews
    sushiReviews_file = open("reviews.txt", "a")
    # variable for holding input so that it can be put into file
    review = input("Tell us what you thought of your last order! ")
    # writes input to file
    sushiReviews_file.write(review +'\n' + '\n')
    # closes file
    sushiReviews_file.close()
    # leaving message that thanks the user
    print("Thank you for your feedback!")
