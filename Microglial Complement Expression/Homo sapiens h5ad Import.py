# Download the dataset
import cellxgene_census

# use the "dataset_h5ad" column for the dataset_id
# Downloaded direct from Amazon AWS Bucket will add to same directory manually -- Recommended as such by authors -- ~70Gb
# https://sea-ad-single-cell-profiling.s3.amazonaws.com/index.html

# cellxgene_census.download_source_h5ad(
#     "c76098ba-eed3-45b1-98f2-96fcac55ed18", to_path="SEAAD_MTG_RNAseq.h5ad"
# )

cellxgene_census.download_source_h5ad(
    "100c6145-7b0e-4ba6-81c1-ffebed0d1ac4", to_path="SEAAD_DLPFC_RNAseq.h5ad"
)