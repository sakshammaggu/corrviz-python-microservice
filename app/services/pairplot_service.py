import seaborn as sns
import matplotlib.pyplot as plt
import base64
from io import BytesIO
# import os
# from datetime import datetime

def generate_pairplot(df):
    numeric_df = df.select_dtypes(include=["number"])
    if numeric_df.empty:
        raise ValueError("Dataframe contains no numeric columns for pairplot generation.")
    
    sns.set_theme(style="whitegrid")
    pairplot = sns.pairplot(numeric_df, hue=df.columns[0])
    pairplot_image = BytesIO()
    pairplot.savefig(pairplot_image, format="png")
    plt.close()

    pairplot_image.seek(0)

    # output_folder = "outputs"
    # os.makedirs(output_folder, exist_ok=True)
    # timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    # pairplot_output_file_path = os.path.join(output_folder, f"pairplot_{timestamp}.png")

    # with open(pairplot_output_file_path, "wb") as f:
    #     f.write(pairplot_image.read())

    pairplot_base64 = base64.b64encode(pairplot_image.getvalue()).decode("utf-8")

    return pairplot_base64