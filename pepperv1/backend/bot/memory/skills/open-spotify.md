# Opening Spotify

## Windows

Use `start spotify:` to open the Spotify desktop app via its URI scheme:

```bash
start spotify:
```

This launches Spotify without blocking the terminal. If Spotify is already running, it brings it to focus.

## Notes

- The executor previously failed with an empty response when attempting this task — likely due to not using the `start` command or incorrect URI format
- The `spotify:` URI scheme works if the Spotify desktop app is installed
- For web-based access, navigate to `https://open.spotify.com` in the browser
