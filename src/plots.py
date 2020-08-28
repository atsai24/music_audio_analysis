import matplotlib.pyplot as plt

def plot_genre_attribute_hist(genres, attribute, titles):
    fig, axs = plt.subplots(2,3, figsize = (20,10))
    for i, ax in enumerate(axs.flatten()):
        ax.hist(getattr(genres[i].audio_features, attribute), bins = 20)
        ax.set_title(f'{titles[i]} {attribute} histogram', color = 'slategray')
    