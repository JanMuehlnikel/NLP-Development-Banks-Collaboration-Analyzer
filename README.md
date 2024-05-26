# NLP Development Banks Collaboration Analyzer 🌏
The project aims to explore the collaborative potential among development banks using Natural Language Processing (NLP) techniques. By analyzing textual data such as project declerations from various development banks, the goal is to uncover insights into potential areas of collaboration and synergy.

## **Installation**
1. ```git clone https://github.com/JanMuehlnikel/NLP-Development-Banks-Collaboration-Analyzer```
2. ```cd synergy-app```
3. ```git clone https://huggingface.co/spaces/GIZ/eb-synergy-app```
4. Install ```NLP-Development-Banks-Collaboration-Analyzer/requirements.txt``` in virtual enviroment

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

**Launch Local (Most likely not possible throgh extremely high RAM usage!!)**
1. ```cd /synergy-app```
2. ```streamlit run app.py```

**Visit HuggingFace Space**
https://huggingface.co/spaces/GIZ/eb-synergy-app
   
...
