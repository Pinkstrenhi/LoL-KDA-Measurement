import os
import pandas as pd

sourceRepository = "D:/Dataset/"
repositoryToSave = "D:/KDA/"

dfAll = []

for roundFile in os.listdir(sourceRepository):
    roundPath = os.path.join(sourceRepository, roundFile)

    if not os.path.isdir(roundPath):
        continue

    for roleFile in os.listdir(roundPath):
        rolePath = os.path.join(roundPath, roleFile)

        df = pd.read_csv(rolePath, encoding="utf-16")

        result = df[["riotIdGameName","kills","deaths","assists"]].copy()

        result["KDA"] = ((result["kills"] + result["assists"])/ result["deaths"].replace(0, 1)).round(2)

        result["round"] = roundFile

        roleName = os.path.splitext(roleFile)[0]
        result["role"] = roleName.split("_")[-1]

        dfAll.append(result)

dfFinal = pd.concat(dfAll, ignore_index=True)

dfFinal.to_csv(os.path.join(repositoryToSave, "allRoundsKDA.csv"),index=False)

dfFinal["roundNumber"] = (dfFinal["round"].str.extract(r"Round_(\d+)").astype(int))

dfFinal["complianceRound"] = ((dfFinal["roundNumber"] - 1) // 2) + 1

dfAggregated = (dfFinal.groupby(["riotIdGameName", "role", "complianceRound"],as_index=False).agg({"kills": "sum","deaths": "sum","assists": "sum"}))

dfAggregated["KDA"] = ((dfAggregated["kills"] + dfAggregated["assists"]) / dfAggregated["deaths"].replace(0, 1)).round(2)

dfAggregated["round"] = ("Round_" + dfAggregated["complianceRound"].astype(str).str.zfill(2))

dfAggregated = dfAggregated[["riotIdGameName","role","round","kills","deaths","assists","KDA"]]

dfAggregated.to_csv(os.path.join(repositoryToSave, "aggregatedKDA.csv"),index=False)

