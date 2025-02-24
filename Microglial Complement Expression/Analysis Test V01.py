# Import ensembl codes from Ensembl_codes.py
from cgi import print_arguments

from Ensembl_codes import homo_ensembl, mus_ensembl

# Import packages
import scanpy as sc

# Load the microglia dataset from a .h5ad file using Scanpy
homo_microglia_SEAAD_A9 = sc.read_h5ad('/Volumes/Vault/PycharmProjects/Alexander-Lab/Complement Microglial Expression/Datasets/SEAAD_A9_RNAseq_final-nuclei.2024-02-13.h5ad')
print(homo_microglia_SEAAD_A9)

# Create a dot plot
# sc.pl.dotplot(homo_microglia_SEAAD_A9, homo_ensembl, groupby='tissue')