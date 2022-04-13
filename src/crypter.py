# Word encrypter by micziz

# Version: 0.0.1
# Creator: micziz
# Liscence: GNU GPL 3.0


# Import required modules
# Random used for shuffuling, string for getting words
from random import *
from string import *

# Get the word to encrypt, in list form, so we can shuffle, and assign it to the inp variable
inp = list(input("Input the word to be encrypted: "))
# Get the security that the user wants
security = input("Security (bad, medium, great, strict): ")
# Get the length of the input, required for random.sample()
leninp = len(inp)
# Generate function
def generate(n, kk): # The args passed are n and kk
    # Shufflue word, with the two args
    temp = sample(n, kk)
    # Salt function
    def salt(f):
        # Bad security
        if f == "bad":
            # Length of the salt
            length = 5 # 5 for bad
            # Get letters
            all = ascii_letters
            # Shuffle letters
            tempp = sample(all,length)
            # Return salt
            return "".join(tempp)
        # Medium security
        elif f == "medium":
            # Length of the salt
            length = 10 # 10 for medium
            # Get letters
            all = ascii_letters
            # Shuffle letters
            tempp = sample(all,length)
            # Return salt
            return "".join(tempp)
        # Great security
        elif f == "great":
            # Length of the salt
            length = 15 # 15 for great
            # Get letters
            letters = ascii_letters
            # Get numbers
            numbers = digits
            # Join everything
            all = letters + numbers
            # Shuffle letters and numbers
            tempp = sample(all,length)
            # Return salt
            return "".join(tempp)
        # Strict security
        elif f == "strict":
            # Salt length
            length = 20 # 20 for strict
            letters = ascii_letters
            numbers = digits
            punctuations = punctuation
            # Get letters
            all = letters + numbers + punctuations
            # Shuffle letters
            tempp = sample(all,length)
            # Return salt
            return "".join(tempp)
        else:
            return ' '
    # Call salt and set it to a variable
    saltt = salt(security)
    # Append salt to the word
    temp.append(saltt)
    # Join everything, and join all spaces
    encrypted = "".join(temp)
    # Print the encrypted thing
    print(encrypted)
# Call generate
generate(inp, leninp) # Pass inp and leninp as arg