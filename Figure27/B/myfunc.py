def dash_to_1(x):
    if x=='-':
        return 1
    else:
        return float(x)
    
# def ref_peri(number):
#     if number == '-':
#         return number
#     else:
#         return df['Perim.'].iloc[int(number)-1]
    
def md_ratio(row):
    """
    calculate ration between mother and daughter
    """
    if (row['classification']=='-') | (row['classification']=='un'):
        return '-'
    elif row['classification']=='bud':
        return float(row['Perim.']) / float(row['ref_peri'])
    else:
        return float(row['ref_peri']) / float(row['Perim.'])
    
def classification_50(row):
    """
    classify cells by perimeter (threshold 0.5) and mother/daughter/no_bud
    """
    if row['classification']=='-':
        return '-'
    elif row['classification']=='un':
        return 'no_bud'
    elif (row['classification']=='bud') & (float(row['ratio'])<=0.5):
        return 'small_daughter'
    elif (row['classification']=='bud') & (float(row['ratio'])>0.5):
        return 'large_daughter'
    elif (row['classification']=='mother') & (float(row['ratio'])<=0.5):
        return 'small_mother'
    else:
        return 'large_mother'

def myfunc():
    return "this is my function from cycle_func.py!"