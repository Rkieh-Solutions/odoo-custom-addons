{
    "name": "Login Branding (client1)",
    "version": "19.0.1.0.0",
    "category": "Hidden",
    "summary": "Custom login page CSS for client1",
    "depends": ["web"],
    "data": [
        "views/login_assets.xml"
    ],
    "assets": {
        "web.assets_frontend": [
            "login_branding/static/src/css/login.css",
        ],
        "web.assets_backend": [
            "login_branding/static/src/css/login.css",
        ],
    },
    "installable": True,
    "application": False,
}
