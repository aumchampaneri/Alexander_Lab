# Import packages
import cellxgene_census

# use the "dataset_h5ad" column for the dataset_id
# File added to .gitignore - too big for git
cellxgene_census.download_source_h5ad(
    "b8c618e5-4b3d-4566-8a3f-7e40047f5c54", to_path="Tabula_Muris_Senis_Kidney_10x.h5ad"
)