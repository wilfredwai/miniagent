import sys
from call_function import call_function, available_functions
from prompts import system_prompt


def agent_call(client, args) -> str:

    messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": args.user_prompt},
    ]
    
    for calls in range(20):

        response = client.chat.completions.create(
            model="stealth/crouton-alpha",
            #model="openrouter/free",
            messages=messages,
            tools=available_functions,
        )

        message = response.choices[0].message
        messages.append(message)
    
        if message.tool_calls:
            #print("Response:")  
            for tool_call in message.tool_calls:
                result_message = call_function(tool_call, args.verbose)
                messages.append(result_message)
                if not result_message["content"]:
                    return "No content return from 'call_function', exiting..."
                if args.verbose:
                    print(f" - Calling function: {tool_call.function.name}")
        else:
            return message.content
    sys.exit("Error: Exceeded maximum number of calls (20) without a final response")