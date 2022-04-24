# NLP_2022_TST
* scoring_generated_sent has rough code for analysis of generated text
*  function to remove special tokens
pattern = re.compile("<END>")
def clean_text(s):
    #print(s)
    #print('-----------------------')
    new_s = pattern.split(s)[0]
    new_s = re.sub(r'<.*?>', '', new_s)
    return new_s
  * The cells in the notebook may be out of order, will correct it 
