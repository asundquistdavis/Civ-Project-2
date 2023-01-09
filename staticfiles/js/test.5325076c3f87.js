let url = `ws://${window.location.host}/ws/socket-server/1`;
let socket = new WebSocket(url);
socket.onmessage = function(e) {
    let data = JSON.parse(e.data);
    console.log(data);
};
let poll = JSON.stringify({
    type: 'poll'
});

function pollButton() {
    socket.send(poll);
};

let game = JSON.stringify({
    type: 'game'
});

async function newGame() {
    await socket.send(game);
};