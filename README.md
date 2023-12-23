# DocSumAI

Example program that use OPenAI's Assistant API to summarize very large files

## RUN Sample

```bash
 Welcome to Large Document Summarization Assistant. I am here to help you summarize very large documents...

 Assistant Info: asst_2JqtOm6HvJyk8XvDfO2otDbO 
{'id': 'asst_2JqtOm6HvJyk8XvDfO2otDbO', 'created_at': 1703358415, 'description': None, 'file_ids': ['file-VOcUZUeuwBiqN9i8eVFuiH0T'], 'instructions': 'You are document summarization assistant. You will summarize large documents', 'metadata': {}, 'model': 'gpt-4-1106-preview', 'name': 'Document Summarization Assistant', 'object': 'assistant', 'tools': [{'type': 'retrieval'}]}
 Thread Info: thread_BbrQaXxauDoKMPgrSiObRk4J 
{'id': 'thread_BbrQaXxauDoKMPgrSiObRk4J', 'created_at': 1703358425, 'metadata': {}, 'object': 'thread'}
 Run Info: asst_2JqtOm6HvJyk8XvDfO2otDbO 
{'id': 'run_md2C9ROTavE46p95mdUmAelB', 'assistant_id': 'asst_2JqtOm6HvJyk8XvDfO2otDbO', 'cancelled_at': None, 'completed_at': None, 'created_at': 1703358425, 'expires_at': 1703359025, 'failed_at': None, 'file_ids': ['file-VOcUZUeuwBiqN9i8eVFuiH0T'], 'instructions': 'You are document summarization assistant. You will summarize large documents', 'last_error': None, 'metadata': {}, 'model': 'gpt-4-1106-preview', 'object': 'thread.run', 'required_action': None, 'started_at': None, 'status': 'queued', 'thread_id': 'thread_BbrQaXxauDoKMPgrSiObRk4J', 'tools': [{'type': 'retrieval'}]}
 OpenAI: Run is not yet completed. Waiting...in_progress 
 OpenAI: Run is not yet completed. Waiting...in_progress 
 OpenAI: Run is not yet completed. Waiting...in_progress 
 OpenAI: Run is not yet completed. Waiting...in_progress 
 ...

Run is completed.
Elapsed time: 66.448655128479, seconds

 Document Summary: 

user: Summarize the document A Survey of Large Language Models. Priority is to capture all important points in the document, do not be concerted about summary size
assistant: The document titled "A Survey of Large Language Models" provides a comprehensive overview of the evolution, current state, and future directions of large language models (LLMs). The document can be summarized broadly into different sections as follows:

1. **Task Solving Capacity of Language Models**: It outlines the evolution of language models over time concerning their task-solving abilities. From functioning as specific task helpers to becoming general-purpose task solvers, the landscape has expanded significantly with neural language models and pre-trained language models culminating in the development of LLMs such as GPT-3 and GPT-4, which can tackle real-world tasks【9†source】.

2. **Overview of LLMs**: The section delves into the background of LLMs, discussing the infrastructure of models like GPT-3 and PaLM, scaling laws guiding model development, potential emergent abilities such as in-context learning, and key techniques that have contributed to the success of LLMs such as distributed training, ability eliciting, alignment tuning, and tool manipulation【13†source】【17†source】【21†source】.

3. **Technical Evolution of GPT-series Models**: It elaborates on the inception of OpenAI’s GPT models and their iterative evolution, describing how GPT-1 laid the foundation with a generative pre-training approach and GPT-2 expanded upon this with increased parameter scale. The document then zeroes in on the major leap in capacity represented by GPT-3, which introduced the concept of in-context learning, and subsequent enhancements leading to GPT-3.5 models. ChatGPT, a model optimized for conversation, and GPT-4, which has the ability to process multimodal signals and improve safety measures, are presented as milestones of language models【31†source】.

4. **Resources for LLMs**: The survey highlights the challenges and demands of reproducing LLMs due to technical and computational complexities. Nonetheless, it shares publicly available resources, including model checkpoints (or APIs), to facilitate incremental development or experimental study within the research community. Several model checkpoints are mentioned, such as mT5, PanGu-α, T0, and GPT-NeoX-20B. It also identifies APIs available for models in different scale levels from tens to hundreds of billions of parameters【35†source】.

This structured summary encapsulates the key points made in each major section of the survey, beginning with the role of language models in task-solving and their subsequent development into powerful tools powered by Transformer architectures, scaling laws, and emergent abilities. It also notes the critical milestones in the GPT series of models and closes with resources that are vital to the development and study of LLMs in the community.


Process finished with exit code 0

