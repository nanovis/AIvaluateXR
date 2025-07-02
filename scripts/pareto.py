import argparse
import json
from pathlib import Path
from typing import Dict

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



def min_max_normalize(series: pd.Series) -> pd.Series:
    return (series - series.min()) / (series.max() - series.min())


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Pareto plot for model metrics")
    p.add_argument("--csv", required=True, type=Path, help="csv file")
    p.add_argument("--output", type=Path, default=Path("pareto_plot.png"), help="Output PNG")
    return p.parse_args()



class ParetoAnalyser:
    quality_metrics = [
        "Hellaswag", "mmlu", "ARC", "Truthful-qa", "winogrande", "Perplexity"]
    performance_metrics = ["PP", "TG", "battery", "memory"]
    stability_metrics = ["PP_CV", "TG_CV"]

    default_weights: Dict[str, Dict[str, float]] = {
        "quality": {m: 1 for m in quality_metrics},
        "performance": {"PP": 3.5, "TG": 3.5, "battery": 1, "memory": 2},
        "stability": {"PP_CV": 1, "TG_CV": 1},
    }

    inverse_metrics = {"Perplexity", "battery", "memory", "PP_CV", "TG_CV"}

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()
        self.weights = self.default_weights

    def run(self) -> None:
        self._prepare_metrics()
        self._calc_weighted_scores()
        self._find_pareto_front()

    def _prepare_metrics(self) -> None:
        for m in self.inverse_metrics:
            self.df[m] = 1.0 / self.df[m]
        for m in (self.quality_metrics + self.performance_metrics + self.stability_metrics):
            self.df[f"{m}_norm"] = min_max_normalize(self.df[m])

    def _calc_weighted_scores(self) -> None:
        for cat, metrics in [
            ("quality", self.quality_metrics),
            ("performance", self.performance_metrics),
            ("stability", self.stability_metrics),
        ]:
            w = self.weights[cat]
            total = sum(self.df[f"{m}_norm"] * w[m] for m in metrics)
            self.df[f"Weighted_Score_Scaled_{cat}"] = min_max_normalize(total)

    def _find_pareto_front(self) -> None:
        pts = self.df[[
            "Weighted_Score_Scaled_quality",
            "Weighted_Score_Scaled_performance",
            "Weighted_Score_Scaled_stability",
        ]].values
        pareto = np.ones(len(pts), dtype=bool)
        for i, c in enumerate(pts):
            if pareto[i]:
                dominated = np.all(pts <= c, axis=1) & np.any(pts < c, axis=1)
                pareto[dominated] = False
        self.df["is_pareto"] = pareto



def device2color(dev: str) -> str:
    palette = {"ML 2": "#377eb8", "Meta Q3": "#f37b53", "Vivo": "#4daf4a", "AVP (CPU)": "#984ea3"}
    return palette.get(dev, "#999999")


def make_plot(df: pd.DataFrame, output: Path, dpi: int = 200) -> None:
    df["device"] = df["model"].str.split("-", n=1).str[0]
    df["short_model"] = df["model"].str.split("-", n=1).str[1]

    fig = plt.figure(figsize=(12, 8), dpi=dpi)
    ax = fig.add_subplot(111, projection="3d")

    # Non‑Pareto cloud
    non_pareto = df[~df["is_pareto"]]
    ax.scatter(non_pareto["Weighted_Score_Scaled_quality"],
               non_pareto["Weighted_Score_Scaled_performance"],
               non_pareto["Weighted_Score_Scaled_stability"],
               color="#d3d3d3", alpha=0.4, s=80)

    # Pareto points + direct labels per device
    for dev in df["device"].unique():
        subset = df[(df["device"] == dev) & (df["is_pareto"])]
        if not subset.empty:
            ax.scatter(subset["Weighted_Score_Scaled_quality"],
                       subset["Weighted_Score_Scaled_performance"],
                       subset["Weighted_Score_Scaled_stability"],
                       color=device2color(dev), s=150, alpha=0.75)
            for _, row in subset.iterrows():
                ax.text(row["Weighted_Score_Scaled_quality"],
                        row["Weighted_Score_Scaled_performance"],
                        row["Weighted_Score_Scaled_stability"],
                        row["short_model"], fontsize=6, ha="center", va="center", weight="bold")
        # Ensure legend entry exists even if no Pareto point
        ax.scatter([], [], [], color=device2color(dev), label=dev)

    ax.set_xlabel("Quality")
    ax.set_ylabel("Performance")
    ax.set_zlabel("Stability")
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(output, dpi=dpi)
    print(f"Saved {output.resolve()}")
    plt.close(fig)

def main() -> None:
    args = parse_args()
    df = pd.read_csv(args.csv)

    analyser = ParetoAnalyser(df)
    analyser.run()
    make_plot(analyser.df, args.output, dpi=200)


if __name__ == "__main__":
    main()
