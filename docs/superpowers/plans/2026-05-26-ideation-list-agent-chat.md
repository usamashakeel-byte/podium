# Conversational Agentic Flow — IdeationList Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the one-way `AgentThinking` component in `screens/IdeationList.html` with `AgentChat` — a chat bubble thread where the Podium Agent messages the user conversationally, asks a question with quick-reply chips, and responds to user input with a final recommendation and CTA.

**Architecture:** Single self-contained React component (`AgentChat`) with an internal state machine driving sequential agent messages, a typing indicator between turns, quick-reply chips, a free-text input bar, and auto-scrolling message thread. No new files — all changes are inside `screens/IdeationList.html`.

**Tech Stack:** React 18 (UMD/Babel, already in the file), Tailwind CSS (CDN config already in file), plain JS `setTimeout` for sequencing.

---

## File Map

| File | Action | Responsibility |
|------|--------|---------------|
| `screens/IdeationList.html` | Modify | Remove `AgentThinking` + all its sub-components and constants; add `AgentChat` and its sub-components in the same `<script type="text/babel">` block |

---

### Task 1: Remove `AgentThinking` and its supporting code

**Files:**
- Modify: `screens/IdeationList.html` (the second `<script type="text/babel">` block, lines ~86–255)

- [ ] **Step 1: Delete `THINKING_STEPS` constant**

Remove these lines entirely:
```js
const THINKING_STEPS = [
  { id:1, label:"Gathering information about your ideations…" },
  { id:2, label:"Searching sources for trending topics…" },
  { id:3, label:"Analysing engagement trends and audience fit…" },
];
```

- [ ] **Step 2: Delete `RECOMMENDATION` constant**

Remove these lines entirely:
```js
const RECOMMENDATION = {
  headline: "I found a high-impact opportunity for your pipeline.",
  body: "Based on your 4 active ideations...",
  tags: ["Enterprise AI","Eval-Driven Dev","Series B+"],
  cta: { label:"Generate Topics", href:"TopicGeneration.html" },
  meta: "Confidence: High · Sources: CIO.com, LinkedIn, Gartner Q1",
};
```

- [ ] **Step 3: Delete `CheckIcon` and `SpinnerIcon` components**

Remove:
```js
const CheckIcon = () => ( ... );
const SpinnerIcon = () => ( ... );
```

- [ ] **Step 4: Delete the entire `AgentThinking` component**

Remove the full component from `const AgentThinking = ({ onDismiss }) => {` through its closing `};` (approximately lines 116–254).

- [ ] **Step 5: Verify the page still renders**

Open `screens/IdeationList.html` in a browser. The page should load without errors — the agent panel will simply be gone. The stats cards, filter pills, and ideation cards must all still render correctly.

---

### Task 2: Add conversation script data and animation styles

**Files:**
- Modify: `screens/IdeationList.html`

- [ ] **Step 1: Add `AGENT_SCRIPT` constant**

In the second `<script type="text/babel">` block, immediately after `const { useState, useEffect, useRef } = React;`, add:

```js
const AGENT_SCRIPT = [
  {
    id: 1,
    text: "Hi Rohan, I'm reviewing your 4 active ideations…",
    tags: [],
    question: false,
  },
  {
    id: 2,
    text: "I found a high-impact opportunity. The Enterprise AI Infrastructure track has the highest relevance score (95) and 'production evals' is your most-clicked term over 30 days.",
    tags: ["Enterprise AI", "Eval-Driven Dev", "Series B+"],
    question: false,
  },
  {
    id: 3,
    text: "Want me to generate topics for this ideation, or explore a different one?",
    tags: [],
    question: true,
    chips: ["Generate Topics", "Explore Another"],
  },
];

const AGENT_FINAL = {
  text: "Great — generating topics for Enterprise AI Infrastructure now.",
  cta: { label: "Generate Topics", href: "TopicGeneration.html" },
  meta: "Confidence: High · Sources: CIO.com, LinkedIn, Gartner Q1",
};
```

