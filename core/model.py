from langchain_community.llms import LlamaCpp
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_openai import ChatOpenAI

def _llama(history, sources_retrieved):
    llm = LlamaCpp(model_path="models/Meta-Llama-3-8B-Instruct-Q3_K_L.gguf", 
                max_tokens=None,
                n_ctx=512,
                stop=["<|eot_id|>"])

    sys_template_str = "Você é um assistente virtual que ajuda a realizar vendas do curso LLM4Devs. Responda a pergunta do usuário em até 30 palavras."
    human_template_str = "{user_prompt}"

    template = """
        <|begin_of_text|>
        <|start_header_id|>system<|end_header_id|>
        {system_prompt}
        <|eot_id|>
        <|start_header_id|>user<|end_header_id|>
        {user_prompt}
        <|eot_id|>
        <|start_header_id|>system<|end_header_id|>
        Para responder a pergunta do usuário, considere as seguintes referências: {sources_retrieved}
        <|eot_id|>
        <|start_header_id|>system<|end_header_id|>
        Considere também o histórico de conversa: {history}
        <|eot_id|>
        <|start_header_id|>assistant<|end_header_id|>
        """

    prompt = PromptTemplate.from_template(template.format(system_prompt = sys_template_str,
                                                          user_prompt = human_template_str,
                                                          sources_retrieved = sources_retrieved,
                                                          history = history))
    return prompt | llm 

def _gpt():
    llm = ChatOpenAI()

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "Você é um assistente virtual que ajuda a realizar vendas do curso LLM4Devs. Responda a pergunta do usuário em até 30 palavras"),
            ("human", "{user_prompt}"),
            ("system", "Para responder a pergunta do usuário, considere as seguintes referências: {sources_retrieved}"),
            ("system", "Considere também o histórico de conversa: {history}"),
        ]
    )

    return prompt | llm 



def get_response(llm, user_prompt, history, sources_retrieved):
    chain = None
    if llm == "llama":
        chain = _llama(history, sources_retrieved)
    
    chain = _gpt()
    
    return chain.invoke({"user_prompt" : user_prompt,
                         "sources_retrieved" : sources_retrieved,
                         "history" : history}).content
