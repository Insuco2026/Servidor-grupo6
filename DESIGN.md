---
name: Kernel Console
colors:
  surface: '#0d1322'
  surface-dim: '#0d1322'
  surface-bright: '#333949'
  surface-container-lowest: '#080e1d'
  surface-container-low: '#151b2b'
  surface-container: '#191f2f'
  surface-container-high: '#242a3a'
  surface-container-highest: '#2f3445'
  on-surface: '#dde2f7'
  on-surface-variant: '#bbcac0'
  inverse-surface: '#dde2f7'
  inverse-on-surface: '#2a3040'
  outline: '#86948a'
  outline-variant: '#3c4a42'
  surface-tint: '#4edea3'
  primary: '#6ffbbe'
  on-primary: '#003824'
  primary-container: '#4edea3'
  on-primary-container: '#005f40'
  inverse-primary: '#006c4a'
  secondary: '#4cd7f6'
  on-secondary: '#003640'
  secondary-container: '#03b5d4'
  on-secondary-container: '#00424e'
  tertiary: '#d6e6db'
  on-tertiary: '#26332c'
  tertiary-container: '#bacabf'
  on-tertiary-container: '#47554d'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#6ffbbe'
  primary-fixed-dim: '#4edea3'
  on-primary-fixed: '#002114'
  on-primary-fixed-variant: '#005236'
  secondary-fixed: '#acedff'
  secondary-fixed-dim: '#4cd7f6'
  on-secondary-fixed: '#001f26'
  on-secondary-fixed-variant: '#004e5c'
  tertiary-fixed: '#d7e6db'
  tertiary-fixed-dim: '#bbcac0'
  on-tertiary-fixed: '#111e18'
  on-tertiary-fixed-variant: '#3c4a42'
  background: '#0d1322'
  on-background: '#dde2f7'
  surface-variant: '#2f3445'
  surface-base: '#0d1322'
  border-subtle: '#3c4a42'
  text-primary: '#dde2f8'
  text-secondary: '#bbcabf'
  accent-terminal: '#4edea3'
  accent-cyan: '#4cd7f6'
  status-error: '#ff6e6e'
  status-warning: '#f5a623'
typography:
  headline-xl:
    fontFamily: Inter
    fontSize: 44px
    fontWeight: '700'
    lineHeight: 52px
  headline-xl-mobile:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
  headline-lg-mobile:
    fontFamily: Inter
    fontSize: 26px
    fontWeight: '600'
    lineHeight: 34px
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  headline-sm:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '600'
    lineHeight: 26px
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 26px
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 22px
  body-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 18px
  code-lg:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 22px
  code-md:
    fontFamily: JetBrains Mono
    fontSize: 13px
    fontWeight: '400'
    lineHeight: 20px
  label-md:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.05em
  label-sm:
    fontFamily: JetBrains Mono
    fontSize: 11px
    fontWeight: '500'
    lineHeight: 14px
    letterSpacing: 0.08em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  gutter: 1.5rem
  gutter-mobile: 1rem
  margin: 2rem
  margin-mobile: 1rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 1rem
  space-lg: 1.5rem
  space-xl: 2.5rem
  space-2xl: 4rem
---

## Brand & Style

This design system embodies a specialized, high-precision technical interface tailored for Linux systems engineering, systems administration, and server lab documentation. Rooted in terminal ergonomics and industrial computing aesthetics, it balances mission-critical utility with modern developer ergonomics.

The visual style is **Developer/Console Dark Modern**:
- **Atmosphere:** Deep obsidian navy foundation layered with slate terminal containers, precision hairline framing, and CRT/phosphor-inspired chromatic accents.
- **Personality:** Methodical, authoritative, low-distraction, and structurally explicit. Visual noise is minimized to prioritize command syntax, packet flows, network topology, and procedural logs.
- **Target Audience:** Systems engineers, DevOps practitioners, Linux administrators, and computing students working with infrastructure configuration, Bash routines, and network daemons.
- **Emotional Intent:** Reliability, total command-line authority, and immediate clarity during critical server deployments and diagnostics.

## Colors

The palette employs a deep-space navy base with tiered slate-blue containers, punctuated by phosphor terminal green and high-frequency network cyan:

- **Primary Accent (`#4edea3` — Terminal Emerald):** Reserved for execution points, active services, positive validations (`active (running)`), key copy triggers, and primary actions.
- **Secondary Accent (`#4cd7f6` — Tech Cyan):** Signals network interfaces (`enp0s3`), protocols (SSH/HTTP), routes, hostnames, and secondary analytical points.
- **Tertiary Token (`#3c4a42` — Steel Moss Border):** The defining 1px hairline boundary color providing crisp architectural containment without harshness.
- **Surface Elevation Hierarchy:**
  - `surface-base` (`#0d1322`): Canvas background and body backdrop.
  - `surface-container-low` (`#151b2b`): Broad section areas, tables, and side rails.
  - `surface-container` (`#191f2f`): Default card modules, interactive blocks, and form panels.
  - `surface-container-high` (`#242a3a`): Code terminals, elevated modal layers, and header bars.
- **Text Hierarchy:**
  - `text-primary` (`#dde2f8`): High-legibility cool white for core reading content, titles, and active inputs.
  - `text-secondary` (`#bbcabf`): Muted sage gray for descriptions, metadata, author labels, and passive annotations.

