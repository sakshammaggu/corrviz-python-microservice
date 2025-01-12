import seaborn as sns
import matplotlib.pyplot as plt
import base64
from io import BytesIO
# import os
# from datetime import datetime

def generate_correlation_heatmap(df):
    numeric_df = df.select_dtypes(include=["number"])
    if numeric_df.empty:
        raise ValueError("Dataframe contains no numeric columns for correlation calculation.")

    correlation_matrix = numeric_df.corr()

    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", square=True, linewidths=0.5)
    plt.title("Correlation Heatmap")
    heatmap_image = BytesIO()
    plt.savefig(heatmap_image, format="png")
    plt.close()

    heatmap_image.seek(0)

    # output_folder = "outputs"
    # os.makedirs(output_folder, exist_ok=True)
    # timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    # heatmap_output_file_path = os.path.join(output_folder, f"heatmap_{timestamp}.png")

    # with open(heatmap_output_file_path, "wb") as f:
    #     f.write(heatmap_image.read())

    heatmap_base64 = base64.b64encode(heatmap_image.getvalue()).decode("utf-8")

    return heatmap_base64