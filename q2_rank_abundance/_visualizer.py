import os
import qiime2
import biom
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# from qiime2.plugin import Str, Int


def boxplot(
    output_dir: str,
    collapsed_table: biom.Table,
    metadata: qiime2.Metadata,
    group_column: str = None,
) -> None:
    collapsed_rel_freq = collapsed_table.norm(axis="sample", inplace=True)
    df_collapsed_rel_freq = (collapsed_rel_freq.to_dataframe() * 100).T
    index_fp = os.path.join(output_dir, "index.html")

    def build_rank_plot(data):
        # Melt dataframe to long format
        df_melt = pd.melt(data.reset_index(), "index", var_name="Taxon").replace(
            {0: np.nan}
        )
        df_melt.sort_values(["value", "Taxon"], ascending=False, inplace=True)

        # Boxplot
        sns.set_theme(style="ticks")
        # sns.set_style("whitegrid")
        sns.set_context("talk")
        plot_height = (len(df_melt["Taxon"].unique())) / 2.5
        f, ax = plt.subplots(figsize=(7, plot_height))
        ax.set_xscale("log")
        ax.set_xlim(left=0.01, right=100)
        sns.despine(trim=False, left=True, offset={"left": 50})
        sns.boxplot(
            data=df_melt, x="value", y="Taxon", dodge=True, whis=[0, 100], width=0.6
        )
        ax.xaxis.grid(True)
        ax.tick_params(labelbottom=True, labeltop=True, bottom=True, top=True)
        ax.set_xlabel(f"Relative frequency (log scale)")

    if group_column == None:
        build_rank_plot(df_collapsed_rel_freq)
        plt.savefig(
            os.path.join(output_dir, "rank_abundance_plot_all_samples.jpg"),
            dpi=300,
            bbox_inches="tight",
        )
        with open(index_fp, "w") as f:
            f.write("<html><body>\n")
            f.write("<font face='Arial'>\n")
            f.write("<div style='text-align: center;'>\n")
            f.write(
                "Rank Abundance Plot <br>"
                "<img src='rank_abundance_plot_all_samples.jpg' alt='Rank abundance boxplot' style='object-fit:contain; max-width: 75%; height: auto;' >\n"
            )
            f.write("</div>\n")
            f.write("</font>")

    else:
        # Subset the relative frequency table by group_col
        group_col_values = list(metadata.get_column(group_column).to_series().unique())
        metadata_df = metadata.to_dataframe()
        for _ in group_col_values:
            group_ix = list(metadata_df[metadata_df[group_column] == _].index)
            group_df = df_collapsed_rel_freq[df_collapsed_rel_freq.index.isin(group_ix)]
            build_rank_plot(group_df)
            plot_name = f"rank_abundance_plot_{_}.jpg"
            plot_title = f"Rank Abundance Plot: {_}"
            plt.savefig(
                os.path.join(output_dir, plot_name),
                dpi=300,
                bbox_inches="tight",
            )
            with open(index_fp, "a") as f:
                f.write("<html><body>\n")
                f.write("<font face='Arial'>\n")
                f.write("<div style='text-align: center;'>\n")
                f.write(
                    f"{plot_title} <br>"
                    f"<img src={plot_name} alt={plot_name} style='object-fit:contain; max-width: 75%; height: auto;'> <br><br>\n"
                )
                f.write("</div>\n")
                f.write("</font>")
