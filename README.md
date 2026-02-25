# Proposal: Zero-Shot Visual-language feature alignment via ViT-based Contrastive LearningProblem 

DONG, Yunao ydongbd@connect.ust.hk

LIU, Xiyue xliufp@connect.ust.hk

CHEN, Hongyu hchendu@connect.ust.hk


## Investigation & Interest:
Standard classifiers suffer from rigid, pre-set labels. We mitigate this by employing a pre-trained text encoder to match label semantics with image features, enhancing both transferability and generalization. Unlike traditional closed-set classifiers, our model will recognize unseen categories by measuring the similarity between image embeddings and text-derived category prompts. 
This is highly interesting because it shifts computer vision from "learning to label" to "learning to understand concepts," enabling a model trained on general image-caption pairs to generalize to specialized tasks like ImageNet classification without any category-specific training. 
## Data:  
MicrosoftCOCO, ImageNet, etc. 
## Methodology:
Our methodology focuses on a dual-encoder architecture. We will use a Vision Transformer (ViT) as the image encoder and a pre-trained text-encoder. Critically, we will freeze the text encoder to preserve its linguistic knowledge while actively training the ViT image encoder and a learnable linear projection layer that maps both modalities into a shared d-dimensional latent space. 
## Evaluation:
We will evaluate the results both qualitatively and quantitatively. Qualitatively, we will visualize "similarity heatmaps" and retrieve the Top-k most likely classes for sample images to inspect if the model captures correct semantic attributes. Quantitatively, we will report Zero-shot Top-1 and Top-k Accuracy on the ImageNet validation set. We will also perform an ablation study comparing our trained ViT's performance against a standard supervised image classification model in similar scale to demonstrate the advantages of the open-vocabulary approach.