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
| NB-TFIDF-NGRAM 	| 87.64 	|
| FASTTEXT-DEFAULT 	| 89.66 	|
| FASTTEXT-AUTOTUNE 	| 90.42 	|
| ST-BERT-BASE-CASED   	| 91.00 	|
| FASTAI-ULMFIT     	| ---- 	|

Get Started
------------

Prerequisites:  
- Acanconda/Miniconda  

Start by cloning the repo.  

To create the `imdb` conda environment, enter the following in the command prompt:  
```bash
conda env create -f environment.yml
```  

To activate the `imdb` environment, enter the following:  
```bash
conda activate imdb
```  

Notebooks
-----------
| Notebooks                               |
| ----------------------------------------|
| [0.0_explore_data.ipynb](https://github.com/JustinCharbonneau/IMDB-Sentiment-Benchmark/blob/master/notebooks/0.0_explore_data.ipynb)           |
| [0.1_explore_preprocessing.ipynb](https://github.com/JustinCharbonneau/IMDB-Sentiment-Benchmark/blob/master/notebooks/0.1_explore_preprocessing.ipynb)  |
| [1.0_naive_bayes.ipynb](https://github.com/JustinCharbonneau/IMDB-Sentiment-Benchmark/blob/master/notebooks/1.0_naive_bayes.ipynb)  |
| [2.0_fasttext.ipynb](https://github.com/JustinCharbonneau/IMDB-Sentiment-Benchmark/blob/master/notebooks/2.0_fasttext.ipynb)  |
| [3.0_simple_transformers.ipynb](https://github.com/JustinCharbonneau/IMDB-Sentiment-Benchmark/blob/master/notebooks/3.0_simple_transformers.ipynb)  |
| [4.0_fastai.ipynb](https://github.com/JustinCharbonneau/IMDB-Sentiment-Benchmark/blob/master/notebooks/4.0_fastai.ipynb)  |


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


