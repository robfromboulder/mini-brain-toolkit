# mini-brain-toolkit 🧠

A **mini-brain** captures knowledge about your software project that can't be derived from code or git history: why decisions went one way and not another, what was tried and discarded, what was surprising. Normally these details live in your team's heads or are scattered across tickets, wikis, and project docs. Using a mini-brain with your codebase helps iterate and triage faster, and gives Claude the context to make more changes autonomously.

**Using a mini-brain is just chatting with Claude.** Your coding sessions are the raw material. At a natural stopping point, you'll be asked to save what the session decided and learned. There's nothing to file, no format to learn, and you never leave the repo you're working in.

**Mini-brains are built for software teams.** A mini-brain is just Markdown files in a dedicated git repo, alongside your regular project repos. Changes to a mini-brain are made through commits and PRs, reviewed like any other code — the knowledge belongs to the team, and teammates and AI agents all work from the same brain.

**Mini-brains are self-improving.** On a schedule, a mini-brain dreams: verifying all claims against the codebase, pruning what's become derivable, and doing follow-on research. The brain stays small enough to read completely, and curious about what it doesn't know.

## Usage

These examples assume you're chatting with Claude from a repo cloned alongside the toolkit.

#### Create a new mini-brain for a project:

> Read ../mini-brain-toolkit/MBT_CREATE_BRAIN for instructions and set up a mini-brain for &lt;my project&gt;

👆 asks about your project, picks a namespace token, produces the seed file set from `templates/`, and hooks the brain into your project repos

#### Check an existing mini-brain repo against the pattern:

> Read ../mini-brain-toolkit/MBT_CHECK_BRAIN for instructions and check ../some-repo

👆 scores the repo against the pattern's principles and suggests improvements
