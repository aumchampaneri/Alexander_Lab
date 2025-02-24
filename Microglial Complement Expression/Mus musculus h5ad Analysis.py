# Import ensembl codes from Ensembl_codes.py
from Ensembl_codes import homo_ensembl, mus_ensembl

# Import packages
import scanpy as sc
import anndata as ad

# Load the microglial datasets from a .h5ad file using Scanpy
mus_microglia_myeloid = sc.read_h5ad('/Users/aumchampaneri/PycharmProjects/Alexander_Lab/Microglial Complement Expression/Tabula_Muris_Senis_Brain_Myeloid.h5ad')
mus_microglia_nonmyeloid = sc.read_h5ad('/Users/aumchampaneri/PycharmProjects/Alexander_Lab/Microglial Complement Expression/Tabula_Muris_Senis_Brain_Non-Myeloid.h5ad')

# Concatenate the two Tabula Muris Senis datasets using anndata
'''
Concatenation of these is broken but the myeloid set has the majority of the cells anyways
'''
# mus_microglia = ad.concat([mus_microglia_myeloid, mus_microglia_nonmyeloid])

# Create a dot plot
sc.pl.dotplot(mus_microglia_myeloid, mus_ensembl, groupby='tissue', save='mus_musculus')