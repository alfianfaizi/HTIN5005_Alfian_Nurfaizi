# Explainable Hospital Admission & Resource Allocation using SCI-XAI
This repository contains notebooks that explore the prediction of hospital admissions and resource allocation using an adapted version of the Interpretable and Explainable AI (SCI-XAI) pipeline. The project demonstrates both binary and multiclass prediction models and integrates explainability using SHAP.

---

##  Notebooks

This project includes two main Jupyter notebooks:

1.  **`Explainable Hospital Admission SCI-XAI`**
    * **Description:** This notebook implements the SCI-XAI pipeline for a **binary classification** task to predict patient admission (Admit vs Discharge).
    * **Explainability:** Uses SHAP (SHapley Additive exPlanations) to interpret the model's predictions and understand which features are most influential.

2.  **`Resource Allocation SCI-XAI`**
    * **Description:** This notebook adapts the pipeline for a **multiclass classification** task. This can be framed as a resource allocation problem to different hospital wards or levels of care.

---

## Methodology

The core methodology involves a re-implementation of the **SCI-XAI pipeline**, which is designed to integrate human-centred perspectives into the development of XAI systems.
The models in these notebooks are adapted from the original pipeline with some adjustments by the author.

---

## Dataset

The dataset used for both notebooks is publicly available from the following PLOS ONE publication:

* **Title:** Predicting hospital admission at the time of triage in the emergency department
* **Source:** [https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0216972](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0216972)

Please refer to the article for a detailed description of the data, its collection, and its features.

---

## Acknowledgments

This work is based on and adapted from the original **SCI-XAI-Pipeline** repository.
* **Original Repo:** [https://github.com/petmoreno/SCI-XAI-Pipeline.git](https://github.com/petmoreno/SCI-XAI-Pipeline.git)

---

## Author

* **Alfian Nurfaizi**
