# Procedure Compass — manual acceptance and negative scenarios

Run in Chromium and a mobile viewport; test local `file://` opening and static HTTPS hosting separately. These are *planned manual scenarios*, not a claim that they were executed.

| Scenario | Expected |
|---|---|
| Search `SSO`, `CVE`, `agent` | Correct recipe displayed |
| Search nonexistent phrase | No-match message; no fabricated result |
| On initial render | SAFE STOP, because authorization is absent |
| Confirm authorization with empty case | WAIT |
| Enter scope/owner/reviewer, no checkpoints | WAIT |
| Complete all checks but choose Reported | WAIT |
| Complete all with Observed/Tested, observation dates and refs | READY FOR HUMAN REVIEW only |
| Revoke authorization after all entries | SAFE STOP |
| Enter `<img src=x onerror=alert(1)>` in case field | Displays as text, never executes |
| Click export | Valid JSON with declaration-only provenance and caveat |
| Reset | Clears in-memory case for selected procedure |
| Refresh tab | Does not restore case data |
| Disconnect network | App remains usable, but external references require connection |
| Narrow mobile view | No horizontal overflow, readable controls, visible state |
| Tab-only operation | Search, selection, entries and export reachable |
| Source URLs | Explicit external navigation; no fetch before click |

**Future gate:** automation can prove UI contract behavior in a controlled browser, not whether any organization is truly offboarded, vulnerable, or agent-safe.
