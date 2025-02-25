# Import ensembl codes from Ensembl_codes.py
from Ensembl_codes import homo_ensembl, mus_ensembl

# Import packages
import scanpy as sc
import anndata as ad

# Load the microglial datasets from a .h5ad file using Scanpy
homo_microglia_SEAAD_MTG = sc.read_h5ad('/Users/aumchampaneri/PycharmProjects/Alexander_Lab/Microglial Complement Expression/SEAAD_MTG_RNAseq.h5ad')
homo_microglia_SEAAD_DLPFC = sc.read_h5ad('/Users/aumchampaneri/PycharmProjects/Alexander_Lab/Microglial Complement Expression/SEAAD_DLPFC_RNAseq.h5ad')

# Concatenate the two SEAAD datasets using anndata
homo_microglia = ad.concat([homo_microglia_SEAAD_MTG, homo_microglia_SEAAD_DLPFC])

# Filter the dataset to only include normal disease lines
# homo_microglia = homo_microglia[homo_microglia.obs.disease == "normal"]

# Create a dot plot
sc.pl.dotplot(homo_microglia, homo_ensembl, groupby='disease', save='homo_sapiens_test')