#! usr/bin/env python3
# -*- coding:utf-8 -*-
import json
import re

data_path = "/media/filesNew/szq/BERT-Seq-Label-Text-Classification/data/SMP_task1/train.json"
train_label = "/media/filesNew/szq/BERT-Seq-Label-Text-Classification/data/SMP_task1_2/train/label"
train_in = "/media/filesNew/szq/BERT-Seq-Label-Text-Classification/data/SMP_task1_2/train/seq.in"
train_out = "/media/filesNew/szq/BERT-Seq-Label-Text-Classification/data/SMP_task1_2/train/seq.out"

intent_list = []
domain_list = []
slot_list = []
with open(data_path, encoding='utf-8') as f_o, \
     open(train_in, 'w', encoding='utf-8') as f_train_in, \
     open(train_label, 'w', encoding='utf-8') as f_train_label, \
     open(train_out, 'w', encoding='utf-8') as f_train_out:
    data = json.load(f_o)
    for i in data:
        patten = re.compile("[\u4E00-\u9FA5。，？！《》\d$()#+&*“”]")
        patten2 = re.compile(r"\bb\b|\bA\b|\ba\b|\bc\b|\bd\b|\be\b|\bf\b|\bg\b|\bh\b|\bi\b|\bj\b|\bk\b|\bl\b|\bm\b|\bn\b|\bo\b|\bp\b|\bq\b|\br\b|\bs\b|\bt\b|\bu\b|\bv\b|\bw\b|\bs\b|\by\b|\bz\b")
        _text = i['text'].replace(' ', '')
        _text = _text.replace('小c', '姐姐')
        _text = [j for j in _text]
        _text = ' '.join(_text)
        _text_origin = _text

        _intent = i['intent']
        _domain = i['domain']
        if _intent not in intent_list:
            intent_list.append(_intent)
        if _domain not in domain_list:
            domain_list.append(_domain)

        _slot_keys = i['slots'].keys()
        for _ in [key for key in _slot_keys]:
            slot_list.append(_)
        slot_list = list(set(slot_list))

        for k, v in i['slots'].items():
            _name = k
            _value = [i for i in v]

            _slot_value = _value
            _slot_value = ['B-' + _name if index == 0 else 'I-' + _name for index, i in enumerate(_slot_value)]
            _slot_value = ' '.join(_slot_value)
            _value = ' '.join(_value)

            _text = _text.replace(_value, _slot_value)
        _text = re.sub(patten, '0', _text)
        _text = re.sub(patten2, '0', _text)

        f_train_in.write(_text_origin + '\n')
        f_train_label.write(_intent + '\n')
        f_train_out.write(_text + '\n')
    slot_list = ['B-' + i for i in slot_list] + ['I-' + i for i in slot_list]

print(slot_list)
print(intent_list)




