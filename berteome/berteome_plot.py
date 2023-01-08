# AUTOGENERATED! DO NOT EDIT! File to edit: ../notebooks/final/03_plots.ipynb.

# %% auto 0
__all__ = ['seqlogo_plot', 'wtScore_plot', 'n_effective_plot', 'aa_correlation_plot']

# %% ../notebooks/final/03_plots.ipynb 1
import seqlogo
import matplotlib.pyplot as plt
import seaborn as sb

# %% ../notebooks/final/03_plots.ipynb 2
def seqlogo_plot(berteome, ic_scale = False, format = 'svg', size = 'xlarge'):
  berteome_aas = berteome.df[list(berteome.aas)]
  berteome_seqlogoPPM = seqlogo.Ppm(berteome_aas,alphabet_type = "AA")
  return seqlogo.seqlogo(berteome_seqlogoPPM ,ic_scale = ic_scale, format = format, size = size)

# %% ../notebooks/final/03_plots.ipynb 3
def wtScore_plot(berteome):
  fig, ax = plt.subplots()

  ax.plot(berteome.df.index,berteome.df["wtScore"])
  ax.set_xticks(berteome.df.index)
  ax.set_xticklabels(berteome.df["wt"])
  
  return fig, ax

# %% ../notebooks/final/03_plots.ipynb 4
def n_effective_plot(berteome):
  fig, ax = plt.subplots()

  ax.bar(berteome.df.index,berteome.df["n_effective"])
  ax.set_xticks(berteome.df.index)
  ax.set_xticklabels(berteome.df["wt"])
  
  return fig, ax

# %% ../notebooks/final/03_plots.ipynb 5
def aa_correlation_plot(berteome):
  return sb.clustermap(berteome.aa_correlation(), cmap="YlGnBu")
