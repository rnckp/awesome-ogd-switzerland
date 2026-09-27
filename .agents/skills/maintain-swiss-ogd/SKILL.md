---
name: maintain-swiss-ogd
description: Maintain the awesome-ogd-switzerland repository by discovering and verifying new Swiss open-data resources, updating outdated entries, checking links and reuse terms, and correcting duplicates, misplaced entries and editorial issues. Use for recurring refreshes or targeted audits of this directory.
---

# Maintain Swiss Open Data

Keep `rnckp/awesome-ogd-switzerland` useful, current and selective. A run should produce evidence-backed local edits and a concise account of what was checked, changed and left unresolved. More entries are not inherently better.

## Locate the repository and establish scope

Use the repository containing this skill (`.agents/skills/maintain-swiss-ogd/`) as the checkout to maintain. Resolve its root relative to this skill, rather than relying on a machine-specific path. Verify the repository identity from its README and Git remotes before editing. If the skill is installed outside a checkout, use the active checkout when it is this repository; otherwise ask for the checkout path rather than creating or cloning another copy automatically.

Read applicable `AGENTS.md`, `git status`, the current README including its curation/contribution policy, and the helper scripts before acting. The live README and the user's current instructions take precedence over the conventions below. Preserve existing user edits.

Default to a maintenance pass that applies verified additions, corrections, moves and removals locally. If the user asks for an audit or recommendations only, report findings without changing repository files. A narrower topic or time budget limits the pass; explicitly record the coverage. Do not commit, push, publish, open issues/PRs, or create schedules unless the user requests those actions.

Read the most recent available reports in `_ignore/maintenance/`, plus any current link/count reports. Check report dates and relevant Git changes; previous findings are leads, not current verification. Revisit unresolved issues and rotate deeper topic reviews toward areas not checked recently.

## Discover and verify resources

Use live web research. Inspect primary publisher pages, actual catalog records, API documentation, repository licenses, release notices and reuse terms. Search results can identify candidates but do not establish eligibility or a working replacement URL.

For a normal pass:

- Review the whole README for structural and editorial problems and run a full HTTP link check when network access permits.
- Search for valuable additions in Swiss federal, cantonal and municipal publishing, then relevant research and community sources. Use opendata.swiss publisher records and official topic pages as discovery routes. Search in German, French, Italian or English as appropriate.
- Prioritize gaps, newly opened datasets, improved interfaces, official replacements and underrepresented topics. Do not add every new dataset to a portal directory: a specific dataset should offer enough distinct value to warrant its own entry.
- Perform deeper content/license checks on additions, changed destinations, suspicious existing entries and a rotating selection of existing topics. Do not imply that checking HTTP status verified every entry's content or license.
- For each proposed substantive change, retain the evidence URL, check date, relevant finding and decision in the run report. Distinguish a publisher's update date from the date you checked it.

Compare candidates with primary and secondary links already in the README. Different names, languages, domains, mirrors and redirects can refer to the same source. A portal and its API can justify separate navigation routes, but not duplicated full descriptions.

Stop discovery when the requested scope has been covered and additional searches mainly repeat known sources. Do not enforce an addition quota. A verified run with no changes is a valid outcome.

## Apply the curation rules

- Focus on Swiss OGD, with clearly identified complementary research, community and private open data. Judge relevance, provenance and reuse rights rather than the publisher's legal form. Government ownership, public funding, an accessible website, or an API does not by itself make data open.
- Data must permit use, modification and redistribution, including commercial reuse. Check actual terms rather than relying on labels such as “open,” “free,” “FAIR” or “public.” Software needs an OSI-approved license in its source repository.
- Free, non-discriminatory registration can qualify. Record material requirements and exclusions, including image rights separate from dataset rights. Non-commercial-only terms, payment, case-by-case permission and unclear rights do not qualify an individual dataset or tool.
- Mixed-access catalogs can qualify as discovery resources when useful open material is identifiable and the description clearly flags restricted records. Do not use this exception to relabel an otherwise ineligible standalone service as a catalog.
- In cultural collections, distinguish reusable metadata from digitized images, recordings and documents. In research repositories, distinguish a public record from downloadable, openly reusable files.
- Keep the European comparison section small: core European catalogs/statistics and neighboring-country sources with a clear comparison use. Do not rebuild a general world directory.
- For new candidates with unverified rights, defer inclusion and explain what evidence is missing. For an existing entry, uncertain rights alone are a finding to investigate, not proof of ineligibility. Remove or narrow it when verified evidence establishes a policy conflict; note the evidence and any qualifying replacement.

