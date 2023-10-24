## Zero Shot Prediction Results

### Delphi

| Region | TP | TN | FP | FN | Accuracy (Without Abstentions) | Accuracy (Abstentions-Included) | Precision | Recall | F1 Score |
|---|---|---|---|---|---|---|---|---|---|
| India | 2100 | 1023 | 1052 | 227 | 0.71 | 0.69 | 0.666243655 | 0.902449506 | 0.77 |
| EA | 2731 | 1412 | 1802 | 678 | 0.63 | 0.56 | 0.60247077 | 0.801114696 | 0.69 |
| LA | 2460 | 2060 | 1568 | 430 | 0.69 | 0.55 | 0.610724926 | 0.851211073 | 0.71 |
| MEA | 3928 | 1807 | 2491 | 656 | 0.65 | 0.57 | 0.611933323 | 0.856893543 | 0.71 |
| NE | 3640 | 1000 | 926 | 370 | 0.78 | 0.75 | 0.797196671 | 0.907730673 | 0.85 |

### GPT

| Region | TP | TN | FP | FN | Accuracy (Without Abstentions) | Accuracy (Abstentions-Included) | Precision | Recall | F1 Score |
|---|---|---|---|---|---|---|---|---|---|
| India | 1953 | 420 | 1771 | 398 | 0.52 | 0.52 | 0.52443609 | 0.830710336 | 0.64 |
| EA | 3471 | 573 | 2627 | 729 | 0.55 | 0.54 | 0.569203017 | 0.826428571 | 0.67 |
| LA | 3728 | 638 | 2953 | 765 | 0.54 | 0.53 | 0.558000299 | 0.829735144 | 0.67 |
| MEA | 4748 | 733 | 3544 | 960 | 0.55 | 0.55 | 0.572600096 | 0.831814996 | 0.68 |
| NE | 3437 | 358 | 1558 | 767 | 0.62 | 0.62 | 0.688088088 | 0.81755471 | 0.75 |

### Falcon

| Region | TP | TN | FP | FN | Accuracy (Without Abstentions) | Accuracy (Abstentions-Included) | Precision | Recall | F1 Score |
|---|---|---|---|---|---|---|---|---|---|
| India | 1316 | 1371 | 572 | 491 | 0.72 | 0.603 | 0.697033898 | 0.728278915 | 0.71 |
| EA | 2566 | 2149 | 865 | 1372 | 0.68 | 0.621 | 0.747886913 | 0.651599797 | 0.7 |
| LA | 2154 | 2203 |1092 | 1917	| 0.59 | 0.541 |	0.663585952 |	0.529108327 |	0.61 |
| MEA |	3909 | 3011 |	1233 | 1755 |	0.7	| 0.681 |	0.760210035 |	0.690148305 |	0.72 |
|NE |	3263 |	942 | 752 |	746 |	0.74 |	0.697 |	0.782702 | 0.773919 |	0.78|

## Fine Tune Prediction Results
### BERT Five Fold (EA)
![image](https://github.com/Exploration-Lab/EtiCor/assets/72982752/1ab0e1d8-8690-459d-bd38-1de2b1960a8f)

### BERT Five Fold (India)
![image](https://github.com/Exploration-Lab/EtiCor/assets/72982752/f453d9e4-b61d-4c81-a7a2-65a3571b45c6)

### BERT Five Fold (LA)
![image](https://github.com/Exploration-Lab/EtiCor/assets/72982752/4aff925e-d8bf-42cc-8ad3-8337b75958c6)

### BERT Five Fold (MEA)
![image](https://github.com/Exploration-Lab/EtiCor/assets/72982752/8ece37fc-129e-4af8-8a69-75aed631e028)

### BERT Five Fold (NE)
![image](https://github.com/Exploration-Lab/EtiCor/assets/72982752/488f7c72-adca-411a-abe1-ecf6cc5162de)


