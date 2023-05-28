import streamlit as st
from sqllineage.drawing import app
from wsgiref.simple_server import make_server
from threading import Thread

def run_server(app, port):
    server = make_server('localhost', port, app)
    server.serve_forever()

def main():
    st.title('Streamlit with WSGI Server')

    if st.button('Start Server'):
        port = 8000  # Define the port number for the server
        with st.spinner('Starting the server...'):
            server_thread = Thread(target=run_server, args=(app, port))
            server_thread.start()
            st.success('Server started!')

        # Wait for the user to manually stop the server
        st.write('Server is running. To stop, click the "Stop Server" button.')
        if st.button('Stop Server'):
            server_thread.join()
            st.warning('Server stopped!')

if __name__ == '__main__':
    main()
