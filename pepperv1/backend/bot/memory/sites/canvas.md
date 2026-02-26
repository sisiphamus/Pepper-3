# Canvas (Rice University)

**URL:** https://canvas.rice.edu/

## API Access (authenticated via browser session)

Canvas has a full REST API accessible in the browser when the user is logged in. Use API endpoints directly — they return clean JSON, no DOM parsing needed.

### Key Endpoints

| Purpose | Endpoint |
|---------|----------|
| To-do items | `/api/v1/users/self/todo?per_page=50` |
| Upcoming events/assignments | `/api/v1/users/self/upcoming_events?per_page=50` |
| All courses | `/api/v1/courses?enrollment_state=active&per_page=50` |
| Course assignments | `/api/v1/courses/{id}/assignments?per_page=50` |
| Course announcements | `/api/v1/courses/{id}/discussion_topics?only_announcements=true` |
| User profile | `/api/v1/users/self/profile` |
| Dashboard cards | `/api/v1/dashboard/dashboard_cards` |

### Best Approach

**Option 1: Playwright MCP (preferred)**
1. Navigate to `https://canvas.rice.edu/` first to ensure auth session is active.
2. Hit API endpoints directly via `browser_navigate` — they return raw JSON in the page.
3. Use `browser_evaluate` to parse: `() => JSON.parse(document.body.innerText)`
4. For a "what's due" query, combine `/todo` + `/upcoming_events` for the fullest picture.
See knowledge/playwright-mcp-setup for install instructions.

**Option 2: Direct curl/fetch (try if Playwright unavailable)**
```bash
curl -s "https://canvas.rice.edu/api/v1/users/self/todo?per_page=50" \
  -H "Cookie: [browser cookies]" | jq .
```
Requires extracting browser cookies — complex on Windows.

**When Playwright MCP is NOT available:**
- Try WebFetch or curl approaches first
- If all alternatives fail, emit: [NEEDS_MORE_TOOLS: need Playwright MCP browser tools to navigate canvas.rice.edu with existing browser session]
- The system will auto-install Playwright MCP (see knowledge/playwright-mcp-setup) and re-invoke you
- Do NOT just tell the user the tools aren't available and give up

### Notes

- The dashboard To Do sidebar widget uses a loading spinner and is unreliable for scraping — always prefer the API.
- API responses include course names, due dates (ISO 8601), assignment descriptions (HTML), and submission status.
- User's school: **Rice University**
- Known course: **BUSI 365** (startup/product class with sprint-based assignments)
