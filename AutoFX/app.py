import gradio as gr
import os
import glob
# 获取当前路径下的所有文件夹
folder_path = r"E:\Workdirs\AutoFX\arxiv\2023-12-13"

def load_markdown_files(selected_file):
    file_path = os.path.join(folder_path, selected_file + '_abs.md')
    print(file_path)
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def markdown_viewer(selected_file):
    content = load_markdown_files(selected_file)
    content = content.replace('./', folder_path)
    return content



markdown_files = glob.glob(os.path.join(folder_path, '*.md'))
print(markdown_files)

topics = [os.path.basename(f).split('_abs')[0] for f in markdown_files]
print(topics)
def main():
    with gr.Blocks(analytics_enabled=False) as inference:
        gr.Markdown("## Markdown Viewer")
        with gr.Row():
            with gr.Column():
                selected_file = gr.Dropdown(['Audio Driven 人脸生成', 'Domain Adaptation', 'dropdown', 'LLM', 'MMT', '元宇宙_虚拟人'], 
                                            label="Selected File", type = 'value')
                
                submit_btn = gr.Button("Submit", variant='primary')
                print(selected_file)
                submit_btn.click(
                    fn=markdown_viewer,
                    inputs=[selected_file],
                    outputs=gr.Markdown(),
                )
                
        return inference
if __name__ == "__main__":
    demo = main()
    demo.queue()
    demo.launch(server_port=7870)