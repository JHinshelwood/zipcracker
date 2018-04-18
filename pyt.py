import itertools

chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

reducedchars = [4, 2, 0, 'b', 'l', 'a', 'z', 'e']

#for L in range(0, len(reducedchars)+1):
#    for subset in itertools.combinations(reducedchars, L):
 #       print("h")

        
import subprocess
subprocess.call(["unzip", "-P", password, "books.zip"])
