# Macy Runs Big Sur

Fundraising site for Macy Toronjo's 2027 Big Sur International Marathon run for ALS TDI (ALS Therapy Development Institute).

- **Donation page (Haku):** https://fundraisers.hakuapp.com/fundraisers/7e737b754f559c246316
- **Site files:** `index.html` (whole site, one file), `fundraising-data.json` (live total), `songs.json` (song requests), `photos/`, `favicon.svg`
- **Auto-update:** `.github/workflows/update-fundraising.yml` runs `scripts/update_fundraising.py` hourly, reads the raised total and goal from Haku, and commits them to `fundraising-data.json`. The page reads that file on load. The course marker, mile grid, and progress bar all move from it.

## Publish on GitHub Pages

1. Create a public repo (e.g. `big-sur-marathon-fundraiser`) on Macy's GitHub account.
2. Upload every file in this folder, including the hidden `.github/` folder.
3. Settings → Pages → Source: *Deploy from a branch* → `main` / root → Save.
4. Settings → Actions → General → Workflow permissions → *Read and write* (so the hourly updater can commit).
5. Actions tab → *Update fundraising total* → *Run workflow* once to confirm it works.

The site goes live at `https://<username>.github.io/big-sur-marathon-fundraiser/`.

## Edit

Text lives in `index.html`. Settings (race start time, fallback totals) are at the top of the `<script>` block. The donate link appears in several buttons; find-and-replace it if it ever changes.

## Add a song request

When a donor leaves a song in their note, edit `songs.json` (on GitHub: open the file → pencil icon → commit):

```json
{
  "playlist_url": "https://open.spotify.com/playlist/...",
  "songs": [
    { "title": "Dancing in the Moonlight", "artist": "King Harvest", "from": "Aunt Heather" }
  ]
}
```

`from` is optional. Leave `playlist_url` empty to hide the "Listen" button.

## Photos

All four gymnastics photos are by Angie Wang / Daily Bruin (2017), credited on the page. Ask the Daily Bruin photo desk for permission before the site goes public, or swap in Macy's own copies.
