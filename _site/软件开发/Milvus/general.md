# Hybrid search
Since Milvus 2.4, we introduced multi-vector support and a hybrid search framework, 
which means users can bring in several vector fields (up to 10) into a single collection. 
These vectors in different columns represent diverse facets of data, originating from different embedding models or undergoing distinct processing methods. 
The results of hybrid searches are integrated using reranking strategies, such as Reciprocal Rank Fusion (RRF) and Weighted Scoring.

## Reciprocal Rank Fusion (RRF)


# Unified Lambda structure
Milvus combines stream and batch processing for data storage to balance timeliness and efficiency. Its unified interface makes vector similarity search a breeze.


# ANN search
Approximate Nearest Neighbor (ANN)
