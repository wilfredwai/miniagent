
from call_function import available_functions, call_function

def agent_call() -> str:
    
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": args.user_prompt},
    ]
    
    args = parser.parse_args()
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        tools=available_functions,
    )
    message = response.choices[0].message
    messages.append(message)
    for calls in range(20):
        if message.tool_calls:
            print("Response:")  
            for tool_call in message.tool_calls:
                result_message = call_function(tool_call, args.verbose)
                if not result_message["content"]:
                    raise Exception ("Error No content return from 'call_function'")
                if args.verbose:
                    print(f"-> {result_message['content']}")
        messages.append(result_message)
        if tool_call