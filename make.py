import os
from string import Template


substitutions = dict(
    WELCOME="Welcome!",
    MESSAGE="Is that really how it works?",
    BUILD=os.environ.get("BUILD", "SNAPSHOT"),
    THING=os.environ.get("THING", "NOTHING")
    )

with open("app/index.html") as f:
    template = Template(f.read())

with open("build/index.html", "w") as f:
    f.write(template.substitute(substitutions))
