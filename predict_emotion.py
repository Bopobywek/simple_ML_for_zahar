from catboost import CatBoostClassifier
from pyAudioAnalysis import audioFeatureExtraction as At


results = []
classifier2 = CatBoostClassifier(iterations=1000, learning_rate=0.25,
                                 depth=5, loss_function='MultiClassOneVsAll',
                                 eval_metric="Accuracy")
classifier2.load_model("stable_model")
data = At.dirsWavFeatureExtraction(["data/"], 1, 1, 0.05, 0.05)
for element in data[0]:
    result = classifier2.predict(element)
    results.append(result)
