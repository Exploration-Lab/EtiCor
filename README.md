# EtiCor
## Eticor: Corpus for Analyzing LLMs for Etiquettes

This repository contains the entire codebase of experiments and results of the EMNLP 2023 paper "Eticor: Corpus for Analyzing LLMs for Etiquettes". You can access the Eticor Dataset in the `Dataset` folder.

### Contributions

* We create a new Corpus (Eticor) containing social norms and etiquettes from 5 primary regions of the world.
* We define a new task: Ettiquete Sensitivity, where we check whether an etiquette is appropriate or not according to the regional context.
* We tested three Language Based Models: Delphi, Falcon 40B, and GPT 3.5-turbo to perform the task of Ettiquete Senstivity. Code Files can be found in `Models` and Results are compiled in the `results` folder.

### Dataset

The Eticor Dataset is a new corpus containing social norms and etiquettes from 5 primary regions of the world:

* **East Asia:** Japan, Korea,Taiwan, Malaysia ,Phillipines and Vietnam
* **India**
* **North America and Europe:** Canada, USA, Europian Countries
* **Latin America:** South American countries
* **Middle East and Africa:** Middle East and African Countries.

The dataset contains a total of 36,347 examples. Each example contains a social norm or etiquette statement, along with a label indicating whether the statement is appropriate or not according to the regional context.

### Task

The Ettiquete Sensitivity task is a new task that we define to evaluate the ability of Language Based Models to understand and apply social norms and etiquettes. The task is to predict whether a given etiquette statement is appropriate or not according to the regional context.

### Models

We tested three Language Based Models on the Ettiquete Sensitivity task:

* **Delphi:** A 175B parameter language model from Google AI.
* **Falcon 40B:** A 40B parameter language model from Hugging Face.
* **GPT 3.5-turbo:** A 175B parameter language model from OpenAI.
## License

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)


The Eticor dataset and follows [CC-BY-NC](CC-BY-NC) license. Thus, users can share and adapt our dataset if they give credit to us and do not use our dataset for any commercial purposes.



## Citation

```
@inproceedings{dwivedi-etal-2022-eticor,
    title = "{EtiCor}: Corpus for Analyzing LLMs for Etiquettes",
    author = "Dwivedi, Ashutosh and
      Lavania, Pradhyumna and
      Modi, Ashutosh",
    booktitle = "Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing",
    month = dec,
    year = "2023",
    address = "Singapore,
    publisher = "Association for Computational Linguistics",
    abstract = "Etiquettes are an essential ingredient of day-to-day interactions among people. Moreover, etiquettes are region-specific, and etiquettes in one region might contradict those in other regions. In this paper, we propose EtiCor, an Etiquettes Corpus, having texts about social norms from five different regions across the globe. The corpus provides a test bed for evaluating LLMs for knowledge and understanding of region-specific etiquettes. Additionally, we propose the task of Etiquette Sensitivity. We experiment with state-of-the-art LLMs (Delphi, Falcon40B, and GPT-3.5). Initial results indicate that LLMs, mostly fail to understand etiquettes from regions from non-Western world.",
}
```

## Contact

In case of any queries, please contact <ashutoshm.iitk@gmail.com>
