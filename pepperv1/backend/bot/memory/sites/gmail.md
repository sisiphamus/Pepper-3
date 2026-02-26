# Gmail — Browser Patterns

## Navigation
- `browser_navigate` to Gmail will **always** return a token overflow. Don't try to parse the navigate output.
- After navigating, immediately take a snapshot with `filename: "memory/short-term/gmail.md"`, then Grep for what you need.

## Compose Dialog

**Best method:** Navigate directly to `https://mail.google.com/mail/u/N/#inbox?compose=new` (where N = account number)

Alternative: Press keyboard shortcut `c` after navigating to Gmail

- Compose dialog appears as: `dialog "Compose: New Message"` or `dialog "New Message"`
- **To field**: `combobox "To recipients"` — use `browser_type` to fill (auto-focuses, no click needed)
- **Subject field**: `textbox "Subject"` — use `browser_type` to fill
- **Body field**: `textbox "Message Body"` — use `browser_type` to fill
- **Send button**: `button "Send ‪(Ctrl-Enter)‬"` — click to send

**Refs are stable** within a compose session. Once you have refs, you can type all fields without re-snapshotting.

## Reading Email
- Inbox rows are `row` elements. Click to open.
- Email body is inside the main content area — snapshot with filename and Grep for the text you need.

## Multiple Accounts
- Account switching: `mail.google.com/mail/u/0/` (first account), `/u/1/` (second), etc.
- If the wrong account loads, change the `/u/N/` in the URL.

## Browser Setup for Gmail
- Gmail requires an authenticated session. **Always use the user's existing Edge session** — see `preferences/browser.md` for how to connect.
- "Use my personal page" = connect to the user's default Edge profile (which has cookies) rather than launching a fresh browser.
- The #1 failure mode is launching Edge without first killing existing instances — the debug port flag gets silently ignored.
- **Never use `launch_chrome.bat` for Gmail** — it creates a DebugProfile that isn't logged in. Gmail redirects to the marketing page. Always use Edge with the real user profile via `launch_edge_debug.bat`.
- Before killing Edge, **warn the user** — they may have tabs open. The Feb 19 incident: Chrome debug profile had no Gmail session, then Edge was killed without warning, losing the user's open tabs.

## Resolving Contact Names to Emails

**Gmail autocomplete resolves names.** When the user says "email antony saleh," don't ask for the email address. Type the name into the To field and Gmail's autocomplete will suggest matching contacts from Google Contacts.

**Flow:**
1. Type the name into the To field using `browser_type` (do NOT press Enter/submit yet)
2. Wait briefly, then take a snapshot — look for autocomplete suggestions (usually `option` or `listbox` elements)
3. Click the matching contact suggestion to confirm it
4. If no autocomplete results appear, **then** ask the user for the email address

**Never give up on a name without trying autocomplete first.** The user's Google Contacts almost certainly has the person if they're asking you to email them by name.

## Compose Email — Optimal Flow (5 tool calls)
1. `browser_navigate` → `mail.google.com/mail/u/N/#inbox?compose=new`
2. `browser_snapshot` with `filename` param → save to temp file
3. `Grep` the snapshot for `To recipients|Subject|Message Body|Send` → get all refs in one call
4. `browser_type` × 3 → To (type name, wait for autocomplete, select contact), Subject, Body
5. `browser_click` → Send button ref (from step 3)
6. Clean up: `rm` the snapshot file

**Grep for Send button:** use pattern `Send.*ref=` or `button.*Send` on the snapshot to find the send button ref alongside the field refs in step 3.

## Key Principle
Gmail's accessibility tree is enormous. **Always** use `filename` param on snapshots, then Grep for specific refs. Never try to read the full snapshot output inline.
