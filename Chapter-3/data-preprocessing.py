# Mini Project: Text Preprocessing for Sentiment Analysis
# Objective

# Build a text cleaner + basic sentiment analyzer using only:

# string functions
# lists
# conditions

# No ML libraries yet.

# 🧠 Problem Statement

# You are given user reviews like:

# "I LOVE this product!!!"
# "This is BAD and horrible"
# "  Amazing quality, very good  "

# You must:

# Clean the text
# Convert into tokens (words)
import re

positive_words = ["good", "love", "amazing"]
negative_words = ["bad", "horrible"]

while True:
    try:
        text = input("\nEnter review (type 'exit' to stop): ")
    except EOFError:
        print("\nNo input received. Program stopped.")
        break

    if text.lower() == "exit":
        print("Program stopped.")
        break
   
    # Step 1: Clean
    clean = text.strip().lower()
    output = re.sub(r'[^\w\s]', '', clean)
    print("Cleaned:", output)

    # Step 2: Tokenize
    words = output.split()
    print("Word count:", len(words))

    # Step 3: Count sentiment
    pos_count = 0
    neg_count = 0

    for word in words:
        if word in positive_words:
            pos_count += 1
        elif word in negative_words:
            neg_count += 1

    print("Positive words:", pos_count)
    print("Negative words:", neg_count)

    # Step 4: Decision
    if pos_count > neg_count:
        print("Positive review")
    elif neg_count > pos_count:
        print("Negative review")
    else:
        print("Neutral review")









# Count positive & negative words



# Output sentiment: Positive / Negative / Neutral
