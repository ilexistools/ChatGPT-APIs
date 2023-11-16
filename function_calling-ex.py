from openai import OpenAI
import json
import os 


client = OpenAI(api_key=os.environ.get("CUSTOM_ENV_NAME"),)


# Função apenas de exemplo para retornar o tempo.
#  Em produção, poderia ser uma API.
def get_current_weather(location, unit="fahrenheit"):
    """Retorna o tempo em uma dada localização"""
    if "tokyo" in location.lower():
        return json.dumps({"location": "Tokyo", "temperature": "10", "unit": "celsius"})
    elif "san francisco" in location.lower():
        return json.dumps({"location": "San Francisco", "temperature": "72", "unit": "fahrenheit"})
    elif "paris" in location.lower():
        return json.dumps({"location": "Paris", "temperature": "22", "unit": "celsius"})
    else:
        return json.dumps({"location": location, "temperature": "unknown"})

def run_conversation():
    # Passo 1: envia a conversa e as funções disponíveis para o modelo 
    messages = [{"role": "user", "content": "What's the weather like in San Francisco, Tokyo, and Paris?"}]
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_current_weather",
                "description": "Get the current weather in a given location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city and state, e.g. San Francisco, CA",
                        },
                        "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                    },
                    "required": ["location"],
                },
            },
        }
    ]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=messages,
        tools=tools,
        tool_choice="auto",  # auto é padrão, apenas para deixar explícito
    )
    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls
    # Passo 2: verifica se o modelo quis chamar a função 
    if tool_calls:
        # Passo 3: chama a função
        # Nota: o JSON retornado pode ser inválido; certifique-se de gerenciar erros
        available_functions = {
            "get_current_weather": get_current_weather,
        }  # apenas uma função de exemplo, mas você pode adicionar mais
        messages.append(response_message)  # extende a conversa com a resposa do assistente
        # Passo 4: envia as informação para cada chamada de função e resposta para o modelo 
        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_to_call = available_functions[function_name]
            function_args = json.loads(tool_call.function.arguments)
            function_response = function_to_call(
                location=function_args.get("location"),
                unit=function_args.get("unit"),
            )
            messages.append(
                {
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "name": function_name,
                    "content": function_response,
                }
            )  # este conversation with function response
        second_response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=messages,
        )  # retonar uma nova resposta do modelo em que é possível ver a resposta da função 
        return second_response
print(run_conversation())