from sklearn.pipeline import Pipeline
from sklearn.dummy import DummyClassifier
from delite.processing import preprocessors as pp
from delite.config import config

pipe = Pipeline(
    [
        (
            "first_step",
            pp.CategoricalImputer(variables=config.VARIABLES),
        ),
        (
            "last_step",
            DummyClassifier(strategy="most_frequent")
        )
    ]
)