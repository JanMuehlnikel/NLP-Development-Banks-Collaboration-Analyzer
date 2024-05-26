# NLP Development Banks Collaboration Analyzer 🌏
The project aims to explore the collaborative potential among development banks using Natural Language Processing (NLP) techniques. By analyzing textual data such as project declerations from various development banks, the goal is to uncover insights into potential areas of collaboration and synergy.

## **Features**
- Data pipeline to fetch and preprocess development cooperation projects from IATI Datastore (https://iatistandard.org/en/)
- Calculation of text similarities between fetched projects to find similar projects
- Calculation of extended similarity score which includes cosine text similarity, CRS3 Codes, CRS5 Codes and SDGs
- Visualization of results in a web application through Streamlit

## Tech Stack

- **Python**: The core programming language used for development.
  <img src="https://www.python.org/static/community_logos/python-logo-master-v3-TM.png" alt="Python Logo" width="50" height="50">

- **Streamlit**: A framework for creating interactive web applications directly from Python scripts.
  <img src="https://streamlit.io/images/brand/streamlit-mark-color.png" alt="Streamlit Logo" width="50" height="50">

- **Hugging Face**: A platform providing a wide range of pre-trained NLP models and tools.
  <img src="https://huggingface.co/front/assets/huggingface_logo-noborder.svg" alt="Hugging Face Logo" width="50" height="50">

- **Transformers**: A library by Hugging Face for state-of-the-art NLP models.
  <img src="https://github.com/huggingface/transformers/raw/main/docs/source/imgs/transformers_logo_name.png" alt="Transformers Logo" width="50" height="50">

- **Jupyter**: An interactive computing environment that allows you to create and share documents that contain live code, equations, visualizations, and narrative text.
  <img src="https://jupyter.org/assets/main-logo.svg" alt="Jupyter Logo" width="50" height="50">



## **Installation**
1. ```git clone https://github.com/JanMuehlnikel/NLP-Development-Banks-Collaboration-Analyzer```
2. ```cd synergy-app```
3. ```git clone https://huggingface.co/spaces/GIZ/eb-synergy-app```
4. Install ```NLP-Development-Banks-Collaboration-Analyzer/requirements.txt``` in virtual enviroment (e.g. conda)

## **Run Pipeline**
1. Navigate to **```/data/pipeline```**
2. Run **```python pipeline.py```**
3. Wait till pipeline finishes
4. See results in **```/src/merged_orgas.csv```**

## **Calculate Similarities Between All Projects**
1. Navigate to **```/data/models```**
2. Run **```similarity_minilm.ipynb```** Notebook
3. Text based cosine similarity scores stored in **```/src/similarities.npz```**
4. Navigate to **```/data/models```**
5. Run **```extended_similarities.ipynb```** Notebook
6. Extended Similarity Results stored in **```synergy-app/src/```**

## **Launch App**

**Launch Local (Most likely not possible throgh extremely high RAM usage!)**
1. ```cd /synergy-app```
2. ```streamlit run app.py```

**Visit HuggingFace Space**

https://huggingface.co/spaces/GIZ/eb-synergy-app
   
...
