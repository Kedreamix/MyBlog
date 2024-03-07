import gradio as gr

def arxiv_search(*kwargs):
    N = len(kwargs)
    assert N % 3 == 0, "Number of arguments must be a multiple of 3."
    part_size = N // 3

    logics = kwargs[:part_size]
    terms = kwargs[part_size:2 * part_size]
    fields = kwargs[2 * part_size:]

    base_url = "https://arxiv.org/search/advanced?advanced="

    # Ensure the lengths of logics, terms, and fields are the same
    assert len(logics) == len(terms) == len(fields), "Lengths of logic operators, terms, and fields must be the same."

    # Construct the query parameters dynamically
    params = {}
    for i, (logic, term, field) in enumerate(zip(logics, terms, fields)):
        params[f"terms-{i}-operator"] = logic
        params[f"terms-{i}-term"] = term
        params[f"terms-{i}-field"] = field.lower()

    params.update({
        "classification-physics_archives": "all",
        "classification-include_cross_list": "include",
        "date-filter_by": "all_dates",
        "date-year": "",
        "date-from_date": "",
        "date-to_date": "",
        "date-date_type": "submitted_date",
        "abstracts": "show",
        "size": 50,
        "order": "-announced_date_first"
    })

    # Construct the URL without making a request
    url_params = "&".join([f"{key}={value}" for key, value in params.items()])
    result_url = base_url + url_params

    # Generate HTML link with explanatory text, larger font size, and centered alignment
    html_link = (
        "<div style='text-align:center; font-size:18px;'>"
        "<p>Click the link below to view the search results on arXiv:</p>"
        f"<a href='{result_url}' target='_blank'>View ArXiv Search Results</a>"
        "</div>"
    )

    print(html_link)
    return html_link


with gr.Blocks(title='Arxiv Search', description='Search Arxiv Papers') as demo:
    gr.HTML("<center><h1>Arxiv Search</h1></center>")
    Logics, Keywords, Fields = [], [], []
    for i in range(5):
        with gr.Row():
            with gr.Column(scale=1):
                logics = gr.Dropdown(['AND', 'OR', 'NOT'], label='Logic', value = "OR")
            with gr.Column(scale=6):
                keyword = gr.Textbox(lines=1, label='Search Term')
            with gr.Column(scale=3):
                tag = gr.Dropdown(['Title', 'Abstract', 'All'], label='Search Type', value='All')
        Logics.append(logics)
        Keywords.append(keyword)
        Fields.append(tag)
        
    arxiv_res = gr.HTML(label = 'Arxiv Search Results')
    submit = gr.Button(label='Search', variant='primary')
    submit.click(fn=arxiv_search, inputs=[*Logics, *Keywords, *Fields], outputs=arxiv_res)
    
    demo.launch(debug = True)

