# Screens — Context & Edit Guide

This single file consolidates the per-screen context so you can read only this file and get complete context for the `screens/` folder. Each entry includes: one-line purpose, key constants/data, main components, and edit hotspots (exact names to change).

---

## screens/BrandVoice.html
- Purpose: Brand voice / tone editor (manage voices, principles, audience segments).
- Key constants/data: `CHANNELS`, `TONE_TRAITS`, `SEED_VOICES`, `DEFAULT_PRINCIPLES`, `KB_TABS`, `AUDIENCE_SEGMENTS`.
- Main components: `VoiceEditor`, `VoiceCard`, `LiveSummary`.
- Hotspots / edit points:
  - Edit `SEED_VOICES` to add or change example voices.
  - Change `DEFAULT_PRINCIPLES` to modify default saved principles.
  - Update `VoiceEditor` save handler to persist differently.

---

## screens/BriefDetail.html
- Purpose: Edit a single brief with inline editing and assistant panel.
- Key constants/data: `INIT_QUESTIONS`, `INIT_AREAS`, `PERSONA_RESEARCH_ANGLES`.
- Main components: `InlineEdit`, `EditableList`, `BriefAgent`, `QuestionSectionHeader`.
- Hotspots / edit points:
  - Modify `INIT_QUESTIONS` or `INIT_AREAS` to change primary brief sections.
  - Adjust `InlineEdit` to change validation or content types.
  - Update assistant (`BriefAgent`) prompts and callbacks.

---

## screens/BriefList.html
- Purpose: List briefs and create new briefs using a modal.
- Key constants/data: `BRIEFS`, `APPROVED_EPISODES`, `STATUS_STYLE`.
- Main components: `BriefCard`, `NewBriefModal`, filter controls.
- Hotspots / edit points:
  - Edit `BRIEFS` to seed list entries.
  - Modify `NewBriefModal` creation and validation flow.
  - `STATUS_STYLE` controls color mapping for status pills.

---

## screens/CMDashboard.html
- Purpose: Content Marketer dashboard (action cards and AI suggestions).
- Key constants/data: `INITIAL_ACTIONS`, `SUGGESTIONS`, `WORKFLOW`.
- Main components: `ActionCard`, `SuggestionCard`, `AgentBanner`, `WorkflowStep`.
- Hotspots / edit points:
  - Edit `INITIAL_ACTIONS` to change dashboard tiles.
  - Update `SUGGESTIONS` seed items.
  - Wire CTAs to other screens via handlers.

---

## screens/Configuration.html
- Purpose: Configuration landing page (links to Brand Library, Hosts, etc.).
- Key constants/data: small presentational arrays inside file.
- Main components: `ConfigCard`, shared `Sidebar`/`Topbar`.
- Hotspots / edit points:
  - Edit config cards array to add/remove links.

---

## screens/EpisodeDetail.html
- Purpose: Episode detail with AI guest persona and host recommendations.
- Key constants/data: `EPISODE`, `AI_RECOMMENDATION`, `STATUS_STYLE`.
- Main components: `RecommendationCard`, `FitBadge`/`FitMeter`, `HostUploadPanel`, `GuestProfilePhoto`.
- Hotspots / edit points:
  - Modify `AI_RECOMMENDATION` to change suggested personas/hosts/briefPlan.
  - Update host upload/save handlers to change persistence.
  - Edit CTA handler for "Lock Guest and Generate Brief".

---

## screens/EpisodeTopics.html
- Purpose: Manage topic groups and episodes; add/edit episodes; send revisions for approval.
- Key constants/data: `TOPIC_GROUPS` (array of topic groups with `episodes`), `AI_EPISODE_ADDITIONS`, `FILTERS`, `SEG_COLOR`, `STATUS_STYLE`.
- Main components: `TopicGroup`, `EpisodeRow`, `TopicEditor`, `RevisionPanel`.
- Hotspots / edit points:
  - Change `TOPIC_GROUPS` to add/remove topics or edit seed episodes. Structure: `topic.id`, `topic.name`, `topic.episodes[]` (each episode has `id`, `title`, `status`, etc.).
  - Edit `AI_EPISODE_ADDITIONS` to alter AI-suggested episodes.
  - Modify functions that create revisions or change episode status (send for approval).

---

## screens/Hosts.html
- Purpose: Manage host profiles used by AI and assignment flows.
- Key constants/data: `SEED_HOSTS`, `EMPTY_HOST`, `TONES`.
- Main components: `HostCard`, `HostForm`, `ReadinessMeter`.
- Hotspots / edit points:
  - Edit `SEED_HOSTS` to add host data or sample avatars.
  - Modify `HostForm` save handler to change persistence or validations.

---

## screens/IdeationForm.html
- Purpose: Conversational ideation (collect segment, audience, pain points, context) that feeds TopicGeneration.
- Key constants/data: `SEGMENTS`, `IDEATION_SEGMENT_SUGGESTIONS`, `CONV` (conversation steps array).
- Main components: `ConvAgent`, `FormSummary`, `TagInput`, `StepBar`.
- Hotspots / edit points:
  - Edit `CONV` prompts to change questions and mapping into `formData`.
  - Modify `SEGMENTS` suggestions or default selections.

---

