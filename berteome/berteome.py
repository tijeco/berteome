# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/00_core.ipynb (unless otherwise specified).

__all__ = ['tokenizer', 'model', 'unmasker', 'spacifySeq', 'maskifySeq', 'allResidueCoordinates',
           'allResiduePredictions', 'getTopSeq', 'residuePredictionScore', 'hasNonStandardAA', 'childrenPredictions',
           'childrenPPM']

# Cell
from transformers import BertForMaskedLM, BertTokenizer, pipeline
import pandas as pd

# Cell
tokenizer = BertTokenizer.from_pretrained("Rostlab/prot_bert", do_lower_case=False )
model = BertForMaskedLM.from_pretrained("Rostlab/prot_bert")
unmasker = pipeline('fill-mask', model=model, tokenizer=tokenizer)

# Cell
def spacifySeq(seq):
  return "".join([ aa +" " for aa in seq]).strip()

# Cell
def maskifySeq(seq, pos, mask="[MASK]"):
  seqList = seq.split()
  seqList[pos] = mask
  return "".join(aa +" " for aa in seqList).strip()

# Cell
def allResidueCoordinates(seq,residue):
  return [i for i, x in enumerate(seq) if x == residue]
assert allResidueCoordinates("MENDEL","E") == [1,4]

# Cell
def allResiduePredictions(seq):
  spaceSeq = spacifySeq(seq)

  posPredictions = []
  for aaPos in range(len(seq)):
    aa = seq[aaPos]
    maskPosSeq = maskifySeq(spaceSeq, aaPos)
    prediction = unmasker(maskPosSeq, top_k=30)
    posPredictions.append(prediction)
  return posPredictions

# Cell
def getTopSeq(allPredictions):
  topSeq = ""
  for aaPred in allPredictions:
    topSeq += aaPred[0]["token_str"]
  return topSeq

# Cell
def residuePredictionScore(allPredictions, seq):
  residueScoreDict = {
      "wt":list(seq),
      "wtIndex":list(range(len(seq)+1))[1:],
      "wtScore":[],
      "A":[],
      "C":[],
      "D":[],
      "E":[],
      "F":[],
      "G":[],
      "H":[],
      "I":[],
      "K":[],
      "L":[],
      "M":[],
      "N":[],
      "P":[],
      "Q":[],
      "R":[],
      "S":[],
      "T":[],
      "V":[],
      "W":[],
      "Y":[]
  }
  for aaPredPos in range(len(allPredictions)):
    aaPred = allPredictions[aaPredPos]
    wtAA = seq[aaPredPos]
    for predRank in range(len(aaPred)):
      posPred = aaPred[predRank]
      predAA = posPred["token_str"]
      # print(predRank, posPred["token_str"])
      if predAA in residueScoreDict:
        residueScoreDict[predAA].append(posPred["score"])
        if predAA == wtAA:
          residueScoreDict["wtScore"].append(posPred["score"])

  residueScoreDF = pd.DataFrame.from_dict(residueScoreDict)
  return residueScoreDF


# Cell
def hasNonStandardAA(seq, alphabet="ACDEFGHIKLMNPQRSTVWY"):
	return (set(seq) - set(alphabet)) != set()
assert hasNonStandardAA("MENDEL") == False

# Cell
def childrenPredictions(allPredictions,seq):
  residues = "ACDEFGHIKLMNPQRSTVQY"

  parentScoreDF = residuePredictionScore(allPredictions, seq)
  parentScoreDF["seq"] = seq
  scoreDFs = [parentScoreDF]
  for prediction in allPredictions:
    top5predictions = prediction[:5]
    for child in top5predictions:
        childSeq = child["sequence"].replace(" ","")
        if childSeq != seq:
          if not hasNonStandardAA(childSeq):
            # print(childSeq)
            childPredictions = allResiduePredictions(childSeq)
            childScoreDF = residuePredictionScore(childPredictions, childSeq)
            childScoreDF["seq"] = childSeq
            scoreDFs.append(childScoreDF)
  return pd.concat(scoreDFs)

# Cell
def childrenPPM(childrenScores):
  childrenScoreSum = childrenScores.groupby(["wtIndex"]).sum()
  childrenScoreSum = childrenScoreSum[childrenScoreSum.columns[1:]]
  childrenScorePPM = childrenScoreSum.div(childrenScoreSum.sum(axis=1),axis=0)
  return childrenScorePPM