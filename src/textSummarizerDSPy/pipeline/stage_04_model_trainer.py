from textSummarizerDSPy.config.configuration import ConfigurationManager
from textSummarizerDSPy.conponents.model_trainer import ModelTrainer
from textSummarizerDSPy.logging import logger


class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()