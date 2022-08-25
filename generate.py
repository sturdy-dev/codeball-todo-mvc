prompts = [
    "Create a hello world flask webserver",

    "Add a /tasks endpoint listing all tasks in a sqlite database",

    "before_first_request: Make sure that the tasks table exists (id auto incremental id, description text, done bool)",

    "Update the tasks() method to return tasks as objects",

    "Add a /add endpoint that inserts new entries to the tasks table.",

    "Add a /update endpoint that updates task descriptions and done status",

    "Add CORS headers to allow connections from any host",

    "Update the add() method to return the id of the task created in json",

    "Format",

    "before_first_request, before conn.close: if the tasks table is empty, add three rows",
]

import os
import openai
import time

openai.api_key = os.getenv("OPENAI_API_KEY")

file_contents = ""

for idx, prompt in enumerate(prompts):
    print(prompt)

    res = openai.Edit.create(
        model="code-davinci-edit-001",
        input=file_contents,
        instruction=prompt,
        temperature=0,  # Using temperature 0 makes Codex deterministic
        top_p=1,
    )

    file_contents = res.choices[0].text

    # with open(f"/Users/gustav/src/codeball-web/src/lib/blog/todo/steps/app_{idx}.py", "w") as f:
    #     f.write(file_contents)

    with open(f"app.py", "w") as f:
        f.write(file_contents)

    print(os.system("git add app.py"))
    print(os.system(f"git commit --author \"Codeball <bot@codeball.ai>\" -m \"prompt: {prompt}\""))

    time.sleep(10)



