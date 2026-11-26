"""End-to-End-Tests der Todo-Oberflaeche mit pytest und Playwright."""

from playwright.sync_api import Page, expect


def test_todo_kann_erstellt_bearbeitet_und_geloescht_werden(
    page: Page, live_server: str
) -> None:
    page.goto(live_server)

    page.get_by_placeholder("Neue Aufgabe").fill("Playwright kennenlernen")
    page.get_by_role("button", name="Hinzufügen").click()

    todo = page.get_by_role("listitem").filter(has_text="Playwright kennenlernen")
    expect(todo).to_have_count(1)
    expect(page.get_by_placeholder("Neue Aufgabe")).to_have_value("")

    page.once("dialog", lambda dialog: dialog.accept("E2E-Test schreiben"))
    todo.get_by_role("button", name="Bearbeiten").click()
    edited_todo = page.get_by_role("listitem").filter(has_text="E2E-Test schreiben")
    expect(edited_todo).to_have_count(1)

    edited_todo.get_by_role("button", name="Löschen").click()
    expect(edited_todo).to_have_count(0)
    expect(page.get_by_role("status")).to_be_empty()


def test_todo_status_und_filter_funktionieren(page: Page, live_server: str) -> None:
    page.goto(live_server)

    todo = page.get_by_role("listitem").filter(has_text="FastAPI kennenlernen")
    checkbox = todo.get_by_role("checkbox")
    expect(checkbox).not_to_be_checked()
    checkbox.check()
    expect(checkbox).to_be_checked()

    page.get_by_role("combobox").select_option("false")
    expect(todo).to_have_count(0)

    page.get_by_role("combobox").select_option("true")
    completed_todo = page.get_by_role("listitem").filter(
        has_text="FastAPI kennenlernen"
    )
    expect(completed_todo).to_have_count(1)
    expect(completed_todo.get_by_role("checkbox")).to_be_checked()
    expect(page.get_by_role("status")).to_be_empty()