## Typography

Typography establishes an intentional dual-axis discipline:
1. **Structural & Editorial Core (`Inter`):** Handles section heads, overarching context, instructions, and theoretical explanations. It provides clean sans-serif neutral geometry with optical weight adjustments.
2. **Technical & Execution Rigor (`JetBrains Mono`):** Strictly deployed for code bodies, file paths (`/etc/netplan/...`), port indicators (`80/tcp`), IP designations (`192.168.196.150/24`), terminal commands, and metadata telemetry badges.

All monospace text uses uppercase treatment or subtle letter-spacing when serving as classification tags, while retaining case-exact syntax inside code blocks.

## Layout & Spacing

This layout embraces a desktop-first, widescreen command-center posture with a 12-column modular rhythm:
- **Maximum Width:** Confined to `max-w-7xl` (1280px) to prevent excessive text line lengths while facilitating rich side-by-side technical grids.
- **Section Rhythm:** Sections are partitioned by `space-2xl` (4rem / 64px) vertically, bounded by hairline rules or tonal shifts to reinforce modular chapters.
- **Grid Modular Logic:**
  - *2-Column:* Hero intro, core concept contrasts, dual-step split views.
  - *3-Column:* Evidence cards, diagnostic breakdown panels, architecture fundamentals.
  - *4-Column:* Key telemetry stats (Hostname, User, IP, Gateway) and concise milestone objectives.
- **Breakpoints:**
  - Desktop: `1024px` to `1440px` (primary operational tier).
  - Tablet: `768px` to `1023px` (folds 4-column metrics to 2x2, maintains 2-column cards).
  - Mobile: `< 768px` (stacks grids cleanly while preserving full terminal code block width without horizontal window blowout).

## Elevation & Depth

In a technical console environment, physical drop shadows feel out of place. Hierarchy is articulated via **Tonal Layering**, **Crisp Structural Borders**, and **Frosted Backdrops**:

- **Hairline Framing (1px Borders):** Every card, panel, table row, and terminal header is bound by a precise `1px solid #3c4a42` border. This brings CAD-like clarity to all components.
- **Tonal Stepping:**
  - Base layer `#0d1322` remains static.
  - Structural cards step up to `#151b2b` or `#191f2f`.
  - Nested code areas, inputs, and selected states ascend to `#242a3a`.
- **Top Navigation Glass Effect:** The sticky header uses `#0d1322` with a `90%` alpha channel paired with a `backdrop-blur-md` (12px blur) to maintain screen position without obscuring document content during fast scrolling.
- **Accent Glows:** Hovering over interactive cards or focusing terminal inputs produces an intentional low-spread phosphor aura: `box-shadow: 0 0 12px rgba(78, 222, 163, 0.15)`.

## Shapes

The interface embraces a **Soft Industrial Geometry (Level 1)**:
- Standard UI containers, cards, tables, and code snippets use `rounded` (0.25rem / 4px) to retain an authentic console feel without sharp raw brutalism.
- Larger feature containers and modals employ `rounded-lg` (0.5rem / 8px).
- Badges and status pills utilize pill-style rounding or subtle 4px box corners to echo terminal command line switches (e.g., `--status=active`).

## Components

### Buttons
- **Primary Execution Button:** Filled with Terminal Green `#4edea3`, text rendered in deep navy `#0d1322` at 600 weight. Subtle glow on hover.
- **Secondary Action Button:** Transparent background with a `1px solid #3c4a42` border, text in `#dde2f8`. Hover shifts background to `#191f2f` with border transitioning to `#4cd7f6`.
- **Terminal Copy Button:** Compact icon-text combo situated in code block headers. Uses `JetBrains Mono` label-sm, `#bbcabf` text, transitioning to `#4edea3` and showing a "Copied!" check upon action.

### Terminal Code Blocks
- Dual-tier container:
  - Header bar in `#151b2b` featuring the file path or interpreter badge (`bash`, `yaml`, `/etc/netplan/...`), dot controls, and copy action.
  - Body container in `#090e18` (deep sub-base) or `#242a3a`, using `JetBrains Mono` with high-contrast syntax highlighting: commands in `#4edea3`, flags and paths in `#4cd7f6`, comments in `#bbcabf/60`.

### Status Badges & Chips
- Monospaced indicator tags with dot signals.
- **Active / Success:** `#4edea3/15` background, `#4edea3` text, glowing green dot.
- **Info / Network:** `#4cd7f6/15` background, `#4cd7f6` text.
- **Warning / Error:** Red or amber tones (`#ff6e6e/15`, `#f5a623/15`).

### Data Tables
- Header row styled in `#151b2b` with uppercase `JetBrains Mono` label tokens and a bottom border of `1px solid #3c4a42`.
- Alternating row interaction: rows highlight to `#191f2f` on pointer hover with smooth transition.

### Interactive Evaluation Quiz
- Radio question containers rendered as modular `#191f2f` tiles with `1px solid #3c4a42` borders.
- Selected option updates border to `#4cd7f6` with a cyan-tinted inner indicator.
- Post-submit validation: Correct options illuminate in `#4edea3` with a checkmark badge; incorrect options shift to `#ff6e6e` border with explanation notes rendered inline.