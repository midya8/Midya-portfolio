# EpistemLab

Three small tools for inspecting knowledge in a supplied mathematical model.
They distinguish a public announcement, a Boolean disclosure and an event that
not everyone can observe. Python builds and checks the evidence; each browser
tool runs locally after its static files load, without a model service or API.

[Announcement workbench](https://midya8.github.io/epistemlab/) ·
[Disclosure atlas](https://midya8.github.io/epistemlab/disclosures.html) ·
[Event inspector](https://midya8.github.io/epistemlab/events.html) ·
[Source and reproduction](https://github.com/midya8/epistemlab)

## A truthful announcement can undo its own truth

In the default two-world example, "p, but agent a does not know p" is true.
Announcing it removes the world where p is false. Agent a now knows p, so the
announcement's content is false in the remaining world. The fact survives; the
ignorance does not.

The workbench shows every supplied world, each agent's information partition,
every announcement round and every subformula's truth set. A common-knowledge
failure includes an actual shortest path through the agents' relations. Other
controls separate everybody's knowledge from common knowledge, show hypothetical
pooled information and follow three observers through an 8, 7, 4, 1 world
sequence. When an update removes the focus, its pointed answers are null, not
false or vacuously known.

## A restriction is not always a possible disclosure

The disclosure atlas enumerates every retained-world subset for up to eight
worlds. Only restrictions expressible by Boolean formulas over the supplied
atoms count as Boolean announcements. Worlds with identical facts cannot be
separated that way. The atlas provides either defining DNF cubes or an actual
equal-valuation obstruction pair.

The default control has two inclusion-maximal successful disclosures, retaining
two and three worlds. Only the second retains the maximum number. Another
control has successful diagnostic restrictions but no Boolean solution.
Disclosing more can also destroy an ignorance goal. The inspector shows the
restricted model, goal frontiers, truth sets and modal failure paths rather
than returning only a yes or no.

## Learning a fact is different from everyone seeing you learn it

The event inspector keeps pairs of worlds and informational events. In the
read/may-idle control, the receiver learns p while an observer still does not
know whether the receiver learned. A separately labeled public-announcement
comparison gives different answers. Marking the actual event does not remove
other events, and equal preconditions do not merge event copies.

Inspect every candidate pair and its precondition, inherited facts, before/after
partitions and both conditions needed for a product arrow. Every modal formula
has its own obligations and paths. If the designated pair is absent, post-event
focus values are null even when other pairs remain.

## Check the whole report, not only the displayed answer

The generator uses recursive pointwise semantics and breadth-first paths. A
separate checker uses truth-set algebra, partition blocks, greatest fixed points
and Floyd-Warshall distances. The event checker rebuilds the product using
relation rows. Shared strict input validation and written semantics are
disclosed; the checker is separate from the generator, not unrelated software.
Browser exports count as independently checked only after Python accepts the
complete report.

The current source passes 30 Python tests and 13 Node/Chrome tests. Reproduction
includes all 200 three-world/two-agent partition/valuation models, 120 seeded
nested announcement requests, 45 nested-goal disclosure atlases and 648 event
requests. Optional pyModelChecking 1.3.4 checks reconstructed modal truth sets
through an ordinary CTL translation. That is an additional implementation check,
not an independent event parser or a theorem proof.

Live Chrome checks all three routes at 320, 390 and 1280 pixels. A separate
trusted-download run retains all 28 control exports. Each of those live reports
and its local counterpart reproduces exactly through the installed Python API
and CLI and passes the separate checker. Installed-wheel checks also exercise
both command entry points, eleven installed module origins and rejection of
altered reports. The repository documents the commands and bounds needed to
repeat these checks.

## What it does not claim

These are finite, supplied S5 knowledge models, not estimates of what real people
or language models know. Announcements allow up to 16 worlds and four sequential
updates; disclosure atlases allow up to eight worlds; event products allow four
worlds, three events and twelve retained pairs. The event inspector preserves
facts and uses equivalence partitions for both world and event uncertainty.

No factual assignments, probabilities, belief revision, deceptive directed
events, action composition, general planning, human-knowledge inference or
scalability claim. Counting retained worlds is not a privacy guarantee. The
semantics and graph methods are established; the contribution here is the
bounded implementation, controls, inspectable reports and separate checks.

[Announcement contract](https://github.com/midya8/epistemlab/blob/main/CONTRACT.md) ·
[Disclosure contract](https://github.com/midya8/epistemlab/blob/main/DISCLOSURES.md) ·
[Event contract](https://github.com/midya8/epistemlab/blob/main/EVENTS.md) ·
[Sources and attribution](https://github.com/midya8/epistemlab/blob/main/SOURCES.md)
