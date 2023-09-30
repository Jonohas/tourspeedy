/** @format */

import React, {useEffect, useState} from "react";
import {socket} from "../socket";

export function SessionManager() {
	const [ready, setReady] = useState<boolean>(false);
	function sendReady() {
		socket.emit("ready");
	}

	useEffect(() => {
		const onReady = (data: any) => {
			setReady(true);
		};

		const onStart = (data: any) => {
			console.log(data);
		};

		const onStop = (data: any) => {
			console.log(data);
		};

		socket.on("ready", onReady);
		socket.on("start", onStart);
		socket.on("stop", onStop);


		return () => {
			socket.off("ready", onReady);
			socket.off("start", onStart);
			socket.off("stop", onStop);
		};
	}, []);

	return (
		<>
			<button onClick={sendReady}>Ready</button>
			<span>{ready ? "System is ready" : "System is not ready yet"}</span>
		</>
	);
}
