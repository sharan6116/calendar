from app import app


def test_home_page():

    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200


def test_date_selection():

    client = app.test_client()

    response = client.post(
        "/",
        data={"date": "2026-09-10"}
    )

    assert response.status_code == 200
    assert b"2026-09-10" in response.data