- [ ] **Step 2: Add typing-dot animation to `<style>`**

In the `<style>` block in `<head>`, add after the existing `.thinking-bar` rules:

```css
@keyframes dot-bounce {
  0%, 80%, 100% { transform: translateY(0); opacity: .4; }
  40% { transform: translateY(-4px); opacity: 1; }
}
.dot-bounce { animation: dot-bounce 1.2s ease-in-out infinite; }
.dot-bounce:nth-child(2) { animation-delay: .15s; }
.dot-bounce:nth-child(3) { animation-delay: .3s; }
```

- [ ] **Step 3: Verify no browser errors**

Reload the page — no console errors expected. The constants are defined but not yet used.

---

### Task 3: Build `TypingBubble`, `AgentBubble`, and `UserBubble` sub-components

**Files:**
- Modify: `screens/IdeationList.html` (second babel script block, after `AGENT_FINAL`)

- [ ] **Step 1: Add `TypingBubble`**

```js
const TypingBubble = () => (
  <div className="flex items-end gap-2 mb-3">
    <div className="w-6 h-6 rounded-full shrink-0 flex items-center justify-center" style={{background:"#1A1A2E"}}>
      <svg viewBox="0 0 40 40" width="14" height="14" fill="none">
        <rect x="10" y="9" width="5" height="22" rx="1.5" fill="#FFF"/>
        <path d="M15 9h7a7 7 0 010 14h-7" stroke="#FFF" strokeWidth="5" strokeLinejoin="round" fill="none"/>
        <circle cx="27.5" cy="30.5" r="2.4" fill="#6B4EFF"/>
      </svg>
    </div>
    <div className="px-4 py-3 bg-white border border-border rounded-[14px] rounded-tl-[4px] flex items-center gap-1.5">
      <span className="w-2 h-2 rounded-full bg-ink-3 dot-bounce"/>
      <span className="w-2 h-2 rounded-full bg-ink-3 dot-bounce"/>
      <span className="w-2 h-2 rounded-full bg-ink-3 dot-bounce"/>
    </div>
  </div>
);
```

- [ ] **Step 2: Add `AgentBubble`**

```js
const AgentBubble = ({ msg, showCta }) => (
  <div className="flex items-end gap-2 mb-3 step-animate">
    <div className="w-6 h-6 rounded-full shrink-0 flex items-center justify-center" style={{background:"#1A1A2E"}}>
      <svg viewBox="0 0 40 40" width="14" height="14" fill="none">
        <rect x="10" y="9" width="5" height="22" rx="1.5" fill="#FFF"/>
        <path d="M15 9h7a7 7 0 010 14h-7" stroke="#FFF" strokeWidth="5" strokeLinejoin="round" fill="none"/>
        <circle cx="27.5" cy="30.5" r="2.4" fill="#6B4EFF"/>
      </svg>
    </div>
    <div className="max-w-[85%]">
      <div className="px-4 py-3 bg-white border border-border rounded-[14px] rounded-tl-[4px]">
        <p className="text-[13.5px] leading-relaxed text-ink">{msg.text}</p>
        {msg.tags && msg.tags.length > 0 && (
          <div className="flex flex-wrap gap-1.5 mt-2">
            {msg.tags.map(tag => (
              <span key={tag} className="px-2.5 py-0.5 rounded-pill text-[11px] font-medium"
                    style={{background:"#EDE9FF", color:"#5A3FE0"}}>{tag}</span>
            ))}
          </div>
        )}
      </div>
      {showCta && (
        <div className="mt-2 flex items-center justify-between px-1">
          <span className="mono text-[10.5px] text-ink-3">{AGENT_FINAL.meta}</span>
          <a href={AGENT_FINAL.cta.href}
             className="h-8 px-4 rounded-pill text-[12.5px] font-medium inline-flex items-center gap-1.5 text-white transition"
             style={{background:"#6B4EFF", boxShadow:"0 4px 10px -2px rgba(107,78,255,.40)"}}>
            {AGENT_FINAL.cta.label}
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
              <path d="M9 6l6 6-6 6"/>
            </svg>
          </a>
        </div>
      )}
    </div>
  </div>
);
```

