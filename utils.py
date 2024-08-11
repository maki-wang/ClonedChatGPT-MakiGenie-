# -*- coding: utf-8 -*-
# @Time    : 2024/8/10 18:59
# @Author  : Maki Wang
# @FileName: utils.py
# @Software: PyCharm
# !/usr/bin/env python3

from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain

def get_chat_response(prompt, memory, openai_api_key):
    model = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=openai_api_key)
    chain = ConversationChain(llm=model, memory=memory)

    response = chain.invoke({"input": prompt})
    return response["response"]


