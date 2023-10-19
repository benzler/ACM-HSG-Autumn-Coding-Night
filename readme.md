# ACM HSG Autumn Coding Night
Welcome to the ACM HSG Autumn Coding Night! This is a repository for the event. You can find the data, slides and some sample code here.

## **Setup**
Before starting please make sure that you have the following installed:
- Python
- Pandas
- Scikit-learn
- Matplotlib
- Seaborn

## **Task**
The goal is to write a python script to detect fraudulent transactions. The group that detects the most amount of correct transactions wins. The script should take the filepath to the input file as an argument and write the transaction ids of the detected frauds to a text file in the required structure. The output should be one single output text file containing the ids of fraudulent transactions, one per line.

### **Suggested Approach**
1. Fork or download the repository
2. Examine the training data (data structure, plots, etc.)
3. Write one or multiple scripts (with or without ML) to detect frauds
4. Make sure the script is able to import and export the data in the correct format
5. Analyze the results to decide on a script
6. Run the script on the competition data
7. Submit the output file

**Additional Challenge:**
- Make sure that the script runs as fast as possible
- Try to lower the false-positive rate


## 📚 **Resources**
### 📊 **Training Data**
You can find the training data in the `training-data` folder. There is a data set describing the terminals and one that contains all customer data. Then there are two transaction folders. One containing all the inputs and another one with the outputs. For each day there is one input and one output file. The input file contains all the transactions that happened on that day. The output file contains all the transaction ids that were marked as frauds.

To be able to start faster we also provide you the raw files for the training data set where for each transaction it is already stated in the dataframe whether it is a transaction or not. You can find the files in the `simulated-training-data-raw` folder.

### 📝 **Code Samples**
For the beginners there are code samples in the `introduction` folder. The code samples show you how to import from the data files, how to use pandas, how to analyze the dataframes with plots and how to use scikit-learn.

### 📝 **Slides**
You can find the slides in the `resources/slides` folder.

### 📚 **Links**
You can find some useful links in the `resources/links.md` file.
