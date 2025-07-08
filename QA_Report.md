# Segwise Dashboard – QA Report  
**Tester**: Roneel V  
**Date**: 9 July 2025

## 1 · Found Bugs / UX Issues

| # | Area | Observed Behaviour | Expected Behaviour | Severity |
|---|------|--------------------|--------------------|----------|
| 1 | Login Page | Extra white space below "OR" in login container. | Should maintain compact, centered layout. | Low |
| 2 | Login Page | Linear gradient is too light compared to the logo on browser tab. | Increase contrast to align better with branding. | Medium |
| 3 | Dashboard Search | Placeholder text is too dark. | Use lighter placeholder to match the light, minimal theme. | Low |
| 4 | Left Menu Hover | Icons show focus, but names only appear on hover. | Name should be visible on keyboard focus for accessibility. | Medium |
| 5 | Crisp Chat Button | Chat button in lower right corner is too dark. | Align button styling with rest of the light theme. | Low |
| 6 | Sidebar Logo | Clicking company logo does nothing. | Logo should redirect to homepage/dashboard overview. | Medium |
| 7 | Missing Footer | No footer found with company info or policies. | Should have a footer with legal and contact links. | High |
| 8 | Calendar Widget | Year selection not supported, current date shows Oct 15, 2024, and later dates disabled. | Allow year selection, fix default date to today, enable all valid future dates. | High |
| 9 | Header Dropdown | User-focus on app switch & other dropdown items looks identical. | Add clear distinction between active hover and current selection. | Medium |
|10 | Header Layout | Header height is too compressed, elements look squished. | Add padding and spacing for visual breathing room. | Low |

---

## 2 · Suggested Test Cases

| Test ID | Test Area | Test Case Description | Expected Result | Status |
|---------|-----------|-----------------------|-----------------|--------|
| TC‑01 | Filters | Filter based on calendar | Data updates according to selected date | ✓ |
| TC‑02 | Filters | Filter by dimensions / tags / metrics | Table & charts refresh with correct data | ✓ |
| TC‑03 | Filters | Multiple dimension filters (AND / OR) | Results respect selected Boolean logic | ✓ |
| TC‑04 | Filters | Dropdowns open / close / select | List items selectable; outside‑click closes | ✓ |
| TC‑05 | Filters | All table attributes visible post‑filter | No hidden / cut‑off columns | ✓ |
| TC‑06 | Filters | Remove‑filter button | Filter chip disappears and data resets | ✓ |
| TC‑07 | Filters | Save and Reset buttons | Save persists filters; Reset clears all | ✓ |
| TC‑08 | Reports | Edit report name | Name editable and persists on reload | ✓ |
| TC‑09 | Reports | Top 5 / Top 10 / Custom buttons | Table & chart slice data correctly | ✓ |
| TC‑10 | Reports | Download / Share / extra menu | Each action triggers correct function | ✓ |
| TC‑11 | Reports | Unsaved changes → navigate away | “Discard / Save changes?” modal appears | ✓ |
| TC‑12 | Boards | Add previous board’s data | Existing reports attach to new board | ✓ |
| TC‑13 | Boards | Board edits don’t alter originals | Original reports stay unchanged | ✓ |
| TC‑14 | Boards | Toggle board visibility (public/private) | Visibility toggle persists & controls access | ✓ |
| TC‑15 | Boards | Delete board | Board removed from list & DB | ✓ |
| TC‑16 | Reports → New | “Create New Report” shows sample viz + table | Default layout rendered | ✓ |
| TC‑17 | Layout | Reorder viz & table (drag‑and‑drop) | Drag‑drop reorders elements and persists | ✗ |
| TC‑18 | Layout | Reorder viz & table using layout buttons | Buttons reorder elements and persist | ✗ |
| TC‑19 | Table | Add attributes → table updates | New columns appear immediately | ✓ |
| TC‑20 | Chart | Add attributes → chart updates | Graph reflects new attribute data | ✓ |
| TC‑21 | Table | Overflow columns show horizontal scroll | Horizontal scrollbar functional | ✓ |
| TC‑22 | Sidebar | Drag left‑menu border to resize | Resize cursor shows & panel width adjusts | ✗ |
| TC‑23 | Reports | Custom button refresh | Selecting **Custom** clears Top 5/Top 10 and applies custom limits | ✗ |
| TC‑24 | Boards | Duplicate board option | Clicking **Duplicate** creates an exact copy with widgets/data | ✓ |
| TC‑25 | Boards | Make board visible to all | “Visible to All” toggles board to public and persists | ✓ |
