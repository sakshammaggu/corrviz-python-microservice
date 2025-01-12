import seaborn as sns
import matplotlib.pyplot as plt
import base64
import itertools
from io import BytesIO
# from datetime import datetime
# import os

def generate_scatterplots(df):
    numeric_columns = df.select_dtypes(include=["number"]).columns
    if len(numeric_columns) < 2:
        raise ValueError("The dataframe must have at least two numeric columns to generate scatterplots.")
    
    column_pairs = list(itertools.combinations(numeric_columns, 2))
    num_pairs = len(column_pairs)

    cols = 3 
    rows = -(-num_pairs // cols)  
    fig, axes = plt.subplots(rows, cols, figsize=(cols * 6, rows * 5), squeeze=False)
    axes = axes.flatten()

    for idx, (x_col, y_col) in enumerate(column_pairs):
        sns.scatterplot(
            data = df,
            x = x_col,
            y = y_col,
            hue = None,  
            ax = axes[idx]
        )
        axes[idx].set_title(f"{x_col} vs {y_col}", fontsize=12)
        axes[idx].set_xlabel(x_col)
        axes[idx].set_ylabel(y_col)

    for idx in range(num_pairs, len(axes)):
        axes[idx].set_visible(False)

    plt.tight_layout()
    scatterplots_image = BytesIO()
    plt.savefig(scatterplots_image, format="png")
    plt.close()

    # output_folder = "outputs"
    # os.makedirs(output_folder, exist_ok=True)
    # timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    # scatterplot_output_file_path = os.path.join(output_folder, f"scatterplots_{timestamp}.png")

    # with open(scatterplot_output_file_path, "wb") as f:
    #     f.write(scatterplots_image.getvalue())

    scatterplots_base64 = base64.b64encode(scatterplots_image.getvalue()).decode("utf-8")

    return scatterplots_base64