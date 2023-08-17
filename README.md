# Qiime2 Plugin: Rank Abundance Boxplot

#### Python package for the Qiime2 framework to generates Rank Abundance Boxplots visualization

##### Qiime2 CLI usage example  
```
qiime rank-abundance boxplot \
--i-collapsed-table collapsed_feature_table.qza \
--m-metdata-file metadata.tsv \
--p-group-column "column name" \
--o-visualization rank_abundance_boxplot.qzv
