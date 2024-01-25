from model import build
from utils import move_to_device
import torch


class Experiment:

    def __init__(self, config, args):

        self.args = args

        self.model = build(config, config['MODEL']['NAME'])
        self.criteria = None
        self.scheduler = None

    def train_model(self, a_batch):
        self.model.train()
        x, y = move_to_device(a_batch, self.args.cpu)
        pass

    def validate_model(self, a_batch):
        self.model.eval()
        with torch.no_grad():
            x, y = move_to_device(a_batch, self.args.cpu)
            pass
        pass

    def init_model(self):
        pass

    def save_model(self, model, criteria, scheduler, loss, epoch):
        pass

    def load_model(self, checkpoint_path):
        pass

