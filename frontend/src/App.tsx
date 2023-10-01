/** @format */

import React, {useState, useCallback, useEffect} from "react";
import {socket} from "./socket";

// import useWebSocket, {ReadyState} from "react-use-websocket";
import "./index.css";
import {ConnectionState} from "./components/ConnectionState";
import {ConnectionManager} from "./components/ConnectionManager";
import {SessionManager} from "./components/SessionManager";
import { OnlineBanner } from "./components/OnlineBanner";

function App() {
	const [isConnected, setIsConnected] = useState(socket.connected);

	useEffect(() => {
		function onConnect() {
			setIsConnected(true);
		}

		function onDisconnect() {
			setIsConnected(false);
		}

		socket.on("connect", onConnect);
		socket.on("disconnect", onDisconnect);

		return () => {
			socket.off("connect", onConnect);
			socket.off("disconnect", onDisconnect);
		};
	}, []);

	return (
		<div className="App flex flex-col">

			<SessionManager />
			<OnlineBanner online={isConnected} />
		</div>
	);
}

export default App;
