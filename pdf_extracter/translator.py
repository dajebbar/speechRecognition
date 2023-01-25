from transformers import (
    AutoTokenizer,
    AutoModelForSeq2SeqLM,
    pipeline
)

model = AutoModelForSeq2SeqLM.from_pretrained(
      "facebook/nllb-200-distilled-600M"
)

tokenizer = AutoTokenizer.from_pretrained(
    "facebook/nllb-200-distilled-600M"
)
  
translator = pipeline(
    task="translation",
    model=model,
    tokenizer=tokenizer,
    src_lang="eng_Latn",
    tgt_lang="fra_Latn",
    max_length=300
    
    )

def translate_text(file):
    with open(file, "r") as f:
      content_size = 100
      f_content = f.read(content_size)
      while len(f_content) > 0:
        text = f_content
        f_content = f.read(content_size)
        text_tr = translator(text)[0]["translation_text"]
    return text_tr

file = "pdf.txt"
text = translate_text(file)
print(text)
  
