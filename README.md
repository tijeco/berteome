# berteome



```python
from berteome import prot_bert
```

    Some weights of the model checkpoint at Rostlab/prot_bert were not used when initializing BertForMaskedLM: ['cls.seq_relationship.bias', 'cls.seq_relationship.weight']
    - This IS expected if you are initializing BertForMaskedLM from the checkpoint of a model trained on another task or with another architecture (e.g. initializing a BertForSequenceClassification model from a BertForPreTraining model).
    - This IS NOT expected if you are initializing BertForMaskedLM from the checkpoint of a model that you expect to be exactly identical (initializing a BertForSequenceClassification model from a BertForSequenceClassification model).


```python
from berteome import esm
```

```python
from berteome import berteomeDF
```


    ---------------------------------------------------------------------------

    ImportError                               Traceback (most recent call last)

    /var/folders/x1/098shbqn0rs8vd5ybvyb0k9h0000gn/T/ipykernel_70195/4107489332.py in <module>
    ----> 1 from berteome import berteomeDF
    

    ImportError: cannot import name 'berteomeDF' from 'berteome' (/Users/jeffcole/miniconda3/envs/berteome/lib/python3.7/site-packages/berteome-0.1.0-py3.7.egg/berteome/__init__.py)


```python
prot_bert.bertPredictionDF("MENDEL")
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>wt</th>
      <th>wtIndex</th>
      <th>A</th>
      <th>C</th>
      <th>D</th>
      <th>E</th>
      <th>F</th>
      <th>G</th>
      <th>H</th>
      <th>I</th>
      <th>...</th>
      <th>M</th>
      <th>N</th>
      <th>P</th>
      <th>Q</th>
      <th>R</th>
      <th>S</th>
      <th>T</th>
      <th>V</th>
      <th>W</th>
      <th>Y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>M</td>
      <td>1</td>
      <td>0.036685</td>
      <td>0.011501</td>
      <td>0.048229</td>
      <td>0.118868</td>
      <td>0.024064</td>
      <td>0.039190</td>
      <td>0.012617</td>
      <td>0.066477</td>
      <td>...</td>
      <td>0.076580</td>
      <td>0.072637</td>
      <td>0.024714</td>
      <td>0.038660</td>
      <td>0.043091</td>
      <td>0.070257</td>
      <td>0.056526</td>
      <td>0.049911</td>
      <td>0.007779</td>
      <td>0.021692</td>
    </tr>
    <tr>
      <th>1</th>
      <td>E</td>
      <td>2</td>
      <td>0.045712</td>
      <td>0.015659</td>
      <td>0.041913</td>
      <td>0.074816</td>
      <td>0.037146</td>
      <td>0.044317</td>
      <td>0.018260</td>
      <td>0.073063</td>
      <td>...</td>
      <td>0.043572</td>
      <td>0.062655</td>
      <td>0.025272</td>
      <td>0.036905</td>
      <td>0.055532</td>
      <td>0.064412</td>
      <td>0.049945</td>
      <td>0.056779</td>
      <td>0.012689</td>
      <td>0.029887</td>
    </tr>
    <tr>
      <th>2</th>
      <td>N</td>
      <td>3</td>
      <td>0.043558</td>
      <td>0.009684</td>
      <td>0.162566</td>
      <td>0.184336</td>
      <td>0.033777</td>
      <td>0.044654</td>
      <td>0.012353</td>
      <td>0.052622</td>
      <td>...</td>
      <td>0.041478</td>
      <td>0.041984</td>
      <td>0.019989</td>
      <td>0.025511</td>
      <td>0.029428</td>
      <td>0.048098</td>
      <td>0.030299</td>
      <td>0.054734</td>
      <td>0.007428</td>
      <td>0.024920</td>
    </tr>
    <tr>
      <th>3</th>
      <td>D</td>
      <td>4</td>
      <td>0.042079</td>
      <td>0.013243</td>
      <td>0.049744</td>
      <td>0.086189</td>
      <td>0.039733</td>
      <td>0.055907</td>
      <td>0.016860</td>
      <td>0.073291</td>
      <td>...</td>
      <td>0.040078</td>
      <td>0.060817</td>
      <td>0.032022</td>
      <td>0.039686</td>
      <td>0.046224</td>
      <td>0.062319</td>
      <td>0.044898</td>
      <td>0.058933</td>
      <td>0.010875</td>
      <td>0.026594</td>
    </tr>
    <tr>
      <th>4</th>
      <td>E</td>
      <td>5</td>
      <td>0.046638</td>
      <td>0.018769</td>
      <td>0.079816</td>
      <td>0.086908</td>
      <td>0.050634</td>
      <td>0.050462</td>
      <td>0.022395</td>
      <td>0.074495</td>
      <td>...</td>
      <td>0.028960</td>
      <td>0.062229</td>
      <td>0.023877</td>
      <td>0.030532</td>
      <td>0.040486</td>
      <td>0.065190</td>
      <td>0.044934</td>
      <td>0.068032</td>
      <td>0.012155</td>
      <td>0.038031</td>
    </tr>
    <tr>
      <th>5</th>
      <td>L</td>
      <td>6</td>
      <td>0.035695</td>
      <td>0.008615</td>
      <td>0.060928</td>
      <td>0.142576</td>
      <td>0.019581</td>
      <td>0.046287</td>
      <td>0.013043</td>
      <td>0.060374</td>
      <td>...</td>
      <td>0.037424</td>
      <td>0.090177</td>
      <td>0.019358</td>
      <td>0.032733</td>
      <td>0.043823</td>
      <td>0.045863</td>
      <td>0.043224</td>
      <td>0.045121</td>
      <td>0.009800</td>
      <td>0.021241</td>
    </tr>
  </tbody>
</table>
<p>6 rows × 22 columns</p>
</div>



```python
esm.esmPredictionDF("MENDEL")
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>wt</th>
      <th>wtIndex</th>
      <th>A</th>
      <th>C</th>
      <th>D</th>
      <th>E</th>
      <th>F</th>
      <th>G</th>
      <th>H</th>
      <th>I</th>
      <th>...</th>
      <th>M</th>
      <th>N</th>
      <th>P</th>
      <th>Q</th>
      <th>R</th>
      <th>S</th>
      <th>T</th>
      <th>V</th>
      <th>W</th>
      <th>Y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>M</td>
      <td>1</td>
      <td>0.033952</td>
      <td>0.007039</td>
      <td>0.054737</td>
      <td>0.063365</td>
      <td>0.018590</td>
      <td>0.029267</td>
      <td>0.010216</td>
      <td>0.028865</td>
      <td>...</td>
      <td>0.456082</td>
      <td>0.029166</td>
      <td>0.023344</td>
      <td>0.019043</td>
      <td>0.023603</td>
      <td>0.030170</td>
      <td>0.023352</td>
      <td>0.033982</td>
      <td>0.004791</td>
      <td>0.013076</td>
    </tr>
    <tr>
      <th>1</th>
      <td>E</td>
      <td>2</td>
      <td>0.058999</td>
      <td>0.021031</td>
      <td>0.054622</td>
      <td>0.072057</td>
      <td>0.037186</td>
      <td>0.053090</td>
      <td>0.025848</td>
      <td>0.065879</td>
      <td>...</td>
      <td>0.024329</td>
      <td>0.059710</td>
      <td>0.035728</td>
      <td>0.040369</td>
      <td>0.052300</td>
      <td>0.073618</td>
      <td>0.057319</td>
      <td>0.062975</td>
      <td>0.014029</td>
      <td>0.030339</td>
    </tr>
    <tr>
      <th>2</th>
      <td>N</td>
      <td>3</td>
      <td>0.055626</td>
      <td>0.014060</td>
      <td>0.077887</td>
      <td>0.122153</td>
      <td>0.034727</td>
      <td>0.058822</td>
      <td>0.019171</td>
      <td>0.061401</td>
      <td>...</td>
      <td>0.031318</td>
      <td>0.044172</td>
      <td>0.029668</td>
      <td>0.034335</td>
      <td>0.052372</td>
      <td>0.057394</td>
      <td>0.047432</td>
      <td>0.069432</td>
      <td>0.013282</td>
      <td>0.025859</td>
    </tr>
    <tr>
      <th>3</th>
      <td>D</td>
      <td>4</td>
      <td>0.044610</td>
      <td>0.017627</td>
      <td>0.036298</td>
      <td>0.071025</td>
      <td>0.031629</td>
      <td>0.049782</td>
      <td>0.023518</td>
      <td>0.061833</td>
      <td>...</td>
      <td>0.058515</td>
      <td>0.043762</td>
      <td>0.037227</td>
      <td>0.054164</td>
      <td>0.055120</td>
      <td>0.060091</td>
      <td>0.052912</td>
      <td>0.070125</td>
      <td>0.017567</td>
      <td>0.027211</td>
    </tr>
    <tr>
      <th>4</th>
      <td>E</td>
      <td>5</td>
      <td>0.045966</td>
      <td>0.027927</td>
      <td>0.047431</td>
      <td>0.057574</td>
      <td>0.052450</td>
      <td>0.054545</td>
      <td>0.030670</td>
      <td>0.071293</td>
      <td>...</td>
      <td>0.025417</td>
      <td>0.051106</td>
      <td>0.033450</td>
      <td>0.038940</td>
      <td>0.055194</td>
      <td>0.076423</td>
      <td>0.050060</td>
      <td>0.063550</td>
      <td>0.017663</td>
      <td>0.038091</td>
    </tr>
    <tr>
      <th>5</th>
      <td>L</td>
      <td>6</td>
      <td>0.048226</td>
      <td>0.016231</td>
      <td>0.060284</td>
      <td>0.100391</td>
      <td>0.031534</td>
      <td>0.052584</td>
      <td>0.023015</td>
      <td>0.065281</td>
      <td>...</td>
      <td>0.029354</td>
      <td>0.063840</td>
      <td>0.025546</td>
      <td>0.039313</td>
      <td>0.062937</td>
      <td>0.064147</td>
      <td>0.053790</td>
      <td>0.060177</td>
      <td>0.013714</td>
      <td>0.028147</td>
    </tr>
  </tbody>
