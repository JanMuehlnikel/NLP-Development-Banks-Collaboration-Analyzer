# NLP Development Banks Collaboration Analyzer 🌏
The project aims to explore the collaborative potential among development banks using Natural Language Processing (NLP) techniques. By analyzing textual data such as project declerations from various development banks, the goal is to uncover insights into potential areas of collaboration and synergy.

## **Features**
- **Data Pipeline:** Data pipeline to fetch and preprocess development cooperation projects from IATI Datastore ([IATI](https://iatistandard.org/en/))
- **Similarity Scores:** Calculation of text similarities between fetched projects to find similar projects
- **Extended Similarity Scores:** Calculation of a extended similarity score which includes cosine text similarity, CRS3 Codes, CRS5 Codes and SDGs
- **Application:** Visualization of results in an web application through Streamlit ([App](https://huggingface.co/spaces/GIZ/eb-synergy-app))

## Tech Stack

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge">
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy Badge">
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas Badge">
  <img src="https://img.shields.io/badge/SciPy-8CAAE6?style=for-the-badge&logo=scipy&logoColor=white" alt="SciPy Badge">
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git Badge">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit Badge">
  <img src="https://img.shields.io/badge/Hugging%20Face-339933?style=for-the-badge&logo=huggingface&logoColor=white" alt="Hugging Face Badge">
  <img src="https://img.shields.io/badge/Transformers-FFD700?style=for-the-badge&logo=transformers&logoColor=white" alt="Transformers Badge">
  <img src="https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white" alt="Jupyter Badge">
</p>

## Models Used

| Model Name     | Description                                                 | Link                                                                                               |
|----------------|-------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| all-MiniLM-L6-v2       | A small, efficient transformer model for various NLP tasks, used here with Sentence Transformer. Used to create text embeddings to calculate cosine similarity. | [MiniLMv2 on Hugging Face](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)           |
| jonas/bert-base-uncased-finetuned-sdg | A classifier model for SDG (Sustainable Development Goals) classification from Hugging Face. | [SDG Classifier on Hugging Face](https://huggingface.co/jonas/bert-base-uncased-finetuned-sdg)                    |


## **Installation**
1. ```git clone https://github.com/JanMuehlnikel/NLP-Development-Banks-Collaboration-Analyzer```
2. ```cd synergy-app```
3. ```git clone https://huggingface.co/spaces/GIZ/eb-synergy-app```
4. Install ```NLP-Development-Banks-Collaboration-Analyzer/requirements.txt``` in virtual enviroment (e.g. conda)

## **Run Pipeline**
1. Navigate to ```/config/```
2. Create KEYS.py
3. Add line ```IATI_KEY = "{Your_Iati_Datastore_Key}"```
4. Create IATI Datastore API Key and replace it with the placeholder ([Create Key](https://developer.iatistandard.org/subscriptions) - Full Access Key subscription used)
5. Navigate to ```/data/pipeline```
6. Run ```python pipeline.py```
7. Wait till pipeline finishes
8. See results in ```/src/merged_orgas.csv```

## **Calculate Similarities Between All Projects**
1. Navigate to ```/data/models```
2. Run ```similarity_minilm.ipynb``` Notebook
3. Text based cosine similarity scores stored in **```/src/similarities.npz```**
4. Navigate to ```/data/models```
5. Run **```extended_similarities.ipynb```** Notebook
6. Extended Similarity Results stored in ```synergy-app/src/```

## **App**

**Launch Local (Most likely not possible throgh extremely high RAM usage!)**
1. ```cd /synergy-app```
2. ```streamlit run app.py```

**Visit HuggingFace Space**

Through high RAM usage the Streamlit App is hosted in a Hugging Face Space:

https://huggingface.co/spaces/GIZ/eb-synergy-app

## **Project Structure**
```
├── config/               # configuration files, constants and keys
├── data/                 # pipeline, models and validation
├── src/                  # sources
├── synergy-app/          # Streamlit App to display results (different repo (https://huggingface.co/spaces/GIZ/eb-synergy-app))
├── .gitignore            # files ignored (especially large memmory files)
├── README.md             # project information
└── requirments.txt       # dependecies and libs that need to be installed
```
