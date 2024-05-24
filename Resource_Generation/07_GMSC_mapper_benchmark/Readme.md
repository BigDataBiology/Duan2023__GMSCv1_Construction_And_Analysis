## 07_GMSC_mapper_benchmark

### 01_sensitivity

| **Code** | **Description** | 
| :---: | :---: | 
| 01_sensitivity.sh | Test the recovery of smORFs by different sensitivity of Diamond and MMseqs2 with different length | 

### 02_time

| **Code** | **Description** |
| :---: | :---: |
| 01_time.sh | Test the time cost by Diamond and MMseqs2 | 

### 03_identity

| **Code** | **Description** |
| :---: | :---: | 
| 01_select_mutation.py  | Randomly selected and mutated 10,000 sequences from 90AA smORFs with different length (20,30,40,60,80,all) at different identity. | 
| 02_identity.sh | Test the recovery of smORFs between Blast,Diamond,MMseqs with different length (20,30,40,60,80,all) and different identity | 