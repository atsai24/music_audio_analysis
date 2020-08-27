import matplotlib.pyplot as plt

def plot_genre_attribute_hist(genres, attribute, titles):
    fig, axs = plt.subplots(3,2, figsize = (15,15))
    for i, ax in enumerate(axs.flatten()):
        ax.hist(getattr(genres[i].audio_features, attribute), bins = 20)
        ax.set_title(f'{titles[i]} {attribute} histogram')
    