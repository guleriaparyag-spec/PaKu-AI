# COMPLETE ORIGINAL KNOWLEDGE BASE – ALL 35 SECTIONS ARE PRESERVED BELOW.
MANUAL = """

# COMPLETE KNOWLEDGE BASE – LARGE LANGUAGE MODELS (LLMs)

## 1. Introduction to Artificial Intelligence

Artificial Intelligence (AI) is a technology that enables computers and machines to perform tasks that normally require human intelligence.

Examples:
- Understanding language.
- Recognizing images.
- Solving problems.
- Making predictions.
- Generating content.
- Understanding speech.

### Types of AI

1. Narrow AI: AI designed for specific tasks.
2. General AI: A theoretical form of AI that could perform a wide range of intellectual tasks like humans.
3. Superintelligent AI: A hypothetical AI that exceeds human intelligence across most areas.

### Main Branches of AI

- Machine Learning (ML): Machines learn patterns from data.
- Deep Learning: Uses multi-layer neural networks.
- Natural Language Processing (NLP): Helps computers understand and process human language.
- Computer Vision: Helps computers understand images and videos.
- Generative AI: Creates new content such as text, images, audio and video.

## 2. What is Generative AI?

Generative AI is a type of artificial intelligence that creates new content based on learned patterns.

It can generate:
- Text.
- Images.
- Videos.
- Music and audio.
- Computer code.
- Presentations.
- Documents.

Examples:
- ChatGPT.
- Google Gemini.
- Claude.
- Microsoft Copilot.
- Image-generation models.

### Traditional AI vs Generative AI

Traditional AI mainly analyzes information, classifies data and makes predictions.

Generative AI creates new content based on user instructions and learned patterns.

Example:

Traditional AI: Predicting whether an email is spam.

Generative AI: Writing a new email based on instructions.

## 3. What is a Large Language Model (LLM)?

A Large Language Model is an advanced AI model trained on large amounts of data to understand and generate human-like language.

LLMs can:
- Answer questions.
- Explain difficult concepts.
- Summarize documents.
- Translate languages.
- Generate computer code.
- Write emails and reports.
- Analyze information.
- Help with research.
- Perform reasoning tasks.

LLMs generally work by predicting the next token based on the preceding context.

Examples of LLM model families:
- GPT by OpenAI.
- Gemini by Google.
- Claude by Anthropic.
- Llama by Meta.
- Qwen by Alibaba.
- DeepSeek.
- Mistral.
- Gemma by Google.

## 4. How Does an LLM Work?

An LLM processes input and generates output through several stages.

1. User Input: The user enters a question or instruction.
2. Tokenization: The input text is converted into tokens.
3. Embedding: Tokens are represented as numerical vectors.
4. Transformer Processing: The model processes relationships between tokens using neural network layers.
5. Prediction: The model calculates probabilities for possible next tokens.
6. Generation: Tokens are generated sequentially to create a response.
7. Output: The generated answer is displayed to the user.

Example:

Input: "Artificial Intelligence is"

Possible output: "a technology that enables machines to perform intelligent tasks."

## 5. Transformer Architecture

The Transformer is a neural network architecture widely used in modern LLMs.

It was introduced in the 2017 research paper "Attention Is All You Need".

### Important Components

**1. Tokenization**

Converts text into smaller units called tokens.

**2. Embeddings**

Convert tokens into numerical representations that the model can process.

**3. Positional Information**

Helps the model understand the position and order of tokens.

**4. Self-Attention**

Helps the model identify relationships between different tokens in the input.

**5. Feed-Forward Networks**

Process information through neural network layers.

**6. Output Layer**

Calculates probabilities for the next token.

### Types of Transformer Architectures

- Encoder-only: Mainly used for understanding and representing input. Example: BERT.
- Decoder-only: Mainly used for generating text. Example: GPT-style models.
- Encoder-decoder: Uses an encoder and decoder for tasks such as translation. Example: T5.

## 6. What Are Tokens?

Tokens are the basic units of text processed by an LLM.

A token can represent:
- A complete word.
- Part of a word.
- Punctuation.
- A number.
- Other text symbols.

Example:

"Artificial Intelligence is amazing."

The sentence is divided into smaller token units by the model's tokenizer.

Important:
- Tokens are not always equal to words.
- Different models can use different tokenizers.
- Longer inputs generally require more tokens.
- Input and output tokens can affect API costs.

## 7. What Are Parameters?

Parameters are numerical values learned during model training.

They help the model identify patterns and generate responses.

Examples of model sizes:
- 1 billion parameters (1B).
- 7 billion parameters (7B).
- 70 billion parameters (70B).

More parameters do not automatically mean a better model. Data quality, architecture, training, optimization and evaluation also matter.

## 8. What Is a Context Window?

A context window is the maximum amount of input and conversation information a model can process in a single interaction.

It is generally measured in tokens.

A context window may include:
- System instructions.
- User questions.
- Previous conversation messages.
- Retrieved documents.
- Tool information.
- Generated responses.

A larger context window can help with processing long documents and conversations, but it does not guarantee better answers.

## 9. How Are LLMs Trained?

LLMs are developed through different training and adaptation stages.

### 1. Pretraining

The model learns language patterns from large datasets.

It learns to predict missing or next tokens.

### 2. Supervised Fine-Tuning (SFT)

The pretrained model is trained on examples of instructions and suitable responses.

This helps the model follow instructions and behave like an assistant.

### 3. Alignment and Preference Optimization

The model is further adjusted to produce more useful, safe and preferred responses.

Methods may include:
- RLHF (Reinforcement Learning from Human Feedback).
- DPO (Direct Preference Optimization).
- Other preference and reinforcement-learning techniques.

Not every model uses the same training pipeline.

## 10. What Is Prompt Engineering?

Prompt Engineering is the process of writing effective instructions to get better responses from an AI model.

A prompt tells the model what to do and how to respond.

### Elements of a Good Prompt

1. Role: Define who the AI should act as.
2. Task: Explain what it needs to do.
3. Context: Provide relevant background information.
4. Instructions: Explain rules and limitations.
5. Output Format: Define how the answer should look.
6. Examples: Show the model what a good response looks like.

### Example of a Basic Prompt

"Explain Artificial Intelligence."

### Example of an Improved Prompt

"Act as an AI teacher. Explain Artificial Intelligence to a beginner in simple English. Give five examples and a short conclusion."

### Types of Prompting

- Zero-shot prompting: Giving instructions without examples.
- One-shot prompting: Providing one example.
- Few-shot prompting: Providing multiple examples.
- Chain-of-thought prompting: Techniques that encourage structured reasoning.
- Role prompting: Assigning a role to the model.
- Structured prompting: Asking for output in a specific format.

## 11. What Is an API?

API stands for Application Programming Interface.

It allows different software applications to communicate with each other.

In AI development, an API allows a Python application, website or chatbot to send requests to an AI model and receive responses.

### Common API Providers

- OpenAI API.
- Groq API.
- Google Gemini API.
- Anthropic API.
- Together AI.
- Fireworks AI.
- Mistral API.

### Basic API Workflow

1. Create an account with an API provider.
2. Generate an API key.
3. Install the required Python library.
4. Connect to the API.
5. Select an available model.
6. Send a user prompt.
7. Receive and display the response.

An API key should be stored securely and never shared publicly.

## 12. What Is Groq?

Groq provides infrastructure for running AI models through its API.

It allows developers to access supported language models using API requests.

### Groq Features

- AI model inference.
- API access.
- Developer integration.
- Support for selected open and other available models.
- Streaming responses for supported requests.
- Tool-calling support for compatible models.

### Groq Python Library

The Groq Python SDK can be installed using:

pip install groq

Example:

from groq import Groq

client = Groq(api_key="YOUR_API_KEY")

response = client.chat.completions.create(
    model="AVAILABLE_MODEL_ID",
    messages=[
        {"role": "user", "content": "What is an LLM?"}
    ]
)

print(response.choices[0].message.content)

Note: Model IDs and features can change. Always check the current Groq model documentation.

## 13. Popular LLM Models and Providers

### OpenAI – GPT

GPT is a family of generative AI models developed by OpenAI.

Common applications:
- Conversational AI.
- Content generation.
- Coding.
- Reasoning.
- Data analysis.
- Multimodal applications.

### Google – Gemini

Gemini is Google's family of AI models.

Common applications:
- Text generation.
- Image and document understanding.
- Coding.
- Multimodal tasks.
- Reasoning.

### Anthropic – Claude

Claude is a family of AI models developed by Anthropic.

Common applications:
- Writing.
- Coding.
- Document analysis.
- Reasoning.
- Business tasks.

### Meta – Llama

Llama is a family of large language models developed by Meta.

It includes models with different sizes and capabilities. Many Llama model weights are available for developers under their applicable licenses.

Common applications:
- Chatbots.
- Research.
- Local AI applications.
- Custom AI development.

### DeepSeek

DeepSeek develops AI models for language, coding and reasoning tasks.

### Mistral

Mistral develops language models for general-purpose AI and specialized applications.

### Qwen

Qwen is a family of AI models developed by Alibaba.

### Gemma

Gemma is Google's family of lightweight, open models designed for developers and researchers.

Important: Availability, licensing, capabilities and pricing differ between model providers and individual model versions.

## 14. What Is RAG?

RAG stands for Retrieval-Augmented Generation.

RAG allows an LLM to retrieve information from an external knowledge source before generating an answer.

It is useful when a chatbot needs information that is not reliably available in the model's built-in knowledge.

### How RAG Works

1. User asks a question.
2. System searches the knowledge base.
3. Relevant information is retrieved.
4. Retrieved information is added to the model's context.
5. The LLM generates an answer using that information.

### Components of RAG

- Documents.
- Document processing.
- Text chunking.
- Embeddings.
- Vector database or search index.
- Retriever.
- LLM.
- Final response.

### Benefits of RAG

- Uses external knowledge.
- Supports private documents.
- Helps provide updated information.
- Can provide source references.
- Reduces dependence on model memory.

### Applications

- College information chatbots.
- Company support assistants.
- Document question-answering systems.
- Customer service applications.

## 15. What Is Fine-Tuning?

Fine-tuning is the process of adapting a pretrained model using additional task-specific training data.

It helps a model become more suitable for a particular task.

### Types of Fine-Tuning

- Full Fine-Tuning: Updates all or most model parameters.
- Parameter-Efficient Fine-Tuning (PEFT): Updates a smaller set of parameters.
- LoRA: Low-Rank Adaptation, a popular PEFT technique.
- QLoRA: Combines quantization and LoRA to reduce memory requirements.

### Benefits

- Better task-specific performance.
- Consistent output formats.
- Adaptation to specialized language.
- Improved performance on selected tasks.

### RAG vs Fine-Tuning

RAG provides relevant external information during a request.

Fine-tuning changes model parameters through additional training.

RAG is generally useful for providing changing or private information. Fine-tuning is useful for adapting behavior and specialized task performance.

They can also be used together.

## 16. What Are Embeddings?

Embeddings are numerical representations of text, images or other data.

They represent information in vector form.

Similar meanings can be represented by vectors that are closer together in an embedding space.

Applications:
- Semantic search.
- Document retrieval.
- Recommendation systems.
- RAG applications.
- Similarity detection.

Example:

"Best mobile phone"

"Top smartphone"

These sentences have similar meanings even though their words differ.

## 17. What Is a Vector Database?

A vector database stores and searches numerical vector representations called embeddings.

It is commonly used in semantic search and RAG systems.

Examples:
- Pinecone.
- Chroma.
- Weaviate.
- Milvus.
- Qdrant.
- FAISS (a similarity-search library, not a full database service).

Main functions:
- Store embeddings.
- Search similar vectors.
- Retrieve relevant information.
- Support AI knowledge systems.

## 18. What Is an AI Chatbot?

An AI chatbot is a software application that communicates with users using artificial intelligence.

It can understand questions and generate responses.

### Types of Chatbots

1. Rule-Based Chatbot: Follows predefined rules and responses.
2. Retrieval-Based Chatbot: Selects answers from stored information.
3. LLM-Based Chatbot: Uses a language model to generate responses.
4. RAG-Based Chatbot: Uses an LLM with an external knowledge source.
5. AI Agent: Can use tools and perform multi-step tasks under defined permissions.

### Basic LLM Chatbot Architecture

User → Application → Prompt → LLM API → Response → User

### Important Chatbot Components

- User interface.
- Backend.
- LLM provider.
- API key.
- System prompt.
- User prompt.
- Conversation history.
- Knowledge base.
- Output handling.

## 19. What Is an AI Agent?

An AI agent is a system that uses an AI model to work toward a goal.

Depending on its design, an agent can:
- Understand a task.
- Plan actions.
- Use tools.
- Retrieve information.
- Interact with external services.
- Evaluate results.
- Continue until a stopping condition is reached.

### Examples of Tools

- Web search.
- Calculator.
- Database.
- Email services.
- Calendar.
- Python execution.
- External APIs.

An LLM chatbot does not automatically become an agent just because it can answer questions.

## 20. What Is Tool Calling?

Tool calling allows a model to request the use of an external function or service.

Example:

User: What is 25 multiplied by 40?

The model may request a calculator tool.

The application executes the calculator function and sends the result back to the model.

Tool calling allows AI systems to interact with external software and data.

## 21. What Is Multimodal AI?

Multimodal AI can process or generate more than one type of information.

Modalities include:
- Text.
- Images.
- Audio.
- Video.
- Other structured data.

Examples:
- Asking questions about a photograph.
- Transcribing spoken language.
- Summarizing a video.
- Generating speech.
- Understanding documents containing images.

Not every LLM supports every modality.

## 22. Important LLM Parameters

### Temperature

Controls randomness in generated responses.

Lower temperature generally produces more predictable outputs.

Higher temperature generally produces more varied outputs.

### Top-p

Controls token selection by considering a cumulative probability distribution.

### Max Tokens

Limits the number of tokens generated or allowed, depending on the API parameter.

### Stop Sequences

Tell the model when to stop generating.

### Frequency Penalty

Can reduce repeated tokens or phrases in supported APIs.

### Presence Penalty

Can encourage the model to introduce new topics or tokens in supported APIs.

Parameter names and behavior may differ between providers.

## 23. What Is Hallucination?

Hallucination occurs when an AI model produces information that sounds correct but is false, unsupported or fabricated.

Reasons may include:
- Missing context.
- Ambiguous questions.
- Outdated information.
- Weak retrieval.
- Limitations in model reasoning.
- Probabilistic text generation.

### Ways to Reduce Hallucination

- Provide trusted knowledge sources.
- Use RAG.
- Write clear system prompts.
- Ask the model to acknowledge uncertainty.
- Verify important information.
- Use suitable evaluation datasets.
- Apply human review where necessary.

No technique guarantees that hallucinations will disappear completely.

## 24. What Is Quantization?

Quantization reduces the numerical precision used to represent model parameters.

It can reduce:
- Memory requirements.
- Storage requirements.
- Hardware requirements.

It can make model deployment more efficient.

Examples include 8-bit and 4-bit quantization.

Quantization may affect model quality and performance depending on the method and model.

## 25. What Is Model Inference?

Inference is the process of using a trained model to generate predictions or outputs.

In an LLM application, inference occurs when a user sends a prompt and the model generates a response.

Inference speed can depend on:
- Model size.
- Hardware.
- Quantization.
- Input length.
- Output length.
- Server capacity.
- Batch size.

## 26. What Is Open-Source and Open-Weight AI?

Open-source AI generally refers to systems where important parts of the source, data, code or development process are made available under appropriate licenses.

Open-weight models make trained model weights available under specified licenses.

Important difference:
- Open-source software provides source code under a license.
- Open-weight AI provides model weights under a license.
- Open-weight does not automatically mean every training dataset and development detail is public.

Always check the individual model's license before commercial use.

## 27. What Is LLM Evaluation?

LLM evaluation measures how well a model performs on particular tasks.

Important evaluation criteria:

- Accuracy.
- Relevance.
- Helpfulness.
- Reliability.
- Response time.
- Cost.
- Safety.
- Instruction following.

### Common Evaluation Metrics

- Accuracy.
- Precision.
- Recall.
- F1 Score.
- Exact Match.
- BLEU.
- ROUGE.
- Perplexity.

Different tasks require different metrics. There is no single metric that fully measures LLM quality.

## 28. Limitations of LLMs

LLMs have several limitations:

1. They can generate incorrect information.
2. They may have outdated knowledge.
3. They can misunderstand ambiguous questions.
4. They may struggle with complex calculations.
5. They can produce biased outputs.
6. They may generate insecure code.
7. They can be sensitive to prompt wording.
8. They may have context-window limitations.
9. Their use can involve financial and computational costs.
10. They require safety and privacy controls.

## 29. Applications of LLMs

### Education
- AI tutors.
- Study assistants.
- Question-answering systems.
- Notes generation.
- Exam preparation.

### Healthcare
- Medical document summarization.
- Administrative support.
- Medical information assistance under professional supervision.

### Business
- Customer support.
- Report generation.
- Data analysis.
- Document processing.

### Software Development
- Code generation.
- Debugging assistance.
- Documentation.
- Code explanation.

### Marketing
- Content generation.
- Email drafting.
- Campaign ideas.
- Customer communication.

### Research
- Literature summarization.
- Information extraction.
- Research assistance.
- Data organization.

## 30. LLM Development Tools and Frameworks

### Python
A programming language widely used for AI development.

### LangChain
A framework for building applications using language models, tools and external data.

### LlamaIndex
A framework for connecting LLM applications with external data sources.

### Hugging Face
A platform and ecosystem for accessing models, datasets and machine-learning tools.

### PyTorch
A machine-learning framework used for developing and training neural networks.

### TensorFlow
A machine-learning framework used to develop and deploy machine-learning models.

### Ollama
A tool for running supported LLMs locally.

### Streamlit
A Python framework for creating interactive data and AI applications.

### Gradio
A Python framework for building interfaces for machine-learning applications.

### Vector Databases
Pinecone, Chroma, Qdrant, Weaviate and Milvus.

## 31. LLM vs Traditional Machine Learning

Traditional machine-learning models are often trained for specific tasks such as classification, regression and prediction.

LLMs are large neural networks trained to process and generate language and, in some cases, other modalities.

Examples:

Traditional ML:
- Predicting house prices.
- Detecting spam.
- Predicting customer churn.

LLMs:
- Writing reports.
- Answering questions.
- Summarizing documents.
- Generating code.

## 32. Important LLM Terminology

AI: Artificial Intelligence.

ML: Machine Learning.

DL: Deep Learning.

NLP: Natural Language Processing.

LLM: Large Language Model.

GPT: Generative Pre-trained Transformer.

API: Application Programming Interface.

SDK: Software Development Kit.

RAG: Retrieval-Augmented Generation.

SFT: Supervised Fine-Tuning.

RLHF: Reinforcement Learning from Human Feedback.

DPO: Direct Preference Optimization.

PEFT: Parameter-Efficient Fine-Tuning.

LoRA: Low-Rank Adaptation.

QLoRA: Quantized Low-Rank Adaptation.

NLP: Natural Language Processing.

GPU: Graphics Processing Unit.

CPU: Central Processing Unit.

TPU: Tensor Processing Unit.

## 33. LLM Learning Roadmap

A beginner can learn LLM development in the following order:

Step 1: Understand Artificial Intelligence.

Step 2: Learn Machine Learning and Deep Learning basics.

Step 3: Learn Python programming.

Step 4: Understand NLP and tokenization.

Step 5: Learn Transformer architecture.

Step 6: Understand popular LLM models.

Step 7: Learn prompt engineering.

Step 8: Learn API integration.

Step 9: Build a basic LLM chatbot.

Step 10: Learn embeddings and vector databases.

Step 11: Build a RAG chatbot.

Step 12: Learn fine-tuning and model evaluation.

Step 13: Explore AI agents and tool calling.

Step 14: Deploy an AI application.

## 34. Official Learning Resources

OpenAI: https://platform.openai.com/docs/

Google AI: https://ai.google.dev/

Anthropic: https://docs.anthropic.com/

Groq: https://console.groq.com/docs

Hugging Face: https://huggingface.co/docs

Meta Llama: https://www.llama.com/

Microsoft Learn: https://learn.microsoft.com/

PyTorch: https://pytorch.org/docs/

LangChain: https://python.langchain.com/

LlamaIndex: https://docs.llamaindex.ai/

## 35. Important Knowledge Disclaimer

AI models, model names, API availability, pricing, features and technical documentation change frequently.

For current model versions, pricing, context windows, API limits and provider-specific capabilities, users should consult the official documentation.

Never invent benchmark scores, model rankings, pricing or technical specifications.

END OF LLM KNOWLEDGE BASE.
"""

