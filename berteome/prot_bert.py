# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/01_bert.ipynb (unless otherwise specified).

__all__ = ['tokenizer', 'model', 'unmasker', 'spacifySeq', 'maskifySeq', 'allResidueCoordinates', 'aaPosDict',
           'bertPredictionDF']

# Cell
from transformers import BertForMaskedLM, BertTokenizer, pipeline
import pandas as pd

# Cell
from berteome import berteomeDF

# Cell
tokenizer = BertTokenizer.from_pretrained("Rostlab/prot_bert", do_lower_case=False )
model = BertForMaskedLM.from_pretrained("Rostlab/prot_bert")
unmasker = pipeline('fill-mask', model=model, tokenizer=tokenizer)

# Cell
def spacifySeq(seq):
  return ' '.join(list(seq))

# Cell
def maskifySeq(seq, pos, mask="[MASK]"):
  spacifiedSeq = spacifySeq(seq)
  seqList = spacifiedSeq.split()
  seqList[pos] = mask
  return " ".join(seqList)

# Cell
def allResidueCoordinates(seq,residue):
  return [i for i, x in enumerate(seq) if x == residue]

# Cell
def aaPosDict(aas):
    aaDict = {}
    for aaPos in range(len(aas)):
        aa = aas[aaPos]
        aaDict[aa] = aaPos
    return aaDict

# Cell
def bertPredictionDF(seq, aas="ACDEFGHIKLMNPQRSTVWY"):
  aaDict = aaPosDict(aas)
  bertPredDict = {}
  # posPredictions = []
  for aaPos in range(len(seq)):
    aa = seq[aaPos]
    maskPosSeq = maskifySeq(seq, aaPos)
    predictions = unmasker(maskPosSeq, top_k=30)
    predList = [0]*len(aas)
    for prediction in predictions:
      predAA = prediction["token_str"]
      if predAA in aaDict:
        predList[aaDict[predAA]] = prediction["score"]
    bertPredDict[aaPos] = predList
  bertPredDF = berteomeDF.modelPredDF(bertPredDict,seq, aas).predDf
  return bertPredDF