---
name: design-stack
description: Runs the full UI design stack in order (design language, de-genericizing, visual direction, motion, build, brand). Use whenever the user asks to design or redesign an app, website, interface, or screen, or says "design stack" or "full design pass", or invokes /design-stack.
---

# Design Stack

Run these six layers in order. For each layer, invoke the named skill with the Skill tool, apply its guidance, and carry its decisions forward. Do not skip a layer unless it clearly does not apply; say so in one line if you do.

| # | Layer | Skill to invoke | Job |
|---|-------|-----------------|-----|
| 1 | UI UX Pro Max | `ui-ux-pro-max` | Choose the design language |
| 2 | Taste | `design-taste-frontend` | Remove the generic decisions |
| 3 | Frontend Design | `frontend-design` | Establish the visual direction |
| 4 | Transitions | `transitions-dev` (then `transitions-polish` to tune) | Make interaction feel deliberate |
| 5 | Web Artifacts | `web-artifacts-builder` | Build the working interface |
| 6 | Brand Guidelines | `brand-guidelines` | Keep everything recognizably yours |

## Where to get the skills

Before step 2, confirm each skill exists (it appears in the skills list, or lives in `~/.claude/skills/` or `~/.agents/skills/`; also check the current project's `.claude/skills/`). If one is missing, tell the user which, and point them here. Do not install anything without asking.

| Skill | Source |
|-------|--------|
| `ui-ux-pro-max` | https://github.com/nextlevelbuilder/ui-ux-pro-max-skill |
| `design-taste-frontend` | https://github.com/Leonxlnx/taste-skill (`skills/taste-skill`) |
| `frontend-design` | https://github.com/anthropics/skills (`skills/frontend-design`) |
| `transitions-dev`, `transitions-polish` | https://github.com/Jakubantalik/transitions.dev |
| `web-artifacts-builder` | https://github.com/anthropics/skills (`skills/web-artifacts-builder`) |
| `brand-guidelines` | https://github.com/anthropics/skills (`skills/brand-guidelines`) |

UI UX Pro Max installs as a Claude Code plugin: `/plugin marketplace add nextlevelbuilder/ui-ux-pro-max-skill`, then `/plugin install ui-ux-pro-max@ui-ux-pro-max-skill`. Or `npm install -g ui-ux-pro-max-cli` and `uipro init --ai claude` in a project.

Other install options: `npx skills add <owner/repo>` (the `skills` CLI from vercel-labs/skills, which installed taste and transitions here), or copy the skill folder into `~/.claude/skills/`. `find-skills` can also search for them.

If a skill stays unavailable, skip that layer, say so, and cover its job from the neighboring layers.

## Procedure

1. **Frame.** Restate the goal, audience, and target (artifact vs. project code) in two lines. If the target is a project, build in the project's stack; use layer 5's guidance only when the output is a claude.ai artifact.
2. **Design language (1).** Invoke `ui-ux-pro-max`. Output: style, type pairing, palette, spacing and layout principles. If that skill is not installed, say so and derive the language yourself from layers 2–3.
3. **Taste (2).** Invoke `design-taste-frontend`. Audit the language from step 2 and replace template defaults (stock gradients, centered-hero-plus-three-cards, default fonts and radii) with specific choices.
4. **Visual direction (3).** Invoke `frontend-design`. Lock the aesthetic direction, typography, and composition. Write the resulting decisions down as a short spec (tokens: colors, type scale, spacing, radius, elevation) before any code.
5. **Motion (4).** Invoke `transitions-dev` and pick transitions for the interactions that exist (menus, modals, toasts, tabs, loaders). Later, invoke `transitions-polish` to tune durations and easing against the token scale.
6. **Build (5).** Invoke `web-artifacts-builder` (artifact output) or build natively (project output). Implement the spec from step 4 with the motion from step 5. Use the tokens, not ad-hoc values.
7. **Brand (6).** Invoke `brand-guidelines` last and reconcile: colors, type, and tone must match the brand. Where the brand conflicts with earlier layers, the brand wins on color/type; keep the layout and motion decisions.
8. **Verify.** Look at the result (screenshot or run it), check against the spec, fix anything generic that crept back, then summarize the decisions made per layer in a few lines.

## Rules

- Earlier layers set constraints; later layers refine, never silently contradict. If one must override another, say which and why.
- The spec from step 4 is the single source of truth for the build.
- Keep it proportionate: for a small component, do each layer in a sentence or two rather than a full pass.
