from openai import OpenAI
import os
import time

client = OpenAI(api_key=os.environ.get("CUSTOM_ENV_NAME"))

# 1. Cria o assistente
assistant = client.beta.assistants.create(
    name="Assistente de cálculos",
    instructions="Você é um assistente de cálculos matemáticos. Escreva e execute código.",
    tools=[{"type": "code_interpreter"}],
    model="gpt-4-1106-preview"
)

# 2. Cria a thread
thread = client.beta.threads.create()

# 3. Adiciona mensagens à thread
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="Preciso resolver a equação: `3x + 11 = 14`."
)

# 4. Executa o assistente
run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id,
    instructions="O usuário possui conta premium."
)

run_status = client.beta.threads.runs.retrieve(
        thread_id=thread.id,
        run_id=run.id
    )

# 5. Espera ativa para verificar o status da execução
while True:
    run_status = client.beta.threads.runs.retrieve(
        thread_id=thread.id,
        run_id=run.id
    )
    if run_status.status in ['completed', 'failed']:
        break
    time.sleep(1)  # Espera 1 segundo antes de verificar novamente

# 6. Imprime a resposta
messages = client.beta.threads.messages.list(
    thread_id=thread.id
)

# Supondo que 'messages' é a variável que contém a resposta da API
for message in messages:
    # Verifica se a mensagem é do assistente
    if message.role == 'assistant':
        # Itera sobre o conteúdo da mensagem do assistente
        for content in message.content:
            if content.type == 'text':
                print(content.text.value)  # Imprime o texto da resposta
                break  # Quebra o loop após encontrar a primeira resposta do assistente

    