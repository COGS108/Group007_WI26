{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Rubric\n",
    "\n",
    "Instructions: DELETE this cell before you submit via a `git push` to your repo before deadline. This cell is for your reference only and is not needed in your report. \n",
    "\n",
    " Scoring: Out of 10 points\n",
    "\n",
    "- Each Developing  => -2 pts\n",
    "- Each Unsatisfactory/Missing => -4 pts\n",
    "  - until the score is 0\n",
    "\n",
    "If students address the detailed feedback in a future checkpoint they will earn these points back\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "|                                  | **Unsatisfactory**                                                                                                                                                                                                                                                                                                                        | **Developing**                                                                                                                                                                                                       | **Proficient**                                                                                                                                                                                            | **Excellent**                                                                                                                                                                            |\n",
    "|----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|\n",
    "| **EDA relevance**                | EDA is mostly neither relevant to the question nor helpful in figuring out how to address the question. Or the EDA does address the question, but many obviously relevant variables / analyses / figures were not included. | EDA is partly irrelevant/unhelpful. EDA missed one or two obvioulsy relevant analysis (distributions of single variables or relationships between variables) | EDA includes the obviously relevant / helpful variables in addressing the question.                                                              | Thorough EDA fully explored the dataset                                                                                                                 |\n",
    "| **EDA analysis and description** | Many of the analyses are poor choices (e.g., using means instead of medians for obviously skewed data), or are poorly described in the text, or do not aid understanding the data                                                                                                                                                     | Some of the analyses are poor choices, or are poorly described in the text, or do not aid understanding the data                                                                                                 | All analyses are correct choices. Only one or two have minor issues in the text descriptions supporting them. Mostly they fit well with other elements of the EDA and support understanding the data  | All analyses are correct choices with clear text descriptions supporting them. The figures fit well with the other elements of the EDA, producing a clear understanding of the data. |\n",
    "| **EDA figures**                  | Many of the figures are poor plot choices (e.g., using a bar plot to represent a time series where it would be better to use a line plot) or have poor aesthetics (including colormap, data point shape/color, axis labels, titles, annotations, text legibility) or do not aid understanding the data                                | Some of the figures are poor plot choices or have poor aesthetics. Some figures do not aid understanding the data                                                                                                | All figures are correct plot choices. Only one or two have minor questionable aesthetic choices. The figures mostly fit well with the other elements of the EDA and support understanding the data    | All figures are correct plot choices with beautiful aesthetics. The figures fit well with the other elements of the EDA, producing a clear understanding of the data.                |\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# COGS 108 - EDA Checkpoint"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Authors\n",
    "\n",
    "Instructions: REPLACE the contents of this cell with your team list and their contributions. Note that this will change over the course of the checkpoints\n",
    "\n",
    "This is a modified [CRediT taxonomy of contributions](https://credit.niso.org). For each group member please list how they contributed to this project using these terms:\n",
    "> Analysis, Background research, Conceptualization, Data curation, Experimental investigation, Methodology, Project administration, Software, Visualization, Writing – original draft, Writing – review & editing\n",
    "\n",
    "Example team list and credits:\n",
    "- Alice Anderson: Conceptualization, Data curation, Methodology, Writing - original draft\n",
    "- Bob Barker:  Analysis, Software, Visualization\n",
    "- Charlie Chang: Project administration, Software, Writing - review & editing\n",
    "- Dani Delgado: Analysis, Background research, Visualization, Writing - original draft"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Research Question"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Instructions: REPLACE the contents of this cell with your work, including any updates to recover points lost in your proposal feedback\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Background and Prior Work"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Instructions: REPLACE the contents of this cell with your work, including any updates to recover points lost in your proposal feedback"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Hypothesis\n"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Instructions: REPLACE the contents of this cell with your work, including any updates to recover points lost in your proposal feedback"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Data"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Data overview\n",
    "\n",
    "Instructions: REPLACE the contents of this cell with your work, including any updates to recover points lost in your data checkpoint feedback\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Run this code every time when you're actively developing modules in .py files.  It's not needed if you aren't making modules\n",
    "#\n",
    "## this code is necessary for making sure that any modules we load are updated here \n",
    "## when their source code .py files are modified\n",
    "\n",
    "%load_ext autoreload\n",
    "%autoreload 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Setup code -- Run only once after cloning!!! \n",
    "#\n",
    "# this code downloads the data from its source to the `data/00-raw/` directory\n",
    "# if the data hasn't updated you don't need to do this again!\n",
    "\n",
    "# if you don't already have these packages (you should!) uncomment this line\n",
    "# %pip install requests tqdm\n",
    "\n",
    "import sys\n",
    "sys.path.append('./modules') # this tells python where to look for modules to import\n",
    "\n",
    "import get_data # this is where we get the function we need to download data\n",
    "\n",
    "# replace the urls and filenames in this list with your actual datafiles\n",
    "# yes you can use Google drive share links or whatever\n",
    "# format is a list of dictionaries; \n",
    "# each dict has keys of \n",
    "#   'url' where the resource is located\n",
    "#   'filename' for the local filename where it will be stored \n",
    "datafiles = [\n",
    "    { 'url': 'https://raw.githubusercontent.com/fivethirtyeight/data/refs/heads/master/airline-safety/airline-safety.csv', 'filename':'airline-safety.csv'},\n",
    "    { 'url': 'https://raw.githubusercontent.com/fivethirtyeight/data/refs/heads/master/bad-drivers/bad-drivers.csv', 'filename':'bad-drivers.csv'}\n",
    "]\n",
    "\n",
    "get_data.get_raw(datafiles,destination_directory='data/00-raw/')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Dataset #1 \n",
    "\n",
    "Instructions: REPLACE the contents of this cell and the one below with your work, including any updates to recover points lost in your data checkpoint feedback"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "## YOUR CODE TO LOAD/CLEAN/TIDY/WRANGLE THE DATA GOES HERE\n",
    "## FEEL FREE TO ADD MULTIPLE CELLS PER SECTION "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Dataset #2\n",
    " as above, add any more copies of this that you need to given how many datasets you have"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "## YOUR CODE TO LOAD/CLEAN/TIDY/WRANGLE THE DATA GOES HERE\n",
    "## FEEL FREE TO ADD MULTIPLE CELLS PER SECTION "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Results\n",
    "\n",
    "### Exploratory Data Analysis\n",
    "\n",
    # Exploratory Data Analysis (EDA)

Exploratory Data Analysis (EDA) is all about understanding the data before you do any modeling. The EDA process assesses five essential elements which must be present in every dataset. 

## 1. Missing Values
The EDA process assesses which columns in the dataset contain missing values and determines the extent of missing data.

**Example:** If 40% of a column’s values are missing, you might need to drop it or impute values.

## 2. Data Types and Structure
The system needs to identify every column's data type as either numeric, categorical, datetime, or text.

This helps determine which analyses or visualizations are appropriate.

## 3. Summary Statistics
The system uses six different statistical measures together with nine separate statistical measurements.

This method enables users to comprehend distribution patterns while discovering uncommon data points.

## 4. Outliers
Extreme values which EDA identifies through its analysis process can either distort research results or reveal errors in data collection.

Visualizations like **boxplots** or **scatterplots** are often used for this.

## 5. Relationships Between Variables
The system detects three types of relationships through:

- Numerical correlations between variables  
- Categorical associations  
- Feature interaction connections  

This approach helps to identify which features will have the most significant impact on modeling results.
    "Please explicitly load the fully wrangled data you will use from `data/02-processed`.  This is a good idea rather than forcing people to re-run the data getting / wrangling cells above.  Sometimes it takes a long time to get / wrangle data compared to reloading the fixed up dataset.\n",
    "\n",
    "Carry out whatever EDA you need to for your project in the code cells below.  Because every project will be different we can't really give you much of a template at this point. But please make sure you describe the what and why in text here as well as providing interpretation of results and context.\n",
    "\n",
    "Please note that you should consider the use of python modules in your work.  Any code which gets called repeatedly should be modularized. So if you run the same pre-processing, analysis or visualiazation on different subsets of the data, then you should turn that into a function or class.  Put that function or class in a .py file that lives in `modules/`.  Import the module you made and use it to get your work done.  For reference see `get_raw()` which is inside `modules/get_data.py`. \n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Missing Values \n",
    "\n",
    "## Why Missing Values Affect a Dataset

Missing values can have a significant impact on data analysis and modeling. Here’s why:

1. **Bias in Analysis**  
   - If missing values are not handled properly, the results of statistical analysis can be skewed.  
   - Example: Calculating the mean of a column with many missing entries may give a misleading result.

2. **Reduced Data Availability**  
   - Missing values reduce the amount of usable data for modeling, which can lower the performance of machine learning algorithms.

3. **Errors in Algorithms**  
   - Many algorithms, such as regression or clustering, cannot handle missing data directly and may produce errors or fail to run.

4. **Impact on Relationships**  
   - Missing data can weaken or distort relationships between variables, leading to incorrect conclusions.

5. **Decision-Making Issues**  
   - Incomplete data can mislead stakeholders, resulting in poor decisions based on partial information.

**Handling Missing Values:**  
- **Imputation:** Fill in missing values using mean, median, mode, or predictive methods.  
- **Removal:** Drop rows or columns with too many missing values.  
- **Flagging:** Create indicator variables to mark missing data.
  },