## screens/IdeationList.html
- Purpose: Appears to be a bundler/manifest/loader variant — likely a build artifact, not canonical source.
- Note: Avoid editing unless you identify the canonical source file.

---

## screens/MMReviewDetail.html
- Purpose: Manager review detail for ideation/briefs, with approve/reject decision UI.
- Key constants/data: `REVIEW_DETAILS` (map keyed by item id with payloads), `STATUS_STYLE`.
- Main components: `DecisionPanel`, `HostDetailModal`, `PersonaDetailModal`, `GuestDetailModal`.
- Hotspots / edit points:
  - Edit `REVIEW_DETAILS` to change sample review items and modal content.
  - Modify `DecisionPanel` handlers to change approval/rejection logic.

---

## screens/RecordingBriefLink.html
- Purpose: Link recordings to briefs using a brief picker.
- Key constants/data: `RECORDINGS`, `AVAILABLE_BRIEFS`, `INIT_LINKS`, `FILTER_TABS`.
- Main components: `RecordingRow`, `BriefPickerModal`.
- Hotspots / edit points:
  - Edit `AVAILABLE_BRIEFS` or `INIT_LINKS` to change seeded mapping.
  - Update `doLink`/`doUnlink` handlers for persistence.

---

## screens/RecordingDetail.html
- Purpose: Bundler/unpacking scaffold (uses DOMParser + manifest injection) — not a simple React page.
- Note: Likely a build artifact. Do not edit unless you know the build pipeline.

---

## screens/RecordingsList.html
- Purpose: Recordings index + upload pair modal (host/guest + transcript pairing + link to briefs).
- Key constants/data: `BRIEFS_DATA`, `INIT_RECORDINGS`, `PAGE_SIZE`.
- Main components: `UploadPairModal`, `RecordingCard`, pagination.
- Hotspots / edit points:
  - Edit `INIT_RECORDINGS` to change seeded recordings.
  - `UploadPairModal` handles uploads and transcript parsing — change validation or pairing logic here (see `hasAssetMismatch`).

---

## screens/Settings.html
- Purpose: Settings (users, roles, SSO, audit) and also acts as a shell exporting shared UI primitives.
- Key constants/data: `USERS`, `ROLES`, `STATUS_PILL` mapping.
- Main components: `UsersTable`, `RoleCard`, shared components exported to `window` (e.g., `Icon`, `Logo`, `Avatar`, `Sidebar`, `Topbar`).
- Hotspots / edit points:
  - Modify `USERS` and `ROLES` seeds.
  - Use exported primitives as canonical shared chrome across screens.

---

## screens/TopicGeneration.html
- Purpose: Topic planning and episode generation (consumes Ideation form outputs).
- Key constants/data: `TOPICS`, `TOPIC_PLANS`, `planEpisode()` helper, `selections` state shape.
- Main components: `TopicGenerationPage`, `EpisodePreview`, `StepBar`.
- Hotspots / edit points:
  - Edit `TOPICS` or `TOPIC_PLANS` seed arrays.
  - Change `planEpisode()` to alter episode construction logic.

---

## screens/extra/BriefReady.html
- Purpose: Small brief-ready view with share link and editable lists.
- Key constants/data: small brief/session seeds.
- Main components: `CopyLinkPill`, `EditableGeneratedList`, `InlineEdit`.
- Hotspots / edit points:
  - `CopyLinkPill` uses `navigator.clipboard` (update UX or fallback behavior).

---

## screens/extra/SocialContentBuilder.html
- Purpose: Generate platform-specific social content per recording/brief.
- Key constants/data: `SEED_SESSIONS`, `RECORDINGS`, `CONTENT_REC001/002`, `TABS` with char limits.
- Main components: `BriefContextCard`, `SessionList`, generator flow.
- Hotspots / edit points:
  - Session shape (`session.content` keys: notes,youtube,linkedin,twitter,instagram) — edit generation or char limits.

---

## screens/extra/Studio.html
- Purpose: Studio for clip generation & editing.
- Key constants/data: `STUDIO_RECORDING`, `TRANSCRIPT`, `VIRAL_TITLES`, `INIT_CLIPS`, `LAYOUTS`.
- Main components: `ClipCard`, `ClipTimeline`, `generateMore()`.
- Hotspots / edit points:
  - `generateMore()` logic and clip seeds in `INIT_CLIPS`.

---

## screens/extra/TopicReview.html
- Purpose: Redirect page to `TopicGeneration.html` (meta refresh + JS replace).
- Hotspots: None significant.

---

## Notes & recommendations
- Many files embed seed data arrays (e.g., `TOPIC_GROUPS`, `AI_RECOMMENDATION`, `SEED_HOSTS`, `RECORDINGS`). To change default demo content, edit those constants inside the appropriate HTML file.
- A few files are bundler scaffolds (e.g., `RecordingDetail.html`, `IdeationList.html`) — avoid editing these unless you're working with the build system.
- `Settings.html` exports shared UI primitives which are used across screens. Consider centralizing these primitives into a single shared JS file if you plan refactors.

---

## How to use this file
- Open the specific `screens/<name>.html` file listed above and use the Hotspots section to find the exact constant or component to edit.
- If you want me to make a specific change (example: "Add a new host to `SEED_HOSTS` in `Hosts.html`"), tell me the exact edit and I will apply a patch.

---

Generated: 30 May 2026
