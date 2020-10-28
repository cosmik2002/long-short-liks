from links_transform import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host="127.0.0.1", debug=True, use_debugger=False, use_reloader=False, passthrough_errors=True)