```python
import pandas as pd

# Load the cleaned dataset from your repository
# If running locally, you can use the relative path
file_path = "data/02-processed/covid_mobility_clean.csv"
df = pd.read_csv(file_path)

# Preview the first few rows
print(df.head())

# Check for missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# Basic info about the dataset
print("\nDataset info:")
print(df.info())

  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "## YOUR CODE HERE\n",
    "## FEEL FREE TO ADD MULTIPLE CELLS PER SECTION"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Section 2 of EDA if you need it  - please give it a better title than this\n",
    "\n",
    "Some more words and stuff.  Remember notebooks work best if you interleave the code that generates a result with properly annotate figures and text that puts these results into context."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "## YOUR CODE HERE\n",
    "## FEEL FREE TO ADD MULTIPLE CELLS PER SECTION"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Ethics"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Instructions: REPLACE the contents of this cell with your work, including any updates to recover points lost in your proposal feedback"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Team Expectations "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Instructions: REPLACE the contents of this cell with your work, including any updates to recover points lost in your proposal feedback"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Project Timeline Proposal"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Instructions: Replace this with your timeline.  **PLEASE UPDATE your Timeline!** No battle plan survives contact with the enemy, so make sure we understand how your plans have changed.  Also if you have lost points on the previous checkpoint fix them"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.13"
  },
  "vscode": {
   "interpreter": {
    "hash": "16b860a9f5fc21240e9d88c0ee13691518c3ce67be252e54a03b9b5b11bd3c7a"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
