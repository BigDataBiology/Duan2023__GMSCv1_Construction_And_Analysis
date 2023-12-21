GMSC Analysis - Gene rarefaction for 100AA smORFs

This folder contains the following scripts:

- split_samples.py: First code needed to run. It separates the samples into files given the initial dataset, also discretizing the smORFs by their unique numbers.
- jugfile.py: Main code for doing the rarefaction. Select the samples for the expected environments.
- rarefaction.py: Auxiliary functions for the rarefaction. It creates persistent storage for an environment to store the samples. After this, it reads random samples from the storage to run the rarefaction calculations.
- generate_figures.py: For generating the figures after running the rarefaction code.

Run the code with `jug execute`.

More details at [GMSC figures - CodiMD](https://aws.big-data-biology.org:1300/WS2U5sgnSsKKuUMVzUXxbg).