- [ ] **Step 3: Add `UserBubble`**

```js
const UserBubble = ({ text }) => (
  <div className="flex justify-end mb-3 step-animate">
    <div className="max-w-[75%] px-4 py-3 rounded-[14px] rounded-tr-[4px] text-[13.5px] leading-relaxed text-white"
         style={{background:"#6B4EFF"}}>
      {text}
    </div>
  </div>
);
```

- [ ] **Step 4: Verify no browser errors**

Reload — no console errors. Components defined but not rendered yet.

---

### Task 4: Build `QuickReplies` and `InputBar` sub-components

**Files:**
- Modify: `screens/IdeationList.html` (after `UserBubble`)

- [ ] **Step 1: Add `QuickReplies`**

```js
const QuickReplies = ({ chips, onSelect }) => (
  <div className="flex flex-wrap gap-2 ml-8 mb-3 step-animate">
    {chips.map(chip => (
      <button key={chip} onClick={() => onSelect(chip)}
        className="h-8 px-4 rounded-pill text-[12.5px] font-medium border transition"
        style={{borderColor:"#6B4EFF", color:"#6B4EFF", background:"#FFFFFF"}}
        onMouseEnter={e => e.currentTarget.style.background="#EDE9FF"}
        onMouseLeave={e => e.currentTarget.style.background="#FFFFFF"}>
        {chip}
      </button>
    ))}
  </div>
);
```

- [ ] **Step 2: Add `InputBar`**

```js
const InputBar = ({ onSend }) => {
  const [val, setVal] = React.useState("");
  const send = () => {
    const trimmed = val.trim();
    if (!trimmed) return;
    onSend(trimmed);
    setVal("");
  };
  return (
    <div className="flex items-center gap-2 px-4 py-3 border-t border-border shrink-0">
      <input
        className="flex-1 text-[13px] outline-none bg-transparent placeholder-ink-3 text-ink"
        placeholder="Ask Podium Agent…"
        value={val}
        onChange={e => setVal(e.target.value)}
        onKeyDown={e => e.key === "Enter" && send()}
      />
      <button onClick={send} disabled={!val.trim()}
        className="w-8 h-8 rounded-full grid place-items-center transition shrink-0"
        style={{background: val.trim() ? "#6B4EFF" : "#E2E2EE"}}>
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="white" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
          <path d="M9 6l6 6-6 6"/>
        </svg>
      </button>
    </div>
  );
};
```

- [ ] **Step 3: Verify no browser errors**

Reload — no console errors.

---

### Task 5: Build the `AgentChat` parent component with state machine

**Files:**
- Modify: `screens/IdeationList.html` (after `InputBar`)

- [ ] **Step 1: Add `AgentChat` component**

