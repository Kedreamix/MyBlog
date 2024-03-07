from configs import root_path
import os 
import time
from utils.update_hexo_kedreamix import check_filename
from utils.update_hexo_kedreamix import control_blog
keywords_dict = {
    # 'LLM': ['ti:LLM+OR+abs:"Large Language Models"',
    #         'ti:LLM'],
    # 'MMT': ['abs:multimodal+AND+abs:machine+AND+abs:translation'],
    # 'Domain Adaptation': ['ti:Domain+AND+ti:Adaptation', 'abs:Domain+AND+abs:Adaptation'],
    # '元宇宙/虚拟人': ['ti:"Virtual Avatar"+OR+ti:"Virtual Avatar"', 
    #             'ti:Metaverse', 
    #             'ti:Avatar'],
    # 'Open-Set': ['ti:Open+AND+ti:Set'],
    # '强化学习': ['ti:reinforcement+AND+ti:learning'],
    # 'Few-Shot': ['ti:few+AND+ti:shot', 'abs:few+AND+abs:shot'],
    # '场景文本检测识别': ['ti:Scene+AND+ti:Text', 'abs:Text+AND+abs:detection+AND+abs:End-to-End+AND+abs:scene'],
    # 'I2I Translation': ['abs:image+AND+abs:translation', 'ti:image+AND+ti:translation'],
    # '视频理解': ['ti:video+AND+ti:understanding'],
    # 'Anti-Spoofing': ['ti:anti+AND+ti:spoofing', 'abs:anti+AND+abs:spoofing'],
    # 'Vision Transformer': ['abs:ViT+AND+abs:image', 'abs:prompt+AND+abs:learning+AND+abs:image+AND+abs:vision'],
    # '检测/分割/跟踪': ['ti:object+AND+ti:detection+AND+abs:image', 'ti:semantic+AND+ti:segmentation+AND+abs:image',
    #              'ti:instance+AND+ti:segmentation+AND+abs:image', 'ti:object+AND+ti:tracking+AND+image'],
    # '对抗攻击': ['ti:attack+AND+abs:adversarial+AND+abs:attack+AND+image',
    #          'ti:example+AND+abs:adversarial+AND+abs:attack+AND+abs:example+AND+image'],
    # '人脸相关': ['ti:face+AND+ti:recognition+AND+abs:image', 'ti:face+AND+ti:detection+AND+abs:image',
    #          'ti:face+AND+ti:parse+AND+abs:image'],
    # '无监督/半监督/对比学习': ['ti:contrastive+AND+abs:image'],
    # '医学影像/息肉检测分割': ['ti:polyp+AND+ti:segmentation+AND+abs:polyp', 'all:polyp+AND+all:classification'],
    # '医学影像/Breast Ultrasound': ['all:breast+AND+all:ultrasound'],
    # 'Speech': ['abs:speech+AND+all:enhancement', 'abs:self-supervised+AND+abs:speech',
    #            'abs:speech+AND+abs:separation', 'abs:speech+AND+abs:recognition'],
    
    # 'Face Swapping': ['ti:Swapping+AND+abs:face+AND+abs:swapping', 'abs:face+AND+abs:swap',
    #                   'all:face+AND+all:swapping', 'all:head+AND+all:swapping'],
    # 'GAN': ['abs:image+AND+abs:GAN', 'abs:StyleGAN+OR+abs:StyleGAN2+OR+abs:StyleGAN3'],
    # 'Diffusion Models': ['abs:"Diffusion Model"+OR+abs:"Image"',
    #                      'ti:"generative"+OR+abs:"score-base"',
    #                      'ti:"Diffusion"+OR+abs:"score-base"'],
    'Talking Head Generation': ['all:"Talking Head"',
                                'AND+all:"Talking Portrait"+OR+all:"Talking Face"+OR+all:"Talking Human"',
                                'all:"Audio-Driven"+OR+all:"Speech Driven"',
                                '(ti:NeRF+OR+ti:"Neural Radiance")+AND+(all:"Talking Head"+OR+all:"Talking Face"+OR+all:"Audio-driven"+OR+all:"Talking Portrait"+OR+all:"Speech Driven")',
                                '(ti:Diffusion+OR+ti:Diffuse)+AND+(all:"Talking Head"+OR+all:"Talking Face"+OR+all:"Audio-driven"+OR+all:"Talking Portrait"+OR+all:"Speech Driven")',
                                '(all:"Gaussian Splatting"+OR+all:Splatting+OR+all:Gaussian)"+AND+(all:"Talking Head"+OR+all:"Talking Face"+OR+all:"Audio-driven"+OR+all:"Talking Portrait"+OR+all:"Speech Driven")',
                                'all:Talk+OR+all:talking',
    ],
    "3DGS": ['ti:"Gaussian Splatting"+OR+abs:"Gaussian Splatting"', 
                            '(ti:"Gaussian Splatting"+OR+abs:"Gaussian Splatting")+AND+(ti:Head+OR+ti:Avatar+OR+ti:Human)'],
    'NeRF': ['ti:NeRF', 
                'abs:"Neural Radiance Field"+OR+ti:"Neural Radiance"', 
                'ti:GAN-NeRF'],
    '3D reconstruction': ['all:"surface reconstruction"+OR+all:"shape reconstruction"+OR+all:"texture reconstruction"',
                            'all:"human-object interaction reconstruction"+OR+all:"hand-object interaction reconstruction"+OR+all:"human reconstruction"+OR+all:"object reconstruction"',
                            'all:"shape generation"+OR+all:"shape synthesis"',
                            'all:"implicit field"+OR+all:"deformation"',
                            'all:"image-to-3d"+OR+all:"text-to-3d"',
                            '(ti:NeRF+OR+ti:"Neural Radiance")+AND+(all:"surface reconstruction"+OR+all:"shape reconstruction"+OR+all:"texture reconstruction")',
                            '(ti:Diffusion+OR+ti:Diffuse)+AND+(all:"surface reconstruction"+OR+all:"shape reconstruction"+OR+all:"texture reconstruction")',
                            'all:"Gaussian Splatting"+AND+(all:"surface reconstruction"+OR+all:"shape reconstruction"+OR+all:"texture reconstruction")',
                        ],
}
save_dir = os.path.join(root_path, time.strftime("%Y-%m-%d"))

for key in keywords_dict.keys():
    key_name = check_filename(key)
    target_md = os.path.join(save_dir, f'{key_name}_abs.md')
    if not os.path.exists(target_md): continue
    control_blog(key, target_md)
    # time.sleep(120)