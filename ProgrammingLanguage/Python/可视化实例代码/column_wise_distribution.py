from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns


df = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD'))


def column_dist(df, col):
    sns.distplot(df[col])
    plt.show()


# plot subplots for every columns
def subplots(df):
    N = len(df.columns)

    fig, axes = plt.subplots(ncols=4
                             , nrows=N//4 + 1, figsize=(10, 3 * (N//4 + 1)))
    for ax, col in zip(axes.flatten(), df.columns):
        sns.histplot(df[col], ax=ax)
    plt.tight_layout()
    plt.show()


