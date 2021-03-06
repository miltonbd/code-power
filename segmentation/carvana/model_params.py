from base.base_model_params import BaseModeParams

class ModeParams(BaseModeParams):
    def __init__(self):
        self.num_gpus=1
        self.num_gpus= 1
        self.epochs = 200
        self.learning_rate = 0.0001
        self.dropout=0.6
        self.batch_size_test_per_gpu  =2
        self.batch_size_train_per_gpu =2
