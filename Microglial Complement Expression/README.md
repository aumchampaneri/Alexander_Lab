> This folder has all the files you need to reproduce the analysis 

---

## File Structure
> Purpose of each file in the folder
- CellXGene Datasets.py — This file contains the code to generate the CellXGene datasets for the analysis
- Ensembl_codes.py — This file contains all the gene names and corresponding Ensembl codes for _Homo sapiens_ and _Mus musculus_
- ...h5ad Import.py — Downloads the neccesary .h5ad to generate figures and do analysis
- ...h5ad Analysis.py — The code to import the .h5ad files and then do analysis and generate figures

---

## Usage
> How to use these files
- Use the CellXGene Datasets file to generate a .csv file with all the CellXGene datasets and select what you're interested in
- Then use the ...h5ad Import file to download the .h5ad and perform analysis and visualization using scanpy or R

---

## ToDo:
- [x] Factor H and C3aR1 in microglia for mouse and humans 
- [ ] Expression of FH in brain and kidney
- [ ] Expression of FH and C3aR in Brain and Kidney
- [ ] Expression of complement proteins in Brains and Kidneys (Mouse and Human)
- [ ] Single cell transcriptinomics time-lapse of mouse and embryonic development from gastrula to pup
  - [ ] FH in endothelial cells
  - [ ] FH in placenta
