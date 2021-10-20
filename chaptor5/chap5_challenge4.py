from typing import MappingView


me = {
    "height": "171cm",
    "weight": "75.6kg",
    "hobby": "listening to music, playing soccer and wathing YouTube",
    }

answer = input("Type 'height', 'weight' or 'hobby': ")
if answer in me:
    result = me[answer]
    print(result)
else:
    print("Not found: '" + answer + "'")