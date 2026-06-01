---
name: ideation-list-agent-chat
description: Replace the one-way AgentThinking display on IdeationList.html with a Conversational Agentic Flow (chat bubble thread)
metadata:
  type: project
---

# Conversational Agentic Flow — IdeationList.html

## Overview

Replace the existing `AgentThinking` component (auto-running thinking steps + static recommendation card) with `AgentChat` — an inline chat bubble thread where the Podium Agent speaks in sequential message bubbles, asks the user a question with quick-reply chips, and responds to user input with a final recommendation and CTA.

Position: same inline slot above the stats cards. Dismissible via the × button.

---

## Component Architecture

**`AgentChat`** — single self-contained React component replacing `AgentThinking`.

Internal state machine:

```
idle → typing → msg1 → typing → msg2 → typing → question → awaiting → user-replied → typing → final
```

Sub-components (defined inside `AgentChat`):

- `TypingBubble` — animated three-dot indicator in an agent bubble shell
- `AgentBubble` — left-aligned agent message with optional tag chips and optional CTA button
- `UserBubble` — right-aligned user message in primary purple
- `QuickReplies` — row of pill chips that fire a user reply on click
- `InputBar` — bottom text input + send button

---

## Conversation Script (prototype data)

| Turn | Speaker | Content |
|------|---------|---------|
| 1 | Agent | "Hi Rohan, I'm reviewing your 4 active ideations…" |
| 2 | Agent | "I found a high-impact opportunity. The **Enterprise AI Infrastructure** track has the highest relevance score (95) and 'production evals' is your most-clicked term over 30 days." + tags: `Enterprise AI`, `Eval-Driven Dev`, `Series B+` |
| 3 | Agent | "Want me to generate topics for this ideation, or explore a different one?" + quick-reply chips: **Generate Topics** / **Explore Another** |
| 4 | User | (chip click or free-text input) |
| 5 | Agent | "Great — generating topics for Enterprise AI Infrastructure now." + primary CTA button → `TopicGeneration.html` |

Timing between turns: 1 000 ms typing indicator before each agent message resolves.

---

## Visual Language

### Agent bubbles
- Left-aligned, `max-w-[85%]`
- Background: `#FFFFFF`, border: `1px solid #E2E2EE`
- Border-radius: `14px` with `4px` top-left corner (chat tail)
- Font: 13.5px / `text-ink`

### User bubbles
- Right-aligned, `max-w-[75%]`
- Background: `#6B4EFF`, text: `#FFFFFF`
- Border-radius: `14px` with `4px` top-right corner
- Font: 13.5px

### Typing indicator
- Three dots inside an agent bubble shell
- Each dot: `w-2 h-2 rounded-full bg-ink-3`, pulse animation staggered by 150 ms

### Inline tags (agent bubble)
- Same pill style as existing source chips: `bg-[#EDE9FF] text-[#5A3FE0]`, `rounded-pill`, `text-[11px]`

### Quick-reply chips
- `border border-primary text-primary bg-white`, `rounded-pill`, `px-3 py-1`, `text-[12.5px] font-medium`
- On hover: `bg-primary-soft`
- Disappear after user selects one

### Input bar
- `border-t border-border`, `px-4 py-3`
- Input: `flex-1 text-[13px] outline-none placeholder-ink-3`
- Send button: `w-8 h-8 rounded-full bg-primary text-white grid place-items-center`
- Send icon: right-arrow chevron (existing `I.chevR`)

### Panel header
- Unchanged from current `AgentThinking`: shimmer gradient, Podium logo mark, status label, × dismiss

---

## Animations

| Event | Animation |
|-------|-----------|
| Panel mount | fade + translateY(10px → 0), 400 ms |
| Each message appears | fade + translateY(6px → 0), 320 ms (`step-animate`) |
| Typing indicator | three-dot pulse, staggered 150 ms per dot |
| Quick-reply chips appear | same `step-animate` as messages |
| Panel dismiss | fade + translateY(0 → -6px), 260 ms |

Reuse existing keyframes: `step-in`, `reveal`, `pulse-dot`.

---

## Interaction Details

- **Chip click**: appends user bubble with chip label text, hides chips, triggers typing → final agent message
- **Free-text send**: Enter key or send button click, same flow as chip click
- **Empty send**: no-op (send button disabled when input is empty)
- **Dismiss (×)**: sets `dismissed=true`, CSS transition plays, then `onDismiss()` callback removes component from parent
- **Thread scroll**: message area is `overflow-y-auto max-h-[260px]`; auto-scrolls to bottom on each new message via `useRef` + `scrollIntoView`

---

## What Does NOT Change

- `Sidebar`, `Topbar`, `IdeationCard`, stats grid, filter pills — untouched
- `AgentThinking` component definition can be removed entirely
- The `showAgent` / `setShowAgent` state in `IdeationListPage` is reused as-is

---

## Files Affected

- `screens/IdeationList.html` — replace `AgentThinking` component with `AgentChat`; no other files change
