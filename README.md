# LoL KDA Measurement

This repository contains code and data related to KDA (Kill/Death/Assist) ratio measurement, including both per-match values and aggregated metrics designed to support the proposed performance analysis.

## Files

### `allRoundsKDA.csv`

Contains KDA ratio values computed at the individual match level.

### `aggregatedKDA.csv`

Contains aggregated KDA metrics, computed by grouping matches according to championship rounds.

## Method Overview

The repository implements KDA calculations considering:

* individual match performance
* aggregated performance across competitive stages

These representations are used to align with the evaluation framework proposed in the study.

## Anonymization

Player and team names were anonymized to preserve confidentiality during the double-blind review process.

A "Team_Number" convention is used, where the number corresponds to the ordinal appearance of each team in the dataset.

**Note:**

* The same team identifier is consistently used across both `.csv` files, enabling direct comparison between per-match and aggregated data.
