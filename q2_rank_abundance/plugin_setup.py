from qiime2.plugin import Plugin
from qiime2.plugin import Str, Int, Metadata

# from q2_types.feature_data import FeatureData, Taxonomy
from q2_types.feature_table import FeatureTable, Frequency

import q2_rank_abundance
from ._visualizer import boxplot

plugin = Plugin(
    name="rank_abundance",
    version="0.1.0",
    website="https://gitlab.nzcorp.net/mdsa/sequencing-workgroup/q2-rank-abundance/",
    user_support_text="https://forum.qiime2.org",
    package="q2_rank_abundance",
    description=(
        "This QIIME 2 plugin produces a rank abundance plot inspired by "
        "the Whittaker curve concept, where the taxa relative frequencies "
        "are ranked by maxima and represented on a log-scale for readability "
        ""
    ),
)

plugin.visualizers.register_function(
    function=boxplot,
    inputs={
        "collapsed_table": FeatureTable[Frequency],
        # "taxonomy": FeatureData[Taxonomy]
    },
    parameters={
        "metadata": Metadata,
        # "rank": Int,
        "group_column": Str,
    },
    input_descriptions={
        "collapsed_table": "Collapsed FeatureTable[Frequency] artifact",
        # "taxonomy": "FeatureData[Taxonomy] artifact",
    },
    parameter_descriptions={
        "metadata": "The sample metadata .tsv file",
        # "rank": "Collapse taxa at this taxonomic rank",
        "group_column": "Create a separate boxplot for each group in this column",
    },
    name="Rank Abundance Boxplot",
    description=(
        "Horizontal boxplot of taxa relative abundance in a feature table, sorted or "
        "ranked by maxima values, and plotted on a log scale for readability"
        ""
    ),
)
