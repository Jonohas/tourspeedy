/** @format */

import React, {useEffect} from "react";
import {socket} from "../socket";

export function SessionManager() {
	function ready() {
		socket.emit("ready");
	}

	useEffect(() => {
		const onReady = (data: any) => {
			console.log(data);
		};

		socket.on("ready", onReady);

		return () => {
			socket.off("ready", onReady);
		};
	}, []);

	return (
		<>
			<button onClick={ready}>Ready</button>
			<span>{}</span>
		</>
	);
}
