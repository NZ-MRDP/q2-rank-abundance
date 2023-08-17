"""QIIME 2 plugin for running Rank Abundance Plot."""

from setuptools import find_packages, setup

setup(
    name="q2-rank-abundance",
    version="0.0.2",
    packages=find_packages(),
    author="Alexandru Dumitrache",
    author_email="axd@novozymes.com",
    description="QIIME2 plugin for making rank abundance plots",
    entry_points={
        "qiime2.plugins": ["q2-rank-abundance=q2_rank_abundance.plugin_setup:plugin"]
    },
)
