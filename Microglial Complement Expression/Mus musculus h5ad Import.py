# Download the dataset
import cellxgene_census

# use the "dataset_h5ad" column for the dataset_id
cellxgene_census.download_source_h5ad(
    "66ff82b4-9380-469c-bc4b-cfa08eacd325", to_path="Tabula_Muris_Senis_Brain_Non-Myeloid.h5ad"
)

cellxgene_census.download_source_h5ad(
    "c08f8441-4a10-4748-872a-e70c0bcccdba", to_path="Tabula_Muris_Senis_Brain_Myeloid.h5ad"
)