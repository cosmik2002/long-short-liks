from links_transform import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False, use_debugger=False, use_reloader=False, passthrough_errors=True)

