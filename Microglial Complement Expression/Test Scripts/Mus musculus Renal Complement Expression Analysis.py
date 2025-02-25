# Import packages
import scanpy as sc
# import anndata as ad

# Copy of mus musculus codes from 'Ensembl_codes.py'

# Ensembl Codes for Mouse Complement Genes
# 2025-02-25 Copy Date
mus_ensembl = {
    'C1QA': 'ENSMUSG00000029385',
    # 'C1QB': 'ENSMUSG00000029382',
    'C1QC': 'ENSMUSG00000029379',
    'C2': 'ENSMUSG00000024399',
    'C3': 'ENSMUSG00000024164',
    # 'C4A': 'ENSMUSG00000038219',
    # 'C4B': 'ENSMUSG00000038220',  # Updated to correct ID
    'C5': 'ENSMUSG00000037940',
    'C6': 'ENSMUSG00000029757',
    'C7': 'ENSMUSG00000026395',
    # 'C8B': 'ENSMUSG00000026396',  # Updated to correct ID
    # 'C8G': 'ENSMUSG00000026397',  # Updated to correct ID
    'C9': 'ENSMUSG00000026398',   # Updated to correct ID
    'CFB': 'ENSMUSG00000090231',  # Updated to correct ID
    # 'CFD': 'ENSMUSG00000011537',  # Updated to correct ID
    'CFH': 'ENSMUSG00000026365',
    'C3AR1': 'ENSMUSG00000040552',
    'C5AR1': 'ENSMUSG00000027399',  # Updated to correct ID
    'C5AR2': 'ENSMUSG00000027400',  # Updated to correct ID
    # 'CR1': 'ENSMUSG00000029758',    # Updated to correct ID
    'CR2': 'ENSMUSG00000029759',    # Updated to correct ID
    # 'CR3': 'ENSMUSG00000029760',    # Updated to correct ID
    'CR4': 'ENSMUSG00000029761',    # Updated to correct ID
    # 'CR1Q': 'ENSMUSG00000029386'    # Updated to correct ID
}

# Load the Kidney dataset from a .h5ad file using Scanpy
mus_musculus_kidney = sc.read_h5ad('/Users/aumchampaneri/PycharmProjects/Alexander_Lab/Microglial Complement Expression/Test Scripts/Tabula_Muris_Senis_Kidney_10x.h5ad')
print(mus_musculus_kidney)

# Create a dot plot
# Compare Complement Gene Expression vs. source renal tissue of the cell
# Complement vs. tissue
sc.pl.dotplot(mus_musculus_kidney, mus_ensembl, groupby='cell_type', save='mus_musculus_cell-type')