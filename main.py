from links_transform import create_app, db_session

app = create_app()

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, use_debugger=False, use_reloader=False, passthrough_errors=True)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