```js
const AgentChat = ({ onDismiss }) => {
  const { useState, useEffect, useRef } = React;
  const [messages, setMessages] = useState([]);
  const [showTyping, setShowTyping] = useState(false);
  const [showChips, setShowChips] = useState(false);
  const [showInput, setShowInput] = useState(false);
  const [dismissed, setDismissed] = useState(false);
  const [phase, setPhase] = useState("idle");
  const threadRef = useRef(null);
  const timers = useRef([]);

  const after = (ms, fn) => {
    const t = setTimeout(fn, ms);
    timers.current.push(t);
  };

  const scrollBottom = () => {
    if (threadRef.current) {
      threadRef.current.scrollTop = threadRef.current.scrollHeight;
    }
  };

  const pushAgentMsg = (msg, withCta = false) => {
    setMessages(prev => [...prev, { type: "agent", msg, withCta }]);
  };

  const pushUserMsg = (text) => {
    setMessages(prev => [...prev, { type: "user", text }]);
  };

  useEffect(() => {
    // msg 1
    after(400,  () => setShowTyping(true));
    after(1400, () => { setShowTyping(false); pushAgentMsg(AGENT_SCRIPT[0]); });
    // msg 2
    after(1800, () => setShowTyping(true));
    after(2800, () => { setShowTyping(false); pushAgentMsg(AGENT_SCRIPT[1]); });
    // msg 3 (question)
    after(3200, () => setShowTyping(true));
    after(4200, () => {
      setShowTyping(false);
      pushAgentMsg(AGENT_SCRIPT[2]);
      after(300, () => { setShowChips(true); setShowInput(true); setPhase("question"); });
    });
    return () => timers.current.forEach(clearTimeout);
  }, []);

  useEffect(() => { scrollBottom(); }, [messages, showTyping, showChips]);

  const handleUserReply = (text) => {
    setShowChips(false);
    setShowInput(false);
    setPhase("replied");
    pushUserMsg(text);
    after(200,  () => setShowTyping(true));
    after(1200, () => { setShowTyping(false); pushAgentMsg(AGENT_FINAL, true); });
  };

  const handleDismiss = () => {
    setDismissed(true);
    after(260, () => onDismiss && onDismiss());
  };

  if (dismissed) return null;

  const isActive = phase === "idle" || phase === "question";

  return (
    <div className="mb-6 rounded-card border border-border bg-white shadow-card overflow-hidden"
         style={{transition:"opacity .26s,transform .26s", opacity: dismissed ? 0 : 1, transform: dismissed ? "translateY(-6px)" : "none"}}>

      {/* Header */}
      <div className="agent-shimmer flex items-center gap-3 px-5 py-3 border-b border-[#DDD8FF]">
        <div className="w-8 h-8 rounded-[9px] shrink-0 flex items-center justify-center" style={{background:"#1A1A2E"}}>
          <svg viewBox="0 0 40 40" width="22" height="22" fill="none">
            <rect x="10" y="9" width="5" height="22" rx="1.5" fill="#FFF"/>
            <path d="M15 9h7a7 7 0 010 14h-7" stroke="#FFF" strokeWidth="5" strokeLinejoin="round" fill="none"/>
            <circle cx="27.5" cy="30.5" r="2.4" fill="#6B4EFF"/>
          </svg>
        </div>
        <div className="flex-1 min-w-0">
          <div className="text-[13px] font-semibold text-ink leading-tight">Podium Agent</div>
          <div className="text-[11px] text-ink-2 leading-tight">
            {showTyping ? "Typing…" : phase === "replied" ? "Analysis complete" : "Thinking…"}
          </div>
        </div>
        <div className="shrink-0">
          {phase === "replied" && !showTyping && (
            <span className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-pill text-[11px] font-semibold" style={{background:"#D9F1E2",color:"#1E7E34"}}>
              <span className="w-1.5 h-1.5 rounded-full bg-success inline-block"/>Ready
            </span>
          )}
        </div>
        <button onClick={handleDismiss}
          className="w-7 h-7 rounded-input grid place-items-center text-ink-3 hover:text-ink hover:bg-lavender transition shrink-0 ml-1"
          title="Dismiss">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round">
            <path d="M18 6L6 18M6 6l12 12"/>
          </svg>
        </button>
      </div>

      {/* Message thread */}
      <div ref={threadRef} className="px-4 pt-4 overflow-y-auto" style={{maxHeight:260}}>
        {messages.map((m, i) =>
          m.type === "agent"
            ? <AgentBubble key={i} msg={m.msg} showCta={m.withCta}/>
            : <UserBubble key={i} text={m.text}/>
        )}
        {showTyping && <TypingBubble/>}
        {showChips && <QuickReplies chips={AGENT_SCRIPT[2].chips} onSelect={handleUserReply}/>}
      </div>

      {/* Input bar */}
      {showInput && <InputBar onSend={handleUserReply}/>}
    </div>
  );
};
```

