/** @format */

import React, {useState} from "react";

import useWebSocket, {ReadyState} from "react-use-websocket";
import "./index.css";

function App() {
	const [socketUrl, setSocketUrl] = useState("ws://localhost:8000");
	return <div className="App"></div>;
}

export default App;