ORIGINAL_ASSISTANT_GUIDELINES = """
# SYSTEM PROMPT – PaKuai (LLM EXPERT AI ASSISTANT)

## 1. ROLE AND IDENTITY

You are an intelligent AI assistant specializing in Large Language Models (LLMs), Artificial Intelligence, Generative AI and modern AI technologies.

Your name is "PaKuai" (LLM Expert Assistant).

Your purpose is to teach, explain and guide students, beginners, developers and AI enthusiasts about LLMs.

You must behave like an experienced AI teacher and technical mentor.

## 2. MAIN OBJECTIVES

Your responsibilities include:

- Explain Artificial Intelligence and Generative AI.
- Teach Large Language Models from beginner to advanced level.
- Explain popular LLM models and their differences.
- Teach Prompt Engineering.
- Explain Transformer Architecture.
- Explain Tokenization, Embeddings and Parameters.
- Explain APIs and Groq integration.
- Teach RAG and Fine-Tuning.
- Explain AI Agents and Tool Calling.
- Help users build AI chatbots.
- Explain Python code related to LLM development.
- Guide users through practical AI projects.
- Explain technical concepts using real-world examples.
- Answer general questions clearly and helpfully using your general knowledge and any provided Wikipedia context.

## 3. KNOWLEDGE BASE RULES

You have access to an LLM Knowledge Base.

Use this knowledge as your primary reference for LLM and AI topics.

Rules:

1. Give accurate technical explanations.
2. Never invent model specifications.
3. Never create fake API endpoints.
4. Never invent model names or benchmark results.
5. Clearly distinguish facts from examples.
6. If information is unavailable, acknowledge it.
7. For changing information such as pricing, model availability and API limits, recommend checking official documentation.
8. Do not claim to have checked live information unless Wikipedia context is provided in the prompt.

## 4. COMMUNICATION STYLE

- Use simple English.
- Understand English, Hindi and Hinglish questions.
- Reply in the language used by the user.
- Explain difficult concepts in beginner-friendly language.
- Avoid unnecessary technical jargon.
- Be friendly, patient and professional.
- Keep simple answers short.
- Give detailed explanations when requested.
- Use examples from everyday life.

## 5. EXPLANATION FORMAT

When a user asks about a technical concept, follow this structure:

**1. Meaning:** What is it?

**2. Simple Explanation:** Explain it in easy language.

**3. How It Works:** Explain the working process.

**4. Example:** Give a practical example.

**5. Applications:** Where is it used?

**6. Key Points:** Summarize the most important information.

Do not force all six sections into very simple questions. Keep answers relevant.

## 6. BEGINNER TEACHING MODE

Assume that the user may have no technical background.

For beginners:

- Start from the basics.
- Explain abbreviations.
- Use simple comparisons.
- Explain one concept at a time.
- Provide practical examples.
- Do not assume programming knowledge.
- Explain code line by line when requested.

## 7. COMPARISON MODE

When users compare two or more AI technologies, provide a simple comparison table.
Never claim that one technology is always better than another. Explain which is more suitable for the given task.

## 8. CODING ASSISTANT MODE

When users ask for LLM programming assistance:

- Use Python by default unless another language is requested.
- Provide complete and understandable code.
- Explain required libraries.
- Explain installation commands.
- Use placeholders for API keys.
- Never expose real API credentials.
- Explain how to run the code.
- Identify common errors and their solutions.
- Never invent unsupported model IDs or API methods.
- Make clear which provider-specific documentation should be checked.

## 9. PROMPT ENGINEERING MODE

When a user requests a prompt:

Create a structured prompt containing:
- Role.
- Objective.
- Context.
- Instructions.
- Restrictions.
- Output format.
- Example, when useful.

Make the prompt ready to copy and use.

## 10. PROJECT GUIDANCE MODE

Help users develop practical AI projects such as LLM Chatbots, RAG-Based Assistants, AI Study Assistants, and AI Agents.
For project questions, explain:
1. Project objective.
2. Required technologies.
3. Project architecture.
4. Implementation steps.
5. Expected output.
6. Possible improvements.

## 11. MODEL COMPARISON RULES

When comparing GPT, Gemini, Claude, Llama, DeepSeek, Mistral, Qwen or other models:
- Explain their strengths, typical use cases, and licensing/access model (open-weight vs proprietary API) neutrally without fabricating benchmarks.
"""
