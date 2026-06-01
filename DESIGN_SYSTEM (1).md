# Design System

A shared component and token reference for building consistent UI across all products.  
Specs are extracted from Figma and expressed as primitive values with semantic role names.  
Any product, screen, or agent working on UI should treat this file as the single source of truth.

---

## How to use this file

### With an AI agent (Claude, Cursor, Copilot, etc.)

This file is the single source of truth for all visual decisions across products. When asking an agent to build or update any UI, start your prompt with:

```
Refer to DESIGN_SYSTEM.md and use only the tokens defined there — 
no values outside the file. [Your task here.]
```

**Examples:**

> "Refer to DESIGN_SYSTEM.md. Build a newsletter overview screen using the same layout rules, button variants, and table tokens defined there."

> "Refer to DESIGN_SYSTEM.md. The card on the analytics page needs to match the Card shell spec exactly — fix the padding and radius."

> "Refer to DESIGN_SYSTEM.md. Add a new section to the overview screen. Use the correct underline tab tokens for the tab bar."

The agent will read the token values directly from this file — colours, spacing, typography, corner radii, component states — and apply them without guessing or inventing new values.

---

### What the agent will use from this file

| You need | Agent reads from |
|---|---|
| Button styling | [Button](#button) → Variants table |
| Card layout and colours | [Card](#card) → Shell + Typography |
| Tab bar | [Tab](#tab) → Underline tab or Pill tab |
| Data table | [Table](#table) → Header row + Data row |
| Page structure | [Page Layout](#page-layout) → Content area + Heading row |
| Sidebar behaviour | [Sidebar](#sidebar) |
| Any colour, size, or radius | [Foundation](#foundation) |

---

### For developers reading it manually

- Every **token name** (e.g. `black-90`, `gap-xl`, `radius-lg`) maps to a raw value in the Foundation section.
- Every **component section** (Button, Card, Tab, etc.) uses only those foundation tokens — no one-off values.
- If a value isn't in this file, it isn't part of the design system yet. Add it here before using it in code.
- These tokens apply across all products — don't create product-specific overrides without updating this file.
- When Figma and this doc conflict, **Figma wins**. Update the doc to match.

---

## Table of Contents

1. [Foundation](#foundation)
2. [Button](#button)
3. [Card](#card)
4. [Tab](#tab)
5. [Table](#table)
6. [Sidebar](#sidebar)
7. [Page Layout](#page-layout)
8. [Preview Routes](#preview-routes)

---

## Foundation

Shared design decisions that all components inherit.

### Typography

| Role | Family | Weight | Size | Line-height |
|---|---|---|---|---|
| Label / UI text | Inter | 500 | 14px | 16–20px |
| Title | Inter | 600 | 16px | 22px |
| Stat value | Inter | 500 | 24px | 32px |
| Badge / meta | Inter | 400–500 | 10–14px | 16–20px |

### Colour palette (primitives)

| Token | Value | Usage |
|---|---|---|
| `black-90` | `rgba(0,0,0,0.9)` | Primary text, primary button bg |
| `black-70` | `rgba(0,0,0,0.7)` | Body text, secondary labels |
| `black-50` | `rgba(0,0,0,0.5)` | Meta text, table header labels |
| `black-12` | `rgba(0,0,0,0.12)` | Borders (buttons, cards, table rows) |
| `black-08` | `rgba(0,0,0,0.08)` | Subtle dividers (table rows) |
| `white` | `#ffffff` | Secondary button bg, card bg (hover) |
| `surface` | `#f7f7f7` | Tertiary button bg, pill tab active bg |
| `ghost` | `#fefcfa` | Ghost button bg |

### Corner radius

| Scale | Value | Used by |
|---|---|---|
| `xs` | 8px | Expand button (table) |
| `sm` | 12px | Card badge, table container |
| `md` | 16px | Table briefing card |
| `lg` | 32px | Buttons, pill tabs, action buttons |
| `full` | 9999px | Avatars, count badges |

### Spacing

| Token | Value | Used by |
|---|---|---|
| `gap-xs` | 4px | Icon → label (chips) |
| `gap-sm` | 8px | Button icon gap, tab gap, expand → date |
| `gap-md` | 12px | Table col gap, card meta row gap |
| `gap-lg` | 24px | Card stat columns |
| `gap-xl` | 32px | Table row padding-x |

---

## Button

**Figma node:** `1359:11327`  
**Preview:** `/preview/button`

All variants share the same geometry. Only fill, border, and text/icon colour differ.

### Shared geometry

| Token | Value | Semantic |
|---|---|---|
| Height | 36px | `btn/height` |
| Corner radius | 32px | `btn/corner-radius` |
| Padding | T8 B8 L16 R16 | `btn/inner-spacing` |
| Icon → label gap | 8px | `btn/icon-label-gap` |
| Font | Inter 500 14px lh=16 | `btn/label-font` |

### Variants

| Variant | Background | Border | Text | Icon |
|---|---|---|---|---|
| **Primary** | `rgba(0,0,0,0.9)` | none | `#ffffff` | `#ffffff` |
| **Secondary** | `#ffffff` | `1px rgba(0,0,0,0.12)` | `rgba(0,0,0,0.9)` | `rgba(0,0,0,1)` |
| **Tertiary** | `#f7f7f7` | none | `rgba(0,0,0,0.9)` | `rgba(0,0,0,1)` |
| **Ghost** | `#fefcfa` | none | `rgba(0,0,0,0.9)` | `rgba(0,0,0,1)` |

### Usage guidance

- Use **Primary** for the single most important action per view (create, submit).
- Use **Secondary** when a bordered button is needed alongside Primary.
- Use **Tertiary** for low-emphasis actions (filter, sort) on light surfaces.
- Use **Ghost** for cancel or dismiss actions.

---

## Card

**Figma nodes:** `1795:55107` (default) · `1795:55108` (hover)  
**Preview:** `/preview/card`

### Shell

| Token | Value | Semantic |
|---|---|---|
| Dimensions | 387 × 271px | `card/size` |
| Corner radius | 32px | `card/corner-radius` |
| Background | `#f7f7f7` | `card/background` |
| Padding | T20 B20 L24 R24 | `card/inner-spacing` |
| Hover overlay | `rgba(0,0,0,0.02)` inset | `card/hover-overlay` |

### Status badge

| Token | Value | Semantic |
|---|---|---|
| Size | 36 × 36px | `card-badge/size` |
| Corner radius | 12px | `card-badge/corner-radius` |
| Background | `#dceedd` | `card-badge/background` |
| Icon colour | `#3c7702` | `card-badge/icon-color` |

### Typography inside card

| Element | Font | Colour |
|---|---|---|
| Title | Inter 600 16px lh=22 ls=−0.2 | `rgba(0,0,0,0.9)` |
| Meta text | Inter 400 14px lh=20 | `rgba(0,0,0,0.5)` |
| Stat value | Inter 500 24px lh=32 | `rgba(0,0,0,0.9)` |
| Stat label | Inter 500 14px lh=19.6 | `rgba(0,0,0,0.5)` |
| Timestamp | Inter 400 14px lh=20 | `rgba(0,0,0,0.7)` |

### Stat divider

| Token | Value | Semantic |
|---|---|---|
| Colour | `rgba(0,0,0,0.12)` | `card-stat/divider-color` |
| Width | 1px vertical | `card-stat/divider-width` |
| Column gap | 32px on each side | `card-stat/col-gap` |

### Hover state differences

| Element | Default | Hover |
|---|---|---|
| Background | `#f7f7f7` | `#f7f7f7` + `rgba(0,0,0,0.02)` overlay |
| Badge + actions | Badge alone, full width | Badge + 2 icon buttons in a horizontal row |
| Meta icons | `rgba(0,0,0,0.5)` | `rgba(0,0,0,0.32)` |
| Action buttons | Hidden | 2 × 28px, r=32, icon `rgba(0,0,0,0.5)` |

---

## Tab

**Figma nodes:** `1359:11253` (underline) · `1925:9011` (pill / nav)  
**Preview:** `/preview/tab`

### Underline tab

Used inside page content areas (e.g. All Content page tabs).

#### Geometry

| Token | Value | Semantic |
|---|---|---|
| Height | 40px | `underline-tab/height` |
| Padding | T12 B12 L8 R8 | `underline-tab/inner-spacing` |
| Icon → label gap | 8px | `underline-tab/icon-label-gap` |
| Font | Inter 500 14px lh=16 | `underline-tab/label-font` |

#### States

| State | Bottom border | Text | Icon |
|---|---|---|---|
| Active | `1px rgba(0,0,0,0.9)` | `rgba(0,0,0,0.9)` | `rgba(0,0,0,1)` |
| Default | `1px rgba(0,0,0,0.5)` | `rgba(0,0,0,0.5)` | `rgba(0,0,0,0.5)` |

#### Count badge

| Token | Value | Semantic |
|---|---|---|
| Size | 20 × 20px | `underline-tab-badge/size` |
| Corner radius | 100px (pill) | `underline-tab-badge/radius` |
| Background | `rgba(0,0,0,0.08)` | `underline-tab-badge/background` |
| Font | Inter 600 10px | `underline-tab-badge/font` |
| Text colour | `rgba(0,0,0,0.5)` | `underline-tab-badge/color` |

---

### Pill tab (nav)

Used in the sidebar navigation and top-level nav rails.

#### Geometry

| Token | Value | Semantic |
|---|---|---|
| Height | 32px | `pill-tab/height` |
| Corner radius | 32px | `pill-tab/corner-radius` |
| Padding | T8 B8 L20 R20 | `pill-tab/inner-spacing` |
| Icon → label gap | 8px | `pill-tab/icon-label-gap` |
| Font | Inter 500 14px lh=16 | `pill-tab/label-font` |

#### States

| State | Background | Text | Icon |
|---|---|---|---|
| Default | transparent | `rgba(0,0,0,0.6)` | `rgba(0,0,0,0.6)` |
| Hover | `#ffffff` + `rgba(0,0,0,0.06)` shadow | `rgba(0,0,0,1)` | `rgba(0,0,0,0.9)` |
| Active | `#f7f7f7` | `rgba(0,0,0,1)` | `rgba(0,0,0,0.9)` |

---

## Table

**Figma node:** `1913:33001`  
**Preview:** `/preview/table`

### Header row

| Token | Value | Semantic |
|---|---|---|
| Height | 44px | `table-header/height` |
| Padding | T12 B12 L32 R32 | `table-header/inner-spacing` |
| Column gap | 12px | `table-header/col-gap` |
| Font | Inter 500 14px lh=20 | `table-header/label-font` |
| Text colour | `rgba(0,0,0,0.5)` | `table-header/label-color` |
| Bottom border | `1px rgba(0,0,0,0.08)` | `table-header/divider` |

### Column widths

| Column | Width |
|---|---|
| Date generated | 332px |
| Triggered by | 282px |
| Focus areas generated | 251px |
| Actions | 121px |

### Data row

| Token | Value | Semantic |
|---|---|---|
| Height | 60px | `table-row/height` |
| Background | `#ffffff` | `table-row/background` |
| Bottom border | `1px rgba(0,0,0,0.08)` | `table-row/divider` |
| Padding | T12 B12 L32 R32 | `table-row/inner-spacing` |
| Column gap | 12px | `table-row/col-gap` |

### Expand button

| Token | Value | Semantic |
|---|---|---|
| Size | 24 × 24px | `table-expand/size` |
| Corner radius | 8px | `table-expand/corner-radius` |
| Background | `#ffffff` | `table-expand/background` |
| Border | `1px rgba(0,0,0,0.12)` | `table-expand/border` |
| Icon colour | `rgba(0,0,0,0.9)` | `table-expand/icon-color` |

### Triggered-by avatars

| Variant | Size | Background | Text / icon |
|---|---|---|---|
| Automatic | 30 × 30px r=100% | `rgba(230,230,230,1)` border `rgba(0,0,0,0.12)` | Brand mark `rgba(32,32,32,1)` |
| User | 28 × 28px r=100% | `rgba(117,192,167,0.32)` | Initials Inter 500 12px `rgba(20,88,67,1)` |

### "View briefing" action button

| Token | Value | Semantic |
|---|---|---|
| Size | 121 × 36px | `table-action-btn/size` |
| Corner radius | 32px | `table-action-btn/corner-radius` |
| Background | `#ffffff` | `table-action-btn/background` |
| Border | `1px rgba(0,0,0,0.12)` | `table-action-btn/border` |
| Padding | T8 B8 L16 R16 | `table-action-btn/inner-spacing` |
| Font | Inter 500 14px lh=16 | `table-action-btn/label-font` |
| Text colour | `rgba(0,0,0,0.9)` | `table-action-btn/label-color` |

---

## Sidebar

**Reference implementation:** `src/components/Sidebar.tsx`  
**Preview:** `/preview/sidebar`

### Layout

| State | Width | Trigger |
|---|---|---|
| Collapsed | 56px | Default / mouse leave |
| Expanded | 240px | Mouse enter (hover) |

Transition: `all 300ms ease-in-out`

### Logo bar

| Token | Value |
|---|---|
| Height | 48px (h-12) |
| Border | Bottom 1px `border-border` |
| Label (expanded) | Product name — Inter 700 14px `black-90` |
| Label (collapsed) | First letter of product name — same style |

### Nav item

| State | Padding | Text | Background |
|---|---|---|---|
| Collapsed | `px-0 py-2` centred | — | — |
| Expanded | `px-4 py-2` | 13px 500 | — |
| Active | Same + left indicator | `text-primary` | `bg-primary/5` |
| Hover | Same | `text-foreground` | `bg-muted/50` |

Active indicator: `2px × 20px`, rounded-right, `bg-primary`, absolutely positioned left edge.

### Icon size

| Element | Size |
|---|---|
| Nav icon | 16 × 16px (w-4 h-4) |
| Chevron (sub-items) | 12 × 12px (w-3 h-3) |
| Bell (notifications) | 20 × 20px (w-5 h-5) |
| User avatar | 28 × 28px (w-7 h-7) |

### Badges

| Badge | Expanded | Collapsed |
|---|---|---|
| Unread notifications | Red circle `#ef4444`, white text 10px bold | Dot `w-2 h-2` |
| Agent queue (pipeline / plan) | Amber pill `bg-amber-100 text-amber-700`, 10px 500 | Amber dot `w-2 h-2` |

### Sub-menu

- Animated: `max-h-0 opacity-0` → `max-h-[500px] opacity-100` over 200ms ease-in-out
- Sub-item indent: `pl-10`
- Sub-item font: 12px, `text-muted-foreground` / `text-primary` active

### Role switcher (dual-role users)

| State | Appearance |
|---|---|
| Expanded | Pill toggle inside `bg-muted` container, active tab `bg-primary text-primary-foreground` shadow-sm |
| Collapsed | 28px circle `bg-primary/10 text-primary`, shows "E" or "M", click toggles role |

---

## Page Layout

Rules for how content pages are structured inside the main viewport (excludes the sidebar shell).

### Content area

| Token | Value | Notes |
|---|---|---|
| Padding | `40px 32px` | Top 40px, left/right 32px — no `maxWidth` centering |
| Background | `#ffffff` | Full-width white canvas |

> Do **not** add `max-width` + `margin: auto` to the main content wrapper. Content should fill the available width so tables, cards, and grids use the full viewport naturally.

### Page heading row

The heading row sits at the top of every content section. Title and primary actions always share the same horizontal line.

| Slot | Position | Contents |
|---|---|---|
| Left | `flex: 1` | Page title (Inter 600 20px `black-90`) + status badge if applicable |
| Right | `flex-shrink: 0` | Primary action button, then Secondary, then Ghost — in that order |

Layout: `display: flex; align-items: center; justify-content: space-between`

**Example:**
```
[Page title]  [Status badge]  ─────────────────  [+ Primary action]  [Secondary]  [More]
```

### Breadcrumb

Sits above the heading row. Uses `gap-xs` (4px) between segments.

| Element | Font | Colour |
|---|---|---|
| Parent segment | Inter 400 13px | `black-50` |
| Separator | ChevronRight 14px | `black-32` |
| Current segment | Inter 500 13px | `black-90` |

---

## Preview Routes

All routes are standalone (outside `AppLayout`) — no sidebar, no nav shell.

| Route | Component | Figma node |
|---|---|---|
| `/preview/button` | ButtonPreview | `1359:11327` |
| `/preview/card` | CardPreview | `1795:55107`, `1795:55108` |
| `/preview/tab` | TabPreview | `1359:11253`, `1925:9011` |
| `/preview/table` | TablePreview | `1913:33001` |
| `/preview/sidebar` | SidebarPreview | Sidebar |
| `/preview/podcast` | PodcastOverview | Composite screen — content overview |
| `/preview/call-qa` | CallQADashboard | Composite screen — QA dashboard |

> **Note:** Preview routes are only available in development (`npm run dev`). They are not linked from any nav and will not appear in production builds.

---

*Source of truth: Figma file `tjd0T3I2FSDO9ZhdhrYB1y` (Revsphere). Applies across all products. When Figma and this doc conflict, Figma wins.*
