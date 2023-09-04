/** @format */

import React, {useState, useCallback, useEffect} from "react";
import {socket} from "./socket";

// import useWebSocket, {ReadyState} from "react-use-websocket";
import "./index.css";

function App() {
	const [isConnected, setIsConnected] = useState(socket.connected);

	useEffect(() => {
		socket.on("connect", () => {
			setIsConnected(socket.connected);
		});

		socket.on("disconnect", () => {
			setIsConnected(socket.connected);
		});
	}, []);

	return (
		<div className="App flex flex-col">
			{isConnected ? "Connected" : "Not connected"}
		</div>
	);
}

export default App;
