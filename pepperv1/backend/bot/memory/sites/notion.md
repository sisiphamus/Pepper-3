# Notion

## Search

- The Notion MCP API search often misses pages — it doesn't have full workspace access. If API search returns nothing for something the user says exists, **go to browser immediately**. Don't retry the API with different modes.
- In-browser search: `Ctrl+P` opens quick search. Type the query, results appear in a listbox. Click the link (not the option) to navigate.
- After typing in Notion search, give it a moment then snapshot to file (pages can be large), then grep the snapshot for the result refs.

## Navigation Rule

- **Always start from PARA.** When navigating Notion for any task, begin at the PARA top-level page and drill down from there. Do not jump directly to subpages via URL unless you already know the exact page. PARA is the root of Adam's workspace organization.

## Workspace

- **Always use Adam's workspace**, not the "Null's" workspace. If you land in the wrong workspace, switch to Adam's. The Notion MCP API connection may default to a different workspace — verify you're in Adam's before reading or writing.

## Page Access

- Adam's workspace is at notion.so
- Pages are organized under a PARA system
- Bible page: `https://www.notion.so/Bible-2fb2c4366aa28014a3fefa446dd0a153` (under PARA > Rage - Just Fucking Pick Something)
- Startup hub: `https://www.notion.so/Startup-2b62c4366aa280feb6acdc21a7e63448` (under PARA)
- Key sections: Knowledge (contains Startups, Sam Altman, a16z, YC Lectures), Writings (Journal, LinkedIn), meetings
- Favorites: Life, OS

## Notion API Limitations

- The Notion MCP API integration does NOT have access to Adam's workspace pages (404 errors). Always use browser for fetching page content.
- Page IDs from search results use `pvs=26&qid=` params — some work as direct URLs, some don't. Navigate via sidebar or search clicks instead of constructing URLs from IDs.
