"""
This script checks the solution file against your output file and prints the number of lines that are unique to each file.
You need to adjust the paths to the files to check.
"""

def find_unique_entries(file1_path, file2_path):
    # Read the contents of both files into sets
    with open(file1_path, 'r') as file1:
        entries1 = set(file1.read().splitlines())
    
    with open(file2_path, 'r') as file2:
        entries2 = set(file2.read().splitlines())

    # Find entries unique to each file
    unique_to_file1 = entries1 - entries2
    unique_to_file2 = entries2 - entries1

    return unique_to_file1, unique_to_file2

def checkSolution(inputFile, solutionFile):
    unique1, unique2 = find_unique_entries(inputFile, solutionFile)
    print("Unique to input file: ", len(unique1))
    print("Unique to solution file: ", len(unique2))
    print("Total wrong lines: ", len(unique1)+len(unique2))
    return len(unique1)+len(unique2)


# path to the file to check
inputFile = "output.txt"

# path to solution file
solutionFile = "training-data/1/output.txt"

checkSolution(inputFile, solutionFile)
    