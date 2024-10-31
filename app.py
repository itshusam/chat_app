from socketweb import WebSocketServer, socketio, app
from flask_socketio import join_room, leave_room

app = WebSocketServer().create_app()

@socketio.on('connect')
def handle_connect():
    print('A client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('A client disconnected')

@socketio.on('join')
def handle_join(data):
    room = data['room']
    join_room(room)
    print(f"User joined room: {room}")
    socketio.emit('message', f"User has entered the room {room}", to=room)

@socketio.on('leave')
def handle_leave(data):
    room = data['room']
    leave_room(room)
    print(f"User left room: {room}")
    socketio.emit('message', f"User has left the room {room}", to=room)

@socketio.on('message')
def handle_message(data):
    room = data['room']
    message = data['message']
    print(f"Message from {data['user']}: {message}")
    socketio.emit('message', f"{data['user']}: {message}", to=room)

if __name__ == '__main__':
    socketio.run(app)