- [ ] **Step 2: Replace `AgentThinking` with `AgentChat` in `IdeationListPage`**

In the `IdeationListPage` component, find:
```js
{showAgent && <AgentThinking onDismiss={() => setShowAgent(false)}/>}
```

Replace with:
```js
{showAgent && <AgentChat onDismiss={() => setShowAgent(false)}/>}
```

- [ ] **Step 3: Verify full flow in browser**

Open `screens/IdeationList.html`. Expected sequence:
1. Panel appears with shimmer header "Thinking…"
2. Typing dots appear (~400 ms after load)
3. First agent bubble: "Hi Rohan, I'm reviewing your 4 active ideations…" (~1 400 ms)
4. Second typing → second bubble with Enterprise AI text + purple tag chips (~2 800 ms)
5. Third typing → question bubble + two quick-reply chips + input bar (~4 200 ms)
6. Click "Generate Topics" chip → user bubble appears, chips/input hidden, typing → final agent bubble with CTA button
7. Click "Generate Topics" CTA → navigates to `TopicGeneration.html`
8. Click × → panel fades out

- [ ] **Step 4: Verify thread scrolls to bottom on new messages**

After the final message appears, the thread should be scrolled so the latest bubble is visible. If the thread overflows 260 px, the scroll position must be at the bottom.

- [ ] **Step 5: Verify send button disabled state**

In the input bar, the send button background should be `#E2E2EE` (grey) when the input is empty, and `#6B4EFF` (purple) when there is text. Pressing Enter with an empty input should do nothing.

- [ ] **Step 6: Commit**

```bash
git add "screens/IdeationList.html"
git commit -m "feat: replace AgentThinking with conversational AgentChat on IdeationList"
```

---

## Self-Review

**Spec coverage:**
- ✓ Chat bubble thread replacing AgentThinking — Task 1 removes old, Tasks 3–5 add new
- ✓ Agent opens proactively — `useEffect` sequence in Task 5
- ✓ Typing indicator between turns — `TypingBubble` in Task 3, `showTyping` state in Task 5
- ✓ Three agent messages + question — `AGENT_SCRIPT` in Task 2, sequenced in Task 5
- ✓ Inline tag chips on message 2 — `AgentBubble` renders `msg.tags` in Task 3
- ✓ Quick-reply chips — `QuickReplies` in Task 4, shown after question bubble
- ✓ Free-text input — `InputBar` in Task 4
- ✓ User bubble right-aligned purple — `UserBubble` in Task 3
- ✓ Final agent message + CTA — `AGENT_FINAL` + `showCta` prop in Task 3
- ✓ Auto-scroll on new messages — `scrollBottom` + `useEffect` in Task 5
- ✓ Dismiss with fade — `handleDismiss` + CSS transition in Task 5
- ✓ Header shimmer, logo, status label — header JSX in Task 5
- ✓ "Ready" badge after user replies — conditional in header JSX in Task 5

**Placeholder scan:** No TBDs, no "implement later", no vague steps. All code blocks are complete.

**Type consistency:**
- `AGENT_SCRIPT[2].chips` used in `QuickReplies` in Task 5 — defined in Task 2 ✓
- `AGENT_FINAL.cta.href` / `AGENT_FINAL.meta` used in `AgentBubble` in Task 3 — defined in Task 2 ✓
- `onDismiss` prop used in `handleDismiss` in Task 5 — matches `IdeationListPage` call site ✓
- `msg.tags`, `msg.text`, `msg.chips`, `msg.question` — all properties defined in `AGENT_SCRIPT` in Task 2 and consumed correctly in Tasks 3 & 5 ✓
