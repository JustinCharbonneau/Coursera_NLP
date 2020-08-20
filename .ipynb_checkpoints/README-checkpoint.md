IMDB Sentiment Benchmark
==============================

[Dataset available here](https://www.kaggle.com/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews) 

The data was initially shuffled.  
I used 80% of the data to train different algorithms and tested them on the remaining 20%.  


Summary Results
------------
| Model 	| Accuracy 	|
|-	|-	|
| NB-BOW 	| 85.41 	|
| NB-BOW-NGRAM 	| 86.76 	|
| NB-TFIFG-NGRAM 	| 87.64 	|
| FASTTEXT-DEFAULT 	| 89.66 	|
| FASTTEXT-AUTOTUNE 	| 90.42 	|
| ST-BERT-BASE-CASED   	| 91.00 	|

Get Started
------------

Prerequisites:  
- Acanconda/Miniconda  

Start by cloning the repo.  

To create the `imdb` conda environment, enter the following in the command prompt:  
`conda env create -f environment.yml`  

To activate the `imdb` environment, enter the following:  
`conda activate imdb`


Project Organization
------------


    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── notebooks          <- Jupyter notebooks. 
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── environment.yml    <- File for creating the conda environment
    │
    └── src                <- Source code for use in this project.
        ├── __init__.py    <- Makes src a Python module
        │
        └── utils          <- Scripts
            └── PreProcessor.py
            
<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>



--------


