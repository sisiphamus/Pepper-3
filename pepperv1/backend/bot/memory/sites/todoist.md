# Todoist

**URL:** https://todoist.com/

## Access Method

**Always use Playwright MCP browser automation.** Do NOT use API tokens, OAuth, REST API keys, or any other token-based authentication method.

### Why Playwright Over Tokens
- User is already logged into Todoist in their Edge browser
- Playwright connects to the existing Edge session with cookies/auth intact
- No need to manage, store, or rotate API tokens
- Browser automation sees exactly what the user sees

### Best Approach

1. Use `mcp__playwright__browser_navigate` to go to `https://todoist.com/app/`
2. Use `mcp__playwright__browser_snapshot` to read the current task list
3. Use `mcp__playwright__browser_click` and `mcp__playwright__browser_type` to create/edit/complete tasks
4. Use `mcp__playwright__browser_evaluate` for extracting structured data if needed

### Common Operations

| Action | Method |
|--------|--------|
| View tasks | Navigate to `/app/today` or `/app/upcoming`, then snapshot |
| Add task | Click "Add task" button, type task content, press Enter |
| Complete task | Click the checkbox next to the task |
| View project | Navigate to `/app/project/{id}` |
| Search | Use the search bar or navigate to `/app/search/{query}` |

### When Playwright MCP is NOT available
- Try WebFetch to `https://todoist.com/app/` as a fallback (may not work without auth)
- If all alternatives fail, emit: `[NEEDS_MORE_TOOLS: need Playwright MCP browser tools to navigate todoist.com with existing browser session]`
- Do NOT attempt to use Todoist API tokens or REST API — use Playwright only

### Notes
- Todoist web app is a single-page app — wait for content to load after navigation
- The app URL is `https://todoist.com/app/` (not just `todoist.com`)
- Connect to existing Edge browser session per browser preferences
