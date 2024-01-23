from model.build import register
import torch.nn as nn
from utils.model_utils import PatchEmbedding


class ViT(nn.Module):
    def __init__(self, config: dict):
        super(ViT, self).__init__()

        self.patch_embedding = PatchEmbedding(img_dim=(config['INPUT_H'], config['INPUT_W']), input_channel=config['INPUT_CHANNEL'], patch_dim=config['PATCH_DIM'])

    def forward(self, x):
        x = self.patch_embedding(x)


@register
def get_vit(config: dict):
    return ViT(config['MODEL'])