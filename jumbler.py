"""jumbler:  List dictionary words that match an anagram.
2022-06-25 by Your Name Here

Credits: 
"""

""" EXAMPLE OF ERROR: when we don't have a file in the same directory
dict_file2 = open("words.txt") """

# DICT = "shortdict.txt"    # Short version for testing & debugging
DICT = "dict.txt"           # Full dictionary word 

def find(anagram: str):     #defining our find() function
    """
    Print words in DICT that match anagram.
  
    >>> find("AgEmo")
    omega
  
    >>> find("nosuchword")

    >>> find("alpha")
    alpha

    >>> find("KAWEA")
    awake
  
    """
    dict_file = open(DICT, "r") #opening dictionary file
    for line in dict_file:      #looping through each word to see if we have a match
        word = line.strip()     #stripping new lines in dictionary file
        if normalize(word) == normalize(anagram):    #checking to see if we have a match, if we do we print the dictionary word
            print(word)

def normalize(word: str) -> list[str]:    #defining our normalize() function
    """
    Returns a list of characters that is canonical for anagrams.
    
    >>> normalize("gamma") == normalize("magam")
    True
    
    >>> normalize("MAGAM") == normalize("gamma")
    True
    
    >>> normalize("KAWEA") == normalize("awake")
    True
    
    >>> normalize("KAWEA") == normalize("gamma")
    False
    """
    word = word.upper()    #converting every word to upper case letters
    return sorted(word)    #returning the upper cased word

def main(): 
    anagram = input("Anagram to find> ")    #asking user to input an anagram
    find(anagram)                           #pluggin the input word into our find() function to find a match

if __name__ == "__main__":
    main()
    #import doctest
    #doctest.testmod()
    #print("Doctests complete!")





    