</table>
<p>6 rows × 22 columns</p>
</div>



This file will become your README and also the index of your documentation.

## Install

`pip install berteome`

# How to use

Berteome makes use of the masked language model of BERT to determine predictions for all residues in a protein sequence. 



For instance, it uses the `prot_bert` model from the Rostlab to generate predictions for a given residue in a sequence as follows by putting a `[MASK]` token in a spaced out seqeunce.

## single residue predictions

```python
berteome.unmasker('D L I P T S S K L V V [MASK] D T S L Q V K K A F F A L V T')
```




    [{'sequence': 'D L I P T S S K L V V L D T S L Q V K K A F F A L V T',
      'score': 0.11088439077138901,
      'token': 5,
      'token_str': 'L'},
     {'sequence': 'D L I P T S S K L V V S D T S L Q V K K A F F A L V T',
      'score': 0.0840253233909607,
      'token': 10,
      'token_str': 'S'},
     {'sequence': 'D L I P T S S K L V V V D T S L Q V K K A F F A L V T',
      'score': 0.07328338176012039,
      'token': 8,
      'token_str': 'V'},
     {'sequence': 'D L I P T S S K L V V K D T S L Q V K K A F F A L V T',
      'score': 0.06921844929456711,
      'token': 12,
      'token_str': 'K'},
     {'sequence': 'D L I P T S S K L V V I D T S L Q V K K A F F A L V T',
      'score': 0.06382393091917038,
      'token': 11,
      'token_str': 'I'}]



