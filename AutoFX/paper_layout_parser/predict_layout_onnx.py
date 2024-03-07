import os
import cv2 as cv2
import onnxruntime as ort
import numpy as np
import logging
from paper_layout_parser.picodet_postprocess import PicoDetPostProcess

logging.getLogger('PIL').setLevel(logging.WARNING)

def init_model(model_dir):
    model_file_path = model_dir
    if not os.path.exists(model_file_path):
        raise ValueError("not find model file path {}".format(
            model_file_path))
    sess = ort.InferenceSession(model_file_path)
    outputs_name = [tensor.name for tensor in sess.get_outputs()]
    return sess, sess.get_inputs()[0].name, outputs_name


predictor, input_tensor_name, outputs_tensor_name = init_model(
    r"./paper_layout_parser/inference/picodet_lcnet_x1_0_fgd_layout_infer/model.onnx")
post_process = PicoDetPostProcess(labels=['text', 'title', 'list', 'table', 'figure'],
                                  nms_threshold=0.5, score_threshold=0.5)


def load_img(path_img):
    if type(path_img) is str:
        ori_img = cv2.imread(path_img, cv2.IMREAD_COLOR)
        ori_img = cv2.cvtColor(ori_img, cv2.COLOR_BGR2RGB)
    else:
        ori_img = np.array(path_img)
    resized_image = cv2.resize(ori_img, (608, 800), interpolation=cv2.INTER_LINEAR) / 255.

    mean = np.array([0.485, 0.456, 0.406])
    std = np.array([0.229, 0.224, 0.225])

    resized_image = (resized_image - mean[None, None, ...]) / std[None, None, ...]
    resized_image = resized_image.transpose((2, 0, 1))
    resized_image = resized_image.astype('float32')

    resized_image = resized_image[np.newaxis, ...]
    return ori_img, resized_image


def parse_one_page(img):
    ori_img, resized_image = load_img(img)
    input_dict = {}
    input_dict[input_tensor_name] = resized_image
    outputs = predictor.run(outputs_tensor_name, input_dict)
    np_score_list, np_boxes_list = [], []
    output_names = predictor.get_outputs()
    num_outs = int(len(output_names) / 2)
    for out_idx in range(num_outs):
        np_score_list.append(outputs[out_idx])
        np_boxes_list.append(outputs[out_idx + num_outs])
    preds = dict(boxes=np_score_list, boxes_num=np_boxes_list)

    post_preds = post_process(ori_img, resized_image, preds)
    return post_preds


if __name__ == '__main__':
    from layoutparser.elements import TextBlock, Rectangle

    post_preds, ori_img = parse_one_page("../tmp/page_0_0.png")
    print(post_preds)
    for d in post_preds:
        if d['label'] == 'list':
            cv2.rectangle(ori_img, (int(d['bbox'][0]), int(d['bbox'][1])), (int(d['bbox'][2]), int(d['bbox'][3])),
                          color=(0, 0, 255), thickness=5)
    print([Rectangle(d['bbox'][0], d['bbox'][1],
                     d['bbox'][2], d['bbox'][3]) for d in post_preds if d['label'] == 'text'])
    cv2.imwrite("../tmp/result.png", ori_img)
