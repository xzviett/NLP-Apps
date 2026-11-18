import torch
import torch.nn as nn
from transformers import AutoTokenizer, AutoModelForTokenClassification

label_list = ["O", "B-PER", "I-PER", "B-ORG", "I-ORG", "B-LOC", "I-LOC", "B-MISC", "I-MISC"]
label2id = {label: i for i, label in enumerate(label_list)}
id2label = {i: label for i, label in enumerate(label_list)}

words = [
    ["Elon", "Musk", "is", "playing", "at", "SpaceX", "in", "Washington", "."],
    ["Barack", "Obama", "visited", "Paris", "."]
]
word_labels = [
    ["B-PER", "I-PER", "O", "O", "O", "B-ORG", "O", "B-LOC", "O"],
    ["B-PER", "I-PER", "O", "B-LOC", "O"]
]

model_checkpoint = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)

tokenized_inputs = tokenizer(
    words,
    is_split_into_words=True,
    truncation=True,
    padding=True,
    return_tensors="pt"
)

def align_labels_with_tokens(tokenized_inputs, word_labels, label2id):
    aligned_labels = []
    
    for batch_idx, labels in enumerate(word_labels):
        word_ids = tokenized_inputs.word_ids(batch_index=batch_idx)
        previous_word_idx = None
        label_ids = []
        
        for word_idx in word_ids:
            if word_idx is None:
                label_ids.append(-100)
            elif word_idx != previous_word_idx:
                label_str = labels[word_idx]
                label_ids.append(label2id[label_str])
            else:
                label_ids.append(-100)
                
            previous_word_idx = word_idx
            
        aligned_labels.append(label_ids)
        
    return torch.tensor(aligned_labels, dtype=torch.long)

labels_tensor = align_labels_with_tokens(tokenized_inputs, word_labels, label2id)

model = AutoModelForTokenClassification.from_pretrained(
    model_checkpoint,
    num_labels=len(label_list),
    id2label=id2label,
    label2id=label2id
)

model.eval()
with torch.no_grad():
    outputs = model(
        input_ids=tokenized_inputs["input_ids"],
        attention_mask=tokenized_inputs["attention_mask"],
        labels=labels_tensor
    )
    loss = outputs.loss
    logits = outputs.logits 
    predictions = torch.argmax(logits, dim=-1) 

sample_idx = 0
tokens = tokenizer.convert_ids_to_tokens(tokenized_inputs["input_ids"][sample_idx])
input_ids = tokenized_inputs["input_ids"][sample_idx].tolist()
attention_mask = tokenized_inputs["attention_mask"][sample_idx].tolist()
word_ids = tokenized_inputs.word_ids(batch_index=sample_idx)
aligned_lbls = labels_tensor[sample_idx].tolist()
preds = predictions[sample_idx].tolist()

print(f"\nLoss tính được (bỏ qua -100): {loss.item():.4f}")
print(f"Logits shape: {logits.shape} | Predictions shape: {predictions.shape}\n")

print(f"{'Token':<14} | {'Input ID':<10} | {'Attn Mask':<10} | {'Word ID':<9} | {'Aligned Label':<15} | {'Pred Label'}")
print("-" * 82)

for tok, inp_id, mask, w_id, lbl_id, pred_id in zip(tokens, input_ids, attention_mask, word_ids, aligned_lbls, preds):
    w_id_str = str(w_id) if w_id is not None else "None"
    lbl_str = f"{lbl_id} ({id2label[lbl_id]})" if lbl_id != -100 else "-100 (IGNORE)"
    pred_str = id2label[pred_id]
    print(f"{tok:<14} | {inp_id:<10} | {mask:<10} | {w_id_str:<9} | {lbl_str:<15} | {pred_str}")