This gives the top five best predictions for the residues in this sequence, with the following fields:
* sequence
  * the spaced out full sequence including the predicted residue
* score
  * how likely this residue is to be behind the mask
* token
  * the number associated with the residue
* token_str
  * the actual residue

Something to note is that only one mask can be predicted at a time. So it is not possible to predict more than one mask.

Berteome provides two helper functions to help the user generate single residue predictions with ease. To generate predictions the sequences must be space delimeted and have the `[MASK]` token. To expedite this berteome provides `spacifySeq()` which space delimits the sequence. To make the sequence `MENDEL` space delimited, do the following.



```python
mendel_w_spaces = berteome.spacifySeq("MENDEL")
mendel_w_spaces
```




    'M E N D E L'



Then, the user can put a mask in which ever residue they choose using `maskifySeq()`, so to put a mask in the previous sequence on the third residue, do the following.

```python
mendel_mask_3 = berteome.maskifySeq(mendel_w_spaces, 3)
mendel_mask_3
```




    'M E N [MASK] E L'



Now a prediction for the masked residue can be acieved by providing it to `unmasker()`

```python
mendel_mask_3_predictions = berteome.unmasker(mendel_mask_3)
mendel_mask_3_predictions
```




    [{'sequence': 'M E N L E L',
      'score': 0.10907968133687973,
      'token': 5,
      'token_str': 'L'},
     {'sequence': 'M E N K E L',
      'score': 0.09135881811380386,
      'token': 12,
      'token_str': 'K'},
     {'sequence': 'M E N E E L',
      'score': 0.08618851006031036,
      'token': 9,
      'token_str': 'E'},
     {'sequence': 'M E N I E L',
      'score': 0.07329064607620239,
      'token': 11,
      'token_str': 'I'},
     {'sequence': 'M E N S E L',
      'score': 0.06231885030865669,
      'token': 10,
      'token_str': 'S'}]



## multiple residue predictions

Berteome also makes it possible to generate all possible predictions for all residues in the sequence using `allResiduePredictions()`

```python
mendel_all_predictions = berteome.allResiduePredictions("MENDEL")
```

This provides the raw output, so berteome also has a function to make it a more parseable panda dataframe using `residuePredictionScore()`

