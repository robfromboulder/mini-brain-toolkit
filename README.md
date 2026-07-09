# mini-brain-toolkit 🧠
Mini-brains for self-improving software

A **mini-brain** is a small set of Markdown files that captures the *why* behind a project: what problems the project tries to solve (and how), what tradeoffs were considered, why a decision went one way vs another, what was tried and discarded along the way, and what constraints weren't obvious at first. Your code, git history, and tickets rarely hold all this background detail — but this is crucial to understanding how to debug or improve your software.

Most knowledge systems grow forever: wikis, second brains, agent memories, all expanding until no one trusts them. A mini-brain does the opposite. By design, it shrinks toward what matters, staying small enough to trust and to use every day. A Claude session or AI agent can intelligently load mini-brain knowledge into context to plan a feature or track down a bug. Company leaders and new engineers can interactively chat with the mini-brain instead of just reading docs and code.

This toolkit has two workflows: one creates a new mini-brain for a project, the other checks an existing mini-brain against the pattern and suggests improvements. The toolkit is itself a mini-brain and a good example.

## Usage

#### Create a new mini-brain for a project:

> Read ../mini-brain-toolkit/MBT_CREATE_BRAIN for instructions and set up a mini-brain for &lt;my project&gt;

👆 asks about your project, picks a namespace token, and produces the seed file set from `templates/`

#### Check an existing mini-brain (or a repo you suspect should have one):

> Read ../mini-brain-toolkit/MBT_CHECK_BRAIN for instructions and assess ../some-repo

👆 scores the repo against the pattern's principles and reports ranked, concrete opportunities — without modifying it

#### Ask about the toolkit itself:

> Read ../mini-brain-toolkit/CLAUDE for instructions

👆 you can now ask about the toolkit's scope, approach, and design decisions
