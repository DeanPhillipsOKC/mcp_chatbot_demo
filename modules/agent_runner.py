import asyncio
from agents import Runner

def run_agent(loop, agent, chat_history, user_prompt,
              user_type, client_code, employee_email, max_iters=6):
    debug_rows = []

    async def _runner():
        history_txt = "\n".join(
            f"{m['role'].title()}: {m['content']}" for m in chat_history
        )
        security_hdr = (
            f"[USER_TYPE={user_type}; CLIENT_CODE={client_code or 'N/A'}; "
            f"EMAIL={employee_email or 'N/A'}]"
        )
        current = f"{security_hdr}\n{history_txt}\nUser: {user_prompt}"
        ctx = {
            "chat_history": chat_history,
            "user_type": user_type,
            "client_code": client_code,
            "employee_email": employee_email,
        }

        for iteration in range(1, max_iters + 1):
            res = await Runner.run(agent, input=current, context=ctx)

            if getattr(res, "new_items", None):
                rows = []
                for idx, itm in enumerate(res.new_items, start=1):
                    if getattr(itm, "type", "") != "tool_call_item":
                        continue
                    raw = getattr(itm, "raw_item", None)
                    name = getattr(raw, "name", "") if raw else ""
                    args = " ".join(getattr(raw, "arguments", "").split()) if raw else ""
                    rows.append({"#": idx, "Tool": name, "Arguments": args})
                debug_rows.extend(rows)

            current = res.final_output
            if "final answer" in current.lower():
                break

        return current

    final_output = loop.run_until_complete(_runner())
    return final_output, debug_rows