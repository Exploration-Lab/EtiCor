## Eticor
**Access**

To access the dataset, please fill out the following Google form: link: https://forms.gle/NRr6zpdF71qwoEYq8. You will receive an email with a link to the dataset within one week.

**Dataset**

The Eticor dataset is a collection of text data that can be used to train and evaluate language models for ethical reasoning. The dataset contains three folders:

* `Labelled`: Containing labelled dataset
* `Positive Labels`: Containing positive labels
* `Negative Labels`: Containing negative labels

**Corpus Stats**

![image](https://github.com/Exploration-Lab/EtiCor/assets/72982752/3ecf5331-7fa3-4fed-aaa7-1b7b0e46137a)

**Usage**

The Eticor dataset can be used to train and evaluate language models for ethical reasoning. For example, you could use the dataset to train a model to classify text as either ethical or unethical, or to generate text that is consistent with ethical principles.

**Limitations**

The Eticor dataset is still under development, and may contain some minor errors. Additionally, the dataset is focused on English text, and may not be suitable for training models on other languages.


## Data Processing Codebase

This subfolder contains the code used to process the Eticor dataset.

**Negative_Sentence_Generator.py**

This file takes as input a CSV file of positive labels for a particular region and negates them. It was used to negate some of the norms for database generation.

**Dataset_Analysis.ipynb**

This Jupyter Notebook runs a dataset analysis of subcategory distribution based on a bag of words approach. It takes a CSV file as input and returns a pie chart distribution of the subcategories of etiquette.