A HTTP 200 response may be a parked page, login screen, soft 404 or unrelated redirect. A 403, 429, timeout, TLS error or redirect loop does not prove a resource is dead. For suspected dead links, retry selectively, inspect the destination where possible, and look for an official successor. Confirm a 404/410 before removal. If still inconclusive, leave the entry and record the unresolved check; do not repeatedly hammer a blocked site.

## Placement and writing

Follow the current headings rather than imposing a fresh taxonomy every run. The established structure separates data sources, geospatial data, selected APIs/linked data, tools, guides/policy, community/publications and European comparisons.

- Put national thematic resources under their subject, and broad regional portals under cantonal or municipal portals. “National” does not mean every publisher is federal or every dataset has nationwide coverage.
- Put procurement and official notices under administrative data; elections and popular votes under politics; collections under cultural heritage; events under community. Do not recreate miscellaneous or federal-office catch-all sections.
- Keep API links beside their source. The selected interfaces section is an intentional shortlist, not an exhaustive duplicate API inventory. Linked-data descriptions should explain the interface rather than repeat the source's full description.
- Distinguish tools from source-code directories. Keep relevant non-government sources identifiable without repetitive disclaimers.
- Use `- [Resource](URL) — What it contains and its coverage.` Aim for one or two short sentences. Preserve official resource names and use clear English descriptions.
- Omit routine “Access:” clauses and obvious statements such as “access via website,” “data page,” “source links” or “API documentation” when the primary link already conveys that. Keep useful formats, metadata-only limitations, registration and reuse restrictions. Add compact descriptive secondary links, for example `[API](...) · [Source code](...)`.
- Avoid “here,” promotional claims, unverified superlatives, “new/current” without context and volatile undated counts. Explain differences between overlapping services, especially BFS discovery, table, explorer and map services.
- Keep shared explanations at section level and retain the collapsible TOC. Update anchors and cross-references when moving or renaming headings. Avoid broad cosmetic rewrites during routine maintenance.

## Use the repository helpers and verify the edits

Use the existing project environment; prefer `.venv/bin/python` when it is available. If dependencies are missing, use the repository's declared setup rather than modifying dependencies for an editorial task. Inspect the current scripts for options and behavior before running them.

From the repository root, the established commands are:

```sh
make check-links
make count-sources
git diff --check
```

The link checker distinguishes reachable, likely broken and inconclusive results. Its exit status alone is not a curation decision. It does not validate fragment routes, content or licenses. Network restrictions can make an entire run inconclusive; report that limitation rather than treating it as widespread source failure.

The counter counts resource bullets, not unique datasets or publishers. Secondary links do not add entries; deliberate separate interface entries do. Inspect generated reports instead of assuming either helper is correct.

After editing, verify added/changed destinations and material claims, duplicate primary entries, internal anchors, misplaced entries and the diff. Refresh counts. Recheck affected URLs; rerun the full link sweep only if the changes warrant it. Reports must accurately state whether they cover the final README or an earlier snapshot. Never present untested destinations as reachable.

See `src/README.md` for setup and script options. `count_sources.md` and `link-check-report.md` are currently ignored generated files. Respect the checkout's ignore rules; do not force-add them. Change helpers only when a demonstrated defect affects this maintenance task. If helper code changes, run `make check` and meaningful checks for the defect. README-only edits do not require new tests.

## Record the run and hand back

For an update run, write a dated report under `_ignore/maintenance/YYYY-MM-DD.md`, creating the directory if needed. Avoid overwriting an earlier run on the same day; append a timestamp to the filename. This location is currently ignored: check the live rules and do not change `.gitignore` just to store a report. For audit-only requests, provide the report in the response unless file output was requested.

Keep the report useful for the next run:

- Date, checked commit/worktree context, requested scope, topics searched and topics reviewed in depth.
- Additions, updates, moves, merges and removals, with evidence URLs and reasons for substantive decisions.
- Deferred candidates and unresolved failures, stating what is unknown and what to check next. Revisit rejected candidates when new evidence or changed terms justify it, rather than treating them as permanently banned.
- Validation commands, results, network/tool limitations and coverage that remains unchecked. Separate HTTP checks, content checks and license checks.

End with a short summary of actual edits, validation and remaining uncertainties, linking the local run report. Leave a reviewable working tree. Do not claim the directory is exhaustively current merely because its links respond successfully.
