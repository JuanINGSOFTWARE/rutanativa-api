from app import create_app, crear_app


def test_factory_estandarizada_conserva_alias_legacy():
    assert callable(create_app)
    assert crear_app is create_app