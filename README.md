# NLP Development Banks Collaboration Analyzer 🌏
The project aims to explore the collaborative potential among development banks using Natural Language Processing (NLP) techniques. By analyzing textual data such as project declerations from various development banks, the goal is to uncover insights into potential areas of collaboration and synergy.

## **Features**
- Data pipeline to fetch and preprocess development cooperation projects from IATI Datastore (https://iatistandard.org/en/)
- Calculation of text similarities between fetched projects to find similar projects
- Calculation of extended similarity score which includes cosine text similarity, CRS3 Codes, CRS5 Codes and SDGs
- Visualization of results in a web application through Streamlit

## Tech Stack

- **Python**: The core programming language used for development.
- ![Python Logo]([https://via.placeholder.com/50](https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg)) 

- **Streamlit**: A framework for creating interactive web applications directly from Python scripts.
- ![Streamlit Logo](https://via.placeholder.com/50)  <!-- Replace with Streamlit logo URL -->

- **Hugging Face**: A platform providing a wide range of pre-trained NLP models and tools.
- ![Hugging Face Logo](https://via.placeholder.com/50)  <!-- Replace with Hugging Face logo URL -->

- **Transformers**: A library by Hugging Face for state-of-the-art NLP models.
- ![Transformers Logo](https://via.placeholder.com/50)  <!-- Replace with Transformers logo URL -->

- **Jupyter**: An interactive computing environment that allows you to create and share documents that contain live code, equations, visualizations, and narrative text.
- ![Jupyter Logo](https://via.placeholder.com/50)  <!-- Replace with Jupyter logo URL -->


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
