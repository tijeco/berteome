# AUTOGENERATED! DO NOT EDIT! File to edit: ../notebooks/final/01_residue_predictions.ipynb.

# %% auto 0
__all__ = ['modelPredDF', 'modelLoader', 'run_model', 'logits2prob', 'maskifySeq', 'tokenizeSeq', 'naturalAAIndex', 'getNatProbs']

# %% ../notebooks/final/01_residue_predictions.ipynb 2
from transformers import BertTokenizer, BertForMaskedLM, EsmTokenizer, EsmForMaskedLM
import torch
import pandas as pd
import numpy as np

# %% ../notebooks/final/01_residue_predictions.ipynb 3
class modelPredDF():
    def __init__(self, seq, tokenizer, model):
        self.aas = "ACDEFGHIKLMNPQRSTVWY"
        predDict = self.predictionDict(seq, tokenizer, model)
        self.df = pd.DataFrame.from_dict(predDict, orient = "index", columns = list(self.aas))
        self.df = self.df.div(self.df.sum(axis=1),axis=0)
        self.df.insert(0, "wt",list(seq))
        self.df.insert(1, "wtIndex",list(range(1,len(seq)+1)))
        wtScore = self.scoreCol("wt")
        self.df.insert(2, "wtScore",wtScore)
        self.df.insert(3, "n_effective", self.n_effective())
        self.df.insert(4, "topAA",self.topAA())
        topAAscore = self.scoreCol("topAA")
        self.df.insert(5, "topAAscore", topAAscore)
        
        self.wtSeq = ''.join(list(self.df["wt"]))
        self.wtSeqScore = self.scoreSeq(self.wtSeq)

        self.topAASeq = ''.join(list(self.df["topAA"]))
        self.topAASeqScore = self.scoreSeq(self.topAASeq)

    def predictionDict(self, seq, tokenizer, model):
      naturalAAIndices = naturalAAIndex(self.aas,tokenizer)
      predDict = {}
      for wtIndex in range(len(seq)):
        maskedSeq = tokenizeSeq(seq, tokenizer, mask_index = wtIndex)
        seq_logits = run_model(model, maskedSeq)
        seq_probs = logits2prob(seq_logits)
        predDict[wtIndex] = [i.item() for i in getNatProbs(naturalAAIndices, seq_probs[0, wtIndex +1])]
      return predDict

    def scoreCol(self, col):
        score = []
        for row in self.df.to_dict(orient="records"):
	        col_aa = row[col]
	        score.append(row[col_aa])
        return score
    
    def scoreSeq(self, seq):
      seqScore = 0
      if len(seq) != len(self.df):
        raise Exception(f"The provided sequence is of length {len(seq)}, but berteome expected {len(self.df)}")
      for index, row in self.df.iterrows():
        seqScore += row[seq[index]]
      return seqScore / len(self.df)


    def n_effective(self):
      df_aas = self.df[list(self.aas)]
      entropy =  -(np.log(df_aas) * df_aas)
      return np.exp(entropy.sum(axis = 1))

    def topAA(self):
      return self.df[list(self.aas)].idxmax(axis=1)
                            
    def aa_correlation(self):
      return self.df[list(self.aas)].corr()

# %% ../notebooks/final/01_residue_predictions.ipynb 4
class modelLoader():
  def __init__(self):
    self.supported_model_dict = {
        "Rostlab/prot_bert" : self.token_model_dict("prot_bert"),
        "facebook/esm2_t33_650M_UR50D" : self.token_model_dict("esm"),
        "facebook/esm1b_t33_650M_UR50S": self.token_model_dict("esm")
    }
    self.supported_models = list(self.supported_model_dict.keys())

  
  def token_model_dict(self, model_name):
    if model_name == "prot_bert":
      tokenModelDict = {"tokenizer":BertTokenizer, "model":BertForMaskedLM}
    if model_name == "esm":
      tokenModelDict = {"tokenizer":EsmTokenizer, "model":EsmForMaskedLM}
    return tokenModelDict
  
  def load_model(self, model_path):
    tokenizerLM = self.supported_model_dict[model_path]["tokenizer"]
    maskedLM = self.supported_model_dict[model_path]["model"]
    tokenizer = tokenizerLM.from_pretrained(model_path)
    model = maskedLM.from_pretrained(model_path)
    return tokenizer, model

# %% ../notebooks/final/01_residue_predictions.ipynb 5
def run_model(model, inputs):
  with torch.no_grad():
    logits = model(**inputs).logits
  return logits

def logits2prob(logits):
  return torch.softmax(logits,dim=2)

# %% ../notebooks/final/01_residue_predictions.ipynb 6
def maskifySeq(seq, tokenizer, i):
    seqList = list(seq)
    if i != None:
      seqList[i] = tokenizer.mask_token 
    return " ".join(seqList)

def tokenizeSeq(seq, tokenizer, mask_index = None, return_tensors = "pt"):
  maskified_seq = maskifySeq(seq, tokenizer, mask_index)
  return tokenizer(maskified_seq, return_tensors=return_tensors)

def naturalAAIndex(aas, tokenizer):
    return tokenizeSeq(aas, tokenizer, return_tensors=None)["input_ids"][1:-1]

def getNatProbs(natAAList,probList):
    natProbList = []
    for natAAIndex in natAAList:
      natProbList.append(probList[natAAIndex])
    return natProbList
