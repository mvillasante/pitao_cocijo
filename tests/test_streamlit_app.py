from streamlit.testing.v1 import AppTest


def test_streamlit_app_renders():
    at = AppTest.from_file("/workdir/cocijo/streamlit_app.py")
    at.run()
    assert not at.exception
    assert at.title[0].value == "Lluvia Diaria"
    assert len(at.subheader) == 2