```python
mendel_all_predictionDF =  berteome.residuePredictionScore(mendel_all_predictions, "MENDEL")
mendel_all_predictionDF
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>wt</th>
      <th>wtIndex</th>
      <th>wtScore</th>
      <th>A</th>
      <th>C</th>
      <th>D</th>
      <th>E</th>
      <th>F</th>
      <th>G</th>
      <th>H</th>
      <th>...</th>
      <th>M</th>
      <th>N</th>
      <th>P</th>
      <th>Q</th>
      <th>R</th>
      <th>S</th>
      <th>T</th>
      <th>V</th>
      <th>W</th>
      <th>Y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>M</td>
      <td>1</td>
      <td>0.076580</td>
      <td>0.036685</td>
      <td>0.011501</td>
      <td>0.048229</td>
      <td>0.118868</td>
      <td>0.024064</td>
      <td>0.039190</td>
      <td>0.012617</td>
      <td>...</td>
      <td>0.076580</td>
      <td>0.072637</td>
      <td>0.024714</td>
      <td>0.038660</td>
      <td>0.043091</td>
      <td>0.070257</td>
      <td>0.056526</td>
      <td>0.049911</td>
      <td>0.007779</td>
      <td>0.021692</td>
    </tr>
    <tr>
      <th>1</th>
      <td>E</td>
      <td>2</td>
      <td>0.074816</td>
      <td>0.045712</td>
      <td>0.015659</td>
      <td>0.041913</td>
      <td>0.074816</td>
      <td>0.037146</td>
      <td>0.044317</td>
      <td>0.018260</td>
      <td>...</td>
      <td>0.043572</td>
      <td>0.062655</td>
      <td>0.025272</td>
      <td>0.036905</td>
      <td>0.055532</td>
      <td>0.064412</td>
      <td>0.049945</td>
      <td>0.056779</td>
      <td>0.012689</td>
      <td>0.029887</td>
    </tr>
    <tr>
      <th>2</th>
      <td>N</td>
      <td>3</td>
      <td>0.041984</td>
      <td>0.043558</td>
      <td>0.009684</td>
      <td>0.162566</td>
      <td>0.184336</td>
      <td>0.033777</td>
      <td>0.044654</td>
      <td>0.012353</td>
      <td>...</td>
      <td>0.041478</td>
      <td>0.041984</td>
      <td>0.019989</td>
      <td>0.025511</td>
      <td>0.029428</td>
      <td>0.048098</td>
      <td>0.030299</td>
      <td>0.054734</td>
      <td>0.007428</td>
      <td>0.024920</td>
    </tr>
    <tr>
      <th>3</th>
      <td>D</td>
      <td>4</td>
      <td>0.049744</td>
      <td>0.042079</td>
      <td>0.013243</td>
      <td>0.049744</td>
      <td>0.086189</td>
      <td>0.039733</td>
      <td>0.055907</td>
      <td>0.016860</td>
      <td>...</td>
      <td>0.040078</td>
      <td>0.060817</td>
      <td>0.032022</td>
      <td>0.039686</td>
      <td>0.046224</td>
      <td>0.062319</td>
      <td>0.044898</td>
      <td>0.058933</td>
      <td>0.010875</td>
      <td>0.026594</td>
    </tr>
    <tr>
      <th>4</th>
      <td>E</td>
      <td>5</td>
      <td>0.086908</td>
      <td>0.046638</td>
      <td>0.018769</td>
      <td>0.079816</td>
      <td>0.086908</td>
      <td>0.050634</td>
      <td>0.050462</td>
      <td>0.022395</td>
      <td>...</td>
      <td>0.028960</td>
      <td>0.062229</td>
      <td>0.023877</td>
      <td>0.030532</td>
      <td>0.040486</td>
      <td>0.065190</td>
      <td>0.044934</td>
      <td>0.068032</td>
      <td>0.012155</td>
      <td>0.038031</td>
    </tr>
    <tr>
      <th>5</th>
      <td>L</td>
      <td>6</td>
      <td>0.056766</td>
      <td>0.035695</td>
      <td>0.008615</td>
      <td>0.060928</td>
      <td>0.142576</td>
      <td>0.019581</td>
      <td>0.046287</td>
      <td>0.013043</td>
      <td>...</td>
      <td>0.037424</td>
      <td>0.090177</td>
      <td>0.019358</td>
      <td>0.032733</td>
      <td>0.043823</td>
      <td>0.045863</td>
      <td>0.043224</td>
      <td>0.045121</td>
      <td>0.009800</td>
      <td>0.021241</td>
    </tr>
  </tbody>
</table>
<p>6 rows × 23 columns</p>
</div>



For each residue (wt), the score of the actual residue is provided as well as the score for all 20 amino acids. If needed, the raw output looks like this.

```python
mendel_all_predictions
```




    [[{'sequence': 'E E N D E L',
       'score': 0.11886773258447647,
       'token': 9,
       'token_str': 'E'},
      {'sequence': 'K E N D E L',
       'score': 0.10773412883281708,
       'token': 12,
       'token_str': 'K'},
      {'sequence': 'M E N D E L',
       'score': 0.07657960802316666,
       'token': 21,
       'token_str': 'M'},
      {'sequence': 'N E N D E L',
       'score': 0.07263746112585068,
       'token': 17,
       'token_str': 'N'},
      {'sequence': 'L E N D E L',
       'score': 0.07247161120176315,
       'token': 5,
       'token_str': 'L'},
      {'sequence': 'S E N D E L',
       'score': 0.07025714218616486,
       'token': 10,
       'token_str': 'S'},
      {'sequence': 'I E N D E L',
       'score': 0.06647692620754242,
       'token': 11,
       'token_str': 'I'},
      {'sequence': 'T E N D E L',
       'score': 0.05652552843093872,
       'token': 15,
       'token_str': 'T'},
      {'sequence': 'V E N D E L',
       'score': 0.04991144686937332,
       'token': 8,
       'token_str': 'V'},
      {'sequence': 'D E N D E L',
       'score': 0.04822919890284538,
       'token': 14,
       'token_str': 'D'},
      {'sequence': 'R E N D E L',
       'score': 0.04309074580669403,
       'token': 13,
       'token_str': 'R'},
      {'sequence': 'G E N D E L',
       'score': 0.03918968141078949,
       'token': 7,
       'token_str': 'G'},
      {'sequence': 'Q E N D E L',
       'score': 0.03865953907370567,
       'token': 18,
       'token_str': 'Q'},
      {'sequence': 'A E N D E L',
       'score': 0.03668533265590668,
       'token': 6,
       'token_str': 'A'},
      {'sequence': 'P E N D E L',
       'score': 0.024714037775993347,
       'token': 16,
       'token_str': 'P'},
      {'sequence': 'F E N D E L',
       'score': 0.024063965305685997,
       'token': 19,
       'token_str': 'F'},
      {'sequence': 'Y E N D E L',
       'score': 0.0216918233782053,
       'token': 20,
       'token_str': 'Y'},
      {'sequence': 'H E N D E L',
       'score': 0.012617157772183418,
       'token': 22,
       'token_str': 'H'},
      {'sequence': 'C E N D E L',
       'score': 0.01150050014257431,
       'token': 23,
       'token_str': 'C'},
      {'sequence': 'W E N D E L',
       'score': 0.007778722792863846,
       'token': 24,
       'token_str': 'W'},
      {'sequence': 'X E N D E L',
       'score': 0.0003176695026922971,
       'token': 25,
       'token_str': 'X'},
      {'sequence': 'U E N D E L',
       'score': 2.722620462414227e-10,
       'token': 26,
       'token_str': 'U'},
      {'sequence': 'B E N D E L',
       'score': 2.2993504322776914e-10,
       'token': 27,
       'token_str': 'B'},
      {'sequence': 'E N D E L',
       'score': 2.0518205190445116e-10,
       'token': 3,
       'token_str': '[ S E P ]'},
      {'sequence': 'E N D E L',
       'score': 1.9894096092709646e-10,
       'token': 0,
       'token_str': '[ P A D ]'},
      {'sequence': 'E N D E L',
       'score': 1.9621000657554788e-10,
       'token': 2,
       'token_str': '[ C L S ]'},
      {'sequence': 'Z E N D E L',
       'score': 1.7657629525213991e-10,
       'token': 28,
       'token_str': 'Z'},
      {'sequence': 'O E N D E L',
       'score': 1.6853365925051378e-10,
       'token': 29,
       'token_str': 'O'},
      {'sequence': 'E N D E L',
       'score': 1.441355229614416e-10,
       'token': 1,
       'token_str': '[ U N K ]'},
      {'sequence': 'E N D E L',
       'score': 3.96246785383525e-11,
       'token': 4,
       'token_str': '[ M A S K ]'}],
     [{'sequence': 'M L N D E L',
       'score': 0.10648136585950851,
       'token': 5,
       'token_str': 'L'},
      {'sequence': 'M K N D E L',
       'score': 0.10479484498500824,
       'token': 12,
       'token_str': 'K'},
      {'sequence': 'M E N D E L',
       'score': 0.07481565326452255,
       'token': 9,
       'token_str': 'E'},
      {'sequence': 'M I N D E L',
       'score': 0.07306281477212906,
       'token': 11,
       'token_str': 'I'},
      {'sequence': 'M S N D E L',
       'score': 0.06441245973110199,
       'token': 10,
       'token_str': 'S'},
      {'sequence': 'M N N D E L',
       'score': 0.06265531480312347,
       'token': 17,
       'token_str': 'N'},
      {'sequence': 'M V N D E L',
       'score': 0.05677882954478264,
       'token': 8,
       'token_str': 'V'},
      {'sequence': 'M R N D E L',
       'score': 0.0555323101580143,
       'token': 13,
       'token_str': 'R'},
      {'sequence': 'M T N D E L',
       'score': 0.049945324659347534,
       'token': 15,
       'token_str': 'T'},
      {'sequence': 'M A N D E L',
       'score': 0.045712005347013474,
       'token': 6,
       'token_str': 'A'},
      {'sequence': 'M G N D E L',
       'score': 0.04431714862585068,
       'token': 7,
       'token_str': 'G'},
      {'sequence': 'M M N D E L',
       'score': 0.04357245936989784,
       'token': 21,
       'token_str': 'M'},
      {'sequence': 'M D N D E L',
       'score': 0.041912999004125595,
       'token': 14,
       'token_str': 'D'},
      {'sequence': 'M F N D E L',
       'score': 0.03714616224169731,
       'token': 19,
       'token_str': 'F'},
      {'sequence': 'M Q N D E L',
       'score': 0.036904506385326385,
       'token': 18,
       'token_str': 'Q'},
      {'sequence': 'M Y N D E L',
       'score': 0.029887322336435318,
       'token': 20,
       'token_str': 'Y'},
      {'sequence': 'M P N D E L',
       'score': 0.025271963328123093,
       'token': 16,
       'token_str': 'P'},
      {'sequence': 'M H N D E L',
       'score': 0.018260307610034943,
       'token': 22,
       'token_str': 'H'},
      {'sequence': 'M C N D E L',
       'score': 0.015658656135201454,
       'token': 23,
       'token_str': 'C'},
      {'sequence': 'M W N D E L',
       'score': 0.012689119204878807,
       'token': 24,
       'token_str': 'W'},
      {'sequence': 'M X N D E L',
       'score': 0.00018849420303013176,
       'token': 25,
       'token_str': 'X'},
      {'sequence': 'M U N D E L',
       'score': 2.818865696418982e-10,
       'token': 26,
       'token_str': 'U'},
      {'sequence': 'M N D E L',
       'score': 2.734108772717292e-10,
       'token': 2,
       'token_str': '[ C L S ]'},
      {'sequence': 'M O N D E L',
       'score': 2.455574632520552e-10,
       'token': 29,
       'token_str': 'O'},
      {'sequence': 'M B N D E L',
       'score': 2.428661161069101e-10,
       'token': 27,
       'token_str': 'B'},
      {'sequence': 'M N D E L',
       'score': 2.427744116850761e-10,
       'token': 0,
       'token_str': '[ P A D ]'},
      {'sequence': 'M Z N D E L',
       'score': 2.347084193665694e-10,
       'token': 28,
       'token_str': 'Z'},
      {'sequence': 'M N D E L',
       'score': 2.0238072329092915e-10,
       'token': 1,
       'token_str': '[ U N K ]'},
      {'sequence': 'M N D E L',
       'score': 1.2065035082109432e-10,
       'token': 3,
       'token_str': '[ S E P ]'},
      {'sequence': 'M N D E L',
       'score': 3.644244281342246e-11,
       'token': 4,
       'token_str': '[ M A S K ]'}],
     [{'sequence': 'M E E D E L',
       'score': 0.18433618545532227,
       'token': 9,
       'token_str': 'E'},
      {'sequence': 'M E D D E L',
       'score': 0.16256563365459442,
       'token': 14,
       'token_str': 'D'},
      {'sequence': 'M E L D E L',
       'score': 0.09741301834583282,
       'token': 5,
       'token_str': 'L'},
      {'sequence': 'M E V D E L',
       'score': 0.0547335110604763,
       'token': 8,
       'token_str': 'V'},
      {'sequence': 'M E I D E L',
       'score': 0.05262178182601929,
       'token': 11,
       'token_str': 'I'},
      {'sequence': 'M E S D E L',
       'score': 0.04809831455349922,
       'token': 10,
       'token_str': 'S'},
      {'sequence': 'M E G D E L',
       'score': 0.044654298573732376,
       'token': 7,
       'token_str': 'G'},
      {'sequence': 'M E A D E L',
       'score': 0.04355783760547638,
       'token': 6,
       'token_str': 'A'},
      {'sequence': 'M E N D E L',
       'score': 0.04198392480611801,
       'token': 17,
       'token_str': 'N'},
      {'sequence': 'M E M D E L',
       'score': 0.041477616876363754,
       'token': 21,
       'token_str': 'M'},
      {'sequence': 'M E K D E L',
       'score': 0.03501797094941139,
       'token': 12,
       'token_str': 'K'},
      {'sequence': 'M E F D E L',
       'score': 0.03377687186002731,
       'token': 19,
       'token_str': 'F'},
      {'sequence': 'M E T D E L',
       'score': 0.030298525467514992,
       'token': 15,
       'token_str': 'T'},
      {'sequence': 'M E R D E L',
       'score': 0.029428450390696526,
       'token': 13,
       'token_str': 'R'},
      {'sequence': 'M E Q D E L',
       'score': 0.025511162355542183,
       'token': 18,
       'token_str': 'Q'},
      {'sequence': 'M E Y D E L',
       'score': 0.024920152500271797,
       'token': 20,
       'token_str': 'Y'},
      {'sequence': 'M E P D E L',
       'score': 0.019988832995295525,
       'token': 16,
       'token_str': 'P'},
      {'sequence': 'M E H D E L',
       'score': 0.012353409081697464,
       'token': 22,
       'token_str': 'H'},
      {'sequence': 'M E C D E L',
       'score': 0.009683980606496334,
       'token': 23,
       'token_str': 'C'},
      {'sequence': 'M E W D E L',
       'score': 0.0074284737929701805,
       'token': 24,
       'token_str': 'W'},
      {'sequence': 'M E X D E L',
       'score': 0.00015013833763077855,
       'token': 25,
       'token_str': 'X'},
      {'sequence': 'M E D E L',
       'score': 1.6619389198169188e-10,
       'token': 3,
       'token_str': '[ S E P ]'},
      {'sequence': 'M E B D E L',
       'score': 1.3698038536791302e-10,
       'token': 27,
       'token_str': 'B'},
      {'sequence': 'M E Z D E L',
       'score': 1.168956598185389e-10,
       'token': 28,
       'token_str': 'Z'},
      {'sequence': 'M E D E L',
       'score': 1.0862983429449358e-10,
       'token': 1,
       'token_str': '[ U N K ]'},
      {'sequence': 'M E D E L',
       'score': 1.0585952253672204e-10,
       'token': 0,
       'token_str': '[ P A D ]'},
      {'sequence': 'M E D E L',
       'score': 1.0177149400991681e-10,
       'token': 2,
       'token_str': '[ C L S ]'},
      {'sequence': 'M E O D E L',
       'score': 9.655934385399689e-11,
       'token': 29,
       'token_str': 'O'},
      {'sequence': 'M E U D E L',
       'score': 9.435673770097353e-11,
       'token': 26,
       'token_str': 'U'},
      {'sequence': 'M E D E L',
       'score': 2.4889090788349222e-11,
       'token': 4,
       'token_str': '[ M A S K ]'}],
     [{'sequence': 'M E N L E L',
       'score': 0.10907968133687973,
       'token': 5,
       'token_str': 'L'},
      {'sequence': 'M E N K E L',
       'score': 0.09135881811380386,
       'token': 12,
       'token_str': 'K'},
      {'sequence': 'M E N E E L',
       'score': 0.08618851006031036,
       'token': 9,
       'token_str': 'E'},
      {'sequence': 'M E N I E L',
       'score': 0.07329064607620239,
       'token': 11,
       'token_str': 'I'},
      {'sequence': 'M E N S E L',
       'score': 0.06231885030865669,
       'token': 10,
       'token_str': 'S'},
      {'sequence': 'M E N N E L',
       'score': 0.06081739813089371,
       'token': 17,
       'token_str': 'N'},
      {'sequence': 'M E N V E L',
       'score': 0.05893290042877197,
       'token': 8,
       'token_str': 'V'},
      {'sequence': 'M E N G E L',
       'score': 0.055906955152750015,
       'token': 7,
       'token_str': 'G'},
      {'sequence': 'M E N D E L',
       'score': 0.04974446818232536,
       'token': 14,
       'token_str': 'D'},
      {'sequence': 'M E N R E L',
       'score': 0.046224404126405716,
       'token': 13,
       'token_str': 'R'},
      {'sequence': 'M E N T E L',
       'score': 0.044897545129060745,
       'token': 15,
       'token_str': 'T'},
      {'sequence': 'M E N A E L',
       'score': 0.04207944497466087,
       'token': 6,
       'token_str': 'A'},
      {'sequence': 'M E N M E L',
       'score': 0.040077824145555496,
       'token': 21,
       'token_str': 'M'},
      {'sequence': 'M E N F E L',
       'score': 0.03973270207643509,
       'token': 19,
       'token_str': 'F'},
      {'sequence': 'M E N Q E L',
       'score': 0.039686419069767,
       'token': 18,
       'token_str': 'Q'},
      {'sequence': 'M E N P E L',
       'score': 0.032021839171648026,
       'token': 16,
       'token_str': 'P'},
      {'sequence': 'M E N Y E L',
       'score': 0.026594167575240135,
       'token': 20,
       'token_str': 'Y'},
      {'sequence': 'M E N H E L',
       'score': 0.016859525814652443,
       'token': 22,
       'token_str': 'H'},
      {'sequence': 'M E N C E L',
       'score': 0.01324320025742054,
       'token': 23,
       'token_str': 'C'},
      {'sequence': 'M E N W E L',
       'score': 0.010874584317207336,
       'token': 24,
       'token_str': 'W'},
      {'sequence': 'M E N X E L',
       'score': 7.015161827439442e-05,
       'token': 25,
       'token_str': 'X'},
      {'sequence': 'M E N U E L',
       'score': 1.9529618200397891e-10,
       'token': 26,
       'token_str': 'U'},
      {'sequence': 'M E N E L',
       'score': 1.7881504610350873e-10,
       'token': 2,
       'token_str': '[ C L S ]'},
      {'sequence': 'M E N B E L',
       'score': 1.7396527274282647e-10,
       'token': 27,
       'token_str': 'B'},
      {'sequence': 'M E N Z E L',
       'score': 1.563131013515573e-10,
       'token': 28,
       'token_str': 'Z'},
      {'sequence': 'M E N E L',
       'score': 1.494619983333223e-10,
       'token': 1,
       'token_str': '[ U N K ]'},
      {'sequence': 'M E N O E L',
       'score': 1.4341250409444228e-10,
       'token': 29,
       'token_str': 'O'},
      {'sequence': 'M E N E L',
       'score': 1.4239638634894192e-10,
       'token': 0,
       'token_str': '[ P A D ]'},
      {'sequence': 'M E N E L',
       'score': 1.3189571657079568e-10,
       'token': 3,
       'token_str': '[ S E P ]'},
      {'sequence': 'M E N E L',
       'score': 3.212379667827392e-11,
       'token': 4,
       'token_str': '[ M A S K ]'}],
     [{'sequence': 'M E N D L L',
       'score': 0.0907994955778122,
       'token': 5,
       'token_str': 'L'},
      {'sequence': 'M E N D E L',
       'score': 0.08690842986106873,
       'token': 9,
       'token_str': 'E'},
      {'sequence': 'M E N D D L',
       'score': 0.07981622964143753,
       'token': 14,
       'token_str': 'D'},
      {'sequence': 'M E N D I L',
       'score': 0.07449530810117722,
       'token': 11,
       'token_str': 'I'},
      {'sequence': 'M E N D V L',
       'score': 0.06803234666585922,
       'token': 8,
       'token_str': 'V'},
      {'sequence': 'M E N D S L',
       'score': 0.06518951803445816,
       'token': 10,
       'token_str': 'S'},
      {'sequence': 'M E N D K L',
       'score': 0.06457968801259995,
       'token': 12,
       'token_str': 'K'},
      {'sequence': 'M E N D N L',
       'score': 0.062229011207818985,
       'token': 17,
       'token_str': 'N'},
      {'sequence': 'M E N D F L',
       'score': 0.05063425377011299,
       'token': 19,
       'token_str': 'F'},
      {'sequence': 'M E N D G L',
       'score': 0.05046198144555092,
       'token': 7,
       'token_str': 'G'},
      {'sequence': 'M E N D A L',
       'score': 0.04663773626089096,
       'token': 6,
       'token_str': 'A'},
      {'sequence': 'M E N D T L',
       'score': 0.044934190809726715,
       'token': 15,
       'token_str': 'T'},
      {'sequence': 'M E N D R L',
       'score': 0.0404861643910408,
       'token': 13,
       'token_str': 'R'},
      {'sequence': 'M E N D Y L',
       'score': 0.038031402975320816,
       'token': 20,
       'token_str': 'Y'},
      {'sequence': 'M E N D Q L',
       'score': 0.030531685799360275,
       'token': 18,
       'token_str': 'Q'},
      {'sequence': 'M E N D M L',
       'score': 0.028959861025214195,
       'token': 21,
       'token_str': 'M'},
      {'sequence': 'M E N D P L',
       'score': 0.023876836523413658,
       'token': 16,
       'token_str': 'P'},
      {'sequence': 'M E N D H L',
       'score': 0.022395167499780655,
       'token': 22,
       'token_str': 'H'},
      {'sequence': 'M E N D C L',
       'score': 0.01876864954829216,
       'token': 23,
       'token_str': 'C'},
      {'sequence': 'M E N D W L',
       'score': 0.012154660187661648,
       'token': 24,
       'token_str': 'W'},
      {'sequence': 'M E N D X L',
       'score': 7.737120176898316e-05,
       'token': 25,
       'token_str': 'X'},
      {'sequence': 'M E N D L',
       'score': 2.1059337607098882e-10,
       'token': 2,
       'token_str': '[ C L S ]'},
      {'sequence': 'M E N D U L',
       'score': 1.8998401463132808e-10,
       'token': 26,
       'token_str': 'U'},
      {'sequence': 'M E N D L',
       'score': 1.8773518850601079e-10,
       'token': 0,
       'token_str': '[ P A D ]'},
      {'sequence': 'M E N D B L',
       'score': 1.8348496333420172e-10,
       'token': 27,
       'token_str': 'B'},
      {'sequence': 'M E N D Z L',
       'score': 1.6312270978424692e-10,
       'token': 28,
       'token_str': 'Z'},
      {'sequence': 'M E N D O L',
       'score': 1.620216044662115e-10,
       'token': 29,
       'token_str': 'O'},
      {'sequence': 'M E N D L',
       'score': 1.4441979556689688e-10,
       'token': 1,
       'token_str': '[ U N K ]'},
      {'sequence': 'M E N D L',
       'score': 9.434715508849223e-11,
       'token': 3,
       'token_str': '[ S E P ]'},
      {'sequence': 'M E N D L',
       'score': 2.9468927298381686e-11,
       'token': 4,
       'token_str': '[ M A S K ]'}],
     [{'sequence': 'M E N D E E',
       'score': 0.1425764262676239,
       'token': 9,
       'token_str': 'E'},
      {'sequence': 'M E N D E K',
       'score': 0.10200703889131546,
       'token': 12,
       'token_str': 'K'},
      {'sequence': 'M E N D E N',
       'score': 0.09017709642648697,
       'token': 17,
       'token_str': 'N'},
      {'sequence': 'M E N D E X',
       'score': 0.0653640404343605,
       'token': 25,
       'token_str': 'X'},
      {'sequence': 'M E N D E D',
       'score': 0.060928113758563995,
       'token': 14,
       'token_str': 'D'},
      {'sequence': 'M E N D E I',
       'score': 0.06037352606654167,
       'token': 11,
       'token_str': 'I'},
      {'sequence': 'M E N D E L',
       'score': 0.05676602944731712,
       'token': 5,
       'token_str': 'L'},
      {'sequence': 'M E N D E G',
       'score': 0.04628738388419151,
       'token': 7,
       'token_str': 'G'},
      {'sequence': 'M E N D E S',
       'score': 0.04586312174797058,
       'token': 10,
       'token_str': 'S'},
      {'sequence': 'M E N D E V',
       'score': 0.045120641589164734,
       'token': 8,
       'token_str': 'V'},
      {'sequence': 'M E N D E R',
       'score': 0.04382329806685448,
       'token': 13,
       'token_str': 'R'},
      {'sequence': 'M E N D E T',
       'score': 0.04322368651628494,
       'token': 15,
       'token_str': 'T'},
      {'sequence': 'M E N D E M',
       'score': 0.037424322217702866,
       'token': 21,
       'token_str': 'M'},
      {'sequence': 'M E N D E A',
       'score': 0.03569469600915909,
       'token': 6,
       'token_str': 'A'},
      {'sequence': 'M E N D E Q',
       'score': 0.03273263946175575,
       'token': 18,
       'token_str': 'Q'},
      {'sequence': 'M E N D E Y',
       'score': 0.021241357550024986,
       'token': 20,
       'token_str': 'Y'},
      {'sequence': 'M E N D E F',
       'score': 0.019580725580453873,
       'token': 19,
       'token_str': 'F'},
      {'sequence': 'M E N D E P',
       'score': 0.019357955083251,
       'token': 16,
       'token_str': 'P'},
      {'sequence': 'M E N D E H',
       'score': 0.013043095357716084,
       'token': 22,
       'token_str': 'H'},
      {'sequence': 'M E N D E W',
       'score': 0.009800290688872337,
       'token': 24,
       'token_str': 'W'},
      {'sequence': 'M E N D E C',
       'score': 0.008614533580839634,
       'token': 23,
       'token_str': 'C'},
      {'sequence': 'M E N D E',
       'score': 3.9243933103172424e-10,
       'token': 2,
       'token_str': '[ C L S ]'},
      {'sequence': 'M E N D E O',
       'score': 3.0732788536269595e-10,
       'token': 29,
       'token_str': 'O'},
      {'sequence': 'M E N D E U',
       'score': 2.9936808587649466e-10,
       'token': 26,
       'token_str': 'U'},
      {'sequence': 'M E N D E Z',
       'score': 2.7327584639635916e-10,
       'token': 28,
       'token_str': 'Z'},
      {'sequence': 'M E N D E',
       'score': 2.435800450228953e-10,
       'token': 3,
       'token_str': '[ S E P ]'},
      {'sequence': 'M E N D E',
       'score': 2.3922716585467185e-10,
       'token': 0,
       'token_str': '[ P A D ]'},
      {'sequence': 'M E N D E B',
       'score': 2.3354421174737183e-10,
       'token': 27,
       'token_str': 'B'},
      {'sequence': 'M E N D E',
       'score': 2.0876871065222957e-10,
       'token': 1,
       'token_str': '[ U N K ]'},
      {'sequence': 'M E N D E',
       'score': 3.9169806287375764e-11,
       'token': 4,
       'token_str': '[ M A S K ]'}]]


